# Report — SULO MIE 2026 Tutorial (Mary's Clinical Odyssey)

A seven-notebook curriculum that takes a learner from a single date on a clinical timeline to a publishable, FAIRness-scored, OWL 2 DL-clean ontology of one patient's breast-cancer care episode — all expressed using **only** SULO and PRO vocabularies. Total content: ~190 minutes (4-hour tutorial slot including intro, break, Q&A).

---

## i) Domain content covered

### The clinical narrative

A single longitudinal case anchors all seven notebooks: **Mary, 52, breast-cancer journey, 2026-02-18 → 2026-09-30**, ending in remission. Every demo lands on a specific dated event from her timeline.

| Date | Clinical event | Notebook where it lands |
|---|---|---|
| 2026-02-18 | Routine gynecologic visit + manual breast examination + 3 BP readings | NB1, NB4 |
| 2026-02-20 | Ultrasound of left breast | NB1 |
| 2026-02-22 | Preliminary diagnostic assessment | NB1, NB5 |
| 2026-02-25 | Core needle biopsy of left breast → tissue specimen | NB1, NB2, NB5 |
| 2026-03-01 | Histopathology: grade 2; ER+, PR+, HER2− | NB1, NB4 |
| 2026-03-01 | Confirmed diagnosis: invasive carcinoma of breast | NB5 |
| 2026-03-10 → 2026-06-15 | Neoadjuvant chemotherapy (4 cycles) | NB1, NB5 |
| 2026-07-01 | Lumpectomy of left breast | NB1, NB3 |
| 2026-09-30 | Follow-up visit (remission) | NB1, NB2 |

### Clinical concepts modelled

- **Clinical processes** at three granularities — administrative visit, sub-procedures (physical exam, breast exam, BP measurement, documentation), individual chemo administrations
- **Anatomy** — normal breast structure (nipple, mammary gland, adipose tissue, skin), and pathological tissue (tumour) located in but not part of normal anatomy
- **Roles** — patient (Mary), physician (Dr Miller as radiologist, Dr Smith as gynecologist), instrument (biopsy needle), location (the breast), output (the tissue specimen)
- **Qualitative clinical features** — tumour grade (1/2/3), receptor status (ER/PR/HER2 each ±)
- **Quantitative clinical features** — systolic blood pressure with mmHg unit, threshold-classified
- **Disease itself** — invasive carcinoma modelled as a *Process* the body undergoes, distinct from the *tumour* (SpatialObject) and from the *diagnosis statement* (InformationObject) that refers to it
- **Diagnosis lifecycle** — preliminary vs confirmed, distinguished by a quality on the statement
- **Prescription / treatment plan** — non-instantiated future processes referred to via a Collection
- **Cross-system identity** — Mary in MIE linked via `owl:sameAs` to a mock FHIR `Patient/12345`

### What was deliberately **not** covered

- Admission/discharge events (would have repeated visit-process modelling without new lesson)
- Per-drug administration sub-types (would have rehearsed the PRO pattern without new content)
- Surgical sub-process decomposition (process parthood is already taught on the Feb 18 visit)
- Time-varying features and temporal logic (Mary's disease goes from active to remission, but the *transition* is not modelled — only the two states)
- Realisable-entity ontology (BFO-style dispositions, capabilities)

---

## ii) SULO classes used

### Top-level categories

All ten of SULO's principal categories appear, with `Process` taught first (NB1) and information/identity machinery last (NB5).

| SULO class | First used | What it represents in MIE | Local sub-classes |
|---|---|---|---|
| `sulo:Process` | NB1 | Clinical events that take time | 12 sub-classes |
| `sulo:Time`, `TimeInstant`, `StartTime`, `EndTime` | NB1 | Time anchors for processes | (used directly, not subclassed) |
| `sulo:Role` | NB2 (via PRO) | Reified participation tokens | (via PRO sub-classes) |
| `sulo:SpatialObject` | NB2, NB3 | Body parts, persons, equipment, specimens | 11 sub-classes |
| `sulo:Feature` | (parent of qualities) | – | – |
| `sulo:Quality` | NB4 | Categorical features (BP-quality, tumour grade, receptor statuses, diagnosis status) | 13 sub-classes |
| `sulo:Quantity` | NB4 | Numeric measurements with units | 2 sub-classes (`BPMeasurement`, `HypertensiveReading`) |
| `sulo:Unit` | NB4 | Unit of measure | 1 sub-class (`MmHgUnit`) |
| `sulo:InformationObject` | NB5 | Diagnosis statements, prescriptions | 2 sub-classes (`DiagnosisStatement`, `MedicationPrescription`) |
| `sulo:Collection` | NB5 | Set of future administrations | (used directly) |

**Inventory in `dist/mie-05.owl`**: 48 classes, of which all are either subclasses of SULO's top categories or of PRO's role/process subtypes.

### PRO (Process-Role-Object) classes used

| PRO class | Used for |
|---|---|
| `pro:TransformationProcess` | Biopsy (tissue specimen emerges) |
| `pro:DevelopmentalProcess` | Follow-up visit (patient persists) |
| `pro:AgentRole` | Mary's clinicians' agency in procedures |
| `pro:PatientRole` | Mary as subject of care |
| `pro:InstrumentRole` | Biopsy needle |
| `pro:LocationRole` | Breast as procedural location |
| `pro:EmergingRole` | Tissue specimen as procedural output |

The four remaining PRO classes (`ConsumedRole`, `DevelopmentRole`, `PersistingRole`) are imported but not exercised — left available for participant interactions not covered in this tutorial.

---

## ii) SULO properties used

A central constraint of the tutorial: **the MIE ontology declares zero local object or data properties.** Every relation is from SULO. Inventory of which SULO relations are exercised and where:

| Property | Characteristic | First use | Used for |
|---|---|---|---|
| `sulo:hasPart` | TransitiveProperty | NB5 (chemo→admins) | Process-level decomposition |
| `sulo:hasDirectPart` | Sub-property of hasPart, non-transitive | NB1, NB3 | Cardinality-bearing parthood — visit decomposition, anatomical composition |
| `sulo:atTime` | – | NB1 | Anchoring processes to time |
| `sulo:hasValue` | FunctionalProperty (data) | NB1, NB4 | Numeric values, datetimes |
| `sulo:precedes` | (not transitive in SULO; closure via SPARQL property path) | NB1 | Instance-level temporal ordering |
| `sulo:hasParticipant` | – | NB2 | Process → role linkage |
| `sulo:isFeatureOf` | – | NB2, NB4, NB5 | Role → bearer; Quality → bearer |
| `sulo:hasFeature` | Inverse of isFeatureOf | NB4, NB5 | Bearer → Quality |
| `sulo:refersTo` | – | NB4, NB5 | Quantity → Quality; InformationObject → its referent |
| `sulo:isIn` | TransitiveProperty | NB5 | Spatial containment (tumour in breast) |
| `sulo:hasItem` | – | NB5 | Collection → administration |

Notably **omitted from the tutorial** (available in SULO but no occasion to use): `sulo:contains` (inverse of isIn), `sulo:isPartOf` (used only implicitly via the directionality of hasPart assertions), `sulo:isPrecededBy`, `sulo:isTimeOf`.

---

## ii) Design patterns

### PRO — Process-Role-Object pattern (NB2)

The central design pattern of the tutorial, taught once in depth and used by all subsequent notebooks. The pattern reifies *how* an entity participates in a process by interposing a Role between them:

```
process  --sulo:hasParticipant-->  role  --sulo:isFeatureOf-->  object
        \-- one property -------/        \-- one property ---/
```

Two payoffs:
1. **One participation property suffices.** No `hasInstrument`, `hasPerformer`, `hasAnatomicalSite` — the role's class (`InstrumentRole`, `AgentRole`, `LocationRole`) carries the semantics.
2. **Domain growth adds classes, not properties.** New role types extend the role taxonomy; the property vocabulary stays small and aligned with SULO.

NB2 also introduces a complementary modelling choice that the original PRO publication leaves implicit:

**Persistent roles vs event-bound roles.** A role's identity grain depends on whether its *bearer* persists. Mary is the subject of care throughout her odyssey → one `mary_patient_role` reused by every procedure she participates in. The tissue specimen comes into existence only at the biopsy → one `specimen_emerging_role_feb25` bound to that event.

| Role bearer | Role kind | Naming convention |
|---|---|---|
| Persons (Mary, Drs Miller and Smith) | Persistent | `mary_patient_role`, `miller_agent_role`, `smith_agent_role` (no date suffix) |
| Event-specific objects (specimen, needle, location-of-procedure) | Event-bound | `…_role_feb25` (with date suffix) |

### SOLID — Single Object Literal Information Datum (NB4)

The SOLID pattern resolves the temptation to introduce many domain-specific data properties (e.g. `hasBloodPressure`, `hasTumourGrade`, `hasReceptorStatus`) by routing every measurement through a Quantity individual with one functional data property `sulo:hasValue`:

```
                 sulo:refersTo   ───>  Quality (e.g. SystolicBloodPressure)
Quantity individual ──> hasPart  ───>  Unit (e.g. MmHgUnit)
                 sulo:hasValue   ───>  literal (e.g. 142)
```

In MIE, the SOLID pattern is exercised by `BPMeasurement` in NB4. Three BP readings on Mary (118, 142, 165 mmHg) become three Quantity individuals, each carrying the same Unit and referring to the same Quality, with distinct numeric values. The OWL machinery (`ConstrainedDatatype` for thresholding) then classifies the readings ≥ 140 as `HypertensiveReading` without inventing any domain-specific predicate.

The pattern is *not* used for tumour grade or receptor status (NB4 §4–5) — these are categorical and properly modelled as `Quality` subclasses attached via `hasFeature`. The decision rule is pedagogically explicit: **numeric → SOLID with Quantity; categorical → Quality subclass + AllDisjoint**.

### Collection / hasItem pattern (NB5)

A third pattern, taught once in NB5 §3, resolves the question *how do you refer to a process that has not yet been instantiated?* The prescription is written before the infusions occur:

```
MedicationPrescription  ⊑  refersTo some (Collection ⊓ hasItem some MedicationAdministration)
```

The Collection is an `InformationObject` whose `hasItem` is the (eventually populated) set of administrations. The prescription points at the Collection; the actual administration individuals can be added later as they occur.

### Diagnosis triangle (NB5)

A fourth pattern — taught implicitly through example rather than explicitly named — disambiguates three entities that are routinely conflated in clinical informatics:

```
DiagnosticAssessment (Process)
      | (outputs)
      v
DiagnosisStatement (InformationObject) -- refersTo --> BreastCancer (Process)
      |
      | hasFeature
      v
preliminary_status / confirmed_status (Quality)
```

The disease itself is a Process. The statement *about* the disease is an InformationObject. The act of *making* the statement is a Process distinct from both. Status (preliminary, confirmed) is a Quality of the *statement*, not of the disease. This three-entity disambiguation is the most consistently mis-modelled construct in clinical ontologies.

---

## iii) OWL constructs used

### Structural and declaration

| Construct | First use | Anchor |
|---|---|---|
| Class declaration | NB1 | 11 Process subclasses |
| Subclass axiom (`is_a`) | NB1 | `SCT_…` ⊑ `sulo:Process` |
| Named individual | NB1 | Mary's event individuals |
| Multiple typing (subclass of two parents) | NB2 | `SCT_CoreNeedleBiopsyOfBreast` ⊑ `sulo:Process` ⊓ `pro:TransformationProcess` |
| AnnotationProperty declaration | NB7 | dc/dcterms/vann/pav/dcat/foaf/schema/mod terms |
| `rdfs:label` with language tag | NB1 onward | `locstr("…", "en")` on every class |
| `rdfs:comment` (added at deployment in NB7) | NB7 | Label-as-fallback for FAIRness R1.4b |

### Class expressions

| Construct | First use | Anchor demo |
|---|---|---|
| Existential restriction `some` | NB1 | `atTime some StartTime` |
| Universal restriction `only` | NB3 | `hasDirectPart only (Nipple ⊔ MammaryGland ⊔ AdiposeTissue ⊔ SkinOfBreast)` |
| Intersection `&` | NB1, NB2 | nested PRO restrictions on biopsy class |
| Union `\|` | NB4 | `Grade2 ⊔ Grade3`; `(hasFeature.some ERPositive ⊔ hasFeature.some PRPositive)` |
| Value restriction `value` | NB5 | `hasFeature value confirmed_status` |
| Exact cardinality `exactly` | NB1, NB3 | `hasDirectPart exactly 1 SCT_PhysicalExamination`; `hasDirectPart exactly 1 Nipple` |
| Max cardinality `max` | NB1 | `hasDirectPart max 1 SCT_ClinicalDocumentation` |
| Nested existentials | NB2 | `hasParticipant some (PatientRole ⊓ isFeatureOf some Person)` |
| Constrained datatype | NB4 | `ConstrainedDatatype(int, min_inclusive=140)` inside `hasValue.some(...)` |

### Axiom types

| Construct | First use | Anchor demo |
|---|---|---|
| `EquivalentClasses` (defined class) | NB2 | `ProcedureProducingTissueSpecimen`; later `Breast`, `HypertensiveReading`, `IntermediateOrHighGradeTumour`, `HormoneReceptorPositive`, `LocalisedBreastTumour`, `ConfirmedDiagnosis` |
| `AllDisjoint` (classes) | NB3 | 4-way over anatomical parts; later over grade classes and 3 receptor-status pairs and 2 diagnosis statuses |
| `AllDifferent` (individuals) | NB5 | The 4 chemo administration individuals |
| `owl:sameAs` | NB5 | Mary ↔ FHIR Patient/12345 (via `equivalent_to.append()` on individual) |
| TransitiveProperty (inherited from SULO) | (everywhere) | `hasPart`, `isIn` |
| FunctionalProperty (inherited from SULO) | (NB1, NB4) | `hasValue` |
| `owl:versionIRI` | NB7 | `https://w3id.org/ontostart/mie/releases/1.0.0/mie.owl` |
| `owl:imports` | NB1, NB2 | SULO and PRO |

### The split-definition pattern (NB3)

A distinctive OWL pattern foregrounded explicitly in NB3 §4 — *equivalent_to* with existentials only (drives classification under OWA), *plus* sub-class axioms with cardinality and universal closure (active constraints on classified individuals):

```
Breast ≡ SpatialObject ⊓ hasDirectPart some Nipple
                       ⊓ hasDirectPart some MammaryGland
                       ⊓ hasDirectPart some AdiposeTissue
                       ⊓ hasDirectPart some SkinOfBreast

Breast ⊑ hasDirectPart exactly 1 Nipple
Breast ⊑ hasDirectPart only (Nipple ⊔ MammaryGland ⊔ AdiposeTissue ⊔ SkinOfBreast)
```

This pattern is the deepest OWL insight the tutorial teaches: **under OWA, existentials drive classification; cardinality and universals constrain it.** It is verified empirically by Mary's right breast (a fresh untyped SpatialObject) being classified as `Breast` from its four anatomical parts alone.

### SPARQL constructs (NB1, NB5, NB6)

| Construct | First use | Anchor demo |
|---|---|---|
| Property path `+` (one-or-more) | NB1 | `sulo:precedes+` to recover the timeline closure |
| Property path `*` (zero-or-more) | NB6 | `sulo:precedes*` to include the starting event |
| Parameter substitution (`??1`) | NB1 | bound subject in property-path query |
| `COUNT(DISTINCT …)` | NB5, NB6 | counting chemo administrations |
| `UNION` for symmetric traversal | NB6 | bidirectional `owl:sameAs` matching |
| Multi-hop joins | NB5, NB6 | prescription → Collection → administration |
| Type-based filtering | NB6 | `?x rdf:type mie:HypertensiveReading` |
| `FILTER` | NB6 | excluding `owl:NamedIndividual` from class enumerations |

### FAIR-publishing constructs (NB7)

| Vocabulary | Terms used |
|---|---|
| OWL | `versionIRI`, `versionInfo`, `imports` |
| Dublin Core Elements | `creator` |
| Dublin Core Terms | `title`, `description`, `alternative`, `contributor`, `publisher`, `license`, `created`, `issued`, `modified`, `language`, `bibliographicCitation` |
| VANN | `preferredNamespacePrefix`, `preferredNamespaceUri` |
| PAV | `authoredBy` |
| DCAT | `accessURL` |
| FOAF | `homepage` |
| MOD | `status`, `definitionProperty`, `prefLabelProperty`, `hasRepresentationLanguage`, `hasSyntax` |

Three RDF post-processing fixes in NB7 §3 ensure OWL 2 DL compliance: strip core-vocabulary AnnotationProperty declarations, convert `owl:versionIRI` literal to URIRef, canonicalise ontology IRI to the trailing-slash form.

---

## Summary

### What the tutorial teaches

| Layer | What lands |
|---|---|
| **Domain** | A full clinical episode end-to-end — events, anatomy, features, diagnosis, treatment, identity — modelled rigorously |
| **SULO** | All 10 top-level categories used; 11 SULO properties exercised; **zero local object/data properties added** |
| **Design patterns** | PRO (NB2, deep), SOLID (NB4), Collection/hasItem (NB5), Diagnosis triangle (NB5) — each taught once and reused |
| **OWL** | ~25 distinct constructs across structural, expression, axiom, datatype, and metadata layers — each demonstrated with a classification that the reasoner produces |
| **Process** | Reasoner runs at every notebook (consistency); SPARQL queries answer 5 clinical questions; FAIR-publishing pipeline produces RDF/XML + Turtle with FOOPS!-readable metadata |

### What sets it apart from comparable tutorials

- **Pure SULO discipline** — no domain-specific properties invented anywhere, demonstrating that SULO's vocabulary is sufficient for clinical modelling
- **Each construct earns its place by a classification** — every defined class produces a reasoner-derived membership tied to Mary
- **No repetition of design patterns** — the PRO pattern is exercised once with full T-Box restrictions and then reused; the diagnosis triangle is constructed once
- **Honest engagement with OWA** — the universal-restriction-in-equivalent-class issue is taught explicitly in NB3 §4 with the split-definition fix
- **Pragmatic FAIR pipeline** — owlready2 quirks (versionIRI-as-literal, prefix duplication, IRI stripping, lost docstrings) are documented and addressed in NB7

### Notebook map

| NB | Topic | Cells | Time | New SULO category | New OWL construct family |
|---|---|---|---|---|---|
| NB1 | Processes, parts, time, ordering | 20 | 40 min | Process, Time | SubClass, cardinality, transitivity, SPARQL property paths |
| NB2 | Roles & the PRO pattern | 19 | 30 min | Role | Nested existentials, defined class, multiple typing |
| NB3 | Spatial objects & their parts | 17 | 25 min | SpatialObject | AllDisjoint, universal closure, split definition |
| NB4 | Qualities, quantities, thresholds | 14 | 30 min | Quality, Quantity, Unit | DataProperty, ConstrainedDatatype, Union |
| NB5 | Connections (containment / info / identity) | 13 | 30 min | InformationObject, Collection | Value restriction, AllDifferent, owl:sameAs |
| NB6 | Reasoning + SPARQL | 13 | 20 min | — | SPARQL `+`/`*`, `UNION`, `COUNT DISTINCT` |
| NB7 | FAIR publishing | 16 | 15 min | — | AnnotationProperty, versionIRI, dc/dcterms/vann/pav/dcat/foaf/mod |

### Final artefacts

```
dist/mie.owl   ←  RDF/XML, OWL 2 DL-clean, FAIRness 12/12 on the local indicator panel
dist/mie.ttl   ←  Turtle, same content
```

48 classes, 66 individuals, 0 local object properties, 0 local data properties — Mary's clinical odyssey, expressed entirely through SULO.
