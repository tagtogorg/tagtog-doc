---
layout: page
title: Document pool
sidebar_link: true
id: document_pool
---

<div class="two-third-col">
  <p>Your documents are listed in the <strong>pool</strong>. The pool is paginated and you can move to the next or previous page using the navigation menu.</p>
    <h3>Upload text</h3>
    <p>In order to <strong>upload</strong> a new document, please click on {% include inline-image.html name="add-content-button.png" width="70" %}. Once clicked, a modal menu is displayed.</p>
    <p>The different formats accepted are described here: <a href="/ioformats.html#input-formats">Input formats</a></p>
    <h3>Remove a document</h3>
    <p>You can remove a document on the web editor view or in the pool view by clicking on the remove button {% include inline-image.html name="editor-doc-remove.png" %}.</p>
</div>
<div class="one-third-col">
  {% include message.html message='<strong>What is a document?</strong>&nbsp;Any fragment of text. It can be plain text or have one of the formats (PDF, HTML, XML, etc.) defined here: <a href="https://github.com/tagtog/tagtog-doc/wiki/Input-File-Formats">input formats</a>'%}
  {% include image.html name="editor-upload-box.png" caption="Upload box where you can select how to import text" %}
</div>

<div class="two-third-col">
  <h3>Manually confirmed documents</h3>
  <p>In the pool, each document has a check mark, when green, it means the document is confirmed.</p>
  <p>Manually confirmed documents are those with <strong>all annotations complete</strong>. Depending on the project it can also mean that the annotations have been reviewed by a human, and they can be used as training data.</p>
  <p>Confirm documents is helpful to keep the progress of the annotation tasks.</p>
</div>

<div class="one-third-col">
  {% include message.html message="If you are training a model within tagtog, only those documents marked as confirmed are used as <strong>training data</strong> for your machine learning model."%}
  {% include message.html message='Using the API, you can also <a href="/API.html#search-documents-in-a-project-get">retrieve which documents are complete</a>.' %}
</div>

<div class="two-third-col">
  <h3>Test folder</h3>
  Use the test folder to test the <strong>performance of the machine learning methods</strong>. Add here a few documents and annotate them manually. These, so called <strong>gold standard</strong> or set, will never be used for real training. Make sure documents inside this folder have everything tagged correctly according to the most recent guidelines.
</div>

<div class="one-third-col">
  <div class="message">
    Only mind the test folder if you are using machine learning to annotate automatically.
  </div>
</div>

