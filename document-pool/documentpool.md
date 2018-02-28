---
layout: page
title: The document pool
sidebar_link: true
---

<div class="two-third-col">
  <p>Your documents are listed in the <strong>pool</strong>. The pool is paginated and you can move to the next or previous page using the navigation menu.</p>
    <h3>Upload text</h3>
    <p>In order to <strong>upload</strong> a new document, please click on the button with the text `+Content`. Once clicked a modal menu appears:</p>
    {% include image.html name="editor-upload-box.png" caption="Upload box where you can select how to import text" %}

    <p>The different formats accepted are described here: [input formats](inputformats.html)</p>
  
</div>
<div class="one-third-col">
  <div class="message">
    <strong>What is a document?</strong>&nbsp;Any fragment of text. It can be plain text or have one of the formats (PDF, HTML, XML, etc.) defined here: <a href="https://github.com/tagtog/tagtog-doc/wiki/Input-File-Formats">input formats</a>
  </div>
</div>

<div class="two-third-col">
  <h3>Remove a document</h3>
  <p>You can remove a document in the web editor view or in the pool view by clicking on the remove button {% include inline-image.html name="editor-doc-remove.png" %}</p>
</div>

<div class="one-third-col">
  
</div>

<div class="two-third-col">
  <h3>Manually confirmed documents</h3>
  <p>Manually confirmed (or completed) documents are those with <strong>all the annotations reviewed by a human</strong>. In the pool, each document has a checkmark, if it is green, it means the document has been confirmed.</p>
  <p>Confirm documents is helpful to keep the progress of the annotation tasks.</p>
</div>

<div class="one-third-col">
  <div class="message">
    If you are training a model within tagtog, only those documents marked as confirmed are used as <strong>training data</strong> for your machine learning model.
  </div>
</div>

<div class="two-third-col">
  <h3>Test folder</h3>
  Use the test folder to test the <strong>performance of the machine learning methods</strong>. Add here a few documents and annotate them manually. These, so called <strong>gold set</strong>, will never be used for real training. 
</div>

<div class="one-third-col">
  <div class="message">
    Only mind the test folder if you are using machine learning to annotate automatically.
  </div>
</div>

