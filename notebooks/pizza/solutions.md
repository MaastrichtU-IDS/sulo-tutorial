# Exercise Solutions

Model solutions for all exercises in the SULO Pizza Tutorial. Exercises marked **YOUR TURN** appear inline in the notebook; numbered **Exercise N** appear at the end of each notebook.

---

## Notebook 01 — Spatial Objects & Composition

### YOUR TURN 1 — Add PizzaSauce as a class

Define `PizzaSauce` as a subclass of `FoodMaterial`.

```python
with pizza:
    class PizzaSauce(FoodMaterial):
        label = [locstr("pizza sauce", "en")]
        comment = locstr(
            "A pizza sauce is a food material used in the preparation of pizza, "
            "typically made from tomatoes and various herbs and spices.",
            lang="en"
        )
```

---

### YOUR TURN 2 — Add PizzaSauce as a required part

Add a subclass axiom requiring every pizza to have some `PizzaSauce`, then query inferred parts.

```python
with pizza:
    Pizza.is_a.append(sulo.hasDirectPart.some(PizzaSauce))

result = safe_call_reasoner(pizza)
print("Consistent:", result["ok"])
print("Pizza.INDIRECT_hasPart:", Pizza.INDIRECT_hasPart)
```

> **Why does PizzaSauce appear alongside PizzaCrust?** Both are required direct parts of `Pizza`. The reasoner propagates `hasDirectPart ⊑ hasPart`, so both show up in `INDIRECT_hasPart`.

---

### YOUR TURN 3 — Following a part chain

Define `OliveOil` and require every `TomatoSauce` to have it as a direct part, then check what `Pizza.INDIRECT_hasPart` infers.

```python
with pizza:
    class OliveOil(FoodMaterial):
        label = [locstr("olive oil", "en")]

    TomatoSauce.is_a.append(sulo.hasDirectPart.some(OliveOil))

result = safe_call_reasoner(pizza)
print("Pizza.INDIRECT_hasPart:", Pizza.INDIRECT_hasPart)
```

> **Why does OliveOil appear?** `hasPart` is transitive: Pizza hasDirectPart TomatoSauce, TomatoSauce hasDirectPart OliveOil → Pizza hasPart OliveOil. If `hasPart` were not transitive, transitivity closure would not fire and `OliveOil` would not appear.

---

### YOUR TURN 4 — Apply the full pattern to a new pizza

Define `Prosciutto` and `ProsciuttoMozzarellaPizza` with cardinality and universal restrictions.

```python
with pizza:
    class Prosciutto(FoodMaterial):
        label = [locstr("prosciutto", "en")]

    AllDisjoint([Prosciutto, Mozzarella, Gorgonzola, Parmesan, PecorinoRomano])

    class ProsciuttoMozzarellaPizza(Pizza):
        label = [locstr("prosciutto mozzarella pizza", "en")]
        equivalent_to = [Pizza
                         & sulo.hasDirectPart.exactly(1, Mozzarella)
                         & sulo.hasDirectPart.exactly(1, Prosciutto)
                         & sulo.hasDirectPart.only(
                             Mozzarella | Prosciutto | PizzaCrust | PizzaSauce)]

result = safe_call_reasoner(pizza)
print("Is FourCheesePizza:", in_ancestors(pizza, ProsciuttoMozzarellaPizza, FourCheesePizza))
```

> **Will it be a FourCheesePizza?** No. `FourCheesePizza` requires exactly four disjoint cheese parts; `ProsciuttoMozzarellaPizza` has only one cheese (`Mozzarella`) and one non-cheese (`Prosciutto`).

---

### Exercise 1 — MargheritaPizza

Define `TomatoSauce` and `MargheritaPizza`.

```python
with pizza:
    class TomatoSauce(PizzaSauce):
        label = [locstr("tomato sauce", "en")]
        comment = locstr(
            "A pizza sauce made primarily from tomatoes, garlic, and herbs.", lang="en"
        )

    AllDisjoint([TomatoSauce, Mozzarella, Gorgonzola, Parmesan, PecorinoRomano])

    class MargheritaPizza(Pizza):
        label = [locstr("margherita pizza", "en")]
        equivalent_to = [Pizza
                         & sulo.hasDirectPart.exactly(1, TomatoSauce)
                         & sulo.hasDirectPart.exactly(1, Mozzarella)
                         & sulo.hasDirectPart.only(TomatoSauce | Mozzarella | PizzaCrust)]

result = safe_call_reasoner(pizza)
print("Is FourCheesePizza:", in_ancestors(pizza, MargheritaPizza, FourCheesePizza))
```

> **Not a FourCheesePizza**: requires exactly four disjoint cheese classes; `MargheritaPizza` has only one (`Mozzarella`).

---

### Exercise 2 — VegetarianPizza

Define vegetable ingredients, `VegetarianPizza`, and demonstrate that `PepperoniPizza` is inconsistent with it.

```python
with pizza:
    class VegetableIngredient(FoodMaterial):
        label = [locstr("vegetable ingredient", "en")]

    class PepperIngredient(VegetableIngredient): pass
    class MushroomIngredient(VegetableIngredient): pass
    class ArtichokeIngredient(VegetableIngredient): pass

    AllDisjoint([PepperIngredient, MushroomIngredient, ArtichokeIngredient])

    class VegetarianPizza(Pizza):
        label = [locstr("vegetarian pizza", "en")]
        equivalent_to = [Pizza
                         & sulo.hasDirectPart.only(
                             VegetableIngredient | PizzaCrust | PizzaSauce)]

    class PepperoniIngredient(FoodMaterial):
        label = [locstr("pepperoni ingredient", "en")]

    AllDisjoint([PepperoniIngredient, VegetableIngredient, PizzaCrust, PizzaSauce])

    class PepperoniPizza(VegetarianPizza):
        equivalent_to = [VegetarianPizza
                         & sulo.hasDirectPart.some(PepperoniIngredient)]

result = safe_call_reasoner(pizza)
print("Inconsistent classes:", result["inconsistent"])
# PepperoniPizza will be flagged inconsistent:
# it must have a PepperoniIngredient part (by definition) yet VegetarianPizza
# restricts parts to VegetableIngredient | PizzaCrust | PizzaSauce only,
# and PepperoniIngredient is disjoint from all three.
```

---

## Notebook 02 — Qualities & Quantities

### YOUR TURN 1 — Saltiness quality

Define `Saltiness` with three disjoint levels, extend `AnchovyIngredient`, and define `SaltyPizza`.

```python
with pizza:
    class Saltiness(sulo.Quality):
        label = [locstr("saltiness", "en")]

    class LowSalt(Saltiness): pass
    class MediumSalt(Saltiness): pass
    class HighSalt(Saltiness): pass

    AllDisjoint([LowSalt, MediumSalt, HighSalt])

    class AnchovyIngredient(FoodMaterial):
        label = [locstr("anchovy ingredient", "en")]
        is_a = [sulo.hasFeature.some(HighSalt)]

    class SaltyPizza(Pizza):
        label = [locstr("salty pizza", "en")]
        equivalent_to = [Pizza
                         & sulo.hasDirectPart.some(
                             sulo.hasFeature.some(HighSalt))]

    class AnchovyPizza(Pizza):
        label = [locstr("anchovy pizza", "en")]
        equivalent_to = [Pizza
                         & sulo.hasDirectPart.exactly(1, AnchovyIngredient)
                         & sulo.hasDirectPart.exactly(1, PizzaSauce)
                         & sulo.hasDirectPart.only(AnchovyIngredient | PizzaSauce | PizzaCrust)]

result = safe_call_reasoner(pizza)
print("AnchovyPizza is SaltyPizza:", in_ancestors(pizza, AnchovyPizza, SaltyPizza))
```

> **Reasoning chain:** `AnchovyPizza` has exactly 1 `AnchovyIngredient`. `AnchovyIngredient` hasFeature some `HighSalt`. `SaltyPizza ≡ Pizza ⊓ hasDirectPart some (hasFeature some HighSalt)`. The chain fires and `AnchovyPizza` is classified as `SaltyPizza`.

---

### YOUR TURN 2 — Sodium measurement

Add a quantitative saltiness dimension with milligram units.

```python
with pizza:
    class Milligram(sulo.Unit):
        label = [locstr("milligram", "en")]

    class SodiumMeasurement(sulo.Quantity):
        label = [locstr("sodium measurement", "en")]
        is_a = [sulo.refersTo.some(Saltiness)]

    # Extend AnchovyIngredient with a quantitative constraint
    AnchovyIngredient.is_a.append(
        sulo.hasFeature.some(
            SodiumMeasurement & sulo.hasValue.some(
                ConstrainedDatatype(int, min_inclusive=1400))))

    # Extend SaltyPizza with a quantitative branch
    SaltyPizza.equivalent_to = [Pizza & (
        sulo.hasDirectPart.some(sulo.hasFeature.some(HighSalt))
        | sulo.hasDirectPart.some(
            sulo.hasFeature.some(
                SodiumMeasurement & sulo.hasValue.some(
                    ConstrainedDatatype(int, min_inclusive=1400)))))]

    class DesaltedAnchovyIngredient(FoodMaterial):
        label = [locstr("desalted anchovy ingredient", "en")]
        is_a = [sulo.hasFeature.some(LowSalt),
                sulo.hasFeature.some(
                    SodiumMeasurement & sulo.hasValue.some(
                        ConstrainedDatatype(int, max_inclusive=400)))]

    class DesaltedAnchovyPizza(Pizza):
        equivalent_to = [Pizza
                         & sulo.hasDirectPart.exactly(1, DesaltedAnchovyIngredient)
                         & sulo.hasDirectPart.only(
                             DesaltedAnchovyIngredient | PizzaSauce | PizzaCrust)]

result = safe_call_reasoner(pizza)
print("DesaltedAnchovyPizza is SaltyPizza:",
      in_ancestors(pizza, DesaltedAnchovyPizza, SaltyPizza))
```

> **Not a SaltyPizza**: the qualitative branch requires `HighSalt` but `DesaltedAnchovyIngredient` has `LowSalt`; the quantitative branch requires ≥ 1400 mg but the constraint caps at 400 mg. Neither branch fires.

---

## Notebook 03 — Processes, Roles & Temporal Ordering

### YOUR TURN 1 — KneadingTheDough

Model kneading as a `DevelopmentalProcess` with a `Mixer` instrument.

```python
with pizza:
    class Mixer(sulo.SpatialObject):
        label = [locstr("mixer", "en")]
        comment = locstr(
            "A kitchen appliance used to knead or mix dough mechanically.", lang="en"
        )

with pro:
    class KneadingTheDough(pro.DevelopmentalProcess):
        label = [locstr("kneading the dough", "en")]
        equivalent_to = [pro.DevelopmentalProcess
                         & sulo.hasParticipant.some(
                             pro.PersistingRole & sulo.isFeatureOf.some(pizza.PizzaDough))
                         & sulo.hasParticipant.some(
                             pro.InstrumentRole & sulo.isFeatureOf.some(pizza.Mixer))]

result = safe_call_reasoner(pizza)
print("Consistent:", result["ok"])
```

> **DevelopmentalProcess**: the dough persists and changes structure (gluten develops) but remains the same entity — its identity is maintained. A `TransformationProcess` would require destruction of inputs and creation of a new output.

---

### YOUR TURN 2 — Process classification

| Process | Classification | Key participant | Role |
|---|---|---|---|
| Grating Parmesan into shreds | `TransformationProcess` | Parmesan block | `ConsumedRole`; shreds | `EmergingRole` |
| Reducing tomato sauce | `DevelopmentalProcess` | TomatoSauce | `PersistingRole` |
| Freezing a pizza slice | `DevelopmentalProcess` | PizzaSlice | `PersistingRole` |

Implementation of **GratingTheParmesan**:

```python
with pizza:
    class ParmesanShreds(FoodMaterial):
        label = [locstr("parmesan shreds", "en")]

    class Grater(sulo.SpatialObject):
        label = [locstr("grater", "en")]

with pro:
    class GratingTheParmesan(pro.TransformationProcess):
        label = [locstr("grating the parmesan", "en")]
        equivalent_to = [pro.TransformationProcess
                         & sulo.hasParticipant.some(
                             pro.ConsumedRole & sulo.isFeatureOf.some(pizza.Parmesan))
                         & sulo.hasParticipant.some(
                             pro.EmergingRole & sulo.isFeatureOf.some(pizza.ParmesanShreds))
                         & sulo.hasParticipant.some(
                             pro.InstrumentRole & sulo.isFeatureOf.some(pizza.Grater))]
        is_a = [sulo.precedes.some(AssemblingThePizza)]

result = safe_call_reasoner(pizza)
print("Consistent:", result["ok"])
```

---

## Notebook 04 — Information Entities

### YOUR TURN 1 — NutritionalLabel

Define a `NutritionalLabel` information object with a calorie count.

```python
with pizza:
    class NutritionalLabel(sulo.InformationObject):
        label = [locstr("nutritional label", "en")]
        is_a = [sulo.refersTo.some(FoodMaterial)]

    class CalorieCount(sulo.Quantity):
        label = [locstr("calorie count", "en")]

    pizza_slice_label = NutritionalLabel("pizza_slice_label")
    calorie_value = CalorieCount("calorie_value_per_slice")
    calorie_value.hasValue = 285

    pizza_slice_label.hasFeature.append(calorie_value)
    pizza_slice_label.refersTo.append(PizzaSlice)

result = safe_call_reasoner(pizza)
print("Consistent:", result["ok"])
```

---

## Notebook 05 — Time

### YOUR TURN 1 — ProofingDuration

Define a `ProofingDuration` and a `SlowFermentedDough` defined class.

```python
with pizza:
    class ProofingDuration(sulo.Duration):
        label = [locstr("proofing duration", "en")]
        comment = locstr(
            "The time a dough is left to ferment before shaping.", lang="en"
        )

    class SlowFermentedDough(PizzaDough):
        label = [locstr("slow fermented dough", "en")]
        equivalent_to = [PizzaDough
                         & sulo.hasFeature.some(
                             ProofingDuration
                             & sulo.hasValue.some(
                                 ConstrainedDatatype(int, min_inclusive=60)))]

result = safe_call_reasoner(pizza)
print("Consistent:", result["ok"])
```

---

### YOUR TURN 2 — PizzaOrderFulfillment

Define a process that bundles ordering and delivery, then verify a plain individual is classified into it.

```python
with pizza:
    class PizzaOrderFulfillment(sulo.Process):
        label = [locstr("pizza order fulfillment", "en")]
        equivalent_to = [sulo.Process
                         & sulo.hasPart.some(OrderingProcess)
                         & sulo.hasPart.some(DeliveringThePizza)]

    fulfillment_instance = sulo.Process("my_fulfillment")
    ordering_instance    = OrderingProcess("my_ordering")
    delivery_instance    = DeliveringThePizza("my_delivery")

    fulfillment_instance.hasPart.append(ordering_instance)
    fulfillment_instance.hasPart.append(delivery_instance)

result = safe_call_reasoner(pizza)
print("Classified as PizzaOrderFulfillment:",
      PizzaOrderFulfillment in fulfillment_instance.is_a)
```

---

## Notebook 06 — Spatial Containment & Movement

### YOUR TURN — Disjointness stress test

Assert an individual belongs to two disjoint classes and observe the inconsistency.

```python
# Create a role individual asserted to be both ContainmentRole and ContainedRole
bad_role = sulo.Role("bad_role")
bad_role.is_a.append(ContainmentRole)
bad_role.is_a.append(ContainedRole)

result = safe_call_reasoner(pizza)
print("Consistent:", result["ok"])
print("Inconsistent:", result["inconsistent"])
# ContainmentRole and ContainedRole are AllDisjoint → inconsistency detected

# Clean up
destroy_entity(bad_role)
result = safe_call_reasoner(pizza)
print("Consistent after cleanup:", result["ok"])
```

---

## Notebook 07 — Deployment & FAIRness

### Exercise 1 — Add term-level definitions

Add `rdfs:comment` to five classes that are missing definitions.

```python
with pizza:
    PizzaCrust.comment    = [locstr("The outer bread structure of a pizza, forming its base and rim.", lang="en")]
    Mozzarella.comment    = [locstr("A soft Italian cheese with a mild flavour, the classic pizza cheese.", lang="en")]
    SpicyPizza.comment    = [locstr("A pizza whose ingredients include at least one ingredient with a spicy quality or a Scoville value above the spicy threshold.", lang="en")]
    PizzaDough.comment    = [locstr("An elastic mass of flour, water, yeast, and salt that forms the structural base of a pizza after baking.", lang="en")]
    BakedPizza.comment    = [locstr("A pizza that has undergone the baking process and is ready to serve.", lang="en")]
```

> Re-running the FOOPS! pre-check (Step 5) should improve the **R1.4b** (term definitions) indicator.

---

### Exercise 2 — owl:priorVersion

```python
from owlready2 import *

with pizza:
    pizza.metadata.prior_version = ["https://w3id.org/ontostart/pizza/releases/0.9.0/pizza.owl"]
```

> `owl:priorVersion` lets tooling and users trace the release lineage of the ontology. Registries such as AgroPortal and BioPortal use it to surface version history and to alert users when a newer version exists.

---

### Exercise 3 — Identify remaining FAIRness gaps

| Gap | FAIR principle | Fix |
|---|---|---|
| Most classes lack `rdfs:comment` | **R1** (rich metadata) | Add one-sentence definitions to every class and property |
| Version IRI is declared but not resolvable | **A1** (accessible via protocol) | Deploy the ontology at the w3id redirect target, or add a `303 See Other` redirect rule |
| No `owl:priorVersion` link | **I3** / **R1.2** (linked to prior versions) | Add `owl:priorVersion` pointing to the previous release IRI |
| No `dcterms:contributor` or `dcterms:publisher` | **R1.1** (provenance) | Add contributor ORCIDs and an institutional publisher annotation |
