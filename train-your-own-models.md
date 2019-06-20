---
layout: page
title: Train your own models
sidebar_link: true
id: train-your-own-models

api_document_url: https://www.tagtog.net/-api/documents/v1
api_username: yourUsername
api_pwd: yourPassword
api_project: yourProjectName

notoc: true
---

<div class="two-third-col">
  <br>
  <p>You can combine the tagtog interface along with the API to <strong>train your own models</strong> in an <strong>Active Learning (AL)</strong> fashion. The workflow is simple:</p>

  <p class="numbered-item"><span class="number-1">1</span><strong>Train a seed version</strong> of your in-house model (e.g. using <a href="http://scikit-learn.org/stable/">scikit-learn</a>). Have this model annotate new documents and upload them to tagtog through the <a href="/API_documents_v1.html">API</a>.</p>

  <p class="numbered-item"><span class="number-2">2</span>Review <a href="collaboration.html">within your team</a> the newly annotated & uploaded documents using the tagtog interface. The human reviewers, typically subject-matter experts (SMEs) (i.e. domain experts), will go through the predicted annotations, and <strong>accept, reject, or change the annotations</strong> as they see fit. Likely, you will want your team to review documents selected in an AL fashion.</p>  

  <p class="numbered-item"><span class="number-3">3</span>Download the reviewed documents again using the <a href="/API_documents_v1.html">API</a>, and use them to <strong>re-train</strong> your model.</p>
</div>


<div class="two-third-col">
  <br>
  <p>Eventually, you can repeat this same workflow multiple times to <a href="machine-learning.html#continuous-learning"><strong>continuously re-train your models</strong></a>.</p>

  {% include image.html name="diagram_ml_small.svg" caption="Training flow." %}
</div>


<div class="two-third-col">
  <h2>How to upload annotated documents?</h2>

  <p>Use the <a href="anndoc.html">anndoc format</a> to upload both a document's content and its annotations. To do this, a common workflow is the following:</p>

  <!-- -->

  <p class="numbered-item"><span class="number-1">1</span>Upload your document/s using <a href="ioformats.html">any supported format</a>.</p>

  <p class="numbered-item"><span class="number-2">2</span><a href="API_documents_v1.html#output-parameter">Download</a> back the document/s' content in <a href="anndoc.html#plain-html">plain.html</a> format. Have your model read the html's text content and generate the annotations in <a href="anndoc.html#ann-json">ann.json</a>.</p>

  <p class="numbered-item"><span class="number-3">3</span><a href="API_documents_v1.html#files-post">Upload to tagtog in a same API request</a> both the plain.html + ann.json (i.e., 2 files) of the document. The requirement is that both files, except for the final extension, must have the same name. In that way, the tagtog system understands that both files represent the same document. Moreover, you can  send multiple annotated documents at the same time. This means you always upload an even number of files.</p>
</div>

<div class="two-third-col">
    <br/>
    <div id="tabs-container">
      <ul class="tabs-menu">
        <li class="current"><a href="#tab-1-file">Python</a></li>        
      </ul>
      <div class="tab">
      <p class="code-desc">This example shows how to upload a document, download it back in plain.html format, annotate it with your model generating an ann.json, and upload the whole annotated document (plain.html + ann.json) to tagtog.</p>
  <div id="tab-2-file" class="tab-content" style="display: block" markdown="1">
  ```python
  import requests

  tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

  auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
  params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'output':'html'}
  files = [('file', open('text.txt', 'rb'))]
  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)

  # The plain.html (the request's response is in string form). You will have to parse the html's text
  plain_html = response.text
  # Annotate the html with my model. We suppose we generate a json in string format too. We could write down to a file if desired
  ann_json = my_model_annotate(plain_html)
  # ann_json = '{"annotatable":{"parts":["s1p1","s1p2"]},"anncomplete":false,"sources":[],"metas":{},"entities":[{"classId":"e_1","part":"s1p1","offsets":[{"start":12,"text":"first sentence of the first paragrap"}],"confidence":{"state":"pre-added","who":["user:{{ page.api_username }}"],"prob":1},"fields":{},"normalizations":{}}],"relations":[]}'

  # Submit both the plain.html + ann.json in the same request. The important thing: they must have the same name, except for the file extensions
  files = [('file', ('text.plain.html', plain_html)), ('file', ('text.ann.json', ann_json))]
  params['format'] = 'anndoc'
  params['output'] = 'null'
  response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)

  print(response.text)
  ```    
  </div>
</div>
</div>
</div>

<div class="one-third-col">
  <div class="message">
    <p>
      <strong>NOTE:</strong> It is possible to pass an empty array of documents <code>partID</code>'s to the annotatable property of the ann.json format.
    </p>
  </div>
</div>

<div class="one-third-col">
  <p>Response example:</p>
  <div markdown="1">
  ```json
  {
    "ok": 1,
    "errors": 0,
    "items": [{
      "origid": "text",
      "names": ["text.ann.json", "text.plain.html"],
      "rawInputSizeInBytes": 1107,
      "tagtogID": "aZ10o06tnabIXN1wwdw.V3I23fs4-text",
      "result": "updated",
      "parsedTextSizeInBytes": 128
    }],
    "warnings": []
  }
  ```
  </div>
</div>
