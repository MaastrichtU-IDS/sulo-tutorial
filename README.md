# SULO Tutorials

Interactive tutorials for building domain ontologies in [OWL](https://www.w3.org/TR/owl2-overview/) using the [SULO upper-level ontology](https://w3id.org/sulo/github). Tutorials are implemented as Jupyter notebooks using Python and [owlready2](https://owlready2.readthedocs.io), with automated reasoning via HermiT.

SULO (Simplified Upper Level Ontology) provides a lightweight set of categories — `SpatialObject`, `Quality`, `Quantity`, `Process`, `Role`, `InformationObject`, `Time` — and relations that guide principled, FAIR ontology design across domains.

---

## Tutorials

### Pizza — FAIR Ontology Engineering with SULO

A complete, end-to-end ontology engineering tutorial using the pizza domain. Students build a single OWL ontology incrementally across seven notebooks, guided by SULO design patterns, validated with automated reasoning at each step, and published following FAIR principles.

**Topics covered:** spatial composition, qualities and quantities, processes and roles, information entities, time, spatial containment, ontology metadata and FOOPS! FAIRness assessment.

Notebooks: [`notebooks/pizza/`](https://github.com/MaastrichtU-IDS/sulo-tutorial/tree/main/notebooks/pizza) — see the [Pizza Tutorial README](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/README.md) for a full overview of learning objectives, SULO coverage, and OWL constructs.

**Tutorials:**
- [FAIR Ontology Engineering with SULO](https://maastrichtu-ids.github.io/sulo-tutorial/events/eswc2026/) at [ESWC 2026](https://2026.eswc-conferences.org/program/workshops-tutorials/). May 10, 2026


### Clinical Data Modeling with SULO

A clinical-domain tutorial built around *Mary's Clinical Odyssey* — a single breast-cancer patient journey from routine visit to remission. Each notebook formalises one scene from the timeline using SULO categories and the Participation Role Object (PRO) pattern, validates with HermiT, and verifies inferences with SPARQL.

**Topics covered:** processes and temporal ordering, the PRO pattern for clinical participation, spatial objects and anatomical parts, qualities and quantities (with thresholds), information objects and identity, reasoning & SPARQL over the resulting ontology.

Notebooks: [`notebooks/mie2026/`](https://github.com/MaastrichtU-IDS/sulo-tutorial/tree/main/notebooks/mie2026)

**Tutorials:**
- [Clinical Ontology Engineering with SULO](https://maastrichtu-ids.github.io/sulo-tutorial/events/mie2026/) at [MIE 2026](https://mie2026.efmi.org/). May 26, 2026.
- Clinical Data Modeling with SULO at [SWAT4HCLS 2026](https://www.swat4ls.org/). March 23, 2026.
