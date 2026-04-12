# SULO Pizza Tutorial

A hands-on, end-to-end introduction to principled OWL ontology engineering using the **pizza domain** as a running example. You will build a single pizza ontology incrementally across seven notebooks, adding richer structure and semantics at each step. By the end you will have a FAIR-ready, reasoner-validated OWL ontology covering spatial composition, qualities, quantities, processes, information entities, time, and spatial containment.

The notebooks build on the foundation established by the classic Manchester Pizza Tutorial and extend it significantly, using [SULO](https://w3id.org/sulo) (Simplified Upper Level Ontology) to motivate every design decision.

---

## Prerequisites

Start with the setup notebook at the repository root before opening any of these:

| Notebook | What it covers |
|---|---|
| [`../00-SULO-tutorial-setup.ipynb`](../00-SULO-tutorial-setup.ipynb) | Install dependencies, load SULO from the web, visualise the SULO class hierarchy and property map, run the HermiT reasoner on SULO |

---

## Notebook Sequence

The notebooks must be run **in order**. Each one loads the ontology saved by the previous one (`pizza-NN.owl`) and writes `pizza-NN+1.owl` plus `dist/pizza-NN+1.{owl,ttl}`.

### [01 — Spatial Objects & Composition](01-SULO-tutorial-spatial-objects.ipynb)

**You will learn:** How to declare OWL classes, organise them into a hierarchy, and express necessary and/or sufficient conditions for class membership using part-whole composition.

A pizza is defined compositionally: it has exactly one crust, which has exactly one cornicione. You will discover why cardinality restrictions require a *non-transitive* sub-property (`hasDirectPart` rather than `hasPart`) and how the Open World Assumption requires explicit disjointness and universal restrictions to close class definitions.

**Core concept:** A `TraditionalFourCheesePizza` is only inferred as a `FourCheesePizza` once the four cheeses are declared disjoint *and* the pizza is restricted to containing *only* those cheeses.

---

### [02 — Qualities & Quantities](02-SULO-tutorial-qualities-quantities.ipynb)

**You will learn:** How to represent intrinsic characteristics (qualities) and their numeric measurements (quantities), and how to bridge qualitative and quantitative descriptions in a defined class.

Spiciness is modelled as a `Quality`. The Scoville Heat Unit is introduced as a `Unit`, and `SpicynessMeasurement` as a `Quantity` that carries a constrained numeric value. A `SpicyPizza` is defined both in terms of qualitative spiciness level *and* a minimum SHU threshold, illustrating that both kinds of definition coexist and that the reasoner can exploit either.

---

### [03 — Processes, Roles & Temporal Ordering](03-SULO-tutorial-processes.ipynb)

**You will learn:** How to represent processes with typed participants, how to distinguish identity-preserving from identity-destroying change, and how to assert sequential ordering of processes.

This notebook introduces **sulo-ext**, a small extension ontology that adds process sub-types and role classes not present in SULO core. The dough-making process is modelled twice: once linking the process directly to ingredient classes, and once using **role reification** — each ingredient plays a typed role (`TargetRole`, `OutputRole`, `AgentRole`) that precisely characterises *how* it participates.

| Process type | Identity of participants |
|---|---|
| `TransformationProcess` | Inputs are consumed; a new output comes into being |
| `DevelopmentalProcess` | The participant persists; only its qualities change |
| `CompositionProcess` | Multiple inputs merge into one new composite entity |
| `DecompositionProcess` | One input is broken into multiple new outputs |

---

### [04 — Information Entities](04-SULO-tutorial-information-entities.ipynb)

**You will learn:** What makes an information object ontologically distinct from a spatial object, how to create and annotate named individuals, and how OWL handles individual identity under the Open World Assumption.

A `PizzaOrder` and a `PizzaReceipt` are introduced as `InformationObject` subclasses. You will create individuals, attach data properties, assert that two names refer to the same individual (`owl:sameAs`), and assert that a set of individuals are pairwise distinct (`AllDifferent`). A defined class (`OrderForFourCheesePizza`) is used to show that the reasoner can classify order individuals.

---

### [05 — Time](05-SULO-tutorial-time.ipynb)

**You will learn:** How to model time instants, durations, and constrained durations, how to anchor processes to time, and how to build a complete temporal chain for a pizza order lifecycle.

SULO's time hierarchy (`TimeInstant`, `StartTime`, `EndTime`, `Duration`) is used to attach temporal structure to the pizza-making process chain. A new `temporallyPrecedes` transitive property is introduced to order time *instants* (distinct from `sulo:precedes`, which orders processes). A `DeliveryDuration` individual with a 25-minute value is classified as `ExpressDeliveryDuration` by the reasoner via a constrained datatype.

---

### [06 — Spatial Containment & Movement](06-SULO-tutorial-spatial-containment.ipynb)

**You will learn:** The crucial ontological distinction between parthood and spatial containment, why containment transitivity does not propagate into part-whole relations, and how to model an object moving between containers.

A `PizzaOven`, `PizzaDeliveryBox`, and `CustomerTable` are introduced. You will see through concrete individuals that a fridge transitively contains a pizza via a box, yet the fridge's `INDIRECT_hasPart` does *not* include the pizza's crust. A `BoxedPizza` defined class uses containment in its equivalence condition.

---

### [07 — Deployment & FAIRness](07-SULO-tutorial-deployment.ipynb)

**You will learn:** How to add ontology-level metadata required by the FAIR principles, how to version an ontology, and how to interpret a FOOPS! FAIRness assessment report.

The complete pizza ontology receives `owl:versionIRI`, `owl:versionInfo`, Dublin Core annotations (`dc:title`, `dc:description`, `dc:creator`, `dc:license`, `dc:created`), and `rdfs:label` coverage across all classes. The ontology is exported to both RDF/XML and Turtle. A self-assessment against key FOOPS! indicators is included.

---

## SULO Coverage

### Classes used

| SULO class | Introduced | Used for |
|---|---|---|
| `sulo:Object` | NB 01 | Root of all continuants |
| `sulo:SpatialObject` | NB 01 | Pizza, crust, ingredients, containers |
| `sulo:Feature` | NB 02 | Abstract superclass of qualities and quantities |
| `sulo:Quality` | NB 02 | Spiciness and its sub-levels |
| `sulo:Quantity` | NB 02 | SpicynessMeasurement, Duration |
| `sulo:Unit` | NB 02 | ScovilleHeatUnit |
| `sulo:Process` | NB 03 | Pizza-making pipeline |
| `sulo:Role` | NB 03 | Participant roles in processes |
| `sulo:InformationObject` | NB 04 | PizzaOrder, PizzaReceipt, identifiers |
| `sulo:Time` | NB 05 | Abstract superclass of temporal entities |
| `sulo:TimeInstant` | NB 05 | Order, baking, delivery timestamps |
| `sulo:StartTime` | NB 05 | OrderReceivedTime, BakingStartTime |
| `sulo:EndTime` | NB 05 | BakingEndTime, DeliveryTime |
| `sulo:Duration` | NB 05 | DeliveryDuration, BakingDuration |

### sulo-ext classes (created in NB 03)

| Class | Parent | Semantics |
|---|---|---|
| `TransformationProcess` | `sulo:Process` | Inputs consumed, output created |
| `DevelopmentalProcess` | `sulo:Process` | Participant persists, qualities change |
| `CompositionProcess` | `sulo:Process` | Multiple inputs merge into one output |
| `DecompositionProcess` | `sulo:Process` | One input splits into multiple outputs |
| `InputRole` | `sulo:Role` | Generic participant that enters a process |
| `AgentRole` | `InputRole` | Intentional director of the process |
| `TargetRole` | `InputRole` | Entity affected or consumed |
| `InstrumentRole` | `InputRole` | Tool used in the process |
| `OutputRole` | `sulo:Role` | Entity that comes into being |

### Object properties used

| Property | Domain → Range | Key characteristic | Used from |
|---|---|---|---|
| `sulo:hasPart` | SpatialObject → SpatialObject | Transitive; cannot carry cardinality restrictions | NB 01 |
| `sulo:hasDirectPart` | SpatialObject → SpatialObject | Non-transitive sub-property; safe for cardinality | NB 01 |
| `sulo:hasFeature` | Object → Feature | Links an object to its qualities or quantities | NB 02 |
| `sulo:refersTo` | Feature → Object | Links a quantity/info object to what it measures or represents | NB 02, 04 |
| `sulo:hasValue` | Quantity → literal | FunctionalProperty; must be assigned as a scalar | NB 02, 05 |
| `sulo:hasParticipant` | Process → Object | General participant relation | NB 03 |
| `se:hasDirectParticipant` | Process → Object | Non-transitive sub-property for cardinality on participants | NB 03 |
| `sulo:precedes` | Process → Process | Temporal ordering between process classes | NB 03 |
| `sulo:isFeatureOf` | Feature → Object | Inverse of hasFeature; used in role reification | NB 03 |
| `sulo:atTime` | Object → Time | Links a process or object to a time entity | NB 05 |
| `sulo:isIn` | SpatialObject → SpatialObject | Spatial containment (transitive) | NB 06 |

---

## OWL Constructs Covered

### Structural / declaration

| Construct | Introduced |
|---|---|
| Class declaration, subclass axiom | NB 01 |
| ObjectProperty declaration (domain, range) | NB 01, 03 |
| DataProperty declaration | NB 02 |
| AnnotationProperty declaration | NB 04, 07 |
| Named individual | NB 04 |

### Class expressions & restrictions

| Construct | Example use | Introduced |
|---|---|---|
| Existential restriction (`some`) | Pizza has some PizzaCrust | NB 01 |
| Universal restriction (`only`) | TraditionalFourCheesePizza hasDirectPart only (Mozzarella ∨ …) | NB 01 |
| Exact cardinality (`exactly N`) | Pizza hasDirectPart exactly 1 PizzaCrust | NB 01 |
| Min/max cardinality (`min N`, `max N`) | SlicingThePizza hasDirectPart min 4 PizzaSlice | NB 03 |
| Intersection (`&`) | Defined classes combining multiple restrictions | NB 01 |
| Union (`\|`) | Spicy pizza: SpicyHot or SpicyMedium | NB 02 |
| hasValue restriction (`value`) | Constraining individuals via property fillers | NB 04 |
| Constrained datatypes | `ConstrainedDatatype(int, min_inclusive=300000)` | NB 02, 05 |
| Nested class expressions | `hasFeature.some(Measurement & hasValue.some(...))` | NB 02 |

### Axiom types

| Construct | Introduced |
|---|---|
| EquivalentClasses (defined class) | NB 01 |
| AllDisjoint (classes) | NB 01 |
| TransitiveProperty | NB 01 (hasPart), NB 05 (temporallyPrecedes), NB 06 (spatiallyContains) |
| FunctionalProperty | NB 02 (hasValue) |
| SubObjectProperty | NB 01 (hasDirectPart ⊑ hasPart), NB 03 (hasDirectParticipant ⊑ hasParticipant) |
| AllDifferent (individuals) | NB 04 |
| owl:sameAs (individual equality) | NB 04 |

### Ontology-level / metadata

| Construct | Introduced |
|---|---|
| `owl:imports` | NB 01 (imports SULO), NB 03 (imports sulo-ext) |
| `owl:versionIRI` | NB 07 |
| `owl:versionInfo` | NB 07 |
| Dublin Core annotations (`dc:title`, `dc:description`, `dc:creator`, `dc:license`, `dc:created`) | NB 07 |
| `rdfs:label`, `rdfs:comment` | throughout |
| MIREOT import pattern | NB 02 (BioPortal term import) |
| RDF/XML and N-Triples serialisation | NB 07 |

---

## Ontology Artefacts

Each notebook writes two outputs: a root-level file used as input to the next notebook, and versioned copies in `dist/`.

```
pizza-01.owl  ←  01 (spatial objects)
pizza-02.owl  ←  02 (qualities & quantities)
pizza-03.owl  ←  03 (processes)        sulo-ext.owl (created here)
pizza-04.owl  ←  04 (information entities)
pizza-05.owl  ←  05 (time)
pizza-06.owl  ←  06 (spatial containment)
pizza-07.owl  ←  07 (deployment)

dist/
  pizza-01.{owl,ttl} … pizza-07.{owl,ttl}
  pizza.owl   ← final ontology (RDF/XML)
  pizza.nt   ← final ontology (N-Triples)
```
