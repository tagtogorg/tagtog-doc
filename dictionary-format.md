---
layout: page
title: Dictionary TSV format
sidebar_link: true
version: 0.1
id: dictionaries
---

<div class="two-third-col">
  <p>Dictionaries are used to <a href="/webeditor.html#annotation-types">normalize entities</a> (also called entity linking or disambiguation).</p>
  <p markdown="1">The [dictionary file to upload](projects.html#dictionaries) must be a <code>.tsv</code> file (tab-separated values) (or a compressed <code>.zip</code> or <code>.tar.gz</code> containing a single <code>.tsv</code>).</p>
  <p>The dictionary format should follow this pattern:</p>

  <div markdown="1">
  ```
  entity_1_id    recName1    recName2    ...
  entity_2_id    recName1    recName2    @@@    altName1    altName2    ...
  ...
  ```
</div>


</div>
<div class="one-third-col">
  {% capture version %}<strong>Version</strong>: <code>{{ page.version }}</code>{% endcapture %}
  {% include message.html message=version %}
  {% include message.html message="Spreadsheet software is a good choice to manipulate <code>TSV</code> files" %}
</div>


<div class="two-third-col">
  <p>The syntax is simple:</p>
  <p class="list-item"><span class="list-item-1"></span>Each entity is defined in a new line. All columns are separated by tabs.</p>
  <p class="list-item"><span class="list-item-2"></span>The first column is the entity's <strong>unique id</strong>. It can be an internal id (e.g. your database) or recognized (using known sources as Wikipedia).</p>
  <p class="list-item"><span class="list-item-3"></span>After the id, a list of names follows. These are considered different names (synonyms) of the entity.</p>
  <p class="list-item"><span class="list-item-4"></span>You can define <strong>recommended names</strong> and, optionally, <strong>alternative names</strong>. At least one recommended name must be given. Alternative names are those placed after the special delimiter <code>@@@</code> (also separated within tabs). Use them when you know that some names appear less frequently than the standard ones. With this information, the system can handle synonyms better.</p>

  <p markdown="1">👉 Here are some [**sample, reference dictionaries**](https://github.com/tagtogorg/tagtog-doc/tree/master/assets/dictionaries).</p>

</div>
<div class="one-third-col">
  {% include message.html message="<strong>Note</strong>: the id is not considered a name. If you want it to be a name, put it in the list of names. Only in the basic case where the entity has 1 sole name and this matches the id, the name can be omitted and is therefore defined implicitly." %}
  {% include message.html message="<strong>Note</strong>: The entity ids cannot contain spaces nor commas, among other special characters. The exact regular expression is: <code>^[\p{IsAlphabetic}[0-9]\-()_:.@']+$</code>" %}
  {% include message.html message="<strong>Note</strong>: the names SHOULD NOT be tokenized." %}
  {% include message.html message="Limit the <i>recnames</i> or <i>altnames</i> to <strong>up to 7 words</strong>. To reduce the amount of time required to search and annotate dictionary terms, tagtog won't annotate terms over 7 tokens." %}
</div>
