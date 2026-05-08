# Tutorial Design: SULO Pizza Tutorial

Tracks what each notebook covers, what the worked examples demonstrate, and what each exercise tests.

Legend — exercise types:
- **Inline (Try it)**: short cell inserted immediately after the concept is introduced; extends the worked example
- **YOUR TURN**: self-contained exercise block at or near the end of the notebook; applies the full lesson to a new problem
- **End**: longer reflection or multi-part exercise at the close of the notebook

---

## Notebook 00 — Setup and Orientation (`00-SULO-tutorial-setup.ipynb`)

### Purpose
Environment verification, SULO exploration, and reasoner smoke-test. Run once before starting the tutorial. Does not define any pizza classes.

### Concepts covered
- The role of upper-level ontologies; why SULO was designed
- Loading an ontology from the web with owlready2; saving a local copy
- Navigating the SULO class and property hierarchy (ancestors, descendants, labels, comments)
- Running the HermiT reasoner and checking consistency

### Worked examples
| Example | Demonstrates |
|---|---|
| `get_ontology(...).load()` → inspect `base_iri` | Loading and identifying an ontology |
| `sulo.Quantity.label.en`, `sulo.Quantity.comment.en` | Accessing English-tagged annotations |
| `sulo.Quantity.descendants()` | Traversing the class hierarchy |
| `safe_call_reasoner(sulo)` | Running HermiT; interpreting `{ok, inconsistent}` |
| `get_color_tree([sulo])` | Visualising multi-ontology hierarchy with Graphviz |

### Companion reference notebooks
Two notebooks are provided as durable reference material (not part of the main sequence):

| Notebook | Content |
|---|---|
| `00-OWL-primer-reference.ipynb` | Quick-reference card: OWL constructs, axiom types, class expressions, property characteristics |
| `00-owlready2-primer.ipynb` | Comprehensive owlready2 guide — classes, individuals, object/data/annotation properties, class expressions, axioms, SPARQL, saving |

---

## Notebook 01 — Spatial Objects and Composition (`01-SULO-tutorial-spatial-objects.ipynb`)

### Concepts covered
- OWL classes, individuals, subclass axioms
- `hasPart` vs `hasDirectPart`: why cardinality restrictions require a non-transitive property
- Transitivity of `hasPart` and the `INDIRECT_` query prefix in owlready2
- Defined classes with `equivalent_to`
- Open World Assumption (OWA): why disjointness must be asserted
- Closing a class definition with `AllDisjoint` + universal restriction (`only`)

### Worked examples
| Example | Demonstrates |
|---|---|
| `FoodMaterial`, `Pizza`, `PizzaCrust`, `PizzaSauce`, `PizzaTopping` | Class declarations and subclass hierarchy |
| `Pizza.is_a.append(hasPart.exactly(1, PizzaCrust))` → reasoner error | `hasPart` is transitive; cardinality on transitive property is illegal in OWL DL |
| Switch to `hasDirectPart.exactly(1, PizzaCrust)` → consistent | `hasDirectPart` is a non-transitive sub-property that allows cardinality |
| `Pizza.INDIRECT_hasPart` → `[PizzaCrust]` | `INDIRECT_` prefix returns inferred (transitive) values |
| `Cornicione` as part of `PizzaCrust`; `Pizza.INDIRECT_hasPart` → `[Cornicione, PizzaCrust]` | Transitivity propagates parts through the hierarchy |
| `TraditionalFourCheesePizza` not classified as `FourCheesePizza` | OWA: the reasoner does not assume the four cheese instances are distinct |
| `AllDisjoint` + `only` restriction → classification succeeds | Closing a definition makes the reasoner commit to what is known |

### Inline exercises
| Location | Exercise | Tests |
|---|---|---|
| After `Pizza.INDIRECT_hasPart` → `[PizzaCrust]` | Add `hasDirectPart.exactly(1, PizzaSauce)` to `Pizza`; re-run reasoner and `INDIRECT_hasPart` | Applying `hasDirectPart`; predicting what appears in the inferred part list |
| After `Pizza.INDIRECT_hasPart` → `[Cornicione, PizzaCrust]` | Define `Dough` as a `FoodMaterial`; add `hasDirectPart.exactly(1, Dough)` to `PizzaCrust`; call `Pizza.INDIRECT_hasPart` | Understanding transitivity: `Dough` should appear even though it's not directly on `Pizza` |
| After `TraditionalFourCheesePizza` is successfully classified | Define `Prosciutto` (disjoint from cheeses); define `ProsciuttoMozzarellaPizza` with `only` restriction; check if it's a `FourCheesePizza` | Full defined-class pattern; predicting classification based on the definition of `FourCheesePizza` (requires exactly 4 `Cheese` instances, not 1) |

### End exercises
| Exercise | Tests |
|---|---|
| Define `TomatoSauce ⊑ PizzaSauce`; define `MargheritaPizza` (1 TomatoSauce, 1 Mozzarella, nothing else); verify it is NOT a `FourCheesePizza` | Applying the full pattern; reading classification output |
| Define three disjoint crust types; define `ThinCrustPizza`; create a `ThickCrust` individual and confirm it can't be a `ThinCrustPizza` | Disjoint subclasses; individual assertions; negation via disjointness |
| Define `VegetarianTopping` subclasses; define `VegetarianPizza` with `only` restriction; show inconsistency when pepperoni pizza is forced to be vegetarian | Universal restriction; detecting inconsistency with `AllDisjoint` + conflicting assertion |

---

## Notebook 02 — Qualities and Quantities (`02-SULO-tutorial-qualities-quantities.ipynb`)

### Concepts covered
- `sulo:Quality` as an intrinsic, specifically-dependent feature of an entity
- Categorical qualities: disjoint levels of a quality (e.g. `SpicyHot`, `SpicyMild`, `SpicyMedium`)
- `sulo:Quantity` and `sulo:Unit`: numeric measurement of a quality
- `ConstrainedDatatype` for numeric value restrictions (`min_inclusive`, `max_inclusive`)
- `hasFeature` and `refersTo` for linking objects to qualities and quantities
- Bridging quality and quantity: two parallel definitions of `SpicyPizza` (qualitative and quantitative)

### Worked examples
| Example | Demonstrates |
|---|---|
| `Spiciness ⊑ Quality`; `SpicyHot`, `SpicyMild`, `SpicyMedium` disjoint | Categorical quality hierarchy |
| `SpicySalami` with `hasFeature.some(SpicyHot ⊔ SpicyMedium)` | Assigning a quality to a food material |
| `SpicyPizza` defined by `hasPart.some(hasFeature.some(SpicyHot ⊔ SpicyMedium))` | Defined class based on a transitive quality chain |
| `SpicySalamiPizza` classified as `SpicyPizza` | Reasoning through composed class expressions |
| `ScovilleHeatUnit ⊑ Unit`; `SpicinessMeasurement ⊑ Quantity` | Quantity with unit and constrained value |
| `HotPepper` with SHU ≥ 500,000; `HotPepperPizza` not initially classified as `SpicyPizza` | Gap between qualitative and quantitative definitions |
| Add quantitative branch to `SpicyPizza.equivalent_to`; classification succeeds | Bridging quality and quantity |

### End exercises
| Exercise | Tests |
|---|---|
| Define `Crunchiness` quality; three disjoint levels; `CrispyPizza` defined by crust crunchiness | Applying quality hierarchy pattern to a new quality |
| Define `BakingTemperatureMeasurement`; `WoodFiredTemperature` with `hasValue ≥ 450`; `WoodFiredPizza` | Quantity pattern with constrained datatype |
| Explain quality–quantity gap for `HotPepperPizza`; add axiom directly linking `SpicyHot` to SHU ≥ 300,000 | Understanding the OWA gap; bridging quality and quantity |

---

## Notebook 03 — Processes (`03-SULO-tutorial-processes.ipynb`)

### Concepts covered
- `sulo:Process` as a temporally extended event
- Process sub-types: `TransformationProcess` (identity-changing), `DevelopmentalProcess` (identity-preserving), `CompositionProcess`, `DecompositionProcess`
- `hasDirectParticipant` (sub-property of `hasParticipant`) for cardinality restrictions on process participants
- Role reification: `InputRole`, `TargetRole`, `OutputRole`, `AgentRole` mediate between process and participant
- `sulo:precedes` for relative temporal ordering of processes

### Worked examples
| Example | Demonstrates |
|---|---|
| `MakingThePizzaDough` as `TransformationProcess`; ingredients as `hasDirectParticipant.exactly` | Process with consumed inputs |
| Role-based variant `MakingThePizzaDough_with_Roles` | Role reification distinguishes consumed/created participants |
| `ProofingTheDough` as `DevelopmentalProcess` | Identity-preserving process |
| `AssemblingThePizza` as `CompositionProcess` | Combination of inputs into a new whole |
| `DoughBaking` and `CheeseMelting` as sub-processes of `BakingThePizza` | Composite process with sub-processes of different types |
| `SlicingThePizza` as `DecompositionProcess` | Decomposition of a whole into parts |
| `precedes` chain from `MakingThePizzaDough` to `SlicingThePizza` | Relative temporal ordering at the TBox level |

### End exercises
| Exercise | Tests |
|---|---|
| Define `PackagingThePizza` as `CompositionProcess`; chain after `SlicingThePizza` | Applying process and temporal-ordering patterns |
| Model chef as `AgentRole` participant in dough-making and assembly | Role-based participant modelling |
| Refine `Pizza` into `RawPizza` and `BakedPizza`; update `Assembling` and `Baking` processes | Disjoint class refinement; updating process I/O |

---

## Notebook 04 — Information Entities (`04-SULO-tutorial-information-entities.ipynb`)

### Concepts covered
- `sulo:InformationObject` as an entity whose primary function is to carry meaning *about* something else (distinct from `sulo:SpatialObject`)
- `sulo:Document`, `sulo:Record` as sub-types; `sulo:DataItem` for atomic data values
- `refersTo` for linking an information object to what it is about
- OWL individual creation and ABox assertions
- Unique Name Assumption (UNA) vs Open World Assumption: two names do not automatically denote different things
- `AllDifferent` to enforce distinct individual identity
- `owl:sameAs` (`equivalent_to` on individuals in owlready2) to assert identity across identifiers
- Defined classes for information entities: `OrderForFourCheesePizza`, `OrderForSpicyPizza`
- Recipe-to-realization: `PizzaRecipe` as an `InformationObject` that `refersTo` a `PizzaMakingProcess`

### Worked examples
| Example | Demonstrates |
|---|---|
| `PizzaOrder ⊑ InformationObject`; `PizzaReceipt ⊑ InformationObject` | Core information-entity subclasses |
| `OnlineOrder`, `PhoneOrder ⊑ PizzaOrder`; disjoint | Specialising an information class |
| `OrderIdentifier ⊑ DataItem`; `OrderAmount ⊑ Quantity` | Nested data items and measurement quantities |
| `order_001`, `order_002` individuals; no `AllDifferent` → reasoner may merge them | OWA / UNA demonstration |
| `AllDifferent([order_001, order_002])` → distinct identity confirmed | Enforcing identity explicitly |
| `order_001_legacy.equivalent_to.append(order_001)` | `owl:sameAs` merging two records of the same order |
| `OrderForFourCheesePizza` defined as `PizzaOrder & refersTo.some(FourCheesePizza)` | Defined class for information entities |
| `OrderForSpicyPizza` defined as `PizzaOrder & refersTo.some(SpicyPizza)` | Reusing defined classes across domains |
| `PizzaMakingProcess` defined as a sequence through all pizza-making sub-processes | Process as object of description |
| `PizzaRecipe ⊑ InformationObject` with `refersTo.some(PizzaMakingProcess)` | Recipe-to-realization pattern |

### YOUR TURN exercises
| Exercise | Tests |
|---|---|
| **YOUR TURN 1 — NutritionalLabel**: Define `NutritionalLabel ⊑ InformationObject` (`refersTo some FoodMaterial`); define `CalorieCount ⊑ Quantity`; create a `NutritionalLabel` individual for `PizzaSlice` with a `CalorieCount` attached | Full information-entity pattern; `refersTo`; quantity attachment; individual creation |

---

## Notebook 05 — Time (`05-SULO-tutorial-time.ipynb`)

### Concepts covered
- SULO time hierarchy: `TimeInstant`, `StartTime`, `EndTime`, `Duration`
- `sulo:atTime` for linking entities to time individuals; `sulo:isTimeOf` (inverse of `atTime`) used in defined `TimeInstant` subclasses
- `ConstrainedDatatype` for `Duration` value restrictions
- TBox-level temporal annotation with `atTime.some()` on process classes
- ABox-level temporal chain with `precedes` on process individuals
- `INDIRECT_temporallyPrecedes` for transitive ordering queries
- Reasoner classification of duration individuals against defined duration classes

### Worked examples
| Example | Demonstrates |
|---|---|
| `OrderReceivedTime`, `BakingStartTime/EndTime`, `DeliveryTime` defined with `equivalent_to` using `isTimeOf.some(...)` | Defined `TimeInstant` subclasses tied to specific process types |
| `DeliveryDuration ⊑ Duration`; `ExpressPizzaDelivery` defined with `hasValue ≤ 30` | Constrained `Duration` as a defined class |
| `BakingThePizza.is_a.append(atTime.some(BakingStartTime))` etc. | TBox-level temporal annotation of process classes |
| `t_order → t_bake_start → t_bake_end → t_delivery` with `precedes` assertions; `INDIRECT_temporallyPrecedes` | Instance-level temporal ordering and transitivity |
| `dur_001.hasValue = 25.0`; reasoner classifies it as `ExpressPizzaDelivery` | Individual classification against constrained datatype |

### YOUR TURN exercises
| Exercise | Tests |
|---|---|
| **YOUR TURN 1 — ProofingDuration**: Define `ProofingDuration ⊑ Duration` with `hasValue ≥ 60`; define `SlowFermentedDough` as a `FoodMaterial` with `hasFeature.some(ProofingDuration)`; run reasoner | Duration + constrained datatype + defined class; TBox-level feature constraint |
| **YOUR TURN 2 — PizzaOrderFulfillment**: Define `PizzaOrderFulfillment` as a defined `Process` with `hasPart.some(OrderingProcess)` and `hasPart.some(DeliveringThePizza)`; create a plain `Process` individual with both parts attached; run reasoner and verify classification | Defined process class; cross-notebook composition (NB03 process types + NB05 time); individual classification |

---

## Notebook 06 — Spatial Containment (`06-SULO-tutorial-spatial-containment.ipynb`)

### Concepts covered
- `sulo:contains` and `sulo:isIn` as spatial containment (distinct from compositional `hasPart`)
- Transitivity of `contains` and `INDIRECT_contains` for inferred containment chains
- Non-propagation of containment into parthood: `contains` transitivity does not flow into `hasPart`
- Spatial role types in PRO: `ContainmentRole`, `ContainedRole`, `OnTopPositionRole`, `SurfacePositionRole`
- Container subclasses as `sulo:SpatialObject`: `PizzaOven`, `PizzaDeliveryBox`, `Table`
- `BoxedPizza` as a defined class using `isIn.some(PizzaDeliveryBox)`
- Extending `DeliveringThePizza` with spatial participant roles
- SPARQL queries on spatial relations using `default_world.sparql()`
- Role disjointness: `ContainmentRole ⊓ ContainedRole = ⊥`; detecting inconsistency

### Worked examples
| Example | Demonstrates |
|---|---|
| `my_box.contains = [my_pizza]`; `my_fridge.contains = [my_box]`; `INDIRECT_contains` → `[my_box, my_pizza]` | Transitivity of containment; `INDIRECT_` query prefix |
| `my_box.hasPart` remains empty | Containment does not imply parthood |
| `BoxedPizza` defined by `Pizza & isIn.some(PizzaDeliveryBox)`; `my_pizza` classified automatically | Defined class based on spatial relation |
| Spatial roles on `BoxingThePizza`, `UnboxingThePizza`, `PlacingPizzaOnTable` | Spatial participant roles extending PRO pattern from NB03 |
| `default_world.sparql("SELECT ...")` on `sulo:contains` | SPARQL for spatial queries; difference from inferred queries |

### YOUR TURN exercises
| Exercise | Tests |
|---|---|
| **YOUR TURN — Disjointness stress test**: Create an individual and assert it is both `ContainmentRole` and `ContainedRole`; run the reasoner and observe the inconsistency; clean up with `destroy_entity` and verify consistency is restored | Disjoint classes; individual-level inconsistency detection; `destroy_entity` as repair operation |

---

## Notebook 07 — Deployment and FAIRness (`07-SULO-tutorial-deployment.ipynb`)

### Purpose
Takes the completed pizza ontology through the metadata, export, and publishing workflow required to make it a FAIR digital resource. Uses the OntoStart CI/CD pipeline for deployment and the FOOPS! tool for automated FAIRness assessment.

### Concepts covered
- FAIR principles applied to ontologies (Findable, Accessible, Interoperable, Reusable)
- `owl:versionIRI` and `owl:versionInfo` for ontology versioning
- Ontology-level metadata vocabularies: Dublin Core (`dc:`, `dcterms:`), VANN, PAV, DCAT, FOAF, Schema.org, MOD
- Declaring `AnnotationProperty` in a named namespace in owlready2; `python_name` alias
- Term-level `rdfs:label[@en]` and `rdfs:comment` coverage; auto-generating labels from CamelCase names with `locstr`
- Exporting to RDF/XML (owlready2 native) and Turtle (via rdflib; owlready2's Turtle serialiser is broken)
- Local FOOPS! self-assessment (12 locally verifiable indicators)
- Publishing via OntoStart: branch-based CI/CD pipeline on GitHub Actions
- FOOPS! automated FAIRness assessment API (24 indicators; URI-based only — file upload unsupported)

### Workflow steps
| Step | What happens | FAIR dimension |
|---|---|---|
| 1 | `owl:versionIRI`, `owl:versionInfo` declared as annotation properties on `owl:` namespace | Findable — F2 |
| 2 | Full metadata set: `ONTO_ABBREV`, `ONTO_IRI`, DC/VANN/PAV/DCAT/FOAF/MOD annotations | Reusable — R1 |
| 3 | Audit `rdfs:label[@en]` and `rdfs:comment`; auto-fill missing `@en` labels with CamelCase splitter | Reusable — R1.4 |
| 4 | `pizza.save(format="rdfxml")` + `rdflib` conversion to Turtle | Accessible — A1 |
| 5 | Local self-assessment: 12 indicators checked in Python | All |
| 6 | `git checkout -b pizza-{name}` in OntoStart repo; push triggers GitHub Actions pipeline | All |
| 7 | FOOPS! assessment: Option A = web file upload; Option B = API call on deployed URI | All |

### Key techniques
| Technique | Why |
|---|---|
| `class creator(AnnotationProperty): namespace = dc_ns; python_name = "dc_creator"` | Class name sets the local IRI; `python_name` is the Python attribute alias — using `dc_creator` as class name would create the wrong IRI `dc:dc_creator` |
| `rdflib.Graph().parse(...).serialize(format="turtle")` | owlready2's `format="turtle"` produces a 0-byte file |
| `locstr("text", "en")` / `cls.label.en` | Language-tagged RDF labels; `.en` accessor returns only `@en` values |
| `pizza.metadata.versionIRI = [iri_string]` | owlready2 stores as string literal; rdflib post-processing needed to promote to IRI for FOOPS! VER1 |
| `foops_uri = "https://w3id.org/sulo/sulo.owl"` as demo default | FOOPS! API requires a live public URI; `ontologyContent` upload is currently broken in the API |

### Exercises
| Exercise | Tests |
|---|---|
| **Exercise 1 — Add term-level definitions**: Write `rdfs:comment` for 5 classes still missing it; re-run the local pre-check and verify `R1.4b` improves | Hand-curating `rdfs:comment`; understanding difference between auto-generated labels and meaningful definitions |
| **Exercise 2 — `owl:priorVersion`**: Add a `priorVersion` annotation pointing to `https://w3id.org/ontostart/pizza/releases/0.9.0/pizza.owl`; explain how this supports ontology provenance | OWL versioning; ontology provenance and FAIR principle F2 |
| **Exercise 3 — Identify remaining FAIRness gaps** *(reflection)*: For 4 listed gaps (missing `rdfs:comment`, unresolvable version IRI, no `priorVersion`, missing publisher), explain what the gap is, which FAIR principle it affects, and how to fix it | Connecting ontology engineering practice to FAIR principles; gap analysis |
