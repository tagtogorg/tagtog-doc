---
layout: page
title: Search
sidebar_link: true

api_document_url: https://www.tagtog.net/-api/documents/v1
api_username: yourUsername
api_pwd: yourPassword
api_project: yourProjectName
---
<div class="two-third-col">
  <br/>
  <p>You can search using the documents API. You can use it to augment your own search engine or simply create a new one. It is also very simple to use the search API to display statistics. Here we show you how to do it.</p>
</div>
<div class="one-third-col">
  <div class="message">
    You will need an <strong>account at tagtog</strong>. Sign up at tagtog.net if you are using the cloud version or check with your admin if you are using an on-premises version.
  </div>
</div>
<div class="two-third-col">
  <h2>Search documents in a project <code>GET</code></h2>
  <p>Search across your pool folder and retrieve the matching documents.</p>
  <p><strong>Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>search</code></td>
      <td>-</td>
      <td>entity:GGP:P02649</td>
      <td>Search query. Learn how to build queries <a href=".">here</a>.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>Username sending the request</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
  </table>
  <p><strong>Optional Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>page</code></td>
      <td>0</td>
      <td>1</td>
      <td>Number: page number in a paginated search.</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>search</code></td>
      <td><code>search</code></td>
      <td><p>You can choose between <code>search</code> or <code>csv</code></p>
          <p><code>search</code> (<a href="#search-format">search format</a>): use it to perform search queries.</p>
          <p><code>csv</code>: it ignores the query parameter and retrieve the id of each document and the status of each document (true if annotations are completed, false if not)</p>
      </td>
    </tr>
  </table>
</div>
<div class="one-third-col">
  {% include message.html message='Search queries through the API return a response with the JSON <code>search format</code>. <a href="#search-format">Format documentation</a>' %}
</div>
<div class="two-third-col">
  
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-plain-text">cURL</a></li>
      <li><a href="#tab-2-plain-text">Python</a></li>
      <li><a href="#tab-3-plain-text">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example searches across your document pool to find documents that have at least one entity normalized to the gene <a href="https://www.uniprot.org/uniprot/P02649">P02649</a>.</p>
<div id="tab-1-plain-text" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}: {{ page.api_pwd }} '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&search=entity:GGP:P02649'
```
</div>
<div id="tab-2-plain-text" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'search':'entity:GGP:P02649'}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_search.py" %}</p>
</div>
<div id="tab-3-plain-text" class="tab-content" markdown="1">
```javascript
fetch('https://www.tagtog.net/-api/documents/v1?project={{ page.api_project }}&owner={{ page.api_username }}&search=entity:GGP:P02649', {
  method: 'GET',
  headers: {'Authorization' : "Basic " + btoa('{{ page.api_username }}' + ":" + '{{ page.api_pwd }}')},
}).then(response => response.text()).then(text => {
  console.log(text);
}).catch(function(error) {
  console.log('Error: ', error);
});
```
<p style="float:right">{% include github-link.html target="snippets/api_js_search.html" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response <code>search format</code> <a href="#search-format">Format documentation</a></p>
<div markdown="1">
```json
{
  "version":"0.1.0",
  "search":"entity:GGP:P02649",
  "totalFound":1,
  "pages":{"current":0,"previous":-1,"next":-1},
  "docs":
    [
      {"id":"aMHKzF_lIoNrdh9pAx298njgIezy-text", "header":"Certain genes make you more likely to develop Alzheimer's disease. Genes control the function of every cell in your body. Some genes determine basic characterist", "anncomplete":false, "updated":"2018-03-03T20:59:56.467Z"}
    ]
}
```
</div>
</div>



<div class="two-third-col">
  <h3>Building search queries</h3>
  <p>Here you can learn how to build your search queries. Search queries are sent in the parameter <code>search</code></p>
</div>
<div class="one-third-col">
  {% include message.html message='To build more advanced queries you can base on the <a href="http://lucene.apache.org/core/3_1_0/queryparsersyntax.html ">Query Parser Syntax from Lucene</a>' %}
</div>
<div class="two-third-col">
  <h4>Search by string</h4>
  <p>Retrieve documents containing a specific string. Example: <code>insulin</code></p>
</div>
<div class="one-third-col">
  {% include message.html message='Use <code>*</code> as search query to retrieve <strong>all</strong> documents in a project.' %}
</div>


<div class="two-third-col">
  <h4>Search by entity type</h4>
  <p>Retrieve all documents containing at least one entity that belongs to the given entity type. Example: <code>entity:disease</code> , retrieves all documents with at least one entity of the type <code>disease</code>.</p>
  <p>If you add a term, e.g. <code>entity:disease:cancer</code>, you can find all documents containing at least one entity using that term.</p>
  <br/>
  <p>Only by using the entity type id, you can also perform more advanced queries as:</p>
  <ul>
    <li><code>count</code> e.g. <code>count_e_1:[2 TO *]</code>): retrieves documents with at least 2 annotations of the type <code>e_1</code>.</li>
    <li><code>norms_count_uniq</code> e.g. <code>norms_count_uniq_e_1:[2 TO *]</code> retrieves documents with at least 2 annotations of the type <code>e_1</code> that are normalized to different unique names (e.g Rezulin and Romozin - same diabetic drug sold under different commercial names - would be normalized to troglitazone, so it would count 1 unique entity normalized, not 2).</li>
  </ul>
</div>
<div class="one-third-col">
  {% include message.html message='You can also use the entity type id. E.g. <code>entity:e_1</code>.' %}
</div>


<div class="two-third-col">
  <h4>Search by normalization</h4>
  <p>Retrieve all documents containing at least one entity that normalizes to the given normalization. Example: <code>entity:genes:HER2</code> , retrieves all documents with at least one entity <code>gene</code> that normalizes to <code>HER2</code>.</p>
</div>
<div class="one-third-col">

</div>


<div class="two-third-col">
  <h4>Search by date</h4>
  <p>Retrieve all documents imported or updated in a given time frame.</p>
  <p><code>created</code>: documents imported in a given time frame. Examples: <code>created:2018</code>, <code>created:2018-03</code>, <code>created:2018-03-06</code>, <code>created:[2013 to NOW]</code>, <code>created:[2016-12 TO 2017-02]</code>, <code>created:[NOW-1DAY TO NOW]</code> - documents imported since the previous day.</p>
  <p><code>updated</code>: documents updated in a given time frame. Examples: <code>updated:2018</code>, <code>updated:2018-03</code>, <code>updated:2018-03-06</code>, <code>updated:[2013 to NOW]</code>, <code>updated:[2016-12 TO 2017-02]</code>, <code>updated:[NOW-1DAY TO NOW]</code> - documents updated since the previous day.</p>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
  <h4>Wildcard search</h4>
  <p>To perform a single character wildcard search use <code>?</code>. Example: <code>entity:gene:P?2649</code>.</p>
  <p>To perform a multiple character wildcard search use <code>*</code>. Example: <code>"Kepler-2*"</code>, <code>"Kepler-4*c"</code>.</p>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
  <h4>Fuzzy search</h4>
  <p>Find similar terms (string based search) based on the Levenshtein Distance, or Edit Distance algorithm. Use <code>~</code> at the end of a single word term. Example: <code>roam~</code> will also find terms as <code>foam</code>.</p>
  <p>You cand fine tune the <strong>similarity level</strong> by adding, at the end, a number between <code>0</code> (less similar) and <code>1</code> (more similar). Example: <code>roam~0.8</code>.</p>
</div>
<div class="one-third-col">
  {% include message.html message='The default similarity level is <code>0.5</code>.' %}
</div>


<div class="two-third-col">
  <h4>Proximity search</h4>
  <p>Finding words (string based search) within a specific distance away. Example: <code>"diabetes insulin"~10</code>, to search documents with the terms <code>diabetes</code> and <code>insulin</code> within 10 words of each other.</p>
  
</div>
<div class="one-third-col">
  
</div>


<div class="two-third-col">
  <h4>Boolean operators</h4>
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
  <h4>Escaping Special Characters</h4>
  <p>To escape these special characters use the <code>\</code> before the character. For example to search for <code>PD-L1</code> use the query: <code>PD\-L1</code>.</p>
  
</div>
<div class="one-third-col">
  {% include message.html message="The current list <strong>special characters</strong> are <code>+</code> <code>-</code> <code>!</code> <code>&quot;</code> <code>&amp;&amp;</code> <code>&verbar;&verbar;</code> <code>(</code> <code>)</code> <code>{</code> <code>}</code> <code>[</code> <code>]</code> <code>&Hat;</code> <code>~</code> <code>*</code> <code>?</code> <code>:</code> <code>\</code>" %}
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
      <td>Retrieves all documents written in the language specified</td>
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
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h3>Search response format</h3>
  <p>Response format for search queries.</p>
<div markdown="1">
```javascript
{
  "version": "String: this format's version, e.g. 0.1.0",
  "search": "String: user search query",
  "totalFound": "Number: total number of documents that match the search query",
  "pages": {
    //the search is paginated
    "current": "Number: paginated search's current page",
    "previous": "Number: paginated search's previous page; -1 if current page == 0",
    "next": "Number: paginated search's current page; -1 if current page is the last page",
  }
  "docs": 
  [
    {
      "id": "String: full tagtogID -- Use this to download the document",
      "header": "String: title if the document has a natural title or otherwise an excerpt of the text's start",
      "anncomplete": "Boolean: status for the document's annotation completion",
      "updated": "String: date for the document' last update, in ISO_INSTANT format, e.g. 2017-02-23T08:31:40.874Z",
    },
    //next documents in the array of results...
  ]
}
```
</div>
</div>
<div class="one-third-col">

</div>





