---
id: api_projects_v1
title: API projects
sidebar_link: true
layout: page
toc: true
toc_levels: 1,2

version: 1.0
api_endpoint: /-api/projects/v1
api_document_url: https://www.tagtog.net/-api/projects/v1
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

## GET list of my projects

Return the list of projects that the (authenticated) user is a member of. This includes the projects created by the user, and the projects as an invitee.

<table style="width:100%;white-space:nowrap;">
  <tr>
    <td><strong>Endpoint</strong></td>
    <td><code>{{ page.api_endpoint }}/my-projects</code></td>
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
    <li class="current"><a href="#tab-1-plain-text">cURL</a></li>    
  </ul>
  <div class="tab">
<div id="tab-1-plain-text" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword {{ page.api_document_url }}/my-projects
```
</div>
  </div>
</div>

</div>

<div class="one-third-col">
  {% include image.html name="API_projects/GET-my-projects.png" caption="example, GET list of my projects"%}
</div>  
