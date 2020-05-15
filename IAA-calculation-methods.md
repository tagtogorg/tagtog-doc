---
layout: page
title: "IAA: calculation methods"
sidebar_link: false
id: IAA-calculation-methods
toc: false
---

As of now, the **GUI** shows a **default method to calculate the Inter-Annotator Agreement (IAA)** for all annotation types, namely: document labels, entity types, entity normalizations, entity labels, and entity relations. The default method is called in the descriptions below: **`exact_v1`**. The **API**, on top, allows you retrieve the IAA calculated with three different methods, namely: **`{exact_v1, overlapping_v1, documentlevel_v1}`**. **Not all calculation methods are available for all annotation types**. Below we describe the possible IAA calculation methods, grouped by annotation type. First some definitions:

#### Definitions

* `anntaskId`: (also called `classId`) is the unique id of an annotation type, for example, `e_1`, `m_2`, or `r_3`.
* `offsets`: (of an entity) are its 2 string coordinates, `start` and `end` (defined as: `end = start + length(entity's text)`). Moreover, since tagtog's native format ([anndoc](anndoc)) can contain different `parts` (strings) in a same document, there is actually an implicit third coordinate, namely the `partId`. In all descriptions below we always implicitly consider that the `partId`'s of two entities are equal in order to be compared, unless stated otherwise.
* `value`: (of a document label, or an entity normalization, or an entity label) is the absolute value assigned to the annotation. For example `"some"` (a _string_ value) or `true` (a _boolean_ value).


---


## Document labels

Given two different document labels (from two different annotation versions, e.g. different members), they are equal iff:

### `exact_v1` (default)

* The `anntaskId`'s are equal, _AND_
* The `value`'s are equal


---

## Entity Types

Given two entity types (from two different annotation versions, e.g. different members), they are equal iff:

### `exact_v1` (default)

* The `anntaskId`'s are equal, _AND_
* The `offsets` are equal


### `overlapping_v1`

* The `anntaskId`'s are equal, _AND_
* The `offsets` overlap in at least one character

---

## Entity Normalizations

Given two entity normalizations (from two different annotation versions, e.g. different members), they are equal iff:

### `exact_v1` (default)

* The `anntaskId`'s are equal, _AND_
* The (entity) `offsets` are equal, _AND_
* The normalization `value`'s are equal


### `overlapping_v1`

* The `anntaskId`'s are equal, _AND_
* The (entity) `offsets` overlap in at least one character, _AND_
* The normalization `value`'s are equal


### `documentlevel_v1`

* The `anntaskId`'s are equal, _AND_
* The normalization `value`'s are equal

    In this case, the entity offsets are disregarded. In practice, the entity normalizations' values (of a document) are compared as if they were sets. That is, for instance, if annotation version A had the normalization _x_ annotated 5 times, and the annotation version B had the same normalization _x_ annotated only once, the repetitions are disregarded and both annotations, for this particular normalization, are considered equal.


---

## Entity Labels

Given two entity labels (from two different annotation versions, e.g. different members), they are equal iff:

### `exact_v1` (default)

* The `anntaskId`'s are equal, _AND_
* The (entity) `offsets` are equal, _AND_
* The entity label `value`'s are equal


### `overlapping_v1`

* The `anntaskId`'s are equal, _AND_
* The (entity) `offsets` overlap in at least one character, _AND_
* The entity label `value`'s are equal

---

## Entity Relations

Given two entity relations (from two different annotation versions, e.g. different members), relating two entities (e.g. a & b and a' & b', resp.), they are equal iff:

### `exact_v1` (default)

* The `anntaskId`'s (of the relation) are equal, _AND_
* The `anntaskId`'s of the two related entities (a with a' & b with b') are equal, _AND_
* The `offsets` of the both related entities (a wtih a' & b with b') are equal


### `overlapping_v1`

* The `anntaskId`'s (of the relation) are equal, _AND_
* The `anntaskId`'s of the two related entities (a with a' & b with b') are equal, _AND_
* The `offsets` of the both related entities (a wtih a' & b with b') overlap in at least one character
