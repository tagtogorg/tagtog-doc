---
id: api_settings_v1
title: API settings
sidebar_link: true
layout: page
toc: true
toc_levels: 1,2

version: 1.0
api_endpoint: /-api/settings/v1
mandatory_query_parameters: ?owner=...&project=...
mandatory_query_parameters_full: ?owner=yourUsername&project=yourProjectName
api_document_url: https://www.tagtog.net/-api/settings/v1
api_username: yourUsername
api_pwd: yourPassword
api_project: yourProjectName
api_folder_new: myNewFolder
---

<div class="two-third-col">
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

## Settings management

### Export Settings

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/export{{ page.mandatory_query_parameters }}</code></td>
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

None

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
curl -u yourUsername:yourPassword '{{ page.api_document_url }}/export{{ page.mandatory_query_parameters_full }}'
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->

<div class="one-third-col">
  <p>Response example <code>json</code>, export settings</p>
  <div markdown="1">
```json
{
  "version": "1.3",
  "domain": "other",
  "language": "English",
  "usePreSelections": true,
  "usePreDeselections": false,
  "usePreCaseSentive": false,
  "useMachineLearning": true,
  "nativePDF": false,
  "autoSave": false,
  "confirmLayer": false,
  "taskDistributionNumber": 0,
  "taskDistributionOwner": true,
  "folders": {
    "pool": {
      "name": "pool",
      "index": 0,
      "children": {}
    }
  },
  "webhooks": {},
  "metas": {},
  "entities": {
    "e_1": { "id": "e_1", "name": "risk", "oldnames": [], "description": "Risk assessment", "color": "#28c72d", "fields": {}, "normalizations": {} }
  },
  "fields": {},
  "relations": {}
}
```
  </div>
</div>



<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

### Import Settings

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/import{{ page.mandatory_query_parameters }}</code></td>
  </tr>
  <tr>
    <td><strong>Method</strong></td>
    <td><code>POST</code></td>
  </tr>
  <tr>
    <td><strong>Output</strong></td>
    <td>JSON; fields: <code>mapNewIds</code>, <code>newSettings</code> (the new imported project's JSON settings)</td>
  </tr>
</table>

**Input Parameters**

JSON project settings, in the same format as returned by [exporting the settings](#export-settings).

**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/import{{ page.mandatory_query_parameters_full }}' -d @$HOME/Downloads/tagtog_yourUsername_yourProjectName.json
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->




<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

---
## Annotations Legend

GET a JSON map of annotation tasks ids to names (e.g. `{"e_1": "Person"}`).

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/annotationsLegend{{ page.mandatory_query_parameters }}</code></td>
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

None

**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword '{{ page.api_document_url }}/annotationsLegend{{ page.mandatory_query_parameters_full }}'
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->



<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

---

## Folders management

For all folder operations, please note that `pool` must always be the root folder. [More information](search-queries.html#search-by-folder).

### Add folder

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/folders/add{{ page.mandatory_query_parameters }}</code></td>
  </tr>
  <tr>
    <td><strong>Method</strong></td>
    <td><code>POST</code></td>
  </tr>
  <tr>
    <td><strong>Output</strong></td>
    <td>JSON; fields: <code>mapNewIds</code> (always empty), <code>newSettings</code> (the new project's JSON settings)</td>
  </tr>
</table>

**Input Parameters**



Two variants in JSON format:

1. **(Full) path**:
<table style="width:100%;">
  <tr>
    <th>Name</th>
    <th>Default</th>
    <th>Example</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>path</code></td>
    <td>-</td>
    <td><code>pool/new</code></td>
    <td>Full path of the new folder</td>
  </tr>
</table>


2. **Parent path & new folder name** (example):
<table style="width:100%;">
  <tr>
    <th>Name</th>
    <th>Default</th>
    <th>Example</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>parentPath</code></td>
    <td>-</td>
    <td><code>pool</code></td>
    <td>Full path up to the parent (included) of the new folder</td>
  </tr>
  <tr>
    <td><code>newFolderName</code></td>
    <td>-</td>
    <td><code>new</code></td>
    <td>New folder name to be added to the parent path</td>
  </tr>
</table>

In both cases, **the parent path must have been already defined**. In other words, in Unix jargon, `mkdir` is permitted, but not `mkdir -p`.

</div>

<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-add-folder">cURL</a></li>
    <li><a href="#tab-2-add-folder">Python</a></li>
  </ul>
  <div class="tab">
<div id="tab-1-add-folder" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/folders/add{{ page.mandatory_query_parameters_full }}' -d '{"path": "pool/new"}'
```
</div>
<div id="tab-2-add-folder" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}/folders/add"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}'}
payload = {'parentPath': 'pool', 'newFolderName': '{{ page.api_folder_new}}'}
response = requests.post(tagtogAPIUrl, auth=auth, params=params, json=payload)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_add_folder.py" %}</p>
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->


<div class="one-third-col">
  <p>Response example <code>json</code>, add folder to project</p>
  <div markdown="1">
```json
{
  "newSettings": {
    "version": "1.3",
    "domain": "other",
    "language": "English",
    "usePreSelections": true,
    "usePreDeselections": false,
    "usePreCaseSentive": false,
    "useMachineLearning": true,
    "nativePDF": false,
    "autoSave": false,
    "confirmLayer": false,
    "taskDistributionNumber": 0,
    "taskDistributionOwner": true,
    "folders": {
      "pool": {
        "name": "pool",
        "index": 0,
        "children": {
          "mynewfolder": {
            "name": "mynewfolder",
            "index": 12,
            "children": {}
          }
        }
      }
    },
    "metas": {},
    "entities": { "e_1": { "id": "e_1", "name": "risk", "oldnames": [], "description": "Risk assessment", "color": "#28c72d", "fields": {}, "normalizations": {} }},
    "fields": {},
    "relations": {},
    "name": "myProject",
    "webhooks": {}
  },
  "mapNewIds": {}
}
```
  </div>
</div>



<div class="two-third-col" markdown="1">

### Rename folder

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/folders/rename{{ page.mandatory_query_parameters }}</code></td>
  </tr>
  <tr>
    <td><strong>Method</strong></td>
    <td><code>POST</code></td>
  </tr>
  <tr>
    <td><strong>Output</strong></td>
    <td>JSON; fields: <code>mapNewIds</code> (always empty), <code>newSettings</code> (the new project's JSON settings)</td>
  </tr>
</table>

**Input Parameters**
<table style="width:100%;">
  <tr>
    <th>Name</th>
    <th>Default</th>
    <th>Example</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>path</code></td>
    <td>-</td>
    <td><code>pool/new</code></td>
    <td>Full path of the existing folder to be renamed</td>
  </tr>
  <tr>
    <td><code>newFolderName</code></td>
    <td>-</td>
    <td><code>newRenamed</code></td>
    <td>New folder name</td>
  </tr>
</table>

The given path must exist. The last element of the path (in the example: "new") is renamed to "newRenamed"


**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/folders/rename{{ page.mandatory_query_parameters_full }}' -d '{"path": "pool/new", "newFolderName": "newRenamed" }'
```
</div>
  </div>
</div>

</div>






<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

### Remove folder

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/folders/remove{{ page.mandatory_query_parameters }}</code></td>
  </tr>
  <tr>
    <td><strong>Method</strong></td>
    <td><code>POST</code></td>
  </tr>
  <tr>
    <td><strong>Output</strong></td>
    <td>JSON; fields: <code>mapNewIds</code> (always empty), <code>newSettings</code> (the new project's JSON settings)</td>
  </tr>
</table>

**Input Parameters**
<table style="width:100%;">
  <tr>
    <th>Name</th>
    <th>Default</th>
    <th>Example</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>path</code></td>
    <td>-</td>
    <td><code>pool/newRenamed</code></td>
    <td>Full path of the folder to be deleted</td>
  </tr>
</table>

The given path must exist. You can "delete multiple levels" at the same time. That is, if the folder path (in the example) `pool/newRenamed/otherLevel` existed, while deleting `newRenamed`, the folder `otherLevel` would also be deleted.

**⚠️ CAUTION**: **all documents within the (possibly-multiple) deleted folders are also deleted!** Make sure you do not delete valuable documents. At the moment there is no API to "move" documents between folders. However, the same can be implemented by 1) downloading, 2) removing, 3) reuploading to a different folder.


**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/folders/remove{{ page.mandatory_query_parameters_full }}' -d '{"path": "pool/newRenamed" }'
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->
