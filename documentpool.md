---
layout: page
title: Document pool
sidebar_link: true
id: document_pool
toc: true
---

<div class="two-third-col">
  <p>Your <strong>documents are stored in folders</strong>. Folders are paginated and you can move to the next or previous page using the navigation menu.</p>
  <p>The folder tree is expanded by default.</p>

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
</div>
<div class="one-third-col">
  {% include image.html name="editor-upload-box.png" caption="Upload box where you can select how to import text" %}
</div>
<div class="two-third-col">
  <h4>Upload files with predefined document labels</h4>
  <p>If you have document labels defined in your project, you can pre-annotate these labels for the document you want to upload. This is very handy if you have metadata (e.g. time stamp, type of document, industry, severity, etc.) available you want to have <strong>readily available for your annotators or your ML model</strong>.</p>
  <p>For example, let's say your model use <a title="tagtog - project - webhooks" href="projects.html#webhooks">Webhooks</a> to generate predictions once a document is uploaded. If the user has pre-annotated this document before, your model has valuable information to generate these predictions based on the pre-annotations. Language can significantly vary between departments, contexts, industries, time, etc., so you have an opportunity here to pick this info and generate better predictions accordingly.</p>
  <p>This option in the user interface is only available when you upload <strong>files</strong>. Expand the <i>Advanced</i> menu and set the document labels.</p>
  <p>Using the <a title="tagtog - API" href="/API.html">API</a> you can automatically pre-annotate documents uploading together the document/text and the <code><a href="anndoc.html#ann-json">ann.json</a></code> file with the annotations.</p>
</div>
<div class="one-third-col">
  {% include image.html name="preann-doclabels.png" caption="Predefining document labels before uploading the file" %}
  {% include message.html message='If you upload multiple files at the same time, the predefined document labels will apply to all the files.'%}
</div>
<div class="two-third-col">
  <h4>Upload pre-annotated documents</h4>
  <p>If you have pre-annotated documents, you can upload them directly to tagtog. You will need these two files:</p>

  <p class="list-item"><span class="list-item-1"></span><strong>The file wit the text content</strong>. The format of this file should be one of our supported <a title="tagtog - Input formats" href="ioformats.html#input-formats">input formats</a>.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>The file with the annotations</strong>. From the GUI, the only supported format for annotations is the

  <code><a title="tagtog - ann.json format" href="/anndoc.html#ann-json">ann.json</a></code>.</p>
  <p><strong>Please remember to name both files the same, except for the extension</strong>. For example: <code>mydoc.pdf</code> and <code>mydoc.ann.json</code>. You can upload multiple pre-annotated documents at the same time. For example, 5 text files and 5 annotation files.</p>
  <p>Please check the <a title="tagtog - API" href="/API.html">API</a> for more options as replacing existing annotations.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can upload multiple pre-annotated documents at the same time. For example, 5 text files and 5 annotation files.'%}
</div>
<div class="two-third-col">
  <h3>Remove a document</h3>
    <p>You can remove a document on the web editor view or in the document list view by clicking on the remove button {% include inline-image.html name="editor-doc-remove.PNG" %}.</p>
    <p>To <strong>remove documents in batch</strong>, you can use the <a title="Search - web app" href="/search.html#remove-documents-in-batch">search bar</a> or the <a title="API - Delete" href="/API.html#delete-documents-delete">API for batch removal</a>.</p>
</div>
<div class="one-third-col">
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
