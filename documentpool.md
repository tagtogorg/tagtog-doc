---
layout: page
title: Document pool
sidebar_link: true
id: document_pool
toc: true
---

<div class="two-third-col">
  <p>Your <strong>documents are stored in folders</strong>. Folders are paginated and you can move to the next or previous page using the navigation menu.</p>
  <h3>Folders</h3>
  <p>Use folders to organize your documents better. The <strong>root is the <code>pool</code> folder</strong>, which is created by default with each new project.</p>
  <h4>Create a new folder</h4>
  <p>Click on the folder you want to be the parent of the new folder. Click on the folder action <code>Add new</code>, write the name of the new folder and press the key <kbd>↵</kbd>.</p>
  <h4>Rename a folder</h4>
  <p>Click on the folder you want to rename. Click on the folder action <code>Rename</code>, write the new name of the new folder and press <kbd>↵</kbd>.</p>
  <h4>Remove a folder</h4>
  <p>Click on the folder you want to remove. Click on the folder action <code>Remove</code>. Please remember that all <strong>the documents stored in this folder will be also removed</strong>.</p>
</div>
<div class="one-third-col">
  {% include message.html message='<strong>What is a document?</strong>&nbsp;Any fragment of text. It can be plain text or have one of the formats (PDF, HTML, XML, etc.) defined here: <a title="Input formats" href="/ioformats.html#input-formats">input formats</a>'%}
  {% include message.html message='You can <strong>expand or collapse</strong> folders using the arrows on the left of the folder names.'%}
</div>

<div class="two-third-col">
  <h3>Upload text</h3>
  <p>In order to <strong>upload</strong> a new document, please select the folder you want to upload documents to and click on {% include inline-image.html name="add-content-button.png" width="70" %}. Once clicked, a modal menu is displayed.</p>
  <p>The different formats accepted are described here: <a href="/ioformats.html#input-formats">Input formats</a></p>
  <h3>Remove a document</h3>
  <p>You can remove a document on the web editor view or in the document list view by clicking on the remove button {% include inline-image.html name="editor-doc-remove.PNG" %}.</p>
  <p>To <strong>remove documents in batch</strong>, you can use the <a title="Search - web app" href="/search.html#remove-documents-in-batch">search bar</a> or the <a title="API - Delete" href="/API.html#delete-documents-delete">API for batch removal</a>.</p>
</div>
<div class="one-third-col">
  {% include image.html name="editor-upload-box.png" caption="Upload box where you can select how to import text" %}
</div>

<div class="two-third-col">
  <h3>Manually confirmed documents</h3>
  <p>In the document list view, each document has a check mark, when green, it means the document is confirmed.</p>
  <p>Manually confirmed documents are those with <strong>all annotations complete</strong>. Depending on the project, it can also mean that the annotations have been reviewed by a human, and they can be used as training data.</p>
  <p>Confirm documents is helpful to keep the progress of the annotation tasks.</p>
</div>

<div class="one-third-col">
  {% include message.html message="If you are training a model within tagtog, only those documents marked as confirmed are used as <strong>training data</strong> for your machine learning model."%}
  {% include message.html message='Using the API, you can also <a href="/API.html#search-documents-in-a-project-get">retrieve which documents are complete</a>.' %}
</div>


