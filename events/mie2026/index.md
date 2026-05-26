---
layout: default
title: Clinical Ontology Engineering with SULO
description: An MIE 2026 Tutorial
---

## Overview
Clinical informatics is awash in overlapping participation properties, conflated
distinctions between diseases and findings, and quantities modelled as bare numbers.
This tutorial introduces a principled, end-to-end workflow for clinical ontology
engineering based on the Simplified Upper Level Ontology ([SULO](https://w3id.org/sulo/github))
and the Participation Role Object (PRO) pattern. Through a single running clinical
case — *Mary's Clinical Odyssey*, a breast cancer journey from routine visit to remission —
participants formalize each scene as OWL, run automated reasoning, and verify the
inferred answer with SPARQL. The tutorial uses Python and
[owlready2](https://owlready2.readthedocs.io) in Jupyter notebooks, with HermiT as the reasoner.

## Objectives
* Apply SULO's upper-level categories (`Process`, `SpatialObject`, `Quality`, `Quantity`,
  `Role`, `InformationObject`, `Time`) to a clinical domain.
* Master the PRO pattern for participation — replacing dozens of ad-hoc
  participation properties with a single `Role`-mediated design.
* Distinguish disease, finding, statement, and act of diagnosis;
  anchor measurements to patients over time; refer to processes that haven't happened yet.
* Build defined classes that fire under HermiT classification, and verify inferences
  with SPARQL property paths.
* Stay within `sulo:*` / `owl:*` predicates: domain growth arrives as new
  *classes*, not new predicates — keeping the clinical ontology aligned with the upper-level.

## Target Audience
Clinical informaticians, ontology engineers, knowledge graph practitioners, and
researchers working with health data. The tutorial is pitched at a basic to intermediate
level; familiarity with OWL is helpful but not required. Working knowledge of Python is
useful to run the notebooks interactively.

## The Running Case — Mary's Clinical Odyssey
A single patient, nine clinical events, one timeline:

| Date     | Event                              |
| :------- | :--------------------------------- |
| Feb 18   | Routine visit + blood pressure     |
| Feb 20   | Ultrasound                         |
| Feb 22   | Preliminary diagnosis              |
| Feb 25   | Biopsy                             |
| Mar 1    | Histopathology + confirmed diagnosis |
| Mar 10   | Chemotherapy begins                |
| Jun 15   | Chemotherapy ends                  |
| Jul 1    | Lumpectomy                         |
| Sep 30   | Follow-up (remission)              |

Each notebook anchors a SULO construct to one or more scenes from Mary's timeline.

## 🕒 Schedule (May 26, 2026)

Half-day tutorial, 15:00 – 18:00, with a coffee break 16:30 – 17:00. The
[introductory slide deck](intro.html) covers the goals, the running case, and the SULO
+ PRO design patterns used throughout.

| Time  | Duration | Topic                                       | OWL constructs                                            | Notebook |
| :---- | :------- | :------------------------------------------ | :-------------------------------------------------------- | :------- |
| 15:00 | 15 min   | Introduction to the tutorial & SULO         | What we'll build · Mary's odyssey · SULO postcard tour    | [Intro](intro.html) |
| 15:15 | 25 min   | Processes, parts, time, ordering            | `Process`, `Time` &#124; SubClass, cardinality, SPARQL +/* | [NB 01](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/mie2026/01-MIE-processes-parts-time.ipynb) |
| 15:40 | 25 min   | Roles & the PRO pattern                     | `Role` &#124; Nested existentials, defined class           | [NB 02](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/mie2026/02-MIE-roles-PRO-pattern.ipynb) |
| 16:05 | 25 min   | Spatial objects & their parts               | `SpatialObject` &#124; `AllDisjoint`, `only`, split definition | [NB 03](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/mie2026/03-MIE-spatial-objects-parts.ipynb) |
| 16:30 | 30 min   | ☕ Coffee break                              |                                                           |          |
| 17:00 | 20 min   | Qualities, quantities, thresholds           | `Quality`, `Quantity`, `Unit` &#124; ConstrainedDatatype, union | [NB 04](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/mie2026/04-MIE-qualities-quantities.ipynb) |
| 17:20 | 20 min   | Connections — containment, info, identity   | `InformationObject`, `Collection` &#124; value restriction, `AllDifferent`, `sameAs` | [NB 05](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/mie2026/05-MIE-connections.ipynb) |
| 17:40 | 20 min   | Reasoning & SPARQL                          | (queries only) &#124; property paths, `UNION`, `COUNT DISTINCT` | [NB 06](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/mie2026/06-MIE-reasoning-sparql.ipynb) |

A seventh notebook on [FAIR publishing](https://github.com/MaastrichtU-IDS/sulo-tutorial/blob/main/notebooks/mie2026/07-MIE-fair-publishing.ipynb)
covers `versionIRI` and `dc/dcterms/vann/pav/dcat/mod` metadata; it is available as supplementary material outside the live session.

## Slides

Per-notebook slide decks (rendered from the notebooks via `nbconvert`) are linked from
the tutorial page and from each notebook header:

* [01 — Processes, parts, time, ordering](01-MIE-processes-parts-time.slides.html)
* [02 — Roles & the PRO pattern](02-MIE-roles-PRO-pattern.slides.html)
* [03 — Spatial objects & their parts](03-MIE-spatial-objects-parts.slides.html)
* [04 — Qualities, quantities, thresholds](04-MIE-qualities-quantities.slides.html)
* [05 — Connections](05-MIE-connections.slides.html)
* [06 — Reasoning & SPARQL](06-MIE-reasoning-sparql.slides.html)
* [07 — FAIR publishing](07-MIE-fair-publishing.slides.html) *(supplementary)*

## Speakers
[**Michel Dumontier**](https://www.maastrichtuniversity.nl/mj-dumontier) is the Distinguished Professor of Data Science at Maastricht
University and co-founder of the Department of Advanced Computing
Sciences. He is a leading researcher in biomedical ontologies, knowledge graphs,
and Semantic Web technologies. He co-founded the FAIR principles, leads major
EU and US research initiatives, and has extensive experience teaching ontology
engineering, knowledge graphs, and Semantic Web technologies at undergraduate
and graduate level. He is a co-creator of SULO and created the OntoStart
FAIR ontology template project.

[**Remzi Celebi**](https://www.maastrichtuniversity.nl/r-celebi) is an Assistant Professor in the Department of Advanced Computing
Sciences at Maastricht University. His research focuses on semantic data
integration, biomedical ontologies, knowledge graphs, and machine learning methods
for health applications. Remzi is an experienced instructor and teaches
courses on semantic web, knowledge graphs, machine learning, and FAIR data
stewardship. He regularly supervises MSc and PhD students in ontology engineering,
data integration, and representation learning.
