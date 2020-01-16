---
layout: page
title: EntitiesOnlyClassesTsv
sidebar_link: false
id: EntitiesOnlyClassesTsv
toc: true
---

Tabulated format to represent an annotated document's **entities**. The format is a close derivative of the [EntitiesTsv](EntitiesTsv)'s, with two single but important differences:

* The (non-labeled) **"outside" text is NOT written**
* ALL labeled entities are written. Because of this, **overlapping entities are supported**

The document text's sections (parts) are still separated by new line.

## Example

The format is best explained with an example 🙂 (contrast with that of [EntitiesTsv](EntitiesTsv)'s):

* From the annotated _input_ document (note that it contains overlapping entities):
![Sample document](assets/img/EntityTsv/my-sample-overlapping-onlyclasses-tagtog.png)

* The resulting _output_ is (the `»` character represents a tab, `·` a space, and `¬` a new line):

![Sample output](assets/img/EntityTsv/my-sample-overlapping-onlyclasses-output.png)

<div class="vincentformat" style="width:30%;height:0;padding-bottom:20%;position:relative;"><iframe src="https://giphy.com/embed/TA5UdQTc3NVKg" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>
