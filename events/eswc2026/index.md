---
layout: default
title: FAIR Ontology Engineering with SULO
description: An ESWC 2026 Tutorial
---

## Overview
Designing high-quality ontologies that are Findable, Accessible, Interoperable, and Reusable (FAIR) remains a key challenge in
practice. This tutorial introduces a fully integrated workflow for principled ontology engineering based on the Simplified Upper Level Ontology
(SULO), a lightweight upper-level ontology designed to guide conceptual representation. Through a hands-on, end-to-end examples, participants
will (re)conceptualize, formalize, and automatically reason over the pizza domain using SULO design patterns in a notebook setting. Participants will use the OntoStart platform to publish their own ontology in a FAIR manner. The tutorial is aimed at students, researchers, and practitioners building domain ontologies. Participants will learn methodology and leave with a practical skills to bootstrap their own FAIR ontology projects.


## Objectives
This tutorial addresses a persistent gap in applied ontology: the absence of accessible,
end-to-end workflows for producing FAIR, modular, reusable ontologies
with high conceptual and engineering quality. 

The tutorial objectives are to:
* Introduce a coherent, end-to-end workflow for engineering FAIR and
principled OWL ontologies, from conceptualization to publication.
* Demonstrate the value of the Simplified Upper Level Ontology ([SULO](https://w3id.org/sulo/github)) as
an upper-level ontology to guide high-quality ontology representation
across domains.
* Showcase [OntoStart](https://github.com/micheldumontier/ontostart) as a practical framework for creating FAIR ontology
projects with automated versioning, documentation, and quality assessment.
* Contrast conceptual modeling and formal implementation, using
SULO patterns to motivate OWL axioms and ontology design decisions.
* Present complementary tooling ecosystems, including Protégé and
owlready2, for interactive and programmatic ontology development and reasoning.
* Build from the legendary OWL Pizza tutorial with a diversity of representational
problems (e.g. class/individual, identity, equivalence and disjointness,
spatial (containment and mereology) and processual (transformational,
developmental), qualities, quantities, roles and information objects through
concrete examples such as the classification of pizzas based on their toppings
and their qualitative and quantitative spicyness, the loss and gain of identity
in the making of dough, the roles played by individuals and devices in the
making and delivering of pizzas (SULO Pizza Tutorial).
* Empower participants to adopt reproducible, maintainable, and FAIR
engineering practice for their own ontology projects.

## Target Audience
The tutorial aims to balance theory with hands-on ontology engineering over the pizza domain. 
The tutorial is pitched at a basic to intermediate level; no
prior knowledge of upper level ontologies or OWL is required. Attendees that
have knowledge of python may choose to implement the tutorial with python.

## Learning goals
The learning goals of the tutorial are twofold:
1. Develop competency in the use of SULO to conceptualize and formalise a domain
* Explain the role of an upper-level ontology and apply SULO’s categories and design patterns to conceptualize a domain.
* Distinguish parts, features, roles, capabilities, processes, and quantities within a domain using SULO semantics.
* Formalize domain concepts in OWL, translating SULO-based conceptual models into logical axioms.
* Re-design the pizza ontology by applying SULO patterns in OWL for the pizza domain and validate them using tooling.

2. Publish and maintain ontology projects following FAIR practices
* Initialize a new FAIR ontology project using OntoStart, including metadata files, documentation structure, and CI-based quality checks.
* Use owlready2 in Python to construct, manipulate, and reason over ontologies programmatically.
* interpret FOOPS! FAIRness reports and identify steps to improve ontology FAIRness.



### 🕒 Schedule (May 10/11 2026)

A half-day tutorial (4h) structured as a series of [Notebooks](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/README.md). The [introductory slide deck](sulo-tutorial-intro.pptx) covers the goals, methodology, and key tools.

| Duration | Activity | Content | Notebook |
| :--- | :--- | :--- | :--- |
| 10 min | Tutorial Overview  | Introduction, goals, and methodology | [Intro presentation](sulo-tutorial-intro.pptx) |
| 10 min | Reference materials| OWL, SULO, and owlready2 | [NB 00](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/00-SULO-tutorial-setup.ipynb) · [OWL Primer](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/00-OWL-primer-reference.ipynb) · [owlready2 Primer](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/00-owlready2-primer.ipynb) |
| 30 min | Spatial objects & composition | `hasPart`, `hasDirectPart`, cardinality restrictions, Open World Assumption | [NB 01](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/01-SULO-tutorial-spatial-objects.ipynb) |
| 15 min | Qualities & quantities | `hasFeature`, `refersTo`, constrained datatypes | [NB 02](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/02-SULO-tutorial-qualities-quantities.ipynb) |
| 25 min | Processes I | Transformation vs developmental processes; participation roles (PRO pattern) | [NB 03](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/03-SULO-tutorial-processes.ipynb) |
| 30 min | **Break** | | |
| 15 min | Processes II | Process parts, `precedes`, temporal ordering | [NB 03](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/03-SULO-tutorial-processes.ipynb) |
| 15 min | Information entities | Orders, receipts, individual identity, `owl:sameAs` | [NB 04](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/04-SULO-tutorial-information-entities.ipynb) |
| 15 min | Time | Time instants, durations, constrained durations, timelines | [NB 05](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/05-SULO-tutorial-time.ipynb) |
| 15 min | Spatial containment | `isIn` vs `hasPart`, containment transitivity | [NB 06](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/06-SULO-tutorial-spatial-containment.ipynb) |
| 20 min | OntoStart & FAIRness | Metadata, OWL export, GitHub CI, FOOPS! assessment | [NB 07](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/pizza/07-SULO-tutorial-deployment.ipynb) |
| 10 min | Q&A + wrap-up | Modelling discussion and open questions | |



### Speakers
[**Michel Dumontier**](https://www.maastrichtuniversity.nl/mj-dumontier) is the Distinguished Professor of Data Science at Maastricht
University and co-founder of the Department of Advanced Computing
Sciences. He is a leading researcher in biomedical ontologies, knowledge graphs,
and Semantic Web technologies. He co-founded the FAIR principles, leads major
EU and US research initiatives, and has extensive experience teaching ontology
engineering, knowledge graphs, and Semantic Web technologies at undergraduate
and graduate level. He is a co-creator of SULO and created the OntoStart
FAIR ontology template project.

[**Chang Sun**](https://www.maastrichtuniversity.nl/chang.sun) is an Assistant Professor in the Department of Advanced Computing
Sciences at Maastricht University. Her research focuses on federated learning,
privacy-preserving data analysis, synthetic health data, and knowledge representation for health data.
She has extensive experience teaching data science and artificial intelligence.
