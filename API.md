---
layout: page
title: API
sidebar_link: true
---
<p>API to process documents or plain text.</p>
<div class="page-section">
  <div class="two-third-col">
    
    
    <table style="width:100%;white-space:nowrap;">
      <tr>
        <td><strong>Version</strong></td>
        <td><code>0.1.33</code></td>
      </tr>
      <tr>
        <td><strong>Endpoint</strong></td>
        <td>Documents</td>
      </tr>
      <tr>
        <td><strong>URL</strong></td>
        <td><a href="https://www.tagtog.net/api/0.1/documents">https://tagtog.net/api/0.1/documents</a></td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
  </div>
</div>
<div class="two-third-col">
  <h2>Authentication</h2>
  <p>The current API supports <a href="https://en.wikipedia.org/wiki/Basic_access_authentication">Basic Authentication</a>. Note that the username and password are secured via an HTTPS connection.</p>
</div>
<div class="one-third-col">
</div>





## Authentication

The current API supports [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). Note that the username and password are secured via an https connection.

**For free requests**, with some limitations, you can leave the `username:password` combination empty.

## Parameters

The following are the supported parameters in this API version. Those marked as `PUT` can be sent in a PUT request and must be contained in the request body. In addition, those marked as `GET` can be sent in GET or PUT requests and be contained in the body (if PUT) or directly in the URL (which is limited to 2000 characters).

Additionally, those parameters marked with `DELETE` can be sent in an http DELETE request for the the deletion of documents. Using `DELETE`, the output is a single integer indicating the number of effectively deleted documents -- the `output` parameter is discarded.

Those parameters with defined value `...` represent non-empty value lists. Those with defined value `.` represent single values. In particular, all API submissions can be for 1 or more documents (non-empty list). In practice, however, different `output` formats allow either only 1 document or multiple ones.

* Input (each subgroup is incompatible with each other. See below for documentation):
  * By id:
    * (GET+DELETE) `idType`=. (defaults to `tagtogID`)
    * (GET+DELETE) `ids`=... (comma-separated list of ids, all of the same type. For DELETE to work, the `idType` must be `tagtogID`)
  * (PUT) `text`=. (free text / string)
  * (GET) `url`=. (or synonym `target`=.) (url pointing to a document resource)
  * (PUT) `files`=...
  * (GET+DELETE) `search`= [see search options](https://github.com/tagtog/tagtog-doc/wiki/search-parameter). Compatible with the outputs: 
    * [`search`](https://github.com/tagtog/tagtog-doc/wiki/search-(format)) (default)
    * `authors`
    * `csv` (in this case, the query is ignored & all documents are returned)

* (GET) `ontologies`=... -- comma-separated list of the names of your project's ontologies/dictionaries to use for the document entity tagging; defaults to `ontologies=*`, meaning all project-defined ontologies/dictionaries. **Example**: `ontologies=City,Name,SwissProt`. If empty (as in `ontologies=`), no analysis is performed, which effectively serves the purpose of uploading documents as is. **Note:** you can include (the name of) your own dictionaries and also the [[tagtog-ml supported ontologies]].
* (GET) `output`=. (defaults to `visualize` -- _See below for documentation_)

### Optional Parameters

* Project specific:
  * (GET) `owner`=. (defaults to the username sending the request)
  * (GET) `member`=. (defaults to `master`, aka project official annotations. Otherwise this is only applicable if the project has multiple team members)
  * (GET) `folder`=. (defaults to `pool`; possible values: `{pool, test}`)

* Other:
  * (GET) `page`=. (Number: page number in a paginated search; see `search` parameter)
  * (GET) `part`=. (specific document part/section as referenced by the the element if of the `html`) -- **Note:** currently it works only with outputs `html` and `txt` (and their synonyms)
  * (GET) `ann`=. (specific annotation as uniquely identified in the `ann.json`) -- **Note:** currently it works only with output `json-ld`


### Parameters planned for a next API version

* _no specific plans_


## Input

### `idType`

Possible values are:

* `tagtogID` -- tagtog-internal document id or `docid`. Its use implicitly means that the document already exists in the associated project.
* `PMID` -- PubMed ID
* `PMCID` -- PubMed Central ID

### `files`

Any file accepted by tagtog at the time of the request or as limited by the current API version, if any. See [input formats](http://tagtog.github.io/tagtog-doc/inputformats.html).


## `output` Formats

General description of the output formats accepted here: [output formats](http://tagtog.github.io/tagtog-doc/outputformats.html)

The output format can be specified with the `output` parameter. Formats prefixed with `1` support one document only. In practice, for these outputs you must submit multiple API requests to obtain multiple document results. Those formats prefixed with `n` support multiple documents. In practice, for these outputs a single API request suffices to obtain results of multiple documents.

* (1) `visualize` -- choose to visualize the document resource returning the web page directly (`web` or `web-editor-only` if the [User Agent](https://en.wikipedia.org/wiki/User_agent) is a recognized browser and a tagtog project information was given, i.e. `web`, or, respectively, no tagtog project was given, i.e., `web-editor-only`) or otherwise return the `weburl` (typically, the User Agent will be a command line program)
* (1) `web` -- visual representation of the document and its annotations on the tagtog web interface (HTML page)
* (1) `web-editor-only` -- analogously as `web`, yet _without_ the information of a tagtog project, i.e., only the document editor is shown.
* (1) `weburl` -- url of the document resource and its annotations pointing to the tagtog web interface
* (n) `null` -- special output to signify that no document output is desired. A JSON response of the request will be returned instead. Note, you can use `null` for uploading multiple files at once.
* (1) `ann.json` -- annotations part of the [anndoc format](anndoc)
* (1) `html` or `xml` -- content part of the [anndoc format](anndoc)
* (1) `txt` or `text` -- document content in plain text
* (n) `tsv`-- [see here (you must be logged in tagtog)](https://www.tagtog.net/-doc/formats/outFullTsv_v0_2). **Note:** doesn't work at the moment
* (n) `search` -- [JSON format](https://github.com/tagtog/tagtog-doc/wiki/search-(format)) for a search's results. Compatible only with the input `search`
* (n) `csv` -- list of the project's documents and their master (official) annotation status'. **Note:** currently it works only with input `search=*`
* (1) `pubannotation` -- [See here](http://www.pubannotation.org/docs/annotation-format/)
* (1) `docjson` -- experimental output
* (1) `json-ld` -- [See here](http://restful-open-annotation.github.io/spec/)
* (1) `bioc` -- [See here](http://bioc.sourceforge.net/)
* (n) `authors` -- (json format) it will retrieve a ranking with list of authors that has written the documents found with the parameter `search`. `authors-1` will limit the ranking to the author who wrote the largest amount of publications. You can use `authors-2`, `authors-3`, ..., `authors-200`. By default 20. [See the output format here] (https://github.com/tagtog/tagtog-doc/wiki/Authors-view-example)

**Note**: all output formats are returned in their latest format versions. The format versions cannot be chosen.

---

# Examples

## Upload (files) & Search & Download

### 🐍 python

[Use the official tagtog script 😀](https://github.com/tagtog/tagtog-doc/blob/master/tagtog)


## Annotate a web site

Upload and annotate URL.

### 💻 curl

Please remember to use basic authentication.

```shell
curl -u yourUsername:yourPassword 'https://www.tagtog.net/api/0.1/documents?project=yourprojectname&owner=yourusername&url=http%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fprojects%2Fgap%2Fcgi-bin%2Fstudy.cgi%3Fstudy_id%3Dphs000980.v1.p1&output=ann.json'
```

### 🌐browser

Remember you need to be logged in if you want to use the API through the browser.

https://www.tagtog.net/api/0.1/documents?project=yourprojectname&owner=yourusername&url=http%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fprojects%2Fgap%2Fcgi-bin%2Fstudy.cgi%3Fstudy_id%3Dphs000980.v1.p1&output=visualize


## Annotate one document with PMID (or PMCID)

Upload and annotate a PubMed article using its PMID

### 💻 curl

Please remember to use basic authentication.

```shell
curl -u yourUsername:yourPassword 'https://www.tagtog.net/api/0.1/documents?project=yourprojectname&owner=yourusername&idType=PMID&ids=23596191&output=bioc'
```

### 🌐browser

Remember you need to be logged in if you want to use the API through the browser.

https://www.tagtog.net/api/0.1/documents?project=yourprojectname&owner=yourusername&idType=PMID&ids=23596191&output=ann.json

## Annotate plain text

Upload and annotate plain text.

### 💻 curl

Please remember to use basic authentication. 

```shell
curl -u yourUsername:yourPassword -X PUT -d 'text=Antibody-dependent cellular cytotoxicity (ADCC), a key effector function for the clinical effectiveness of monoclonal antibodies, is triggered by the engagement of the antibody Fc domain with the Fcγ receptors expressed by innate immune cells such as natural killer (NK) cells and macrophages. Here, we fused cancer cell-binding peptides to the Fc domain of human IgG1 to engineer novel peptide-Fc fusion proteins with ADCC activity' 'https://www.tagtog.net/api/0.1/documents?project=yourprojectname&owner=yourusername&output=pubannotation'
```

### 🐍 python

```python
#pip install requests
import requests

url = 'https://www.tagtog.net/api/0.1/documents'
auth = requests.auth.HTTPBasicAuth(username='<your_username>', password='<your_password>')
params = {'project':'<your_project>', 'owner':'<your_username>', 'output':'ann.json'}
text = 'Antibody-dependent cellular cytotoxicity (ADCC), a key effector function for the clinical effectiveness of monoclonal antibodies'
payload = {'text': text}
response = requests.put(url, params=params, auth=auth, data=payload)
print(response, response.text)
```

---
## Search documents in a project

### 💻 curl

The following call will retrieve the documents matching the search string, in this case `*` represents all documents.

```shell
curl -u yourUsername:yourPassword 'https://www.tagtog.net/api/0.1/documents?project=project_name&search=*'
```

The format of the output: [search format](https://github.com/tagtog/tagtog-doc/wiki/search-(format))
To build the search string: [search parameter](https://github.com/tagtog/tagtog-doc/wiki/search-parameter)

---

## Get documents already uploaded

You need the Id of the document before you get it. If you don't have this Id, you can find it using the `search` feature. In the next example, we use this id to get the document in `ann.json` format.

```shell
curl -u yourUsername:yourPassword 'https://www.tagtog.net/api/0.1/documents?project=project_name&ids=aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text&output=ann.json'
```

---

## Delete all documents in a project

### 💻 curl

```shell
curl -u yourUsername:yourPassword -X DELETE 'https://www.tagtog.net/api/0.1/documents?project=yourProject&search=*'
```

Similarly, fine-tune the `search` parameter to delete only those documents returned by the search; `search=*` finds all and therefore the DELETE call deletes all documents.