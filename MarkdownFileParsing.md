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
* tagtog blocks (For predefined annotation modules: question answering, tweets, annotator tasks, chatbot conversations, etc.). <a href="tagtog-blocks">Documentation</a>.
* images (not inline)
* lists (both unordered, ordered, and nested)


## Not Supported

The following elements are not interpreted, but parsed as is and escaped. For example, `_em_` is visualized on tagtog literally as `_em_` (and not as _em_).

* Inline content and styles; in particular: `**bold**`, `_emphatic_`, `code`, `~~scratched~~`, `![images](url)`, `[links](url)`.
* Other special style-only elements; in particular: horizontal lines (`<hr/>` or `---`) or line breaks (`<br/>`).
* HTML-only elements. In particular, [HTML entities](https://spec.commonmark.org/0.29/#entity-and-numeric-character-references) are not escaped either, neither in code spans or code blocks, nor in the rest of content types (e.g. paragraphs).
* Block quotes. [Please let us know if you need them](https://tagtog.net/#contact).
* Tables. [Please let us know if you need them](https://tagtog.net/#contact).


## Example

Here is a [markdown reference file](https://www.tagtog.net/tagtog/sample/pool/aqwpeyj_yOishcnevE.c3JBaI6s0-test_spec.md) file to know [how it's parsed and visualized in tagtog](https://www.tagtog.net/tagtog/sample/pool/amyZOgLzTcfL9.aO1AXOsT1zsieS-test_spec.md).
