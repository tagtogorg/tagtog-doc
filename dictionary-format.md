---
layout: page
title: Dictionary TSV format
sidebar_link: true
version: 0.1
group: formats
---

<div class="two-third-col">
  <p>This is the format of dictionary files used at tagtog. More information about dictionaries here: <a href=".">Dictionaries</a></p>
  <p>The dictionary file to upload must be a <code>.tsv</code> file (tab-separated values) (or a comprassed <code>.zip</code> or <code>.tar.gz</code> containing a single <code>.tsv</code>).</p>
  <p>The dictionary format should follow this pattern:</p>

  <div markdown="1">
  ```
  entity_1_id    recname1    recname2    ...
  entity_2_id    recname1    recname2    @@@    altname1    altname2    ...
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
  <ul>
    <li>Each entity is defined in a new line. All columns are separated by tabs.</li>
    <li>The first column is the entity's <strong>unique id</strong>. It can be an internal id (e.g. your database) or recognized (using known sources as Wikipedia)</li>
    <li>After the id, a list of names follows. These are considered different names (synonyms) of the entity.</li>
    <li>You can define <strong>recommended names</strong> and, optionally, <strong>alternative names</strong>. At least one recommended name must be given. Alternative names are those placed after the special delimiter <code>@@@</code> (also separated within tabs). Use them when you know that some names appear less frequently than the standard ones. With this information, the system can handle synonyms better.</li>
  </ul>

  <p>If you want to check out a sample, you can <strong>download this dictionary</strong>: <a href="/assets/dictionaries/arabidopsis_proteins_and_genes_swissprot.zip">Arabidopsis gene names (source: SwissProt)</a>.</p>

</div>
<div class="one-third-col">
  {% include message.html message="<strong>Note</strong>: the id is not considered a name. If you want it to be a name, put it in the list of names. Only in the basic case where the entity has 1 sole name and this matches the id, the name can be omitted and is therefore defined implicitly." %}
  {% include message.html message="<strong>Note</strong>: the names must NOT be tokenized." %}
</div>



