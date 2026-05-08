from owlready2 import *
from graphviz import Digraph
from contextlib import contextmanager
from contextlib import redirect_stdout, redirect_stderr
import os
import re
import types as _types

@contextmanager
def editing(onto):
    with onto:
        yield
    os.makedirs("build", exist_ok=True)
    onto.save(file="build/latest.ttl", format="turtle")

def classify():
    from owlready2 import sync_reasoner
    sync_reasoner()

def show_subclasses(cls):
    return [c for c in cls.subclasses()]


def get_color_tree(ontos):
    # Normalize input to a list
    onto_list = ontos if isinstance(ontos, list) else [ontos]

    # Nice, distinct pastel palette; will cycle if there are more ontologies
    palette = [
        "#A7C7E7", "#F4B6C2", "#B5EAD7", "#FFDAC1", "#C7CEEA",
        "#F1F0B2", "#FFD6E0", "#C9F9FF", "#D5E8D4", "#E1D5E7"
    ]
    onto_colors = {onto.name: palette[i % len(palette)] for i, onto in enumerate(onto_list)}
    
    g = Digraph("classes", graph_attr={"rankdir": "TB"})

    # Collect classes and labels
    all_classes = []
    all_labels = {}
    for onto in onto_list:
        classes = list(onto.classes())
        labels = {c: c.name for c in classes}
        all_classes.extend(classes)
        all_labels.update(labels)

    classes = set(all_classes)
    labels = all_labels

    # Create nodes with color by ontology
    for c in classes:  
        owner = c.namespace.name
        fill = onto_colors.get(owner, "#FFFFFF")
        # Use the IRI as the unique node id; keep a short human label
        g.node(
            name=labels[c],
            style="filled",
            fillcolor=fill,
            tooltip=f"{labels[c]} · {owner}"
        )

    # Create edges for subclass relations
    for c in classes:
        for parent in c.is_a:
            if isinstance(parent, ThingClass) and parent in classes:
                g.edge(all_labels[parent], labels[c])

    return g


def onto_class_tree(onto):
    g = Digraph("sulo_classes", graph_attr={"rankdir":"TB"})
    classes = list(onto.classes())
    names = {c: c.name for c in classes}
    for c in classes: g.node(names[c])
    for c in classes:
        for parent in c.is_a:
            if isinstance(parent, ThingClass) and parent in classes:
                g.edge(names[parent], names[c])
    return g

# ---- helper: property map (domain -> property -> range) ----
def onto_property_map(onto):
    g = Digraph("sulo_props", graph_attr={"rankdir":"LR"})
    for p in onto.object_properties():
        domains = p.domain or [Thing]
        ranges  = p.range  or [Thing]
        
        for d in domains:
            for r in ranges:
                # check if d has an Or class
                if isinstance(d, Or):
                    for dd in d.Classes:
                        g.edge(dd.name, r.name, label=p.name)
                elif isinstance(r, Or):
                    for rr in r.Classes:
                        g.edge(d.name, rr.name, label=p.name)
                else:
                    g.edge(d.name, r.name, label=p.name)
    return g

        
def safe_call_reasoner(onto):
    try:
        with open('/dev/null', 'w') as f, redirect_stdout(f), redirect_stderr(f):
            sync_reasoner(ignore_unsupported_datatypes=True)
            return {
                "ok": True, 
                "inconsistent": list(onto.inconsistent_classes()),
            }
    
    except Exception as e:
        msg = str(e)
        m = re.search(r"Exception:\s*(.*)", msg)
        error = m.group(1).strip() if m else msg
        return {
            "ok": False,
            "error": error,
            "inconsistent": None,
        }

def search_bioportal(term, ontology_acronym, api_key, pagesize=10):
    """
    Search BioPortal for a term in a specific ontology.

    Returns a list of dicts with keys: iri, label, definition, ontology.
    Requires a BioPortal API key from https://bioportal.bioontology.org/account
    """
    import requests
    url = "https://data.bioontology.org/search"
    params = {
        "q": term,
        "ontologies": ontology_acronym,
        "apikey": api_key,
        "pagesize": pagesize,
        "include": "prefLabel,definition,synonym",
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("collection", []):
        defn = item.get("definition")
        results.append({
            "iri": item.get("@id"),
            "label": item.get("prefLabel"),
            "definition": defn[0] if defn else None,
            "ontology": ontology_acronym,
        })
    return results


def mireot_import(target_onto, term_iri, label, parent=None, source_ontology_iri=None, definition=None):
    """
    MIREOT-import an external term into target_onto.

    Creates a stub class at the external IRI with minimal annotations:
    rdfs:label, rdfs:comment (definition), rdfs:isDefinedBy (source ontology).
    If the IRI is already loaded in the world it is returned as-is.

    Parameters
    ----------
    target_onto       : owlready2 Ontology to import into
    term_iri          : str  — full IRI of the external term
    label             : str  — human-readable label (rdfs:label)
    parent            : owlready2 class  — direct parent class (default: owl:Thing)
    source_ontology_iri : str  — IRI of the source ontology (rdfs:isDefinedBy)
    definition        : str  — textual definition (rdfs:comment)
    """
    # Return existing class if already in the world
    existing = IRIS.get(term_iri)
    if existing is not None:
        return existing

    # Split the IRI into a namespace base and a local name
    if "#" in term_iri:
        ns_base, local = term_iri.rsplit("#", 1)
        ns_base += "#"
    else:
        ns_base, local = term_iri.rsplit("/", 1)
        ns_base += "/"

    ns = target_onto.get_namespace(ns_base)
    parent_cls = parent if parent is not None else Thing

    with target_onto:
        stub = _types.new_class(local, (parent_cls,), kwds={"namespace": ns})
        stub.label = [label]
        if definition:
            stub.comment = [definition]
        if source_ontology_iri:
            stub.isDefinedBy = [source_ontology_iri]

    return stub


def _onto_label(entity):
    lbl = entity.label.en.first() if entity.label.en else (entity.label.first() if entity.label else None)
    return lbl

def _onto_comment(entity):
    cmt = entity.comment.en.first() if entity.comment.en else (entity.comment.first() if entity.comment else None)
    return " ".join(cmt.split()) if cmt else None

def build_tree(node, children_fn, depth=0, visited=None, lines=None):
    """Render an ontology hierarchy as an indented Markdown list."""
    if visited is None:
        visited = set()
    if lines is None:
        lines = []
    if node in visited:
        return lines
    visited.add(node)

    indent = "  " * depth
    label = _onto_label(node)
    comment = _onto_comment(node)

    label_str = f" — {label}" if label and label.lower() != node.name.lower() else ""
    comment_str = f": {comment}" if comment else ""
    lines.append(f"{indent}- **{node.name}**{label_str}{comment_str}")

    for child in sorted(children_fn(node), key=lambda n: n.name):
        build_tree(child, children_fn, depth + 1, visited, lines)
    return lines


def in_ancestors(onto, cls, ancestor):
    res = safe_call_reasoner(onto)
    if not res["ok"]:
        print("Reasoner Error: \n", res["error"])
        return

    if ancestor in cls.ancestors():
        print(f"{cls.name} is a subclass of {ancestor.name}")
    else:
        print(f"{cls.name} is NOT a subclass of {ancestor.name}")
