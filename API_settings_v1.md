---
id: api_settings_v1
title: API settings
sidebar_link: true
layout: page
toc: true
toc_levels: 1,2

version: 1.2
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


<!-- -------------------------------------------------------------------------- -->


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

**Input**

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


<!-- -------------------------------------------------------------------------- -->


<div class="two-third-col" markdown="1">

---

## Members management

### Read members

Get the list of confirmed members & pending members in your project.

* Method: `GET`
* Endpoint: `{{ page.api_endpoint }}/members{{ page.mandatory_query_parameters }}`

**Input (parameters)**

Body: None

**Output**

Successful status code: `200` (OK)

Payload: JSON (application/json)

| Name             | Example                                                                                                                                          | Description                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `members`        | `[{"username":"MyOrganization","role":{"name":"admin"},"inTeams":[]}, ...]`                                                                      | Array of confirmed members in the project (including those added via teams). |
| `pendingMembers` | `[{"invitationToken":"invt-8ac3e282-3826-4f1f-a415-2cf1df30b3ce","role":{"name":"curator"},"email":"somebody@example.org"}, ...]`                | Array of pending members in the project.                                     |
| `teams`          | `[{"name":"MyTeam1","defaultRole":{"name":"reader"},"members":[{"username":"test01","role":{"name":"reader"},"inTeams":[{"name":"MyTeam1"}]}]}]` | Array of teams in the project.                                               |

**⚠️ Deprecation**: the output field ~~`roleName`~~ was deprecated on 2020-11-01, and will be removed after 2021-05-01. Please use the new field: `{"role":{"name":"..."}}`.

---

### Create members

Add a member (or team's members) to your project.

* Method: `POST`
* Endpoint: `{{ page.api_endpoint }}/members{{ page.mandatory_query_parameters }}`

**Input (parameters)**

Body: JSON (application/json)

| Type | Name       | Default | Examples           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---- | ---------- | ------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Body | `loginid`  |         | "John" or "MyTeam" | Username or email address of the tagtog user you want to invite to your project to. Moreover, on [tagtog OnPremises ENTERPRISE](https://www.tagtog.net/-plans#ONPREMISES), you can also give the name of a team; in this case, all the team's members will be added to the project.<br><br>If the users exist on tagtog, currently, they will be added immediately to your project without requiring confirmation from the users. This might change in the future.<br><br>If you give an email address that is not associated yet with a tagtog user, the email address will receive an invitation link to join tagtog and your project. Invited members who have not confirmed yet are called _"pending members"_. |
| Body | `roleName` |         | "reader"           | [Role](collaboration.html#roles) (name) to give to the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

**Output**

Successful status code: `205` (Reset Content; no payload)

---

### Update members

Change the role of an existing & confirmed member (or all the members of an existing team) in your project.

* Method: `PUT`
* Endpoint: `{{ page.api_endpoint }}/members/:loginid{{ page.mandatory_query_parameters }}`

**Input (parameters)**

Body: JSON (application/json)

| Type | Name       | Default | Examples           | Description                                                                                                                                                                                                                                   |
| ---- | ---------- | ------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Path | `loginid`  |         | "John" or "MyTeam" | Username or email of the project member to update. Moreover, on [tagtog OnPremises ENTERPRISE](https://www.tagtog.net/-plans#ONPREMISES), you can also give the name of a team; in this case all the existing team's members will be updated. |
| Body | `roleName` |         | "reviewer"         | New [role](collaboration.html#roles) (name) to give to the user.                                                                                                                                                                              |

**Output**

Successful status code: `205` (Reset Content; no payload)

---

### Delete members

Remove an existing & confirmed member (or all the members of an existing team) from your project.

* Method: `DELETE`
* Endpoint: `{{ page.api_endpoint }}/members/:loginid{{ page.mandatory_query_parameters }}`

**Input (parameters)**

Body: None

| Type | Name      | Default | Examples           | Description                               |
| ---- | --------- | ------- | ------------------ | ----------------------------------------- |
| Path | `loginid` |         | "John" or "MyTeam" | Username of the project member to delete. |

**Output**

Successful status code: `205` (Reset Content; no payload)

---

### Get pending members (only)

Get the list of pending members in your project.

* Method: `GET`
* Endpoint: `{{ page.api_endpoint }}/pending-members{{ page.mandatory_query_parameters }}`

**Input (parameters)**

Body: None

**Output**

Successful status code: `200` (OK)

Payload: JSON (application/json)

| Name             | Example                                                                                                                           | Description                              |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `pendingMembers` | `[{"invitationToken":"invt-8ac3e282-3826-4f1f-a415-2cf1df30b3ce","role":{"name":"curator"},"email":"somebody@example.org"}, ...]` | Array of pending members in the project. |

---

### Delete pending member

Remove a pending member from your project.

* Method: `DELETE`
* Endpoint: `{{ page.api_endpoint }}/pending-members/:invitationToken{{ page.mandatory_query_parameters }}`

**Input (parameters)**

Body: None

| Type | Name              | Default | Example                                     | Description                                                                       |
| ---- | ----------------- | ------- | ------------------------------------------- | --------------------------------------------------------------------------------- |
| Path | `invitationToken` |         | "invt-8ac3e282-3826-4f1f-a415-2cf1df30b3ce" | Invitation token, which uniquely identifies the invitation to the pending member. |

**Output**

Successful status code: `205` (Reset Content; no payload)

---

### Update task distribution

Update the configuration of task distribution of your project.

* Method: `PUT`
* Endpoint: `{{ page.api_endpoint }}/task-distribution{{ page.mandatory_query_parameters }}`

**Input (parameters)**

Body: JSON (application/JSON)

| Type | Name                      | Default | Example                             | Description                                  |
| ---- | ------------------------- | ------- | ----------------------------------- | -------------------------------------------- |
| Body | `taskDistributionNumber`  |         | 2                                   | [See docs](projects.html#task-distribution). |
| Body | `taskDistributionMembers` |         | `["yourUsername", "John", "Laura"]` | [See docs](projects.html#task-distribution). |

**Output**

Successful status code: `200` (OK)

Payload: JSON (application/json)

| Name          | Example                                                | Description                                   |
| ------------- | ------------------------------------------------------ | --------------------------------------------- |
| `mapNewIds`   | `{}`                                                   | Not relevant; always empty.                   |
| `newSettings` | [See docs below](API_settings_v1.html#export-settings) | New full settings json object of the project. |


</div> <!-- Closes section: two-third-col -->


<!-- -------------------------------------------------------------------------- -->


<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->

---

## (Full) Settings management

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

**Input**

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
  "version" : "1.6",
  "domain" : "other",
  "language" : "English",
  "usePreSelections" : true,
  "usePreDeselections" : false,
  "usePreCaseSentive" : false,
  "useMachineLearning" : false,
  "nativePDF" : false,
  "autoSave" : false,
  "confirmLayer" : false,
  "taskDistributionNumber" : 0,
  "taskDistributionMembers" : [ ],
  "folders" : {
    "pool" : {
      "name" : "pool",
      "index" : 0,
      "children" : { }
    }
  },
  "requirements" : { },
  "webhooks" : { },
  "metas" : {
    "m_2" : {
      "id" : "m_2",
      "name" : "Type",
      "oldnames" : [ ],
      "description" : "A,B,C",
      "type" : "enum"
    }
  },
  "fields" : { },
  "relations" : { },
  "entities" : { }
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

**Input**

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


<!-- -------------------------------------------------------------------------- -->


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

**Input**

Two variants in JSON format:

1) **(Full) path**:
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

2) **Parent path & new folder name**:
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

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}"}
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
    "version": "1.6",
    "domain": "other",
    "language": "English",
    "usePreSelections": true,
    "usePreDeselections": false,
    "usePreCaseSentive": false,
    "useMachineLearning": false,
    "nativePDF": false,
    "autoSave": false,
    "confirmLayer": false,
    "taskDistributionNumber": 0,
    "taskDistributionMembers": [],
    "folders": {
      "pool": {
        "name": "pool",
        "index": 0,
        "children": {
          "new": {
            "name": "new",
            "index": 10,
            "children": {}
          }
        }
      }
    },
    "requirements": {},
    "webhooks": {},
    "metas": {
      "m_2": {
        "id": "m_2",
        "name": "Type",
        "oldnames": [],
        "description": "A,B,C",
        "type": "enum"
      }
    },
    "fields": {},
    "relations": {},
    "entities": {}
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

**Input**
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

**Input**
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
