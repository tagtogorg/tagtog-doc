---
id: api_documents_v1
title: API documents
layout: page
version: 1.0
sidebar_link: true
toc: true

api_endpoint: /-api/documents/v1
api_document_url: https://www.tagtog.net/-api/documents/v1
api_username: yourUsername
api_pwd: yourPassword
api_project: yourProjectName
api_plain_text: Antibody-dependent cellular cytotoxicity (ADCC), a key effector function for the clinical effectiveness of monoclonal antibodies, is triggered by the engagement of the antibody Fc domain with the Fcγ receptors expressed by innate immune cells such as natural killer (NK) cells and macrophages.
---

<div class="two-third-col">
  <br/>
  <p>Thanks for choosing the <strong>Documents API</strong> to build NLP solutions into your app or website. Getting started with a new API can be challenging, so we have created a step-by-step guide that walks you through how to make your first API calls and more.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You will need an <strong>account at tagtog</strong>. <a href="https://www.tagtog.net/#signup">Sign up at tagtog.net</a> if you are using the cloud version or check with your admin if you are using an on-premises version.' %}
</div>




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
<div class="one-third-col">
  {% include message.html message='Use this <a href="https://github.com/tagtog/tagtog-doc/blob/master/tagtog.py" title="tagtog python script"><strong>tagtog python script</strong></a> ready to do many common operations in tagtog using the API: upload (also folders), search, and download documents!' %}
</div>
<div class="two-third-col">
  <h2>Authentication</h2>
  <p>The current API supports <a href="https://en.wikipedia.org/wiki/Basic_access_authentication">Basic Authentication</a>. Note that the username and password are secured via an HTTPS connection.</p>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h2>Import and annotate text</h2>
  <p>One of the most common scenarios using tagtog is to annotate text automatically. The API is the perfect way to automate this task.</p>


  <h3>Plain text <code>POST</code></h3>
  <p>Annotates automatically plain text.</p>
  <p><strong>Input Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>text</code></td>
      <td>-</td>
      <td>{{ page.api_plain_text }}</td>
      <td>Plain text</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>ann.json</code></td>
      <td>The format of the output you want to be returned by the API. <a href="#output-parameter">API output formats</a>.</td>
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
      <td><code>member</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has <a href="/collaboration.html">multiple team members</a></p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>format</code></td>
      <td>-</td>
      <td><code>verbatim</code></td>
      <td>Force how the <em>format</em> of the inputted text should be interpreted; <a href="ioformats.html#distinguish-format-by-given-format-parameter">more info.</a></td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td><code>John,Laura</code></td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>&ast;</code> means to select all team members to distribute to; and 3) <code>-</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  {% include message.html message='Imported documents are visible in the <a href="/documents.html">document pool</a>'%}
</div>


<div class="two-third-col">
  <h4>Examples: send plain text</h4>
  <br/>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-plain-text">cURL</a></li>
      <li><a href="#tab-2-plain-text">Python</a></li>
      <li><a href="#tab-3-plain-text">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">The example below imports plain text and retrieve the automatic annotations in <code>ann.json</code> format.</p>
<div id="tab-1-plain-text" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST -d 'text={{ page.api_plain_text }}' '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&output=ann.json'
```
</div>


<div id="tab-2-plain-text" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'output':'ann.json'}
payload = {'text': '{{ page.api_plain_text }}'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_annotate_plain_text.py" %}</p>
</div>
<div id="tab-3-plain-text" class="tab-content" markdown="1">
```javascript
fetch('{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&output=ann.json', {
    method: 'POST',
    headers: {'Authorization' : "Basic " + btoa('{{ page.api_username }}' + ":" + '{{ page.api_pwd }}'),
              'Accept': 'application/json',
              'Content-Type': 'application/json',
             },
    body: JSON.stringify({'text':'{{ page.api_plain_text }}'})
}).then(response => response.json()).then(json => {
  console.log(json);
}).catch(function(error) {
  console.log('Error: ', error);
});
```
<p style="float:right">{% include github-link.html target="snippets/api_js_annotate_plain_text.html" %}</p>
</div>
      </div>
    </div>
  </div>

<div class="one-third-col">
  <p>Response <code>ann.json</code></p>
<div markdown="1">
```json
{
  "anncomplete":false,
  "sources":[],
  "entities":
    [
      { "classId":"e_1","part":"s1p1","offsets":[{"start":251, "text":"natural killer"}],"confidence":{"state":"pre-added", "who":["ml:dpeker","prob":0.3287},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O14763","url":null},"recName":"Tumor necrosis factor receptor superfamily member 10B","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.3287}}}},
      { "classId":"e_1","part":"s1p1","offsets":[{"start":267,"text":"NK"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.3287},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O14763","url":null},"recName":"Tumor necrosis factor receptor superfamily member 10B","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.3287}}}}
    ],
    "metas":{},
    "relations":[],
    "annotatable":{"parts":["s1h1","s1p1"]}
}
```
</div>
</div>



<div class="two-third-col">
  <h4>Examples: send plain text as verbatim</h4>
  <br/>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">      
      <li class="current"><a href="#tab-plain-text-verbatim-python">Python</a></li>
    </ul>
    <div class="tab">
      <p class="code-desc">This example imports plain text in verbatim format (pre-formatted) and returns the result of the operation (<code>null</code> output).</p>
<div id="tab-plain-text-verbatim-python" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
params = {"project": "yourProjectName", "owner": "yourUsername", "output": "null"}
payload = {
    "format": "verbatim",
    "text": "The film stars Leonardo DiCaprio, Brad Pitt and Margot Robbie"
}
response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)
print(response.text)
```
</div>

    </div>
  </div>
</div>

<div class="one-third-col">
  <p>Response <code>null</code></p>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "text.txt",
    "names": ["text.txt"],
    "rawInputSizeInBytes": 61,
    "tagtogID": "aumzCn3f5E9zDs4yihXZAipZjLx0-text.txt",
    "result": "created",
    "parsedTextSizeInBytes": 61
  }],
  "warnings": []
}
```
</div>
</div>




{::comment}
URLS
{:/comment}

<div class="two-third-col">
  <h3>URL <code>POST</code> <code>GET</code></h3>
  <p>Import the text content of a URL and annotate it.</p>
  <p><strong>Input Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>url</code></td>
      <td><code>-</code></td>
      <td class="break-all"><a href="https://en.wikipedia.org/wiki/Autonomous_cruise_control_system">https://en.wikipedia.org/wiki/Autonomous_cruise_control_system</a></td>
      <td>URL no annotate</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>weburl</code></td>
      <td>The format of the output you want to be returned by the API. <a href="#output-parameter">API output formats</a>.</td>
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
      <td><code>member</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has <a href="/collaboration.html">multiple team members</a></p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td><code>John,Laura</code></td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>&ast;</code> means to select all team members to distribute to; and 3) <code>-</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  {% include message.html message="<strong>Problems with URL encoding?</strong> encode URLs online <a href='https://meyerweb.com/eric/tools/dencoder/' title='MeyerWeb - URL Decoder/Encoder'>here</a>" %}
</div>
<div class="two-third-col">
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-url">cURL</a></li>
      <li><a href="#tab-2-url">Python</a></li>
      <li><a href="#tab-3-url">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">The example below imports a URL and retrieves the web link for the annotated document. That link redirects to the annotated document at the tagtog app.</p>
<div id="tab-1-url" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&url=https://en.wikipedia.org/wiki/Autonomous_cruise_control_system&output=weburl'
```
</div>
<div id="tab-2-url" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'output':'weburl', 'url':'https://en.wikipedia.org/wiki/Autonomous_cruise_control_system'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_annotate_url.py" %}</p>
</div>
<div id="tab-3-url" class="tab-content" markdown="1">
```javascript
fetch('https://www.tagtog.net/-api/documents/v1?project={{ page.api_project }}&owner={{ page.api_username }}&url=https://en.wikipedia.org/wiki/Autonomous_cruise_control_system&output=weburl', {
  method: 'GET',
  headers: {'Authorization' : "Basic " + btoa('{{ page.api_username }}' + ":" + '{{ page.api_pwd }}')},
}).then(response => response.text()).then(text => {
  console.log(text);
}).catch(function(error) {
  console.log('Error: ', error);
});
```
<p style="float:right">{% include github-link.html target="snippets/api_js_annotate_url.html" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response <code>weburl</code></p>
<div markdown="1">
```shell
http://localhost:9000/gontras/vproject/pool/aXusqkMqtSLvmBDzeVkhNtV2LKUW-Autonomous_cruise_control_system.html
```
</div>
</div>




{::comment}
FILES
{:/comment}

<div class="two-third-col">
  <h3>Files <code>POST</code></h3>
  <p>Import a file and annotate it.</p>
  <p><strong>Input Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>files</code></td>
      <td>-</td>
      <td>text.txt, text2.txt</td>
      <td>List of files to annotate. <a href="/ioformats.html#files">Supported input formats</a></td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>ann.json</code></td>
      <td>The format of the output you want to be returned by the API. <a href="#output-parameter">API output formats</a>.</td>
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
      <td><code>member</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has <a href="/collaboration.html">multiple team members</a></p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td><code>John,Laura</code></td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>&ast;</code> means to select all team members to distribute to; and 3) <code>-</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
  </table>

</div>
<div class="one-third-col">

</div>
<div class="two-third-col">
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-2-file">Python</a></li>
      <li><a href="#tab-3-file">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example imports a file and retrieves the annotations in <code>ann.json</code>. You can extend it easily to upload multiple files.</p>
<div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'output':'ann.json'}
#you can append more files to the list in case you want to upload multiple files
files = [('file', open('files/text.txt'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_annotate_files.py" %}</p>
</div>
<div id="tab-3-file" class="tab-content" markdown="1">
```javascript
var input = document.querySelector('input[type="file"]')
var data = new FormData()
data.append('file', input.files[0])

fetch('{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&output=ann.json', {
  method: 'POST',
  headers: {'Authorization' : "Basic " + btoa('{{ page.api_username }}' + ":" + '{{ page.api_pwd }}')},
  body: data
}).then(response => response.text()).then(text => {
  console.log(text);
}).catch(function(error) {
  console.log('Error: ', error);
});
```
<p style="float:right">{% include github-link.html target="snippets/api_js_annotate_files.html" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response <code>ann.json</code></p>
<div markdown="1">
```json
{
  "anncomplete":false,
  "sources":[],
  "entities":[
    {"classId":"e_1","part":"s1p5","offsets":[{"start":187,"text":"apolipoprotein E"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p5","offsets":[{"start":205,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p6","offsets":[{"start":0,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p7","offsets":[{"start":0,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p8","offsets":[{"start":0,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p9","offsets":[{"start":0,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p11","offsets":[{"start":24,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p11","offsets":[{"start":108,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p11","offsets":[{"start":139,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p11","offsets":[{"start":223,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p12","offsets":[{"start":41,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p12","offsets":[{"start":146,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p12","offsets":[{"start":180,"text":"APOE"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P02649","url":null},"recName":"Apolipoprotein E","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.9293}}}},
    {"classId":"e_1","part":"s1p15","offsets":[{"start":0,"text":"ABCA7"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q8IZY2","url":null},"recName":"ATP-binding cassette sub-family A member 7","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271}}}},
    {"classId":"e_1","part":"s1p15","offsets":[{"start":25,"text":"ABCA7"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q8IZY2","url":null},"recName":"ATP-binding cassette sub-family A member 7","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271}}}},
    {"classId":"e_1","part":"s1p16","offsets":[{"start":0,"text":"CLU"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6826},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P10909","url":null},"recName":"Clusterin","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6826}}}},
    {"classId":"e_1","part":"s1p17","offsets":[{"start":0,"text":"CR1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6826},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"P17927","url":null},"recName":"Complement receptor type 1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6826}}}},
    {"classId":"e_1","part":"s1p18","offsets":[{"start":0,"text":"PICALM"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8617},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13492","url":null},"recName":"Phosphatidylinositol-binding clathrin assembly protein","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8617}}}},
    {"classId":"e_1","part":"s1p19","offsets":[{"start":0,"text":"PLD3"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q8IV08","url":null},"recName":"Phospholipase D3","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s1p19","offsets":[{"start":51,"text":"PLD3"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q8IV08","url":null},"recName":"Phospholipase D3","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s1p20","offsets":[{"start":0,"text":"TREM2"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q9NZC2","url":null},"recName":"Triggering receptor expressed on myeloid cells 2","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271}}}},
    {"classId":"e_1","part":"s1p21","offsets":[{"start":0,"text":"SORL1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q92673","url":null},"recName":"Sortilin-related receptor","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271}}}},
    {"classId":"e_1","part":"s1p21","offsets":[{"start":26,"text":"SORL1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q92673","url":null},"recName":"Sortilin-related receptor","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.8271}}}}
  ],
  "metas":{},
  "relations":[],
  "annotatable":{"parts":["s1h1","s1p1","s1p2","s1p3","s1p4","s1p5","s1p6","s1p7","s1p8","s1p9","s1p10","s1p11","s1p12","s1p13","s1p14","s1p15","s1p16","s1p17","s1p18","s1p19","s1p20","s1p21"]}
}
```
</div>
</div>




{::comment}
PUBMED IDS
{:/comment}

<div class="two-third-col">
  <h3>PubMed Abstracts <code>POST</code> <code>GET</code></h3>
  <p>Import one or more PubMed abstracts and annotate them.</p>
  <p><strong>Input Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>idType</code></td>
      <td><code>tagtogID</code></td>
      <td><code>PMID</code></td>
      <td>Type of Id. <a href="/API_documents_v1.html#idtype-parameter">List of idTypes</a></td>
    </tr>
    <tr>
      <td><code>ids</code></td>
      <td>-</td>
      <td>23596191, 29438695</td>
      <td>Comma-separated list of ids, all the same type. The response is limited to the last id imported. </td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>ann.json</code></td>
      <td>The format of the output you want to be returned by the API. <a href="#output-parameter">API output formats</a>.</td>
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
      <td><code>member</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has <a href="/collaboration.html">multiple team members</a></p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td><code>John,Laura</code></td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>&ast;</code> means to select all team members to distribute to; and 3) <code>-</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  <div class="message">
    You can also import <a href="https://www.ncbi.nlm.nih.gov/pmc/">PubMed Central</a> (PMC) articles by using the PMCIDs. The idType is <code>PMCID</code>
  </div>
</div>
<div class="two-third-col">
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-pmid">cURL</a></li>
      <li><a href="#tab-2-pmid">Python</a></li>
      <li><a href="#tab-3-pmid">JavaScript</a></li>
    </ul>
    <div class="tab">
      <p class="code-desc">The example below imports a list of PMIDs and retrieves the annotations of the last document in <code>ann.json</code> format.</p>
<div id="tab-1-pmid" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&idType=PMID&ids=23596191,29438695&output=ann.json'
```
</div>
<div id="tab-2-pmid" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'idType':'PMID', 'ids':['23596191','29438695'], 'output':'ann.json'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_annotate_pmids.py" %}</p>
</div>
<div id="tab-3-pmid" class="tab-content" markdown="1">
```javascript
fetch('https://www.tagtog.net/api/0.1/documents?project=yourProject&owner=yourUsername&idType=PMID&ids=23596191,29438695&output=ann.json', {
  method: 'POST',
  headers:  { 'Authorization' : "Basic " + btoa('yourUsername' + ":" + 'yourPassword'),
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
}).then(response => response.json()).then(json => {
  console.log(json);
}).catch(function(error) {
  console.log('Error: ', error);
});

```
<p style="float:right">{% include github-link.html target="snippets/api_js_annotate_pmids.html" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response <code>ann.json</code></p>
<div markdown="1">
```json
{
  "anncomplete":false,
  "sources":[{"name":"PMID","id":"23596191","url":"http://www.ncbi.nlm.nih.gov/pubmed/23596191"}],
  "entities":
  [
    {"classId":"e_1","part":"s1h1","offsets":[{"start":60,"text":"RETICULATA-RELATED"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":315,"text":"RETICULATA-RELATED"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":335,"text":"RER"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":444,"text":"RER1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":561,"text":"PROTEIN"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.3289},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q8IVL6","url":null},"recName":"Prolyl 3-hydroxylase 3","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.3289}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1127,"text":"rer1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4836},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4836}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1265,"text":"RER1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1303,"text":"RER1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1391,"text":"RER"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1587,"text":"RER"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1591,"text":"proteins"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4073},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q15517","url":null},"recName":"Corneodesmosin","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4073}}}}
  ],
  "metas":{},
  "relations":[],
  "annotatable":{"parts":["s1h1","s2h1","s2p1"]}
}
```
</div>
</div>




<div class="two-third-col">
  <h3>Import annotated documents <code>POST</code></h3>
  <p>If you have annotated documents you want to import, you need to upload two files:</p>
  <p class="list-item"><span class="list-item-1"></span><strong>The text or document</strong>. This can be a regular file (e.g. txt, xml, pdf, <a title="tagtog - plain.html format" href="/anndoc.html#plain-html">plain.html</a>, etc.), plain text, etc. Check the supported <a title="tagtog - input formats" href="ioformats.html#input-formats">input formats</a></p>
  <p class="list-item"><span class="list-item-2"></span><strong>The annotations</strong>. You pass this as an <code><a title="tagtog - ann.json format" href="/anndoc.html#ann-json">ann.json</a></code>.</p>
  <p><strong>They must have the same name, except for the file extensions</strong>. For example: <code>mydoc.pdf</code> and <code>mydoc.ann.json</code>.</p>

  <p>You can use the same API method you use to upload a single file to annotate: <a href="/API_documents_v1.html#files-post" title="Import files to tagtog">Files API POST</a>.</p>

  <p><strong>Input Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>files</code></td>
      <td>-</td>
      <td>text.txt, text.ann.json</td>
      <td>You need to upload in the same request both: the text (supported input format) and the ann.json (annotations) files.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>null</code></td>
      <td></td>
    </tr>
    <tr>
      <td><code>format</code></td>
      <td><code>default-plus-annjson</code></td>
      <td><code>anndoc</code></td>
      <td>Format of the pre-annotated document. Remember that <code>anndoc</code> format requires the content as <code>plain.html</code>. List of supported pre-annotated formats: <a title="tagtog - Annotation input formats" href="ioformats.html#annotation-input-formats">Pre-annotated input formats</a></td>
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
      <td><code>member</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has <a href="/collaboration.html">multiple team members</a></p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td><code>John,Laura</code></td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>&ast;</code> means to select all team members to distribute to; and 3) <code>-</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
  </table>

</div>

<div class="one-third-col">
  {% include message.html message='You can send multiple annotated documents at the same time. This means you always upload an even number of files.' %}
</div>

<div class="two-third-col">

  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-file">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to upload a preannotated document (txt file + ann.json) to tagtog. In this case we write the content of the ann.json file, but you could easily point to a existing ann.json file. Make sure the ann.json is well formated. The format used is <code>default-plus-annjson</code>.</p>
  <div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
  ```python

  import requests

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"
  auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
  params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'output':'null', 'format': 'default-plus-annjson'}

  files = {
    'ann': ('text.ann.json', '{"annotatable":{"parts":[]},"anncomplete":false,"sources":[],"metas":{"m_1":{"value":"optionA","confidence":{"state":"pre-added","who":["user:{{ page.api_username }}"],"prob":1}}},"entities":[],"relations":[]}'),
    'plain': ('text.txt', open('./text.txt'))
  }

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  ```
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response</p>
<div markdown="1">
```json
{"ok":1,"errors":0,"items":[{"origid":"text","names":["text.txt","text.ann.json"],"rawInputSizeInBytes":208,"tagtogID":"asFec0QPFqIFaySbl.j0caWPSS9m-text","result":"created","parsedTextSizeInBytes":15}],"warnings":[]}
```
</div>
</div>


<div class="two-third-col">
  <h3>Replace annotations of existing document <code>POST</code></h3>
  <p>You should use two files:</p>
  <p class="list-item"><span class="list-item-1"></span><strong>The <a title="tagtog - plain.html format" href="/anndoc.html#plain-html">plain.html</a></strong>. You can obtain this file by <a title="Get files - tagtog API" href="API_documents_v1.html#get-existing-documents-get">downloading it from the API</a> using the output <code>html</code>.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>The annotations</strong>. You pass this as an <code><a title="tagtog - ann.json format" href="/anndoc.html#ann-json">ann.json</a></code>.</p>
  <p><strong>They must have the same name, except for the file extensions</strong>. For example: <code>mydoc-3243hdsfk3.plain.html</code> and <code>mydoc-3243hdsfk3.ann.json</code>.</p>

  <p>You can use the same API method you use to upload a single file to annotate: <a href="/API_documents_v1.html#files-post" title="Import files to tagtog">Files API POST</a>.</p>

  <p><strong>Input Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>files</code></td>
      <td>-</td>
      <td>docidABCDEF.plain.html, docidABCDEF.ann.json</td>
      <td>You need to upload in the same request both: the plain.html (content) and the ann.json (annotations) files.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>null</code></td>
      <td></td>
    </tr>
    <tr>
      <td><code>format</code></td>
      <td><code>anndoc</code></td>
      <td><code>anndoc</code></td>
      <td>Format of the pre-annotated document. List of supported pre-annotated formats: <a title="tagtog - Annotation input formats" href="ioformats.html#annotation-input-formats">Pre-annotated input formats</a> </td>
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
      <td><code>member</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has <a href="/collaboration.html">multiple team members</a></p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td><code>John,Laura</code></td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>&ast;</code> means to select all team members to distribute to; and 3) <code>-</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
  </table>

</div>

<div class="one-third-col">
  {% include message.html message='You can send multiple annotated documents at the same time. This means you always upload an even number of files.' %}
</div>



<div class="two-third-col">

  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-file">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to replace the annotations of an existing document (plain.html + ann.json) to tagtog.</p>
  <div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
  ```python
  import requests

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

  auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
  params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'output':'null', 'format': 'anndoc'}

  files = [('file', open('/annotated-docs/docidABCDEF.plain.html')), ('file', open('/annotated-docs/docidABCDEF.ann.json'))]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  ```
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response</p>
<div markdown="1">
```json
{"ok":1,"errors":0,"items":[{"origid":"text","names":["docidABCDEF.ann.json","docidABCDEF.plain.html"],"rawInputSizeInBytes":1038,"tagtogID":"docidABCDEF","result":"created","parsedTextSizeInBytes":29}],"warnings":[]}
```
</div>
</div>





<div class="two-third-col">
  <h2>Search documents in a project <code>GET</code></h2>
  <p>You can <a href="/search.html">search</a> using the documents API. Search across your project and retrieve the matching documents. You can use it to augment your own search engine or simply create a new one. It is also very simple to use the search API to display statistics. Here we show you how to do it.</p>
  <p>Learn how to <strong>build search queries</strong> <a href="/search-queries.html">here</a>.</p>
  <p><strong>Input Parameters</strong></p>
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
      <td>entity:GGP:P02649 or folder:pool</td>
      <td><strong>Search query</strong>. Learn how to build queries <a href="/search-queries.html">here</a>.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
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
          <p><code>search</code> (<a href="#search-response-format">search response</a>): use it to perform search queries.</p>
          <p><code>csv</code>: it ignores the query parameter and retrieves for each document its id and status (true if annotations are completed/confirmed, false if not)</p>
      </td>
    </tr>
  </table>
</div>
<div class="one-third-col">
  {% include message.html message='Search queries through the API return a response with the JSON <code>search response</code>. <a href="#search-response-format"> Documentation</a>' %}
  {% include message.html message='Use the search features to retrieve the progress of the annotation tasks.' %}
</div>
<div class="two-third-col">

  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-search">cURL</a></li>
      <li><a href="#tab-2-search">Python</a></li>
      <li><a href="#tab-3-search">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example searches across all your folders to find documents that have at least one entity normalized to the gene <a href="https://www.uniprot.org/uniprot/P02649">P02649</a>.</p>
<div id="tab-1-search" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&search=entity:GGP:P02649'
```
</div>
<div id="tab-2-search" class="tab-content" markdown="1">
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
<div id="tab-3-search" class="tab-content" markdown="1">
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
  <p><code>search</code> response</p>
<div markdown="1">
```json
{
  "version": "0.1.0",
  "search": "entity:GGP:P02649",
  "totalFound": 1,
  "pages": {"current": 0, "previous": -1, "next": -1},
  "docs":
    [
      {
        "id": "aMHKzF_lIoNrdh9pAx298njgIezy-text",
        "header": "Certain genes make you more likely to develop Alzheimer's disease. Genes control the function of every cell in your body. Some genes determine basic characterist",
        "updated": "2018-03-03T20:59:56.467Z",
        "anncomplete": false,
        "members_anncomplete": ["someMemberUsername"],
        "folder": "pool/mySubFolder"
      }
    ]
}
```
</div>

<hr/>

<p><code>csv</code> response</p>
<div markdown="1">
```csv
docid,anncomplete
abPz9JKO2jdP9XKbn4Beuh3rk3Y4-text,false
aPvgZql3RogPu90jVkoV7rZODU8u-text,false
ap_FCtCdahae2jMD_opHUD9f7lM8-text,true
aMHKzF_lIoNrdh9pAx298njgIezy-text,false
```
</div>
</div>





<div class="two-third-col">
  <h3>Search response format</h3>
  <p>Response format for search queries.</p>
<div markdown="1">
```javascript
{
  "version": "String: this format's version, e.g. 0.3.0",
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
      "updated": "String: date for the document' last update, in ISO_INSTANT format, e.g. 2017-02-23T08:31:40.874Z",
      "anncomplete": "Boolean: status for the document's annotation completion",
      "members_anncomplete": ["String Array: usernames of members who completed (confirmed) their annotations"],
      "folder": "String: folder path where the document is located; e.g. `pool/mySubFolder`"
    },
    //next documents in the array of results...
  ]
}
```
</div>
</div>
<div class="one-third-col">

</div>


<div class="two-third-col">
  <h2>Get existing documents <code>GET</code></h2>
  <p>You can use the API to export documents. You need the Id of the document to get it. If you don't have this Id, you can find it using the <a href="#search-documents-in-a-project-get">search</a> feature. You can export only 1 document within each request.</p>
</div>
<div class="two-third-col">
  <p><strong>Input Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualization</code></td>
      <td><code>ann.json</code></td>
      <td>The format of the output you want to be returned by the API. <a href="#output-parameter">API output formats</a>.</td>
    </tr>
    <tr>
      <td><code>idType</code></td>
      <td><code>tagtogID</code></td>
      <td><code>tagtogID</code></td>
      <td>Type of Id. <a href="/API_documents_v1.html#idtype-parameter">List of idTypes</a></td>
    </tr>
    <tr>
      <td><code>ids</code></td>
      <td>-</td>
      <td class="break-all">aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text</td>
      <td>Comma-separated list of ids, all the same type. The response is limited to the last id imported. </td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
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
      <td><code>member</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has <a href="/collaboration.html">multiple team members</a></p></td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  {% include message.html message="If while manual annotating you create <strong>pre-annotations</strong>, they will also appear in the output" %}
</div>

<div class="two-third-col">
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-getdoc">cURL</a></li>
      <li><a href="#tab-2-getdoc">Python</a></li>
      <li><a href="#tab-3-getdoc">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example exports a tagtog document into <code>ann.json</code> format. Notice that we don't use the parameter <code>idType</code> because it defaults to <code>tagtogID</code>, the type of the id used.</p>
<div id="tab-1-getdoc" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&ids=aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text&output=ann.json'
```
</div>
<div id="tab-2-getdoc" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'ids':'aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text', 'output':'ann.json'}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_getdoc.py" %}</p>
</div>
<div id="tab-3-getdoc" class="tab-content" markdown="1">
```javascript
fetch('{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&ids=aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text&output=ann.json', {
  method: 'GET',
  headers: {'Authorization' : "Basic " + btoa('{{ page.api_username }}' + ":" + '{{ page.api_pwd }}')},
}).then(response => response.text()).then(text => {
  console.log(text);
}).catch(function(error) {
  console.log('Error: ', error);
});
```
<p style="float:right">{% include github-link.html target="snippets/api_js_getdoc.html" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response <code>ann.json</code></p>
<div markdown="1">
```json
{
  "anncomplete":false,
  "sources":[{"name":"PMID","id":"23596191","url":"http://www.ncbi.nlm.nih.gov/pubmed/23596191"}],
  "entities":
  [
    {"classId":"e_1","part":"s1h1","offsets":[{"start":60,"text":"RETICULATA-RELATED"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":315,"text":"RETICULATA-RELATED"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":335,"text":"RER"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":444,"text":"RER1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":561,"text":"PROTEIN"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.3289},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q8IVL6","url":null},"recName":"Prolyl 3-hydroxylase 3","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.3289}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1127,"text":"rer1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4836},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4836}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1265,"text":"RER1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1303,"text":"RER1"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"O15258","url":null},"recName":"Protein RER1","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.7737}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1391,"text":"RER"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1587,"text":"RER"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q13123","url":null},"recName":"Protein Red","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.6519}}}},
    {"classId":"e_1","part":"s2p1","offsets":[{"start":1591,"text":"proteins"}],"confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4073},"fields":{},"normalizations":{"n_2":{"source":{"name":"SwissProt","id":"Q15517","url":null},"recName":"Corneodesmosin","confidence":{"state":"pre-added","who":["ml:dpeker"],"prob":0.4073}}}}
  ],
  "metas":{},
  "relations":[],
  "annotatable":{"parts":["s1h1","s2h1","s2p1"]}
}
```
</div>
</div>

<div class="two-third-col">
  <h2>Delete documents <code>DELETE</code></h2>

  <h3>Delete documents by search</h3>
  <p>You can delete documents in your project using the API. Fine-tune the <code>search</code> parameter to delete only those documents returned by the <a href="/search-queries.html">search query</a>.</p>
  <p>This request returns the number of documents deleted.</p>
</div>
<div class="two-third-col">
  <p><strong>Input Parameters</strong></p>
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
      <td>entity:GGP</td>
      <td>Search query to list the documents to remove. Learn how to build queries <a href="/search-queries.html">here</a></td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>-</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
  </table>
</div>
<div class="one-third-col">
  {% include message.html message='<code>search=&ast;</code> finds all and therefore the <code>DELETE</code> call deletes all documents.' %}
</div>

<div class="two-third-col">
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-del">cURL</a></li>
      <li><a href="#tab-2-del">Python</a></li>
      <li><a href="#tab-3-del">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example deletes all documents that contain at least one entity of type <code>gene</code>.</p>
<div id="tab-1-del" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X DELETE '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&search=entity:gene'
```
</div>
<div id="tab-2-del" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'search':'entity:gene'}
response = requests.delete(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_delete.py" %}</p>
</div>
<div id="tab-3-del" class="tab-content" markdown="1">
```javascript
fetch('{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&search=entity:gene', {
  method: 'DELETE',
  headers: {'Authorization' : "Basic " + btoa('{{ page.api_username }}' + ":" + '{{ page.api_pwd }}')},
}).then(response => response.text()).then(text => {
  console.log(text);
}).catch(function(error) {
  console.log('Error: ', error);
});
```
<p style="float:right">{% include github-link.html target="snippets/api_js_delete.html" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response </p>
<div markdown="1">
```javascript
4 //number of documents deleted
```
</div>
</div>

<div class="two-third-col">


  <h3>Delete document by id</h3>

  <p>Delete a single document given its tagtog document id.</p>
  <p>This request returns the number of documents deleted (1 if the document was successfully deleted, 0 otherwise).</p>

  <div>
    <p><strong>Input Parameters</strong></p>
    <table style="width:100%;">
      <tr>
        <th>Name</th>
        <th>Default</th>
        <th>Example</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><code>idType</code></td>
        <td>-</td>
        <td><code>tagtogID</code> (mandatory)</td>
        <td></td>
      </tr>
      <tr>
        <td><code>ids</code></td>
        <td>-</td>
        <td>aEVD52vVm.s2zdTmzK_ACNqH7Z1u-text</td>
        <td></td>
      </tr>
      <tr>
        <td><code>project</code></td>
        <td>-</td>
        <td>{{ page.api_project }}</td>
        <td>Name of the project</td>
      </tr>
      <tr>
        <td><code>owner</code></td>
        <td>-</td>
        <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
        <td>Owner of the project you want to use</td>
      </tr>
    </table>
  </div>

  <div>
    <br/>
    <div id="tabs-container">
      <ul class="tabs-menu">
        <li class="current"><a href="#tab-1-del">cURL</a></li>
      </ul>
      <div class="tab">
        <p class="code-desc">This example deletes a document given by its (tagtog) document id.</p>
<div id="tab-1-del" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X DELETE '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&idType=tagtogID&ids=yourDocumentTagtogID'
```
</div>
      </div>
    </div>
  </div>

  <hr/>

    <hr/>
      <hr/>
        <hr/>
          <hr/>
            <hr/>

</div>


<div class="two-third-col">
<h2><code>output</code> parameter</h2>
<p>These are the different types of outputs supported by the API.</p>
<table style="width:100%;" class="table-with-code">
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>visualize</code></td>
    <td>This is the default value. Choose to visualize the document resource returning the web page directly (<code>web</code> or <code>web-editor-only</code> if the User Agent is a recognized browser and a tagtog project information was given, i.e. web, or, respectively, no tagtog project was given, i.e., <code>web-editor-only</code>) or otherwise return the <code>weburl</code> (typically, the User Agent will be a command line program)</td>
  </tr>
  <tr>
    <td><code>web</code></td>
    <td>Visual representation of the document and its annotations on the tagtog web interface (HTML page).</td>
  </tr>
  <tr>
    <td><code>web-editor-only</code></td>
    <td>Analogously as <code>web</code>, yet without the information of a tagtog project, i.e., only the document editor layout. Useful in case you want to create iFrames in your web app.</td>
  </tr>
  <tr>
    <td><code>weburl</code></td>
    <td>URL of the annotated document at tagtog web interface.</td>
  </tr>
  <tr>
    <td><code>null</code></td>
    <td>Special output to signify that no document output is desired. A JSON response of the request will be returned instead. For example, when importing a document:
<div markdown="1">
```javascript
{
  "ok":1 //number of documents successfully changed,
  "errors":0 //number of documents with errors,
  "items": //list of documents changed
  [
    { "origid":"text",
      "names":["text.txt"],
      "tagtogID":"aOM6EFIvULWc6J.7MAYQB3V2sF84-text",
      "result":"created"}
  ],
  "warnings":[]
}
```
<p>You can use this parameter, for example, if you need the API to return you the id of each document imported.</p>

</div>
    </td>
  </tr>
  <tr>
    <td><code>ann.json</code></td>
    <td>Annotations part of the <a href="/anndoc.html#ann-json">anndoc format documentation</a>.</td>
  </tr>
  <tr>
    <td><code>html</code>, <code>xml</code>, <code>plain.html</code></td>
    <td>Content part of the <a href="/anndoc.html#plain-html">anndoc format documentation</a>.</td>
  </tr>
  <tr>
    <td><code>text</code></td>
    <td>Document content in plain text.</td>
  </tr>
  <tr>
    <td><code>orig</code>, <code>original</code></td>
    <td>The originally submitted file.</td>
  </tr>
  <tr>
    <td><code>csv</code></td>
    <td>List of the project's documents and their master (official) annotation status. Currently it works only with parameter <code>search=&ast;</code></td>
  </tr>
</table>

</div>
<div class="one-third-col">
  {% include message.html message="<strong>Note</strong>: all output formats are returned in their latest format versions. The format versions cannot be chosen." %}
</div>



<div class="two-third-col">
<h2><code>idType</code> parameter</h2>
<p>Possible values for the parameter are described below.</p>
<table style="width:100%;">
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>tagtogID</code></td>
    <td>This is the default value. tagtog-internal document id or docid (e.g. <code>ai1AzDk4wQzbL.BKzlrA_CrK8gJi-text</code>). Its use implicitly means that the document already exists in the associated project.</td>
  </tr>
  <tr>
    <td><code>PMID</code></td>
    <td><a href="https://en.wikipedia.org/wiki/PubMed#PubMed_identifier">PubMed ID</a>.</td>
  </tr>
  <tr>
    <td><code>PMCID</code></td>
    <td><a href="https://en.wikipedia.org/wiki/PubMed#PubMed_identifier">PubMed Central ID</a>.</td>
  </tr>
  <tr class="soon">
    <td><code>WikipediaID</code></td>
    <td>Wikipedia ID. Cooming soon.</td>
  </tr>
  <tr class="soon">
    <td><code>TweetID</code></td>
    <td><a href="https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object">Tweet ID</a>. e.g: <a href="https://twitter.com/tagtog_net/status/931029434814959616">931029434814959616</a>. Coming soon</td>
  </tr>
</table>
<br/>
</div>
<div class="one-third-col">

</div>

<div class="two-third-col">
  <h2>API Clients</h2>
  <h3>Python tagtog script</h3>
  <p>If you want to use an <strong>already built API client</strong>. You have the {% include inline-image.html name="icon_leafs.png" width="18" %}<a href="https://github.com/tagtog/tagtog-doc/blob/master/tagtog.py" title="tagtog python script"><strong>tagtog python API script</strong></a> to do many common operations in tagtog using the API: upload (also folders), search, and download documents!</p>
  <div markdown="1">
```shell
usage: tagtog [-h] {upload,search,download} ...

tagtog official script to Upload & Search & Download documents. Version: 0.1.2
Author: tagtog (@tagtog_net) - Contact: Juan Miguel Cejuela (@juanmirocks) API
documentation: http://docs.tagtog.net/API_documents_v1.html

positional arguments:
  {upload,search,download}
    upload              Upload files to tagtog
    search              Search documents by query, e.g. `*` (all)
    download            Download documents by search query, e.g.
                        `updated:[NOW-1DAY to NOW]

optional arguments:
  -h, --help            show this help message and exit
```
  </div>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h4>Search</h4>
  <p>It uses the API to search documents in your project. Parameters can be consulted <a href="#search-documents-in-a-project-get">here</a> or using <code>tagtog.py search --help</code>. You can learn how to build search queries <a href="/search-queries.html">here</a></p>
  <p>The example below retrieves all the documents from your project.</p>
  <div markdown="1">
```shell
python3 tagtog.py search '*' -u {{ page.api_username }} -w {{ page.api_pwd }} -p {{ page.api_project }} -o {{ page.api_username }}
```
  </div>
</div>
<div class="one-third-col">
  {% include message.html message="If you use the on-premises version, you can set the domain using the <code>domain</code> parameter." %}
</div>
<div class="two-third-col">
  <h4>Upload</h4>
  <p>It uses the API to upload documents to your project.</p>
  <h5>Upload PMIDs</h5>
  <p>Parameters can be consulted <a href="#pubmed-abstracts-post-get">here</a> or using <code>tagtog.py upload --help</code>.</p>
  <p>The example below upload the abstract from two PMIDs to your project. Remember to indicate which is the <a href="#idtype-parameter">type of id</a> (<code>--idType</code> or <code>-i</code>) for the document.</p>
  <div markdown="1">
```shell
python3 tagtog.py upload 29539636,29531059 -u {{ page.api_username }} -w {{ page.api_pwd }} -p {{ page.api_project }} -o {{ page.api_username }} -i PMID
```
  </div>

  <h5>Upload files</h5>
  <p>Parameters can be consulted using <code>tagtog.py upload --help</code>. You must include the parameter <code>--extension</code> or <code>-e</code> to indicate the extension of the files to upload (e.g. <code>txt</code>, <code>pdf</code>, etc.). These are the  <a href="/ioformats.html#input-formats">input files supported</a></p>
  <p>The example below upload the PDF documents of a folder, to your project.</p>
  <div markdown="1">
```shell
python3 tagtog.py upload ./myfolder -u {{ page.api_username }} -w {{ page.api_pwd }} -p {{ page.api_project }} -o {{ page.api_username }} --extension pdf
```
  </div>

  <p>The example below upload a single file to your project.</p>
  <div markdown="1">
```shell
python3 tagtog.py upload ./myfile.txt -u {{ page.api_username }} -w {{ page.api_pwd }} -p {{ page.api_project }} -o {{ page.api_username }}
```
  </div>
</div>
<div class="one-third-col">

</div>
<div class="two-third-col">
  <h4>Download</h4>
  <p>It uses the API to download documents from your project. In one call to the script you can <strong>download all documents matching a search query</strong>.</p>
  <p>Parameters can be consulted using <code>tagtog.py download --help</code>.</p>
  <p>You can indicate the folder where you can store the downloaded documents using the parameter <code>--output_folder</code> (it defaults to the folder where the script is running).</p>
  <p>Use the parameter <code>--output</code> or <code>-t</code> to indicate the <a href="/ioformats.html#output-formats">output type</a> for the downloaded files.</p>
  <p>You can learn how to build search queries <a href="/search-queries.html">here</a></p>
  <p>The example below download the annotations (<code>ann.json</code>) for all the documents in a project.</p>
   <div markdown="1">
```shell
python3 tagtog.py download '*' -u {{ page.api_username }} -w {{ page.api_pwd }} -p {{ page.api_project }} -o {{ page.api_username }} --output_folder ./myDownloadFolder -t ann.json
```
  </div>
</div>
<div class="one-third-col">
 {% include message.html message='The search query <code>&ast;</code> finds all documents in a project.' %}
</div>
