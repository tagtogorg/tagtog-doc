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
---

<div class="two-third-col">
  <table style="width:100%;white-space:nowrap;">
    <tr>
      <td><strong>Version</strong></td>
      <td><code>{{ page.version }}</code></td>
    </tr>    
  </table>
</div>


<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

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

## Folders management

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
    <td>JSON; fields: 1) <code>mapNewIds</code> (always empty), and <code>newSettings</code> (the new project's JSON settings)</td>
  </tr>
</table>

**Input Parameters**

Two variants:

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


**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>    
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/folders/add{{ page.mandatory_query_parameters_full }}' -d '{"path": "pool/new"}'
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->


<div class="one-third-col">
  {% include image.html name="API_settings/POST_add_folder_example.png" caption="example output, add folder to project"%}
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
    <td>JSON; fields: 1) <code>mapNewIds</code> (always empty), and <code>newSettings</code> (the new project's JSON settings)</td>
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
    <td>JSON; fields: 1) <code>mapNewIds</code> (always empty), and <code>newSettings</code> (the new project's JSON settings)</td>
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
