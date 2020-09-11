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
api_plain_text: "\"Hello, World!\""
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
  <p>One of the most common scenarios using tagtog is to import text to tagtog. The text will be automatically annotated if you are using any of the mechanisms to annotate text automatically (dictionaries, tagtog ML or your own ML). The API is the perfect way to automate document imports. To import annotated documents, go to the section: <a href="API_documents_v1.html#import-annotated-documents-post">Import annotated documents</a>.</p>


  <h3>Plain text <code>POST</code></h3>
  <p>Import plain text.</p>
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
      <td></td>
      <td>{{ page.api_plain_text }}</td>
      <td>Plain text</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
      <td><code>master</code></td>
      <td>John</td>
      <td><p>Annotation version, either <code>master</code> (aka ground truth) or a project member's username (see <a href="/collaboration.html">multiple team members</a>).</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td>mySubFolder</td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>format</code></td>
      <td>Depends on the input type. <a href="ioformats.html#input-types">Check the default formats</a>.</td>
      <td><code>formatted</code></td>
      <td>Force the <em>format</em> of the input. <a href="ioformats.html#input-formats">More info</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td>John,Laura</td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>"&ast;"</code> means to select all team members to distribute to; and 3) <code>"-"</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
    <tr>
      <td><code>filename</code></td>
      <td>text.txt</td>
      <td>myPlainTextFile.txt</td>
      <td>Force the document's filename with this argument, otherwise the default is used. Note that the filename must end with the extension <code>.txt</code>. Otherwise, this is appended to your given name.</td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  {% include message.html message='Imported documents are visible in the <a href="/documents.html">document pool</a>'%}
</div>


<div class="two-third-col">
  <h4>Examples: send plain text</h4>
  <p>By default, plain text imported to tagtog uses the <code>verbatim</code> <a href="ioformats.html#input-formats">input format</a>. You should use this default mode when you want to keep the same formatting as your input text.</p>
  <br/>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-plain-text">cURL</a></li>
      <li><a href="#tab-2-plain-text">Python</a></li>
      <li><a href="#tab-3-plain-text">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">The example below imports plain text and retrieves the annotations identified (if any) in <code>ann.json</code> format.</p>
<div id="tab-1-plain-text" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST -d 'text={{ page.api_plain_text }}' '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&output=ann.json'
```
</div>


<div id="tab-2-plain-text" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "ann.json"}
payload = {"text": {{ page.api_plain_text }}}
response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_annotate_plain_text.py" %}</p>
</div>
<div id="tab-3-plain-text" class="tab-content" markdown="1">
```javascript
fetch('{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&output=ann.json', {
    method: 'POST',
    headers: {'Authorization' : "Basic " + btoa('{{ page.api_username }}' + ":" + '{{ page.api_pwd }}'),
              'Accept': 'application/json',
              'Content-Type': 'application/json',
             },
    body: JSON.stringify({"text": {{ page.api_plain_text }}})
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
  <p>Response, output=<code>ann.json</code></p>
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
  <h4>Examples: send plain text and format it</h4>
  <p>Use the <a href="ioformats.html#input-formats">input format</a> <code>formatted</code> to clean and format your input.</p>
  <br/>

  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-plain-text-formatted-python">Python</a></li>
    </ul>
    <div class="tab">
      <p class="code-desc">This example imports plain text in <code>formatted</code> format and returns the result of the operation (output format <code>null</code>).</p>
<div id="tab-plain-text-formatted-python" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
params = {"project": "yourProjectName", "owner": "yourUsername", "format": "formatted", "output": "null"}
payload = {
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
  <p>Response, output=<code>null</code></p>
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
  <p>Import the content of a URL (HTML or other file) and annotate it.</p>
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
      <td></td>
      <td class="break-all"><a href="https://en.wikipedia.org/wiki/Autonomous_cruise_control_system">https://en.wikipedia.org/wiki/Autonomous_cruise_control_system</a></td>
      <td>URL to annotate</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
      <td><code>master</code></td>
      <td>John</td>
      <td><p>Annotation version, either <code>master</code> (aka ground truth) or a project member's username (see <a href="/collaboration.html">multiple team members</a>).</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td>mySubFolder</td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td>John,Laura</td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>"&ast;"</code> means to select all team members to distribute to; and 3) <code>"-"</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
    <tr>
      <td><code>filename</code></td>
      <td>The original file name</td>
      <td>Autonomous_cruise_control_system.html</td>
      <td>Force the document's filename with this argument, otherwise the default is used. Note that the filename must end with the original extension. Otherwise, this is appended to your given name.</td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  {% include message.html message="<strong>Problems with URL encoding?</strong> encode URLs online <a href='https://meyerweb.com/eric/tools/dencoder/' title='MeyerWeb - URL Decoder/Encoder'>here</a>" %}
</div>
<div class="two-third-col">
  <h4>Examples: import a web page</h4>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-url">cURL</a></li>
      <li><a href="#tab-2-url">Python</a></li>
      <li><a href="#tab-3-url">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">The example below imports a URL and as the output, it retrieves the web link for the annotated document. That link redirects to the annotated document at the tagtog web app. You can use other <a href="ioformats.html#output-formats">output formats</a>.</p>
<div id="tab-1-url" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&url=https://en.wikipedia.org/wiki/Autonomous_cruise_control_system&output=weburl'
```
</div>
<div id="tab-2-url" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "weburl", 'url':'https://en.wikipedia.org/wiki/Autonomous_cruise_control_system'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_annotate_url.py" %}</p>
</div>
<div id="tab-3-url" class="tab-content" markdown="1">
```javascript
fetch('https://www.tagtog.net/-api/documents/v1?owner={{ page.api_username }}&project={{ page.api_project }}&url=https://en.wikipedia.org/wiki/Autonomous_cruise_control_system&output=weburl', {
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


<div class="two-third-col">
  <h4>Examples: import a file by URL</h4>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-url-file">Python</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">The example below imports a file given by a URL. The content will be represented by the default format associated to the filetype, in this case <code>markdown</code>. You can import other type of files as PDF or txt.</p>
<div id="tab-1-url-file" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "null", 'url':'https://raw.githubusercontent.com/oxford-cs-deepnlp-2017/lectures/master/README.md'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "README.md",
    "filenames": ["README.md"],
    "names": ["README.md"],
    "rawInputSizeInBytes": 19680,
    "docid": "aZkhd3qmP2BRoXhTOhUMjuxrz31i-README.md",
    "tagtogID": "aZkhd3qmP2BRoXhTOhUMjuxrz31i-README.md",
    "result": "created",
    "parsedTextSizeInBytes": 19566
  }],
  "warnings": []
}
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
      <td></td>
      <td>text.txt, text2.txt</td>
      <td>List of files to annotate. <a href="/ioformats.html#files">Supported file types</a></td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
      <td><code>master</code></td>
      <td>John</td>
      <td><p>Annotation version, either <code>master</code> (aka ground truth) or a project member's username (see <a href="/collaboration.html">multiple team members</a>).</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td>myFolder</td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>format</code></td>
      <td></td>
      <td><code>verbatim</code></td>
      <td>Force how the <em>format</em> of the inputted text should be interpreted; <a href="ioformats.html#input-formats">more info.</a></td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td>John,Laura</td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>"&ast;"</code> means to select all team members to distribute to; and 3) <code>"-"</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
    <tr>
      <td><code>filename</code></td>
      <td>The original file name</td>
      <td>MyNewDoc.pdf</td>
      <td>Force the document's filename with this argument, otherwise the default is used. Note that the filename must end with the original extension. Otherwise, this is appended to your given name.</td>
    </tr>
  </table>

</div>
<div class="one-third-col">

</div>


<div class="two-third-col">

  <h4>Examples: import a plain text file</h4>

  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-2-file">Python</a></li>
      <li><a href="#tab-3-file">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example imports a file and retrieves the annotations in <code>ann.json</code>.</p>
<div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "ann.json"}
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

fetch('{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&output=ann.json', {
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
  <p>Response, output=<code>ann.json</code></p>
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


<div class="two-third-col">

  <h4>Examples: import a PDF file</h4>

  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-file-pdf">cURL</a></li>
      <li><a href="#tab-2-file-pdf">Python</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example imports a PDF file and retrieves the annotations in <code>ann.json</code>. Please notice we open the PDF file in binary format. You can extend it easily to upload multiple files.</p>

<div id="tab-1-file-pdf" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST -F 'files=@/files/document.pdf' '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&output=ann.json'
```
</div>

<div id="tab-2-file-pdf" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "ann.json"}
#you can append more files to the list in case you want to upload multiple files
files = [('file', open('files/document.pdf', 'rb'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_import_pdf.py" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response, output=<code>ann.json</code></p>
  <div class="message">
    In PDF each page is identified with a part id (e.g. s1v1 is for page 1, s2v1 is for page 2, etc.). In this response, there were no automatic annotations.
  </div>
<div markdown="1">
```json
{
  "annotatable": {
    "parts": ["s1v1", "s2v1", "s3v1", "s4v1", "s5v1", "s6v1", "s7v1", "s8v1", "s9v1", "s10v1", "s11v1", "s12v1", "s13v1", "s14v1"]
  },
  "anncomplete": false,
  "sources": [],
  "metas": {},
  "entities": [],
  "relations": []
}
```
</div>
</div>


<div class="two-third-col">

  <h4>Examples: import a markdown file</h4>

  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-file-md">cURL</a></li>
      <li><a href="#tab-2-file-md">Python</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example imports a markdown file. You can also import a txt file and force the format to <code>markdown</code>.</p>
    <p class="code-desc">Using Markdown you can also use <a href="tagtog-blocks">tagtog blocks</a> to build a customized annotation layout for your project! E.g. question answering datasets, chatbot training, tweets, etc.</p>

<div id="tab-1-file-md" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST -F "files=@/files/readme.md" '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&output=ann.json'
```
</div>


<div id="tab-2-file-md" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "null"}
files = [('file', open('files/readme.md'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
```
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "README.md",
    "filenames": ["README.md"],
    "names": ["README.md"],
    "rawInputSizeInBytes": 19680,
    "docid": "aZkhd3qmP2BRoXhTOhUMjuxrz31i-README.md",
    "tagtogID": "aZkhd3qmP2BRoXhTOhUMjuxrz31i-README.md",
    "result": "created",
    "parsedTextSizeInBytes": 19566
  }],
  "warnings": []
}
```
</div>
</div>



<div class="two-third-col">

  <h4>Examples: import a list of files</h4>

  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-filelist">cURL</a></li>
      <li><a href="#tab-2-filelist">Python</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example imports a list of plain text files (it can be any other supported file type or a combination) and retrieves the result of the operation.</p>

<div id="tab-1-filelist" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST -F "files=@/files/item1.txt" -F "files=@/files/item2.txt" -F "files=@/files/item3.txt" '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&output=ann.json'
```
</div>

<div id="tab-2-filelist" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "null"}
files = [('file', open('files/item1.txt')), ('file', open('files/item2.txt')), ('file', open('files/item3.txt'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
```
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 3,
  "errors": 0,
  "items": [{
    "origid": "item1.txt",
    "filenames": ["item1.txt"],
    "names": ["item1.txt"],
    "rawInputSizeInBytes": 128,
    "docid": "aGMgsSYn0VJlSHWgGD4zwsIvOqDG-item1.txt",
    "tagtogID": "aGMgsSYn0VJlSHWgGD4zwsIvOqDG-item1.txt",
    "result": "created",
    "parsedTextSizeInBytes": 128
  }, {
    "origid": "item2.txt",
    "filenames": ["item2.txt"],
    "names": ["item2.txt"],
    "rawInputSizeInBytes": 53,
    "docid": "aNkqrGOQX49FemNFJhx5GgPc9UAS-item2.txt",
    "tagtogID": "aNkqrGOQX49FemNFJhx5GgPc9UAS-item2.txt",
    "result": "created",
    "parsedTextSizeInBytes": 53
  }, {
    "origid": "item3.txt",
    "filenames": ["item3.txt"],
    "names": ["item3.txt"],
    "rawInputSizeInBytes": 41,
    "docid": "azUkkxgJ7taVY7mzM71ciFKwp27i-item3.txt",
    "tagtogID": "azUkkxgJ7taVY7mzM71ciFKwp27i-item3.txt",
    "result": "created",
    "parsedTextSizeInBytes": 39
  }],
  "warnings": []
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
      <td></td>
      <td>23596191, 29438695</td>
      <td>Comma-separated list of ids, all the same type. The response is limited to the last id imported. </td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
      <td><code>master</code></td>
      <td>John</td>
      <td><p>Annotation version, either <code>master</code> (aka ground truth) or a project member's username (see <a href="/collaboration.html">multiple team members</a>).</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td>myFolder</td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td>John,Laura</td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>"&ast;"</code> means to select all team members to distribute to; and 3) <code>"-"</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
    <tr>
      <td><code>filename</code></td>
      <td>The original file name</td>
      <td>myPaper.xml</td>
      <td>Force the document's filename with this argument, otherwise the default is used. Note that the filename must end with the original extension. Otherwise, this is appended to your given name.</td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  <div class="message">
    You can also import <a href="https://www.ncbi.nlm.nih.gov/pmc/">PubMed Central</a> (PMC) articles by using the PMCIDs. The idType is <code>PMCID</code>
  </div>
</div>
<div class="two-third-col">
  <h4>Examples: import a a list of PubMed articles by PMID</h4>
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
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X POST '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&idType=PMID&ids=23596191,29438695&output=ann.json'
```
</div>
<div id="tab-2-pmid" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", 'idType':'PMID', 'ids':['23596191','29438695'], "output": "ann.json"}
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
  <p>Response, output=<code>ann.json</code></p>
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
  <p class="list-item"><span class="list-item-1"></span><strong>The text or document</strong>. This can be a regular file (e.g. txt, xml, pdf, <a title="tagtog - plain.html format" href="/anndoc.html#plain-html">plain.html</a>, etc.), plain text, etc. Check the supported <a title="tagtog - input types" href="ioformats.html#input-types">input types</a></p>
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
      <td></td>
      <td>text.txt, text.ann.json</td>
      <td>You need to upload in the same request both: the text (supported input format) and the ann.json (annotations) files.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
      <td>No default for pre-annotated documents, you should always set this parameter</td>
      <td><code>default-plus-annjson</code></td>
      <td>Format of the pre-annotated document. List of supported pre-annotated formats: <a title="tagtog - formats" href="ioformats.html#input-formats">Pre-annotated formats</a></td>
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
      <td><code>master</code></td>
      <td>John</td>
      <td><p>Annotation version, either <code>master</code> (aka ground truth) or a project member's username (see <a href="/collaboration.html">multiple team members</a>).</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td>myFolder</td>
      <td>Folder to store the document to. <a href="/documents.html">More information</a>. You can <a href="search-queries.html#search-by-folder">refer to a folder by index, full path, or simple name</a>.</td>
    </tr>
    <tr>
      <td><code>distributeToMembers</code></td>
      <td><code>-</code></td>
      <td>John,Laura</td>
      <td>
        <p>Parameter that overrides the default <a href="projects.html#task-distribution">project task distribution settings</a>.</p>
        <p>The format is a comma-separated list of the project user members to distribute to, and only those. Moreover, three special values exist: 1) <code>""</code> (the empty string) means to perform no task distribution whatsoever; 2) <code>"&ast;"</code> means to select all team members to distribute to; and 3) <code>"-"</code> means using the project default settings (same as actually not writing this parameter).</p>
        <p>This parameter is useful to fine-control which documents should be distributed to which members, depending on some criteria. For example, you could distribute documents to different members depending on the upload folder.</p>
      </td>
    </tr>
    <tr>
      <td><code>filename</code></td>
      <td>Name of the file imported</td>
      <td>myPlainTextFile.txt</td>
      <td>Force the document's filename with this argument, otherwise the default is used. Note that the filename must end with the original file extension. Otherwise, this is appended to your given name.</td>
    </tr>
  </table>

</div>

<div class="one-third-col">
  {% include message.html message='You can send multiple annotated documents at the same time. This means you always upload an even number of files.' %}
</div>



<div class="two-third-col">
  <h4>Examples: import pre-annotated plain text file</h4>

  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-file">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to upload a preannotated document (txt file + ann.json) to tagtog. The format used is <code>default-plus-annjson</code> to indicate we are importing pre-annotated content, the text content will be represented using the <a href="ioformats.html#input-types">default format</a>. In this case, the default format for plain text is <code>verbatim</code>. Make sure the ann.json is well formated according to the <a href="anndoc.html#ann-json">ann.json specification</a>.</p>
  <div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
  ```python

  import requests

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"
  auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
  params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "null", 'format': 'default-plus-annjson'}

  files=[('file', open('files/text.txt')), ('file', open('files/text.ann.json'))]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  ```
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
  <div class="message">
    Notice the result property is <code>created</code>, indicating that this is a new file in your project
  </div>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "text.txt",
    "filenames": ["text.txt", "text.ann.json"],
    "names": ["text.txt", "text.ann.json"],
    "rawInputSizeInBytes": 1048102,
    "docid": "aqXHSykmx2gmA9AJXW38OAl0DnTe-text.txt",
    "tagtogID": "aqXHSykmx2gmA9AJXW38OAl0DnTe-text.txt",
    "result": "created",
    "parsedTextSizeInBytes": 81360
  }],
  "warnings": []
}
```
</div>
</div>


<div class="two-third-col">
  <h4>Examples: import pre-annotated raw plain text</h4>

  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-file">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to upload a preannotated document (plain text + ann.json) to tagtog. The format used is <code>default-plus-annjson</code> to indicate we are importing pre-annotated content, the text content will be represented using the <a href="ioformats.html#input-types">default format</a>. In this case, the default format for plain text is <code>verbatim</code>. Make sure the ann.json is well formated according to the <a href="anndoc.html#ann-json">ann.json specification</a>. In this example, we put directly in the code the plain text and the ann.json. It might be useful if you don't want to store this content on physical files.</p>
  <div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
  ```python

  import requests

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"
  auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
  params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "null", 'format': 'default-plus-annjson'}
  #you could easily point to an existing ann.json file or text file. e.g.: ('file', open('files/text.ann.json'))
  files=[('hellotag.txt', 'Hello tag world'), ('hellotag.ann.json', '{"annotatable": {"parts": ["s1v1"]},"anncomplete": false,"sources": [],"metas": {},"entities": [{"classId": "e_1","part": "s1v1","offsets": [{"start": 6,"text": "tag"}],"confidence": {"state": "pre-added","who": ["user:{{ page.api_username }}"],"prob": 1},"fields": {},"normalizations": {}}],"relations": []}')]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  ```
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "hellotag.txt",
    "filenames": ["hellotag.ann.json", "hellotag.txt"],
    "names": ["hellotag.ann.json", "hellotag.txt"],
    "rawInputSizeInBytes": 307,
    "docid": "awq0S.5DQRW3Cjpv4u1tJyXl.L3m-hellotag.txt",
    "tagtogID": "awq0S.5DQRW3Cjpv4u1tJyXl.L3m-hellotag.txt",
    "result": "created",
    "parsedTextSizeInBytes": 15
  }],
  "warnings": []
}
```
</div>
</div>



<div class="two-third-col">
  <h4>Examples: import pre-annotated formatted text</h4>
  <p>Follow this sample only if you want to import pre-annotated documents to tagtog when the input text was <code>formatted</code> when annotated.</p>
  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-preannotated-verbatim-python">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to send text to be <code>formatted</code> along with its annotations. The format used is <code>formatted-plus-annjson</code>. The input files are in Github, you can find a link below.</p>
  <div id="tab-preannotated-verbatim-python" class="tab-content" style="display: block" markdown="1">
  ```python
  import requests
  import sys

  content_path = "files/formatted.txt"
  annjson_path = "files/formatted.ann.json"

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

  auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
  params = {"project": "yourProjectName", "owner": "yourUsername", "format": "formatted-plus-annjson", "output": "null"}

  files=[('file', open(content_path)), ('file', open(annjson_path))]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  print(response.text)
  ```
  <p style="float:right">Files{% include github-link.html target="snippets/files" %}</p>
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "formattedtext",
    "filenames": ["formatted.ann.json", "formatted.txt"],
    "names": ["formatted.ann.json", "formatted.txt"],
    "rawInputSizeInBytes": 860,
    "docid": "aAyUEVY5RCLzd8kdaOMg54fXXWj8-formatted",
    "tagtogID": "aAyUEVY5RCLzd8kdaOMg54fXXWj8-formatted",
    "result": "created",
    "parsedTextSizeInBytes": 126
  }],
  "warnings": []
}
```
</div>
</div>

<div class="two-third-col">
  <h4>Examples: import pre-annotated PDF</h4>
  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-preannotated-verbatim-python">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to import a PDF along with its annotations. The format used is <code>default-plus-annjson</code> as we want the PDF to use the default format and import annotations for this file. The input files are in Github, you can find a link below.</p>
  <div id="tab-preannotated-verbatim-python" class="tab-content" style="display: block" markdown="1">
  ```python
  import requests
  import sys

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

  auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
  params = {"project": "yourProjectName", "owner": "yourUsername", "format": "default-plus-annjson", "output": "null"}

  files=[('file', open('files/article.pdf', 'rb')), ('file', open('files/article.ann.json'))]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  print(response.text)
  ```
  <p style="float:right">Files{% include github-link.html target="snippets/files" %}</p>
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "article.pdf",
    "filenames": ["article.ann.json", "article.pdf"],
    "names": ["article.ann.json", "article.pdf"],
    "rawInputSizeInBytes": 1048119,
    "docid": "aqXHSykmx2gmA9AJXW38OAl0DnTe-article.pdf",
    "tagtogID": "aqXHSykmx2gmA9AJXW38OAl0DnTe-article.pdf",
    "result": "created",
    "parsedTextSizeInBytes": 83199
  }],
  "warnings": []
}
```
</div>
</div>

<div class="two-third-col">
  <h4>Examples: import a list of pre-annotated files</h4>
  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-preannotated-verbatim-python">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to import a list of pre-annotated files. The format used is <code>default-plus-annjson</code> as we want each file to use the default format and to be pre-annotated by an annotation file.</p>
  <p class="code-desc">The expected input are pair of content+ann.json files.</p>
  <div id="tab-preannotated-verbatim-python" class="tab-content" style="display: block" markdown="1">
  ```python
  import requests
  import sys

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

  auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
  params = {"project": "yourProjectName", "owner": "yourUsername", "format": "default-plus-annjson", "output": "null"}

  files=[('file', open('article.pdf', 'rb')), ('file', open('article.ann.json')), ('file', open('item1.txt')), ('file', open('item1.ann.json'))]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  print(response.text)
  ```
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 2,
  "errors": 0,
  "items": [{
    "origid": "article.pdf",
    "filenames": ["article.ann.json", "article.pdf"],
    "names": ["article.ann.json", "article.pdf"],
    "rawInputSizeInBytes": 1048119,
    "docid": "aqXHSykmx2gmA9AJXW38OAl0DnTe-article.pdf",
    "tagtogID": "aqXHSykmx2gmA9AJXW38OAl0DnTe-article.pdf",
    "result": "created",
    "parsedTextSizeInBytes": 83199
  }, {
    "origid": "item1.txt",
    "filenames": ["item1.ann.json", "item1.txt"],
    "names": ["item1.ann.json", "item1.txt"],
    "rawInputSizeInBytes": 461,
    "docid": "aGMgsSYn0VJlSHWgGD4zwsIvOqDG-item1.txt",
    "tagtogID": "aGMgsSYn0VJlSHWgGD4zwsIvOqDG-item1.txt",
    "result": "updated",
    "parsedTextSizeInBytes": 128
  }],
  "warnings": []
}
```
</div>
</div>



<div class="two-third-col">
  <h3>Replace annotations of existing document <code>POST</code></h3>
  <p>You should use two files:</p>
  <p class="list-item"><span class="list-item-1"></span><strong>The original content file or the <a title="tagtog - plain.html format" href="/anndoc.html#plain-html">plain.html</a></strong>.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>The annotations</strong>. You pass this as an <code><a title="tagtog - ann.json format" href="/anndoc.html#ann-json">ann.json</a></code>.</p>
  <p>If you use the original content file, it must have the same name as the original. If you want to use the plain.html, it should use the same name as the original plain.html.</p>
  <p><strong>Both files (content and annotations) should have the same name, except for the file extensions</strong>. For example: <code>mydoc.txt</code> and <code>mydoc.ann.json</code>. Or, if with a plain.html: mydoc-3243hdsfk3.plain.html and mydoc-3243hdsfk3.ann.json</p>
  <p>If the original content doesn't exist in your project, the pre-annotated document will be also imported as new.</p>

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
      <td></td>
      <td>mydoc.txt, mydoc.ann.json</td>
      <td>You need to upload in the same request both: the content file and the ann.json (annotations) files.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
      <td>Format of the pre-annotated document. List of supported pre-annotated formats: <a title="tagtog - Annotation input types" href="ioformats.html#input-formats">Pre-annotated formats</a> </td>
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
      <td><code>master</code></td>
      <td>John</td>
      <td><p>Annotation version, either <code>master</code> (aka ground truth) or a project member's username (see <a href="/collaboration.html">multiple team members</a>).</p></td>
    </tr>
  </table>

</div>

<div class="one-third-col">
  {% include message.html message='You can send multiple annotated documents at the same time. This means you always upload an even number of files.' %}
</div>



<div class="two-third-col">

  <h4>Examples: replace the annotations of an existing document using the original content</h4>
  <p>As you can see, this example is basically the same as the example to upload pre-annotated plain text. The only difference is that the original file should already exist in your project.</p>
</div>

<div class="two-third-col">

  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-file">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to replace the annotations of an existing document (content + ann.json) to tagtog. If the original file doesn't exist in your project, it will be created.</p>
  <div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
  ```python
  import requests

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

  auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
  params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "null", 'format': 'default-plus-annjson'}

  files = [('file', open('/annotated-docs/mydoc.txt')), ('file', open('/annotated-docs/mydoc.ann.json'))]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  ```
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
  <div class="message">
    Notice the result property is <code>updated</code>, indicating that the file has been updated with new annotations
  </div>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "mydoc.txt",
    "filenames": ["mydoc.ann.json", "mydoc.txt"],
    "names": ["mydoc.ann.json", "mydoc.txt"],
    "rawInputSizeInBytes": 1048119,
    "docid": "aqXHSykmx2gmA9AJXW38OAl0DnTe-mydoc.txt",
    "tagtogID": "aqXHSykmx2gmA9AJXW38OAl0DnTe-mydoc.txt",
    "result": "updated",
    "parsedTextSizeInBytes": 83199
  }],
  "warnings": []
}
```
</div>
</div>


<div class="two-third-col">
  <h4>Examples: replace the annotations of an existing document using plain.html</h4>
  <p>If it is more convenient, you can use the <code>plain.html</code> version of the original file (plain text representation of the file) to replace the annotations on the original file.</p>
</div>

<div class="two-third-col">

  <div id="tabs-container">
  <ul class="tabs-menu">
    <li class="current"><a href="#tab-1-file">Python</a></li>
  </ul>
  <div class="tab">
  <p class="code-desc">This example shows how to replace the annotations of an existing document (plain.html + ann.json) to tagtog. Please notice that the original file should already exist in your project. tagtog will automatically identify the original file and replace its annotations.</p>
  <div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
  ```python
  import requests

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

  auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
  params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "output": "null", 'format': 'anndoc'}

  files=[('file', open('files/article.html')), ('file', open('files/article.ann.json'))]

  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
  ```
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <p>Response, output=<code>null</code></p>
<div markdown="1">
```json
{
  "ok": 1,
  "errors": 0,
  "items": [{
    "origid": "article.pdf",
    "filenames": ["article2.ann.json", "article2.html"],
    "names": ["article2.ann.json", "article2.html"],
    "rawInputSizeInBytes": 86729,
    "docid": "aqXHSykmx2gmA9AJXW38OAl0DnTe-article.pdf",
    "tagtogID": "aqXHSykmx2gmA9AJXW38OAl0DnTe-article.pdf",
    "result": "updated",
    "parsedTextSizeInBytes": 83199
  }],
  "warnings": []
}
```
</div>
</div>





<div class="two-third-col">
  <h2>Search documents in a project <code>GET</code></h2>
  <p>You can <a href="/search.html">search</a> using the documents API. Search across your project and retrieves the matching documents. You can use it to augment your own search engine or simply create a new one. It is also very simple to use the search API to display statistics.</p>
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
      <td></td>
      <td>entity:GGP:P02649 or folder:pool</td>
      <td><strong>Search query</strong>. Learn how to build queries <a href="/search-queries.html">here</a>.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
  <h4>Search response format</h4>
  <p>Response format for search queries.</p>
<div markdown="1">
```javascript
{
  "version": "String: this format's version, e.g. 0.5.0",
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
      "filename": "String: filename of originally uploaded file",
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
<h4>Examples: search using search queries</h4>

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
curl -u {{ page.api_username }}:{{ page.api_pwd }} '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&search=entity:GGP:P02649'
```
</div>
<div id="tab-2-search" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", "search": "entity:GGP:P02649"}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_search.py" %}</p>
</div>
<div id="tab-3-search" class="tab-content" markdown="1">
```javascript
fetch('{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&search=entity:GGP:P02649', {
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
  "version": "0.5.0",
  "search": "entity:GGP:P02649",
  "totalFound": 1,
  "pages": {"current": 0, "previous": -1, "next": -1},
  "docs":
    [
      {
        "id": "aMHKzF_lIoNrdh9pAx298njgIezy-text",
        "filename": "text.txt",
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
  <h2>Get existing documents <code>GET</code></h2>
  <p>You can use the API to export documents. You need the id of the document to get it. If you don't have this id, you can find it using the <a href="#search-documents-in-a-project-get">search</a> feature. You can export only 1 document within each request.</p>
  <p>Specify the <code>output</code> parameter to define the <a href="ioformats.html#output-formats">output format</a> (e.g. <code>ann.json</code>, <code>html</code>)</p>
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
      <td></td>
      <td class="break-all">aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text</td>
      <td>The id of the document you want to download. Note, the parameter is called "ids" for historical reasons. In the future, we might also allow to download multiple files at once.</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
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
      <td><code>master</code></td>
      <td>John</td>
      <td><p>Annotation version, either <code>master</code> (aka ground truth) or a project member's username (see <a href="/collaboration.html">multiple team members</a>).</p></td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  {% include message.html message="If while manual annotating you create <strong>pre-annotations</strong>, they will also appear in the output" %}
  {% include message.html message="<span markdown='1'>**Note**: if you select as `output` an [annotation format](ioformats.html#output-formats) (e.g. `ann.json`), you will always get an annotation output for a `member`. This works as follows: a) if the specified `member` did annotate the document, its annotations are returned normally. b) If, however, the specified `member` did not annotate the document, by default the `master` annotations are returned. c) Otherwise, if the `master` version was not annotated either, default empty annotations are returned (which of course follow the format of the specified `output`). In case b), i.e. when the master annotations are returned as default for an user, this is properly indicated in the request response with an [HTTP Warning Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Warning).</span>" %}

</div>

<div class="two-third-col">
  <h4>Examples: get the annotations of a document by document id</h4>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-getdoc">cURL</a></li>
      <li><a href="#tab-2-getdoc">Python</a></li>
      <li><a href="#tab-3-getdoc">JavaScript</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example retrieves the annotations of a document in <code>ann.json</code> format. As the <code>member</code> parameter is not defined, the <code>master</code> version of the annotations is served. Notice that we don't use the parameter <code>idType</code> because it defaults to <code>tagtogID</code>, the type of the id used.</p>
<div id="tab-1-getdoc" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}:{{ page.api_pwd }} '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&ids=aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text&output=ann.json'
```
</div>
<div id="tab-2-getdoc" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", 'ids':'aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text', "output": "ann.json"}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_getdoc.py" %}</p>
</div>
<div id="tab-3-getdoc" class="tab-content" markdown="1">
```javascript
fetch('{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&ids=aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text&output=ann.json', {
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
  <p>Response, output=<code>ann.json</code></p>
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
  <h4>Examples: get the member's annotations of a document by document id</h4>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-getdoc-member">Python</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example retrieves the annotations of tagtog document in <code>ann.json</code> format. A document can have different annotation versions, in this case we want the version of the annotations from the member <code>John</code></p>
<div id="tab-1-getdoc" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", 'ids':'aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text', 'member': 'John', "output": "ann.json"}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
</div>
      </div>
    </div>
  </div>



<div class="two-third-col">
  <h4>Examples: get the original document by document id</h4>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-getdoc-orig">Python</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example download the original document (format <code>orig</code>) given a document id. Notice that we don't use the parameter <code>idType</code> because it defaults to <code>tagtogID</code>, the type of the id used.</p>
<div id="tab-1-getdoc-orig" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", 'ids':'aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text', 'output':'orig'}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
if response.status_code == 200:
    with open('mydoc.pdf', 'wb') as f:
        f.write(responseGet.content)
```
</div>
      </div>
    </div>
  </div>

<div class="two-third-col">
  <h4>Examples: get the html version of a document by document id</h4>
  <br/>
  <div id="tabs-container">
    <ul class="tabs-menu">
      <li class="current"><a href="#tab-1-getdoc-html">Python</a></li>
    </ul>
    <div class="tab">
    <p class="code-desc">This example download the HTML version of a document (format <code>html</code>) given a document id. The HTML follows the <a href="anndoc.html#plain-html">plain.html specification</a>, which is the text representation of the original document, used to calculate the offsets of the annotations.</p>
<div id="tab-1-getdoc-html" class="tab-content" style="display: block" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"
docId = "aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", 'ids':docId, "output": "html"}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
if response.status_code == 200:
    with open(docId + '.html', 'wb') as f:
        f.write(responseGet.content)
```
</div>
      </div>
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
      <td></td>
      <td>entity:GGP</td>
      <td>Search query to list the documents to remove. Learn how to build queries <a href="/search-queries.html">here</a></td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td></td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td></td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
  </table>
</div>
<div class="one-third-col">
  {% include message.html message='<code>search=&ast;</code> finds all and therefore the <code>DELETE</code> call deletes all documents.' %}
</div>

<div class="two-third-col">
  <h4>Examples: delete documents using a search query</h4>
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
curl -u {{ page.api_username }}:{{ page.api_pwd }} -X DELETE '{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&search=entity:gene'
```
</div>
<div id="tab-2-del" class="tab-content" markdown="1">
```python
import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username="{{ page.api_username }}", password="{{ page.api_pwd }}")
params = {"owner": "{{ page.api_username }}", "project": "{{ page.api_project }}", 'search':'entity:gene'}
response = requests.delete(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
```
<p style="float:right">{% include github-link.html target="snippets/api_python_delete.py" %}</p>
</div>
<div id="tab-3-del" class="tab-content" markdown="1">
```javascript
fetch('{{ page.api_document_url }}?owner={{ page.api_username }}&project={{ page.api_project }}&search=entity:gene', {
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
        <td></td>
        <td><code>tagtogID</code> (mandatory)</td>
        <td></td>
      </tr>
      <tr>
        <td><code>ids</code></td>
        <td></td>
        <td>aEVD52vVm.s2zdTmzK_ACNqH7Z1u-text</td>
        <td></td>
      </tr>
      <tr>
        <td><code>project</code></td>
        <td></td>
        <td>{{ page.api_project }}</td>
        <td>Name of the project</td>
      </tr>
      <tr>
        <td><code>owner</code></td>
        <td></td>
        <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
        <td>Owner of the project you want to use</td>
      </tr>
    </table>
  </div>

  <div>
    <br/>
    <h4>Examples: delete a document by document id</h4>
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
<p><a href="ioformats.html#output-formats">Output formats supported by the API</a></p>


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
documentation: https://docs.tagtog.net/API_documents_v1.html

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
  <p>Parameters can be consulted using <code>tagtog.py upload --help</code>. You must include the parameter <code>--extension</code> or <code>-e</code> to indicate the extension of the files to upload (e.g. <code>txt</code>, <code>pdf</code>, etc.). These are the  <a href="/ioformats.html#input-types">input files supported</a></p>
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
