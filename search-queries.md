---
layout: page
title: Search queries
sidebar_link: true
id: search_queries

api_document_url: https://www.tagtog.net/-api/documents/v1
api_username: yourUsername
api_pwd: yourPassword
api_project: yourProjectName
---

<div class="two-third-col">
  <p>Here you can learn how to build your search queries.</p>
</div>
<div class="one-third-col">
  {% include message.html message='To build more advanced queries you can base on the <a href="http://lucene.apache.org/core/3_1_0/queryparsersyntax.html ">Query Parser Syntax from Lucene</a>' %}
</div>
<div class="two-third-col">
  <h3>Search by string</h3>
  <p>Retrieve documents containing a specific string. Example: <code>insulin</code></p>
</div>
<div class="one-third-col">
  {% include message.html message='Use <code>*</code> as search query to retrieve <strong>all</strong> documents in a project.' %}
</div>


<div class="two-third-col">
  <h3>Search by entity type</h3>
  <p>Retrieve all documents containing at least one entity that belongs to the given entity type. Example: <code>entity:disease</code>, retrieves all documents with at least one entity of the type <code>disease</code>.</p>
  <p>If you add a term, e.g. <code>entity:disease:cancer</code>, you can find all documents containing at least one entity using that term.</p>
  <br/>
  <p>Only by using the entity type id, you can also perform more advanced queries as:</p>
  <ul>
    <li><code>count</code> e.g. <code>count_e_1:[2 TO *]</code>): retrieve documents with at least 2 annotations of the type <code>e_1</code>.</li>
    <li><code>norms_count_uniq</code> e.g. <code>norms_count_uniq_e_1:[2 TO *]</code> retrieve documents with at least 2 annotations of the type <code>e_1</code> that are normalized to different unique names (e.g Rezulin and Romozin - same diabetic drug sold under different commercial names - would be normalized to troglitazone, so it would count 1 unique entity normalized, not 2).</li>
  </ul>
</div>
<div class="one-third-col">
  {% include message.html message='You can also use the entity type id. E.g. <code>entity:e_1</code>.' %}
</div>


<div class="two-third-col">
  <h3>Search by normalization</h3>
  <p>Retrieve all documents containing at least one entity that normalizes to the given normalization. Example: <code>entity:genes:HER2</code>, retrieves all documents with at least one entity <code>gene</code> that normalizes to <code>HER2</code>.</p>
</div>
<div class="one-third-col">

</div>


<div class="two-third-col">
  <h3>Search by date</h3>
  <p>Retrieve all documents imported or updated in a given time frame.</p>
  <p><code>created</code>: documents imported in a given time frame. Examples: <code>created:2018</code>, <code>created:2018-03</code>, <code>created:2018-03-06</code>, <code>created:[2013 to NOW]</code>, <code>created:[2016-12 TO 2017-02]</code>, <code>created:[NOW-1DAY TO NOW]</code> - documents imported since the previous day.</p>
  <p><code>updated</code>: documents updated in a given time frame. Examples: <code>updated:2018</code>, <code>updated:2018-03</code>, <code>updated:2018-03-06</code>, <code>updated:[2013 to NOW]</code>, <code>updated:[2016-12 TO 2017-02]</code>, <code>updated:[NOW-1DAY TO NOW]</code> - documents updated since the previous day.</p>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
  <h3>Wildcard search</h3>
  <p>To perform a single character wildcard search use <code>?</code>. Example: <code>entity:gene:P?2649</code>.</p>
  <p>To perform a multiple character wildcard search use <code>*</code>. Example: <code>"Kepler-2*"</code>, <code>"Kepler-4*c"</code>.</p>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
  <h3>Fuzzy search</h3>
  <p>Find similar terms (string based search) based on the Levenshtein Distance, or Edit Distance algorithm. Use <code>~</code> at the end of a single word term. Example: <code>roam~</code> will also find terms as <code>foam</code>.</p>
  <p>You can fine tune the <strong>similarity level</strong> by adding, at the end, a number between <code>0</code> (less similar) and <code>1</code> (more similar). Example: <code>roam~0.8</code>.</p>
</div>
<div class="one-third-col">
  {% include message.html message='The default similarity level is <code>0.5</code>.' %}
</div>


<div class="two-third-col">
  <h3>Proximity search</h3>
  <p>Finding words (string based search) within a specific distance away. Example: <code>"diabetes insulin"~10</code>, to search documents with the terms <code>diabetes</code> and <code>insulin</code> within 10 words of each other.</p>
  
</div>
<div class="one-third-col">
  
</div>


<div class="two-third-col">
  <h3>Boolean operators</h3>
  <p>Search queries can be combined using the operators <code>AND</code>, <code>OR</code>, <code>NOT</code> and <code>-</code>. Some examples:</p>
  <ul>
    <li><code>entity:GGP AND entity:Mutation</code> search for documents that contain <code>GGP</code> entities and <code>Mutation</code> entities.</li>
    <li><code>"type 1 diabetes" OR insulin</code> search for documents that contain "type 1 diabetes" or "insulin".</li>
    <li><code>"type 1 diabetes" NOT insulin</code> search for documents that contain "type 1 diabetes" but not "insulin". This operator cannot be used with just one term.</li>
    <li><code>-diabetes</code> search for documents that don't contain the term "diabetes". Only string based search.</li>
  </ul>
  
</div>
<div class="one-third-col">
  {% include message.html message='Remember to use <strong>upper case</strong>: <code>AND</code>, <code>OR</code> and <code>NOT</code>.' %}
</div>

<div class="two-third-col">
  <h3>Escaping Special Characters</h3>
  <p>To escape these special characters use the <code>\</code> before the character. For example to search for <code>PD-L1</code> use the query: <code>PD\-L1</code>.</p>
  
</div>
<div class="one-third-col">
  {% include message.html message="The current list of <br/><strong>special characters</strong> are <code>+</code> <code>-</code> <code>!</code> <code>&quot;</code> <code>&amp;&amp;</code> <code>&verbar;&verbar;</code> <code>(</code> <code>)</code> <code>{</code> <code>}</code> <code>[</code> <code>]</code> <code>&Hat;</code> <code>~</code> <code>*</code> <code>?</code> <code>:</code> <code>\</code>" %}
</div>

<div class="two-third-col">
  <h3>Experimental search query fields</h3>
  <p>These are currently valid for scientific articles.</p>
  <table style="width:100%">
    <tr>
      <th>Field</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>language</code></td>
      <td><code>language:fre</code></td>
      <td>Retrieve all documents written in the language specified</td>
    </tr>
    <tr>
      <td><code>orgs</code></td>
      <td><code>orgs:university of Finland</code></td>
      <td>Retrieve all documents, which were written by authors with affiliations related to the term specified</td>
    </tr>
    <tr>
      <td><code>authors_full</code></td>
      <td><code>authors_full:mueller</code></td>
      <td></td>
    </tr>
    <tr>
      <td><code>authors_key</code></td>
      <td><code>authors_key:"t goldberg"</code></td>
      <td></td>
    </tr>
    <tr>
      <td><code>publication</code></td>
      <td><code>publication:nature</code></td>
      <td>Retrieve all documents, which were written by the specified journal</td>
    </tr>
    <tr>
      <td><code>published</code></td>
      <td><code>published:2018</code> <code>published:2018-03-06</code> <code>published:[2013 to NOW]</code></td>
      <td>Retrieve all documents published in a specified time frame.</td>
    </tr>
  </table> 
  <br/>
</div>
<div class="one-third-col">
</div>






