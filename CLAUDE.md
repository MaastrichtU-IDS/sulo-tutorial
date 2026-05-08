# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A modern OWL ontology tutorial using the pizza domain, built on the **SULO** (Simplified Upper Level Ontology) upper-level ontology. Students learn ontology engineering concepts through interactive Jupyter notebooks using Python and `owlready2`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependencies: `ipykernel`, `owlready2`, `graphviz`

Run notebooks:
```bash
jupyter notebook
```

## Notebook Sequence

The notebooks build on each other and must be run in order:

| Notebook | Topic |
|---|---|
| `00-SULO-tutorial-setup.ipynb` | Environment setup, load SULO, visualize class/property hierarchy, run reasoner |
| `01-SULO-tutorial-composition.ipynb` | Part-whole composition (`hasPart`, `hasDirectPart`), class restrictions, OWA |
| `02-SULO-tutorial-qualities-quantities.ipynb` | Qualities, quantities, constrained datatypes (SHU measurements) |
| `03-SULO-tutorial-processes.ipynb` | Processes, participants, roles, temporal ordering |

Each notebook loads `pizza.owl` (the running ontology artifact) and appends to it, saving back to `pizza.owl` plus a numbered checkpoint (e.g., `pizza-01.owl`, `pizza-02.owl`).

## Architecture

- **SULO** (`https://w3id.org/sulo/sulo.owl`) — loaded remotely; provides `SpatialObject`, `Quality`, `Quantity`, `Process`, `Role`, `hasPart`, `hasDirectPart`, `hasFeature`, `refersTo`, `hasValue`, etc.
- **pizza ontology** (`pizza.owl`) — built incrementally across notebooks; IRI `https://w3id.org/ontostart/pizza/`
- **sulo-ext** — an extension ontology created in notebook 03 (IRI `https://w3id.org/ontostart/sulo-ext/`) that adds process-related properties and classes not in SULO
- **`lib/helpers.py`** — shared utilities: `editing(onto)` context manager that auto-saves to `build/latest.ttl`, `safe_call_reasoner(onto)` (suppresses HermiT stdout/stderr, returns `{ok, inconsistent}`), `get_color_tree(ontos)` (multi-ontology colored Digraph), `onto_class_tree`, `onto_property_map`, `in_ancestors`
- **`lib/`** — also contains Java JARs for HermiT and ELK reasoners (used by owlready2 via JVM)

## Key OWL Concepts Covered

- `hasDirectPart` vs `hasPart`: cardinality restrictions require non-transitive properties, so use `hasDirectPart` (sub-property of `hasPart`) for `exactly`/`max` restrictions
- Open World Assumption: use `AllDisjoint` + universal restriction (`only`) to close a class definition
- `INDIRECT_<property>` prefix in owlready2 to query inferred (transitive) relations
- `equivalent_to` for defined classes (enables classification inference); `is_a` for primitive classes

## Ontology Files

- `sulo.owl` — local copy of SULO
- `pizza.owl` — current working ontology (overwritten by each notebook run)
- `pizza-01.owl`, `pizza-02.owl` — snapshots after notebooks 01 and 02
- `reference_work/pizza.owl` — original Manchester Pizza Tutorial ontology (reference only)
