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


<div class="two-third-col" markdown="1">

## Folders management

### Add folder

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/add{{ page.mandatory_query_parameters }}</code></td>
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

1. **(Full) path** (example):
```shell
{
  "path": "pool/new"
}
```

2. **Parent path & new folder name** (example):
```shell
{
  "parentPath": "pool",
  "newFolderName": "new"
}
```

In both cases, **the parent path must have been already defined**. In other words, in Unix jargon, `mkdir` is permitted, but not `mkdir -p`.


**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>    
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/add{{ page.mandatory_query_parameters_full }}' -d '{"path": "pool/new"}'
```
</div>
  </div>
</div>

</div>

<div class="one-third-col">
  {% include image.html name="API_settings/POST_add_folder_example.png" caption="example output, add folder to project"%}
</div>



<div class="two-third-col" markdown="1">

### Rename folder

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/rename{{ page.mandatory_query_parameters }}</code></td>
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

(example)

```shell
{
  "path": "pool/new"
  "newFolderName": "newRenamed"
}
```

The given path must exist. The last element of the path (in the example: "new") is renamed to "newRenamed"


**Coding examples**

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>    
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/rename{{ page.mandatory_query_parameters_full }}' -d '{"path": "pool/new", "newFolderName": "newRenamed" }'
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
    <td><code>{{ page.api_endpoint }}/remove{{ page.mandatory_query_parameters }}</code></td>
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

(example)

```shell
{
  "path": "pool/newRenamed"  
}
```

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
curl -u yourUsername:yourPassword -H "Content-Type: application/json" -XPOST '{{ page.api_document_url }}/remove{{ page.mandatory_query_parameters_full }}' -d '{"path": "pool/newRenamed" }'
```
</div>
  </div>
</div>

</div> <!-- Closes main section: two-third-cold div -->
