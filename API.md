---
layout: page
title: API
sidebar_link: true

api_document_url: https://www.tagtog.net/-api/documents/v1
api_username: yourUsername
api_pwd: yourPassword
api_project: yourProjectName
api_plain_text: Antibody-dependent cellular cytotoxicity (ADCC), a key effector function for the clinical effectiveness of monoclonal antibodies, is triggered by the engagement of the antibody Fc domain with the Fcγ receptors expressed by innate immune cells such as natural killer (NK) cells and macrophages.
---
<div class="two-third-col">
  <br/>
  <p>Thanks for choosing the Documents API to build NLP solutions into your app or website. Getting started with a new API can be challenging, so we have created a step-by-step guide that walks you through how to make your first API calls and more.</p>
</div>
<div class="one-third-col">
  <div class="message">
    You will need an <strong>account at tagtog</strong>. Sign up at tagtog.net if you are using the cloud version or check with your admin if you are using an on-premises version.
  </div>
</div>


<div class="two-third-col">
  <table style="width:100%;white-space:nowrap;">
    <tr>
      <td><strong>Version</strong></td>
      <td><code>1.0</code></td>
    </tr>
    <tr>
      <td><strong>Endpoint</strong></td>
      <td>Documents</td>
    </tr>
    <tr>
      <td><strong>URL</strong></td>
      <td><a href="{{ page.api_document_url }}">{{ page.api_document_url }}</a></td>
    </tr>
  </table>
</div>
<div class="one-third-col">
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
  <p><strong>Parameters</strong></p>
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
      <td>Username sending the request</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>ann.json</code></td>
      <td>The format of the output you want to be returned by the API. <a href=".">Output formats</a>.</td>
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
      <td><code>members</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has multiple team members</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>You can choose between the folders <code>pool</code> and <code>test</code>. <a href=".">More information</a></td>
    </tr>
  </table>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  
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
curl -u {{ page.api_username }}: {{ page.api_pwd }} -X POST -d 'text={{ page.api_plain_text }}' '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&output=ann.json'
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



{::comment}
PUBMED IDS
{:/comment}




<div class="two-third-col">
  <h3>PubMed Abstracts <code>POST</code> <code>GET</code></h3>
  <p>Import one or more PubMed abstracts and annotate them.</p>
  <p><strong>Parameters</strong></p>
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
      <td>Type of Id. <a href=".">List of idTypes</a></td>
    </tr>
    <tr>
      <td><code>ids</code></td>
      <td>-</td>
      <td>23596191,29438695</td>
      <td>Comma-separated list of ids, all of the same type. The response is limited to the last id imported. </td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>Username sending the request</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>ann.json</code></td>
      <td>The format of the output you want to be returned by the API. <a href=".">Output formats</a>.</td>
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
      <td><code>members</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has multiple team members</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>You can choose between the folders <code>pool</code> and <code>test</code>. <a href=".">More information</a></td>
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
      <p class="code-desc">The example belows imports a list of PMIDs and retrieves the annotations of the last document in <code>ann.json</code> format.</p>
<div id="tab-1-pmid" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}: {{ page.api_pwd }} -X POST '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&idType=PMID&ids=23596191,29438695&output=ann.json'
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




{::comment}
URLS
{:/comment}




<div class="two-third-col">
  <h3>URL <code>POST</code> <code>GET</code></h3>
  <p>Import the text content of a URL and annotate it.</p>
  <p><strong>Parameters</strong></p>
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
      <td><a href="https://en.wikipedia.org/wiki/Autonomous_cruise_control_system">https://en.wikipedia.org/wiki/Autonomous_cruise_control_system</a></td>
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
      <td>Username sending the request</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>weburl</code></td>
      <td>The format of the output you want to be returned by the API. <a href=".">Output formats</a>.</td>
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
      <td><code>members</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has multiple team members</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>You can choose between the folders <code>pool</code> and <code>test</code>. <a href=".">More information</a></td>
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
    <p class="code-desc">The example below imports an URL and retrieves the web link for the annotated document. That link redirects to the annotated document at the tagtog app.</p>
<div id="tab-1-url" class="tab-content" style="display: block" markdown="1">
```shell
curl -u {{ page.api_username }}: {{ page.api_pwd }} -X POST '{{ page.api_document_url }}?project={{ page.api_project }}&owner={{ page.api_username }}&url=https://en.wikipedia.org/wiki/Autonomous_cruise_control_system&output=weburl'
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
  <p><strong>Parameters</strong></p>
  <table style="width:100%;">
    <tr>
      <th>Name</th>
      <th>Default</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>files</code></td>
      <td><code>-</code></td>
      <td>text.txt, text2.txt</td>
      <td>List of files to annotate</td>
    </tr>
    <tr>
      <td><code>project</code></td>
      <td>-</td>
      <td>{{ page.api_project }}</td>
      <td>Name of the project</td>
    </tr>
    <tr>
      <td><code>owner</code></td>
      <td>Username sending the request</td>
      <td>{{ page.api_username }} (in this example we assume the user is also the owner of the project)</td>
      <td>Owner of the project you want to use</td>
    </tr>
    <tr>
      <td><code>output</code></td>
      <td><code>visualize</code></td>
      <td><code>ann.json</code></td>
      <td>The format of the output you want to be returned by the API. <a href=".">Output formats</a>.</td>
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
      <td><code>members</code></td>
      <td><code>master</code> aka project official annotations</td>
      <td>john</td>
      <td><p>Project member you want to use</p>
          <p>Only applicable if the project has multiple team members</p></td>
    </tr>
    <tr>
      <td><code>folder</code></td>
      <td><code>pool</code></td>
      <td><code>pool</code></td>
      <td>You can choose between the folders <code>pool</code> and <code>test</code>. <a href=".">More information</a></td>
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
files = [('file', open('files/text.txt', 'rb'))]
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