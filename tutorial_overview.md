---
layout: default
title: FAIR Ontology Engineering with SULO
description: An ESWC 2026 Tutorial
---

## Overview
Designing high-quality ontologies that are Findable, Accessible, Interoperable, and Reusable (FAIR) remains a key challenge in
practice. This tutorial introduces a fully integrated workflow for principled ontology engineering based on the Simplified Upper Level Ontology
(SULO), a lightweight upper-level ontology designed to guide conceptual representation. Through a hands-on, end-to-end examples, participants
will (re)conceptualize, formalize, and automatically reason over the pizza domain using SULO design patterns in a notebook setting. Participants will use the OntoStart platform to
publish their own ontology in a FAIR manner. The tutorial is aimed at students, researchers, and practitioners building domain ontologies. Participants will
learn methodology and leave with a practical skills to bootstrap their own FAIR ontology projects.


## Objectives
This tutorial addresses a persistent gap in applied ontology: the absence of accessible,
end-to-end workflows for producing FAIR, modular, reusable ontologies
with high conceptual and engineering quality. The tutorial objectives are to:
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
* Extend the legendary OWL Pizza tutorial5 with a diversity of representational
problems (e.g. class/individual, identity, equivalence and disjointness,
spatial (containment and mereology) and processual (transformational,
developmental), qualities, quantities, roles and information objects through
concrete examples such as the classification of pizzas based on their toppings
and their qualitative and quantitative spicyness, the loss and gain of identity
in the making of dough, the roles played by individuals and devices in the
making and delivering of pizzas (SULO Pizza Tutorial)6.
* Empower participants to adopt reproducible, maintainable, and FAIR
engineering practice for their own ontology projects.

## Target Audience
The tutorial aims to balance theory with hands-on ontology engineering over the pizza domain. 
The tutorial is pitched at a basic to intermediate level; no
prior knowledge of upper level ontologies or OWL is required. Attendees that
have knowledge of python may choose to implement the tutorial with python,
otherwise attendees will be expected to run Protege.

## Learning goals
The learning goals of the tutorial are twofold:
1. Develop competency in the use of SULO to conceptualize and formalise a domain
* Explain the role of an upper-level ontology and apply SULO’s categories and design patterns to conceptualize a domain.
* Distinguish parts, features, roles, capabilities, processes, and quantities within a domain using SULO semantics.
* Formalize domain concepts in OWL, translating SULO-based conceptual models into logical axioms.
* Re-design the pizza ontology by applying SULO patterns in OWL for the pizza domain and validate them using tooling.

2. Publish and maintain ontology projects following FAIR practices
* Initialize a new FAIR ontology project using OntoStart, including metadata files, documentation structure, and CI-based quality checks.
* Use Protégé 7 to build, visualize, and test ontology class structures.
* Use owlready2 8 in Python to construct, manipulate, and reason over ontologies programmatically.
* interpret FOOPS! [2] FAIRness reports and identify steps to improve ontology FAIRness.



### 🕒 Schedule (May 10/11 2026)
A half-day tutorial (4h) with two core components
*  SULO-based knowledge representation
*  Hands-on implementation


| Activity | Duration | Description | OWL constructs introduced |
| :--- | :--- | :--- | :--- | 
| Tutorial overview | 5 min | Introduction to the tutorial | |
| What is an ontology? | 10 min | Overview of what ontologies are, and how they differ from terminologies, vocabularies, and schemas | |
| SULO quick overview | 10 min | Brief overview of classes and relations, the SULO postcard as a reference material | |
| OWL Declarations | 15 min | Declaring classes and individuals within an OWL ontology, importing SULO | Entity Declarations (Class, Object and Data Property, Individual), Axioms (Class, Subclass, Disjoint), Annotation Properties, OWL Imports  |
| Spatial objects & their composition | 20 min | Describing necessary and/or sufficient conditions for class membership, focusing on pizzas and their parts | Class Expression Exioms: Class Expressions, Propositional Connectives, Existential and Universal Quantification, Object Property Cardinality Restrictions (minimum, maximum, exact), Object Subproperties ( sub, inverse, domain, range, Functional, Transitive), Complex role inclusions |
| Qualities | 15 min | Qualities as intrinsic characteristics, focusing on the spicyness of a pizza and its ingredients | DisjointUnion |
| Quantities | 15 min | Quantities as associated features, focusing on a numeric representation of the spicyness quality of an ingredient | Functional data property, Data Property Cardinality Restrictions, Datatype Restriction | 
| Processes, process parts, and roles | 30 min | Processes, their parts, participants and their roles, development (maintainance of identity) and transformation (entities are created and destroyed), focusing on making of the pizza dough and crust | Individuals, Individual equality and inequality |
| Information Entities | 15 min | The receipt obtained after having paid for the pizza | | |
| break | 15 min | || 
| Time | 15 min | Time as a measured quantity that can be associated to processes or objects, and temporal ordering, focusing on when a pizza order was received, the pizza baked, and when it was delivered | |
| Spatial containment and movement | 15 min | Differentiating spatial containment from parthood, movement of objects within a process, focusing on the addition and removal of the pizza in the pizza delivery box | |
| Q&A | 30 min | Discussion of modeling approaches within and beyond the tutorial | |
| OntoStart Deployment | 15 min | Publishing FAIR ontologies with documentation through Github actions | Ontology IRI, OWL Versioning, Ontology Annotations, OWL Syntaxes |
| FAIRness assessment | 10 min | Examining the output of a FOOPS! fairness assessment report | |
| Wrap up | 5 min | Q&A and wrap up | |



### Speakers
[**Michel Dumontier**](https://www.maastrichtuniversity.nl/mj-dumontier) is the Distinguished Professor of Data Science at Maastricht
University and co-founder of the Department of Advanced Computing
Sciences. He is a leading researcher in biomedical ontologies, knowledge graphs,
and Semantic Web technologies. He co-founded the FAIR principles, leads major
EU and US research initiatives, and has extensive experience teaching ontology
engineering, knowledge graphs, and Semantic Web technologies at undergruadate
and graduate level. He is a co-creator of SULO and created the ontostart
FAIR ontology template project.

[**Remzi Celebi**](https://www.maastrichtuniversity.nl/r-celebi) is an Assistant Professor in the Department of Advanced Computing
Sciences at Maastricht University. His research focuses on semantic data
integration, biomedical ontologies, knowledge graphs, and machine learning methods
for health applications. Remzi is an experienced instructor and teaches
courses on semantic web, knowledge graphs, machine learning, and FAIR data
stewardship. He regularly supervises MSc and PhD students in ontology engineering,
data integration, and representation learning.

