---
id: api_metrics_v0
title: API metrics
sidebar_link: true
layout: page
toc: true
toc_levels: 1,2

version: 0.0
api_endpoint: /-api/metrics/v0
mandatory_query_parameters: ?owner=...&project=...
mandatory_query_parameters_full: ?owner=yourUsername&project=yourProjectName
api_document_url: https://www.tagtog.net/-api/metrics/v0
api_username: yourUsername
api_pwd: yourPassword
api_project: yourProjectName
api_folder_new: myNewFolder
---

<div class="two-third-col">
  <p><strong>🤠 All the API for metrics are in an alpha version, and can change at any moment. We give early access to the metrics for your benefit.</strong></p>

  <table style="width:100%;white-space:nowrap;">
    <tr>
      <td><strong>Version</strong></td>
      <td><code>{{ page.version }}</code></td>
    </tr>
    <tr>
      <td><strong>Endpoint</strong></td>
      <td><code>{{ page.api_endpoint }}</code></td>
    </tr>
  </table>
</div>


<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

## Project Stats  

### Annotation Stats

Stats for the (master) annotations, such as the count for a document label's specific value, number of _anncomplete_ (confirmed) documents, top normalizations for an entity type, etc.

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/search_stats{{ page.mandatory_query_parameters }}</code></td>
  </tr>
  <tr>
    <td><strong>Method</strong></td>
    <td><code>GET</code></td>
  </tr>
  <tr>
    <td><strong>Output</strong></td>
    <td>JSON</td>
  </tr>
</table>

**Input Parameters**

Defined as URL query parameters.

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
    <td><code>&ast;</code></td>
    <td>Document search, <a href="search-queries.html">allowing any usual search parameter</a>. Common is to just search for <code>&ast;</code> to get all the project's (documents) statistics.</td>
  </tr>
</table>

</div>
<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-export-settings">cURL</a></li>
  </ul>
  <div class="tab">
<div id="tab-1-export-settings" class="tab-content" style="display: block" markdown="1">
```shell
curl -u 'yourUsername:yourPassword' '{{ page.api_document_url }}/search_stats?project=yourProjectName&owner=yourUsername&search=*'
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->

<div class="one-third-col">
  <p>Response example <code>json</code>, search stats</p>
  <div markdown="1">
```json
{  
  "numDocuments": 4101,
  "numAnnotatedDocuments": 14,
  "numConfirmedDocuments": 5,  
  "allDocumentLabelsTotalCount": 7,
  "allEntitiesTotalCount": 12,
  "e_21": {
    "name": "Component",
    "numDocuments": 6,
    "numDocumentsMissing": 4095,
    "percentage": 75,
    "topNormalizations": [
      {
        "dictionaryId": "n_23",
        "dictionaryName": "ComponentDictionary",
        "entityId": "Window",
        "numDocuments": 3
      },
      {
        "dictionaryId": "n_23",
        "dictionaryName": "ComponentDictionary",
        "entityId": "Brakes",
        "numDocuments": 2
      },
      {
        "dictionaryId": "n_23",
        "dictionaryName": "ComponentDictionary",
        "entityId": "Trunk",
        "numDocuments": 1
      }
    ],
    "totalCount": 9
  },
  "e_22": {
    "name": "Status",
    "numDocuments": 2,
    "numDocumentsMissing": 4099,
    "percentage": 25,
    "topNormalizations": [],
    "totalCount": 3
  },
  "m_24": {
    "name": "isRelevant",
    "numDocuments": 4,
    "numDocumentsMissing": 4097,
    "type": "boolean",
    "values": [
      {
        "count": 2,
        "percentage": 50,
        "value": "true"
      },
      {
        "count": 2,
        "percentage": 50,
        "value": "false"
      }
    ]
  },
  "m_25": {
    "name": "OverallRisk",
    "numDocuments": 3,
    "numDocumentsMissing": 4098,
    "type": "enum",
    "values": [
      {
        "count": 1,
        "percentage": 33.33,
        "value": "high"
      },
      {
        "count": 2,
        "percentage": 66.67,
        "value": "medium"
      },
      {
        "count": 0,
        "percentage": 0,
        "value": "low"
      }
    ]
  },
  "m_28": {
    "name": "Comment",
    "numDocuments": 0,
    "numDocumentsMissing": 4101,
    "topValues": [],
    "type": "string"
  }
}
```
  </div>
</div>




<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

## IAA

### Get individual IAA for a pair of members

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/iaa{{ page.mandatory_query_parameters }}</code></td>
  </tr>
  <tr>
    <td><strong>Method</strong></td>
    <td><code>GET</code></td>
  </tr>
  <tr>
    <td><strong>Output</strong></td>
    <td>JSON</td>
  </tr>
</table>

**Input Parameters**

Defined as URL query parameters.

<table style="width:100%;">
  <tr>
    <th>Name</th>
    <th>Default</th>
    <th>Example</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>member1</code></td>
    <td>-</td>
    <td><em>yourUsername</em></td>
    <td>Username of the first member of the members pair to get the IAA for.</td>
  </tr>
  <tr>
    <td><code>member2</code></td>
    <td>-</td>
    <td><em>Laura</em></td>
    <td>Username of the second member of the members pair to get the IAA for.</td>
  </tr>
  <tr>
    <td><code>anntaskId</code></td>
    <td>-</td>
    <td><em>e_21</em></td>
    <td>The id (<em>anntaskId</em>) of one of <a href="API_settings_v1.html#annotations-legend">your annotation types in the project</a></td>
  </tr>
  <tr>
    <td><code>metric</code></td>
    <td>-</td>
    <td><code>exact_v1</code></td>
    <td>The name of the metric you want, typically <code>exact_v1</code> (this is the same metric used in the <a href="collaboration.html#iaa-inter-annotator-agreement">default IAA visualizations</a>). <a title="IAA: how it is calculated" href="IAA-calculation-methods">Possible values: <code>{exact_v1, overlapping_v1, documentlevel_v1}</code></a></td>
  </tr>
</table>

</div>
<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-export-settings">cURL</a></li>
  </ul>
  <div class="tab">
<div id="tab-1-export-settings" class="tab-content" style="display: block" markdown="1">
```shell
curl -u 'yourUsername:yourPassword' '{{ page.api_document_url }}/iaa?project=yourProjectName&owner=yourUsername&member1=yourUsername&member2=Laura&anntaskId=e_21&metric=exact_v1'
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->

<div class="one-third-col">
  <p>Response example <code>json</code>, IAA for a pair of members</p>
  <div markdown="1">
```json
{
  "f1": 0.8333333333333333,
  "overNumDocs": 2
}
```
  </div>
</div>
