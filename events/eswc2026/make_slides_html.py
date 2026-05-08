"""
Generate sulo-tutorial-intro.html — a self-contained slide deck viewable in any browser.
Run with: .venv/bin/python3 make_slides_html.py
"""

SLIDES = [

# ── 1. Title ─────────────────────────────────────────────────────────────────
dict(kind="title", content="""
<div class="title-main">FAIR Ontology Engineering with SULO</div>
<div class="title-sub">A Hands-On Tutorial</div>
<div class="title-meta">ESWC 2026 &nbsp;·&nbsp; May 10/11, 2026</div>
<div class="title-meta">Michel Dumontier &nbsp;·&nbsp; Remzi Celebi</div>
<div class="title-small">Maastricht University &nbsp;·&nbsp; Department of Advanced Computing Sciences</div>
<div class="title-tagline">🍕&nbsp; The pizza domain as a vehicle for principled ontology engineering</div>
"""),

# ── 2. The Challenge ──────────────────────────────────────────────────────────
dict(kind="cols3", header="The Challenge", subheader="Why does this tutorial exist?",
cols=[
("⚠ Engineering Quality", [
    "Ontologies re-invented from scratch",
    "Inconsistent use of upper-level concepts",
    "Ad hoc class/property naming",
    "Missing or wrong axioms",
    "Hard to reason over reliably",
]),
("⚠ FAIRness Gaps", [
    "No stable IRI / version IRI",
    "Missing metadata (title, license, creator…)",
    "Terms lack rdfs:label and rdfs:comment",
    "Not registered in any catalogue",
    "Not reproducible",
]),
("⚠ Tooling & Training Gap", [
    "Learners need end-to-end workflow guidance",
    "Upper ontologies are under-used in teaching",
    "Few tutorials connect modelling → publishing",
    "No practical template for FAIR ontology projects",
]),
]),

# ── 3. Goals & Learning Objectives ───────────────────────────────────────────
dict(kind="cols2", header="Goals & Learning Objectives",
cols=[
("Domain Modelling with SULO", [
    "Master SULO's categories and design patterns",
    "Distinguish parts, features, roles, capabilities, processes, quantities",
    "Translate conceptual models into OWL axioms",
    "Validate designs with automated reasoning (HermiT / ELK)",
    "FAIR Publication",
    "Add FAIR metadata to an ontology",
    "Export to RDF/XML and Turtle",
    "Publish with OntoStart CI/CD pipeline to a persistent IRI",
    "Interpret FOOPS! FAIRness reports and close gaps",
]),
("What Participants Take Home", [
    "End-to-end workflow: idea → axiom → reasoning → publication",
    "Practical owlready2 skills for programmatic ontology engineering",
    "Design patterns reusable in your own domain ontology",
    "A ready-to-use FAIR ontology template (OntoStart)",
    "Critical understanding of the Open World Assumption",
    "Ability to read and act on automated quality reports",
]),
]),

# ── 4. Methodology ────────────────────────────────────────────────────────────
dict(kind="pipeline", header="Methodology", subheader="How the tutorial works",
tagline="Every concept is introduced through a worked pizza example, then immediately applied in an exercise. The ontology is built incrementally across notebooks — each session picks up where the last left off.",
steps=[
    ("📖", "Concept",  "Upper-level category from SULO motivates the modelling choice"),
    ("💻", "Code",     "owlready2 cell: declare classes, axioms, individuals in Python"),
    ("🔍", "Reason",   "HermiT or ELK checks consistency and classifies terms"),
    ("✅", "Verify",   "Query inferred relations; observe OWA behaviour; fix gaps"),
    ("🚀", "Publish",  "Export, annotate, push to OntoStart; assess with FOOPS!"),
]),

# ── 5. What is OWL? ───────────────────────────────────────────────────────────
dict(kind="cols2", header="What is OWL?", subheader="Web Ontology Language — the formal backbone",
footer="Open World Assumption: the absence of information is not the same as false — you must explicitly state what is not the case.",
cols=[
("OWL in a Nutshell", [
    "W3C standard for knowledge representation on the Semantic Web",
    "Formally grounded in Description Logics — enables automated reasoning",
    "Three constructs: Classes, Properties, Individuals",
    "Axioms describe necessary and/or sufficient conditions for class membership",
    "Reasoners (HermiT, ELK) check consistency and infer new facts",
]),
("Key Axiom Types Used", [
    "SubClassOf — every Pizza hasDirectPart some PizzaCrust",
    "EquivalentTo — SpicyPizza ≡ Pizza ⊓ hasPart.∃hasFeature.SpicyHot",
    "DisjointClasses — Mozzarella, Salami, Basil cannot overlap",
    "ObjectPropertyCharacteristics — hasPart is Transitive",
    "AnnotationProperty — rdfs:label, rdfs:comment, dc:creator…",
]),
]),

# ── 6. What is SULO? ──────────────────────────────────────────────────────────
dict(kind="sulo", header="What is SULO?", subheader="Simplified Upper Level Ontology — https://w3id.org/sulo/",
left=[
    "A lightweight, carefully engineered top-level ontology",
    "Provides foundational categories shared across all domains",
    "Designed to be small enough to learn in one session",
    "Grounds domain ontologies in a shared formal framework",
    "Enables cross-domain interoperability and reuse",
    "Aligns with BFO, DOLCE, and other upper-level ontologies",
],
classes=[
    ("SpatialObject",     "A thing that exists in space (pizza, oven, box)"),
    ("Quality",           "An intrinsic feature (spiciness level)"),
    ("Quantity",          "A measured feature with numeric value (SHU)"),
    ("Process",           "A temporally extended event (baking, delivery)"),
    ("Role",              "A relational property played by an entity"),
    ("InformationObject", "An entity whose function is to encode meaning"),
    ("TimeInstant",       "A point on the timeline (order received)"),
    ("Duration",          "An elapsed time quantity (30-min delivery)"),
]),

# ── 7. owlready2 ─────────────────────────────────────────────────────────────
dict(kind="code", header="What is owlready2?", subheader="Python library for OWL ontology engineering",
left=[
    "Python library for loading, editing, and reasoning over OWL ontologies",
    "Natural Python syntax maps directly to OWL axioms",
    "Embeds HermiT and ELK reasoners (via JVM) — no separate install",
    "Saves in RDF/XML; combine with rdflib for Turtle export",
    "Supports SPARQL queries over the asserted graph",
    "Active development; pip-installable; widely used in research",
],
code="""<span class="kw">from</span> owlready2 <span class="kw">import</span> *

sulo  = get_ontology(<span class="st">"https://w3id.org/sulo/"</span>).load()
pizza = get_ontology(<span class="st">"https://w3id.org/ontostart/pizza/"</span>)

<span class="kw">with</span> pizza:
    <span class="kw">class</span> <span class="cls">PizzaCrust</span>(sulo.SpatialObject):
        label = [locstr(<span class="st">"pizza crust"</span>, <span class="st">"en"</span>)]

    <span class="kw">class</span> <span class="cls">Pizza</span>(sulo.SpatialObject):
        is_a = [sulo.hasDirectPart.exactly(<span class="num">1</span>, PizzaCrust)]

    <span class="kw">class</span> <span class="cls">SpicyPizza</span>(Pizza):
        equivalent_to = [Pizza &amp;
            sulo.hasPart.some(
                sulo.hasFeature.some(SpicyHot))]

safe_call_reasoner(pizza)   <span class="cm"># HermiT / ELK</span>
"""),

# ── 8. Tutorial Map ───────────────────────────────────────────────────────────
dict(kind="notebooks", header="Tutorial Map", subheader="8 notebooks · 4 hours · one growing ontology",
notebooks=[
    ("00", "Setup &\nOrientation",    "Load SULO, explore the hierarchy, run reasoner",     False),
    ("01", "Spatial Objects\n& Composition", "hasPart, hasDirectPart, defined classes, OWA", True),
    ("02", "Qualities &\nQuantities", "Spiciness, SHU, constrained datatypes",               True),
    ("03", "Processes",               "Transformation, development, roles, temporal order",  True),
    ("04", "Information\nEntities",   "Orders, receipts, identity, refersTo, recipes",       True),
    ("05", "Time",                    "Time instants, durations, timelines, classification", True),
    ("06", "Spatial\nContainment",    "contains vs hasPart, BoxedPizza, SPARQL",             True),
    ("07", "Deployment\n& FAIRness",  "Metadata, export, OntoStart, FOOPS!",                False),
]),

# ── 9. Why Pizza? ─────────────────────────────────────────────────────────────
dict(kind="pizza", header="Why Pizza?", subheader="A rich, familiar domain for systematic ontology engineering",
tagline="Simple enough to follow without domain expertise, yet rich enough to demonstrate every major representational challenge in applied ontology.",
cards=[
    ("🧩", "Composition",      "A pizza has exactly 1 crust, 1 sauce, ≥1 toppings. Parts have parts (dough, cornicione)."),
    ("🌶",  "Quality",          "Spiciness is a quality. SpicyHot, SpicyMedium, SpicyMild are disjoint categorical levels."),
    ("📏", "Quantity",          "Scoville Heat Units measure spiciness numerically. Constrained datatypes define ranges."),
    ("⚙",  "Process",          "Making dough transforms flour+water→dough. Baking is a developmental process."),
    ("📋", "Information",      "A pizza order refers to a pizza. A receipt records a payment. A recipe describes a process."),
    ("⏱",  "Time",             "Order received → baking starts → ends → delivered. Express delivery ≤ 30 min."),
    ("📦", "Containment",      "Pizza is in the oven. Oven contains box contains pizza. Containment ≠ parthood."),
    ("🚀", "Publication",      "The ontology gets a persistent IRI, full metadata, and a FOOPS! FAIRness score."),
]),

# ── 10. Outcomes ──────────────────────────────────────────────────────────────
dict(kind="cols2", header="What You Will Leave With",
cols=[
("🎁 Tangible Deliverables", [
    "A complete, reasoned OWL ontology of the pizza domain",
    "Published at your own persistent IRI — https://w3id.org/ontostart/pizza-{you}/",
    "Documented with DC, VANN, PAV, DCAT, FOAF, MOD metadata",
    "Assessed by FOOPS! with a score you can improve",
    "Version-controlled on GitHub with auto-generated HTML documentation",
]),
("🧠 Skills & Knowledge", [
    "End-to-end FAIR ontology workflow",
    "SULO design patterns for any domain",
    "owlready2 Python proficiency",
    "Reading and acting on reasoner output",
    "Reading FOOPS! reports",
    "OntoStart as a project template for your next ontology",
    "Critical awareness of OWA and its consequences for modelling",
]),
]),

# ── 11. Schedule ──────────────────────────────────────────────────────────────
dict(kind="schedule", header="Schedule", subheader="Half-day · 4 hours · May 10/11, 2026",
rows=[
    ("5 min",  "Tutorial overview",                  "Introduction and goals",                   ""),
    ("10 min", "What is an ontology?",               "OWL, SULO, and the pizza domain",          ""),
    ("15 min", "Declarations",                       "Classes, individuals, imports",             "NB 00"),
    ("20 min", "Spatial objects & composition",      "hasPart, cardinality, OWA",                 "NB 01"),
    ("15 min", "Qualities",                          "Categorical qualities, disjointness",        "NB 02"),
    ("15 min", "Quantities",                         "SHU, constrained datatypes",                "NB 02"),
    ("30 min", "Processes, parts & roles",           "Transformation, development, PRO roles",    "NB 03"),
    ("15 min", "Information entities",               "Orders, receipts, identity",                "NB 04"),
    ("15 min", "BREAK",                              "",                                          ""),
    ("15 min", "Time",                               "Instants, durations, timelines",            "NB 05"),
    ("15 min", "Spatial containment",                "contains vs hasPart, SPARQL",               "NB 06"),
    ("15 min", "OntoStart deployment",               "Metadata, export, GitHub Actions",          "NB 07"),
    ("10 min", "FAIRness assessment",                "FOOPS! report interpretation",              "NB 07"),
    ("30 min", "Q&A + wrap-up",                      "Modelling discussion",                      ""),
]),

# ── 12. OntoStart & FOOPS! ────────────────────────────────────────────────────
dict(kind="cols2", header="Tools: OntoStart & FOOPS!", subheader="The publication and quality-assessment pipeline",
cols=[
("🚀 OntoStart", [
    "GitHub repository template for FAIR ontology projects",
    "Push a branch → GitHub Actions automatically:",
    "  · Validates OWL DL profile",
    "  · Converts to RDF/XML, Turtle, JSON-LD, N-Triples",
    "  · Generates HTML documentation (Ontospy, PyLODE)",
    "  · Runs FOOPS! and publishes a FAIRness badge",
    "  · Deploys to GitHub Pages",
    "Serves ontology at w3id.org with full content negotiation",
    "→ github.com/micheldumontier/ontostart",
]),
("✅ FOOPS! FAIRness Checker", [
    "Automated FAIR ontology assessment tool (OEG-UPM, Madrid)",
    "Checks 24 indicators across all four FAIR dimensions",
    "F: persistent URI, version IRI, namespace prefix, catalogue",
    "A: content negotiation, open protocol, HTML documentation",
    "I: standard vocabularies reused, OWL/RDF serialisation",
    "R: title, description, license, creator, labels, definitions",
    "→ foops.linkeddata.es",
    "→ foops.linkeddata.es/FAIR_validator.html (file upload)",
]),
]),

# ── 13. Resources ─────────────────────────────────────────────────────────────
dict(kind="resources", header="Additional Resources",
groups=[
("SULO & This Tutorial", [
    "SULO ontology — w3id.org/sulo/",
    "Tutorial repo — github.com/micheldumontier/sulo-tutorial",
    "OntoStart — github.com/micheldumontier/ontostart",
]),
("OWL & Ontology Engineering", [
    "OWL 2 Primer (W3C) — w3.org/TR/owl2-primer/",
    "Protégé editor — protege.stanford.edu",
    "Original Pizza Tutorial — co-ode.org/ontologies/pizza/",
    "OWL 2 Quick Reference — w3.org/TR/owl2-quick-reference/",
]),
("Tools", [
    "owlready2 docs — owlready2.readthedocs.io",
    "rdflib — rdflib.readthedocs.io",
    "FOOPS! — foops.linkeddata.es",
    "ROBOT — robot.obolibrary.org",
]),
("FAIR & Metadata", [
    "FAIR principles — doi.org/10.1038/sdata.2016.18",
    "FOOPS! paper — doi.org/10.3390/app11083950",
    "MOD ontology — w3id.org/mod",
    "W3ID — w3id.org",
]),
]),

# ── 14. Let's Go ──────────────────────────────────────────────────────────────
dict(kind="end", content="""
<div class="end-emoji">🍕</div>
<div class="end-title">Let's Get Started</div>
<div class="end-sub">Open Jupyter Lab and run<br><code>00-SULO-tutorial-setup.ipynb</code></div>
<div class="end-link">github.com/micheldumontier/sulo-tutorial</div>
<div class="end-contact">Questions? → michel.dumontier@maastrichtuniversity.nl</div>
"""),

]

# ══════════════════════════════════════════════════════════════════════════════
# HTML template
# ══════════════════════════════════════════════════════════════════════════════
CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0f0f1a; color: #222; }

/* ── Slide container ── */
.slide {
  width: 1280px; height: 720px; position: relative; overflow: hidden;
  margin: 0 auto 4px; background: #fff; display: none;
  flex-direction: column;
}
.slide.active { display: flex; }

/* ── Header bar ── */
.hbar {
  background: #1A3A5C; padding: 14px 28px 10px;
  flex-shrink: 0;
}
.hbar h1 { color: #fff; font-size: 30px; font-weight: 700; line-height: 1.1; }
.hbar .sub { color: #A8C8E8; font-size: 14px; margin-top: 3px; }
.orange-line { height: 5px; background: #E67E22; flex-shrink: 0; }

/* ── Body area ── */
.body { flex: 1; padding: 16px 24px 10px; overflow: hidden; }

/* ── Title slide ── */
.slide.title-slide {
  background: #1A3A5C;
  align-items: center; justify-content: center; text-align: center;
}
.title-main { color: #fff; font-size: 44px; font-weight: 800; line-height: 1.15; margin-bottom: 14px; }
.title-sub  { color: #A8C8E8; font-size: 22px; margin-bottom: 8px; }
.title-meta { color: #A8C8E8; font-size: 16px; margin-bottom: 4px; }
.title-small { color: #7098B8; font-size: 13px; margin-top: 6px; }
.title-tagline { color: #dde; font-size: 14px; margin-top: 22px; font-style: italic; }
.title-line { width: 600px; height: 4px; background: #E67E22; margin: 18px auto; }

/* ── 3-column layout ── */
.cols3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; height: 100%; }
.cols2 { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; height: 100%; }
.col-box {
  background: #EAF4FB; border-radius: 6px; padding: 14px 16px; overflow: hidden;
}
.col-box.grey { background: #F4F6F7; }
.col-box h3 { color: #206AA8; font-size: 15px; margin-bottom: 10px; font-weight: 700; }
.col-box ul { list-style: none; }
.col-box ul li { font-size: 13px; color: #333; padding: 3px 0 3px 14px; position: relative; line-height: 1.35; }
.col-box ul li::before { content: "▸"; position: absolute; left: 0; color: #E67E22; }

/* ── Pipeline ── */
.pipeline-tagline { font-size: 14px; color: #555; font-style: italic; margin-bottom: 14px; line-height: 1.4; }
.pipeline { display: flex; gap: 12px; align-items: stretch; height: calc(100% - 60px); }
.step {
  flex: 1; background: #EAF4FB; border-radius: 8px; padding: 16px 12px;
  display: flex; flex-direction: column; align-items: center; text-align: center;
}
.step:last-child { background: #1A3A5C; color: #fff; }
.step:last-child .step-title { color: #A8C8E8; }
.step:last-child .step-desc  { color: #cde; }
.step-icon  { font-size: 36px; margin-bottom: 10px; }
.step-title { font-size: 16px; font-weight: 700; color: #1A3A5C; margin-bottom: 8px; }
.step-desc  { font-size: 12.5px; color: #444; line-height: 1.4; }
.arrow { font-size: 24px; color: #206AA8; align-self: center; flex-shrink: 0; }

/* ── SULO classes ── */
.sulo-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; height: 100%; }
.sulo-left { background: #EAF4FB; border-radius: 6px; padding: 14px 16px; }
.sulo-left h3 { color: #206AA8; font-size: 15px; margin-bottom: 10px; font-weight: 700; }
.sulo-left ul { list-style: none; }
.sulo-left ul li { font-size: 13px; color: #333; padding: 3px 0 3px 14px; position: relative; }
.sulo-left ul li::before { content: "▸"; position: absolute; left: 0; color: #E67E22; }
.sulo-table { background: #F4F6F7; border-radius: 6px; overflow: hidden; }
.sulo-table h3 { color: #206AA8; font-size: 15px; padding: 12px 14px 8px; font-weight: 700; }
.sulo-row { display: flex; align-items: baseline; padding: 5px 14px; font-size: 13px; }
.sulo-row:nth-child(odd) { background: #EAF4FB; }
.sulo-cls { font-weight: 700; color: #206AA8; min-width: 155px; font-family: monospace; font-size: 12.5px; }
.sulo-desc { color: #444; }

/* ── Code slide ── */
.code-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; height: 100%; }
.code-left { background: #EAF4FB; border-radius: 6px; padding: 14px 16px; }
.code-left h3 { color: #206AA8; font-size: 15px; margin-bottom: 10px; font-weight: 700; }
.code-left ul { list-style: none; }
.code-left ul li { font-size: 13px; color: #333; padding: 3px 0 3px 14px; position: relative; line-height: 1.35; }
.code-left ul li::before { content: "▸"; position: absolute; left: 0; color: #E67E22; }
.code-block {
  background: #1E1E2E; border-radius: 6px; padding: 18px 20px;
  font-family: 'Cascadia Code', 'Fira Code', 'Courier New', monospace;
  font-size: 13px; line-height: 1.7; overflow: hidden;
}
.kw  { color: #C792EA; }
.cls { color: #89DDFF; }
.st  { color: #A6DA95; }
.cm  { color: #636D83; }
.num { color: #F78C6C; }
.code-block span:not([class]) { color: #CAD3F5; }

/* ── Notebooks ── */
.nb-grid { display: grid; grid-template-columns: repeat(8, 1fr); gap: 8px; height: 100%; }
.nb-card { border-radius: 6px; overflow: hidden; display: flex; flex-direction: column; }
.nb-badge {
  background: #206AA8; color: #fff; text-align: center;
  font-size: 12px; font-weight: 700; padding: 6px 4px;
}
.nb-card.setup .nb-badge  { background: #1A3A5C; }
.nb-card.deploy .nb-badge { background: #E67E22; }
.nb-card.core   { background: #EAF4FB; }
.nb-card.setup, .nb-card.deploy { background: #F4F6F7; }
.nb-title { font-size: 12px; font-weight: 700; color: #1A3A5C; padding: 8px 6px 4px; text-align: center; white-space: pre-line; line-height: 1.3; }
.nb-desc  { font-size: 11px; color: #555; padding: 4px 6px 8px; text-align: center; line-height: 1.35; flex: 1; }
.nb-legend { font-size: 11px; color: #888; text-align: center; margin-top: 6px; font-style: italic; }

/* ── Pizza cards ── */
.pizza-tagline { font-size: 13.5px; color: #555; font-style: italic; margin-bottom: 12px; }
.pizza-grid { display: grid; grid-template-columns: repeat(8, 1fr); gap: 8px; height: calc(100% - 50px); }
.pizza-card { background: #EAF4FB; border-radius: 6px; padding: 10px 8px; text-align: center; }
.pizza-card:last-child { background: #FFF0D6; }
.pizza-icon  { font-size: 28px; margin-bottom: 6px; }
.pizza-topic { font-size: 12px; font-weight: 700; color: #1A3A5C; margin-bottom: 6px; }
.pizza-desc  { font-size: 11px; color: #444; line-height: 1.35; }

/* ── Schedule ── */
.sched { width: 100%; border-collapse: collapse; font-size: 12.5px; }
.sched th { background: #1A3A5C; color: #fff; padding: 6px 10px; text-align: left; }
.sched td { padding: 4px 10px; border-bottom: 1px solid #e8e8e8; }
.sched tr:nth-child(even) td { background: #EAF4FB; }
.sched tr.break td { background: #FFF0D6; color: #E67E22; font-weight: 700; }
.sched td.nb { color: #206AA8; font-weight: 600; }
.sched td.dur { color: #888; white-space: nowrap; }

/* ── Resources ── */
.res-grid { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 14px; height: 100%; }
.res-box { background: #EAF4FB; border-radius: 6px; padding: 14px 14px; }
.res-box:nth-child(even) { background: #F4F6F7; }
.res-box h3 { color: #206AA8; font-size: 14px; font-weight: 700; margin-bottom: 10px; }
.res-box ul { list-style: none; }
.res-box ul li { font-size: 12px; color: #333; padding: 4px 0; line-height: 1.35; border-bottom: 1px solid #dde; }

/* ── End slide ── */
.slide.end-slide {
  background: #1A3A5C; align-items: center; justify-content: center; text-align: center;
}
.end-emoji   { font-size: 64px; margin-bottom: 12px; }
.end-title   { color: #fff; font-size: 46px; font-weight: 800; margin-bottom: 16px; }
.end-sub     { color: #A8C8E8; font-size: 20px; margin-bottom: 12px; line-height: 1.4; }
.end-sub code { background: rgba(255,255,255,0.12); padding: 2px 8px; border-radius: 4px; font-size: 18px; }
.end-link    { color: #A8C8E8; font-size: 15px; margin-bottom: 20px; }
.end-contact { color: #7098B8; font-size: 13px; }

/* ── Footer ── */
.footer-note { font-size: 12.5px; color: #E67E22; font-style: italic; font-weight: 600;
  padding: 6px 24px; background: #fff3e0; }

/* ── Navigation ── */
#nav {
  position: fixed; bottom: 18px; left: 50%; transform: translateX(-50%);
  display: flex; gap: 10px; align-items: center; z-index: 100;
  background: rgba(0,0,0,0.7); padding: 8px 18px; border-radius: 30px;
}
#nav button {
  background: #206AA8; color: #fff; border: none; border-radius: 20px;
  padding: 6px 18px; font-size: 14px; cursor: pointer;
}
#nav button:hover { background: #E67E22; }
#slide-counter { color: #ccc; font-size: 13px; min-width: 60px; text-align: center; }
"""

def render_slide(s):
    kind = s["kind"]

    if kind == "title":
        return f'<div class="slide title-slide active">{s["content"]}<div class="title-line"></div></div>'

    if kind == "end":
        return f'<div class="slide end-slide">{s["content"]}</div>'

    hdr = s.get("header", "")
    sub = s.get("subheader", "")
    sub_html = f'<div class="sub">{sub}</div>' if sub else ""
    footer = s.get("footer", "")
    footer_html = f'<div class="footer-note">{footer}</div>' if footer else ""

    header_html = f'<div class="hbar"><h1>{hdr}</h1>{sub_html}</div><div class="orange-line"></div>'

    if kind == "cols3":
        cols_html = ""
        for i, (title, items) in enumerate(s["cols"]):
            li = "".join(f"<li>{it}</li>" for it in items)
            cls = "grey" if i == 2 else ""
            cols_html += f'<div class="col-box {cls}"><h3>{title}</h3><ul>{li}</ul></div>'
        body = f'<div class="body"><div class="cols3">{cols_html}</div></div>'

    elif kind == "cols2":
        cols_html = ""
        for i, (title, items) in enumerate(s["cols"]):
            li = "".join(f"<li>{it}</li>" for it in items)
            cls = "grey" if i == 1 else ""
            cols_html += f'<div class="col-box {cls}"><h3>{title}</h3><ul>{li}</ul></div>'
        body = f'<div class="body"><div class="cols2">{cols_html}</div></div>'

    elif kind == "pipeline":
        tagline = f'<div class="pipeline-tagline">{s["tagline"]}</div>'
        steps_html = ""
        for i, (icon, title, desc) in enumerate(s["steps"]):
            steps_html += f'<div class="step"><div class="step-icon">{icon}</div><div class="step-title">{title}</div><div class="step-desc">{desc}</div></div>'
            if i < len(s["steps"]) - 1:
                steps_html += '<div class="arrow">→</div>'
        body = f'<div class="body">{tagline}<div class="pipeline">{steps_html}</div></div>'

    elif kind == "sulo":
        li = "".join(f"<li>{it}</li>" for it in s["left"])
        left_html = f'<div class="sulo-left"><h3>Why SULO?</h3><ul>{li}</ul></div>'
        rows_html = "".join(
            f'<div class="sulo-row"><span class="sulo-cls">{cls}</span><span class="sulo-desc">{desc}</span></div>'
            for cls, desc in s["classes"]
        )
        right_html = f'<div class="sulo-table"><h3>Key SULO Classes</h3>{rows_html}</div>'
        body = f'<div class="body"><div class="sulo-grid">{left_html}{right_html}</div></div>'

    elif kind == "code":
        li = "".join(f"<li>{it}</li>" for it in s["left"])
        left_html = f'<div class="code-left"><h3>owlready2 at a Glance</h3><ul>{li}</ul></div>'
        right_html = f'<div class="code-block">{s["code"]}</div>'
        body = f'<div class="body"><div class="code-grid">{left_html}{right_html}</div></div>'

    elif kind == "notebooks":
        cards = ""
        for num, title, desc, is_core in s["notebooks"]:
            cls = "core" if is_core else ("deploy" if num == "07" else "setup")
            cards += f'''<div class="nb-card {cls}">
  <div class="nb-badge">NB {num}</div>
  <div class="nb-title">{title}</div>
  <div class="nb-desc">{desc}</div>
</div>'''
        legend = '<div class="nb-legend">← Reference &nbsp;|&nbsp; Core modelling notebooks &nbsp;|&nbsp; FAIR publication →</div>'
        body = f'<div class="body"><div class="nb-grid">{cards}</div>{legend}</div>'

    elif kind == "pizza":
        tagline = f'<div class="pizza-tagline">{s["tagline"]}</div>'
        cards = ""
        for icon, topic, desc in s["cards"]:
            cards += f'<div class="pizza-card"><div class="pizza-icon">{icon}</div><div class="pizza-topic">{topic}</div><div class="pizza-desc">{desc}</div></div>'
        body = f'<div class="body">{tagline}<div class="pizza-grid">{cards}</div></div>'

    elif kind == "schedule":
        rows_html = ""
        for dur, act, content, nb in s["rows"]:
            br = 'class="break"' if act == "BREAK" else ""
            rows_html += f'<tr {br}><td class="dur">{dur}</td><td>{act}</td><td>{content}</td><td class="nb">{nb}</td></tr>'
        body = f'''<div class="body">
<table class="sched">
<thead><tr><th>Time</th><th>Activity</th><th>Content</th><th>Notebook</th></tr></thead>
<tbody>{rows_html}</tbody>
</table></div>'''

    elif kind == "resources":
        boxes = ""
        for i, (title, items) in enumerate(s["groups"]):
            li = "".join(f"<li>{it}</li>" for it in items)
            boxes += f'<div class="res-box"><h3>{title}</h3><ul>{li}</ul></div>'
        body = f'<div class="body"><div class="res-grid">{boxes}</div></div>'

    else:
        body = f'<div class="body">Unknown kind: {kind}</div>'

    return f'<div class="slide">{header_html}{body}{footer_html}</div>'


slides_html = "\n".join(render_slide(s) for s in SLIDES)

JS = """
const slides = document.querySelectorAll('.slide');
let cur = 0;
function show(n) {
  slides[cur].classList.remove('active');
  cur = (n + slides.length) % slides.length;
  slides[cur].classList.add('active');
  document.getElementById('slide-counter').textContent = (cur+1) + ' / ' + slides.length;
}
document.getElementById('prev').onclick = () => show(cur - 1);
document.getElementById('next').onclick = () => show(cur + 1);
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') show(cur + 1);
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')                     show(cur - 1);
});
document.getElementById('slide-counter').textContent = '1 / ' + slides.length;
"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>FAIR Ontology Engineering with SULO — ESWC 2026</title>
<style>{CSS}</style>
</head>
<body>
{slides_html}
<div id="nav">
  <button id="prev">◀ Prev</button>
  <span id="slide-counter">1 / {len(SLIDES)}</span>
  <button id="next">Next ▶</button>
</div>
<script>{JS}</script>
</body>
</html>
"""

with open("sulo-tutorial-intro.html", "w") as f:
    f.write(HTML)

print(f"Saved: sulo-tutorial-intro.html  ({len(HTML):,} bytes, {len(SLIDES)} slides)")
