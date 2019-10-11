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

<div class="two-third-col" markdown="1">
| **Version** | `{{ page.version }}` |

</div>


<div class="two-third-col" markdown="1">
## Search my projects

| **Endpoint**  | `{{ page.api_endpoint }}/search-my-projects` |
| **Method**    | `GET`                                        |
| **Output**    | JSON                                         |
| **Paginated** | Yes                                          |

###### Input Parameters

| Name | Default | Example   | Description                                                                                                                                                                                                                |
| ---- | ------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `s`  | ""      | "reports" | If the parameter is not given or otherwise it's the empty string, all your projects are returned. Otherwise, the given search parameter is matched against your project names, descriptions, or project members usernames. |
| `p`  | 0       | 7         | Page number (0 indexed) of the search results to fetch.                                                                                                                                                                    |

##### Projects Search: Output JSON Format

```javascript
{
  "version": "String: this format's version; e.g. 1.1.0",
  "search": "String: search parameter. Can be null if no search given.",
  "totalFound": "Number: total number of projects that match the search",
  "pages": {
    //the search is paginated
    "current": "Number: paginated search's current page",
    "previous": "Number: paginated search's previous page; -1 if current page == 0",
    "next": "Number: paginated search's current page; -1 if current page is the last page",
    "numPages": "Number: total number of pages in the search. If numPages <= 1, the current page contains all found results"
    "pageSize": "Number: page size"
  }
  "projectsPage": [
    //current page's array of found projects. This page may or may not contain all results
    {
      "name": "String: project's name; e.g. yourProjectName",
      "owner": "String: project's owner (username); e.g. yourUsername",
      "description": "String: project's description",
      "created": "String: creation date; e.g. 2019-08-05",
      "isPublic": "Boolean: true if this project is public; false otherwise",
      "numDocuments": "Number: total number of documents in this project",
      "url": "String: URL to this project (relative to tagtog's domain)",
      "members": [
        //array of project members. The project owner is always returned (with role admin)
        {
          "username": "String: members username invited to this project",
          "role": "String: member's role; string value in {reader, supercurator, admin}"
        },
        //... next members if any
      ]
    },
    //... next projects in this page if any
  ]
}
```

</div>


<div class="two-third-col" markdown="1">

## ⚠️ DEPRECATED ~~GET list of my projects~~

**👉 Use [search-my-projects](#search-my-projects) instead**

Return the list of projects that the (authenticated) user is a member of. This includes the projects created by the user, and the projects as an invitee.

| **Endpoint** | `{{ page.api_endpoint }}/my_projects` |
| **Method**   | `GET`                                 |
| **Output**   | JSON                                  |


###### Input Parameters

None


###### Coding examples

<div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-curl">cURL</a></li>    
  </ul>
  <div class="tab">
<div id="tab-1-curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u yourUsername:yourPassword {{ page.api_document_url }}/my_projects
```
</div>
  </div>
</div>

</div>

<div class="one-third-col">
  {% include image.html name="API_projects/GET-my-projects.png" caption="example, GET list of my projects"%}
</div>  
