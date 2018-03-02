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
  <p>Annotates plain text.</p>
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
fetch('{{ page.api_document_url }}?project=myProject&owner={{ page.api_username }}&output=ann.json', {
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
  <p>Response</p>
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
      <li class="current"><a href="#tab-1-pmid">cURL</a></li>
      <li><a href="#tab-2-pmid">Python</a></li>
      <li><a href="#tab-3-pmid">JavaScript</a></li>
    </ul>
    <div class="tab">
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
    headers: {'Authorization' : "Basic " + btoa('yourUsername' + ":" + 'yourPassword'), 
              'Accept': 'application/json', 
              'Content-Type': 'application/json',
            },
  }).then(response => response.json()).then(json => {
    console.log(json);
  }).catch(function(error) {
    console.log('Error: ', error);
  });
}
```
<p style="float:right">{% include github-link.html target="snippets/api_js_annotate_pmids.html" %}</p>
</div>
      </div>
    </div>
  </div>
<div class="one-third-col">
  <p>Response</p>
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