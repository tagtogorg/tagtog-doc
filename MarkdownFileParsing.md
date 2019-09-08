---
layout: page
title: Markdown file parsing
sidebar_link: false
id: MarkdownFileParsing
toc: false
---

You can import markdown (`.md`) files onto tagtog.

In particular, we target a subset of [CommonMark (spec 0.28)](https://spec.commonmark.org/0.28/).

![Markdown logo](https://commonmark.org/help/images/favicon.png)


## Supported

Only-text actual content is supported; in particular:

* headings
* paragraphs
* code blocks (both within back ticks or indented)
* images (not inline)
* lists (both unordered, ordered, and nested)


## Not Supported

* Inline content and styles are not supported; in particular: `**bold**`, `_emphatic_`, `code`, `~~scratched~~`, `![images](url)`, `[links](url)`.
* Other special style-only elements are not supported either; in particular: horizontal lines (`<hr/>` or `---`) or line breaks (`<br/>`).
* Block quotes are not supported at the moment but are coming soon.
* Tables are not supported at the moment.
* HTML-only elements are not supported.


## Example

Here is a [markdown reference file](https://www.tagtog.net/tagtog/sample/pool/aqwpeyj_yOishcnevE.c3JBaI6s0-test_spec.md) file to know [how it's parsed and visualized in tagtog](https://www.tagtog.net/tagtog/sample/pool/amyZOgLzTcfL9.aO1AXOsT1zsieS-test_spec.md).
