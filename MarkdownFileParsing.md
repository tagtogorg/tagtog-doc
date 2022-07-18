---
layout: page
title: Markdown file parsing
sidebar_link: false
id: MarkdownFileParsing
toc: false
---

You can import markdown (`.md`) files onto tagtog.

In particular, we target a subset of [CommonMark (spec 0.28)](https://spec.commonmark.org/0.28/) + [tagtog-blocks 🧱](tagtog-blocks) (tagtog-flavored styles for code blocks).

![Markdown logo](https://commonmark.org/help/images/favicon.png)


## Supported

Only-text actual content is supported; in particular:

* headings
* paragraphs
* code blocks (both within back ticks or indented)
* images (not inline)
* lists (both unordered, ordered, and nested)
* [tagtog-blocks 🧱](tagtog-blocks) (tagtog-flavored styles for code blocks). With _tagtog-blocks_ you can customize the layout of your documents to best annotate tasks for: Q&A (Question & Answering), tweets, chatbots, etc.


## Not Supported

The following elements are not interpreted, but parsed as is and escaped. For example, `_em_` is visualized on tagtog literally as `_em_` (and not as _em_).

* Inline content and styles; in particular: `**bold**`, `_emphatic_`, `code`, `~~scratched~~`, `![images](url)`, `[links](url)`.
* Other special style-only elements; in particular: horizontal lines (`<hr/>` or `---`) or line breaks (`<br/>`).
* HTML-only elements. In particular, [HTML entities](https://spec.commonmark.org/0.29/#entity-and-numeric-character-references) are not escaped either, neither in code spans or code blocks, nor in the rest of content types (e.g. paragraphs).
* Block quotes. [Please let us know if you need them](https://tagtog.com/#contact). A current alternative is the [tagtog-block: `quote`](tagtog-blocks#quotes).
* Tables. [Please let us know if you need them](https://tagtog.com/#contact). A current alternative is the [tagtog-block addon: `multi-column`](tagtog-blocks#multi-column).


## Example

Here is a [markdown reference file](https://www.tagtog.com/tagtog/sample/pool/aqwpeyj_yOishcnevE.c3JBaI6s0-test_spec.md) file to know [how it's parsed and visualized in tagtog](https://www.tagtog.com/tagtog/sample/pool/amyZOgLzTcfL9.aO1AXOsT1zsieS-test_spec.md).
