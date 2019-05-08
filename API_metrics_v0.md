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
  <p><strong>⚠️ All the API for metrics are in a beta version, and can change at any moment. We give early access to the metrics for your benefit.</strong></p>

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
curl -u 'yourUsername:yourPassword' 'localhost:9000/-api/metrics/v0/search_stats?project=yourProjectName&owner=yourUsername&search=*'
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
  "anncomplete": {
    "numTrue": 4,
    "values": [
      {
        "count": 4,
        "percentage": 0.1,
        "value": "true"
      },
      {
        "count": 4100,
        "percentage": 99.9,
        "value": "false"
      }
    ]
  },
  "e_21": {
    "name": "Component",
    "numDocuments": 9,
    "numDocumentsMissing": 4095,
    "percentage": 83.33,
    "topNormalizations": [
      {
        "dictionaryId": "n_23",
        "dictionaryName": "ComponentDictionary",
        "entityId": "Brakes",
        "numDocuments": 4
      },
      {
        "dictionaryId": "n_23",
        "dictionaryName": "ComponentDictionary",
        "entityId": "Window",
        "numDocuments": 4
      },
      {
        "dictionaryId": "n_23",
        "dictionaryName": "ComponentDictionary",
        "entityId": "Trunk",
        "numDocuments": 1
      }
    ],
    "totalCount": 10
  },
  "e_22": {
    "name": "Status",
    "numDocuments": 2,
    "numDocumentsMissing": 4102,
    "percentage": 16.67,
    "topNormalizations": [],
    "totalCount": 2
  },
  "m_24": {
    "name": "isRelevant",
    "numDocuments": 7,
    "numDocumentsMissing": 4097,
    "type": "boolean",
    "values": [
      {
        "count": 2,
        "percentage": 28.57,
        "value": "false"
      },
      {
        "count": 5,
        "percentage": 71.43,
        "value": "true"
      }
    ]
  },
  "m_25": {
    "name": "OverallRisk",
    "numDocuments": 6,
    "numDocumentsMissing": 4098,
    "type": "enum",
    "values": [
      {
        "count": 1,
        "percentage": 16.67,
        "value": "low"
      },
      {
        "count": 3,
        "percentage": 50,
        "value": "medium"
      },
      {
        "count": 2,
        "percentage": 33.33,
        "value": "high"
      }
    ]
  },
  "numDocuments": 4104
}
```
  </div>
</div>
