---
layout: page
title: Documents
sidebar_link: true
id: project_documents
toc: true
---

<div class="two-third-col">
  <p>Your <strong>documents are stored in folders</strong>. Folders are paginated and you can move to the next or previous page using the navigation menu.</p>
  <p>The folder tree is expanded by default.</p>

  <h3>Document List View</h3>
  <p>In tagtog, documents are listed based on a <a title="tagtog - search queries" href="search-queries.html">search query</a>. For example, listing the documents of a folder or listing all the documents that contain a specific entity. You can use these lists for <a title="tagtog - batch operations" href="search.html#batch-operations">batch processing</a>, for example, to remove or download documents matching a search.</p>

  <h3>Folders</h3>
  <p>Use folders to organize your documents better. The <strong>root is the <code>pool</code> folder</strong>, which is created by default with each new project. Folders are sorted <strong>alphabetically</strong>.</p>
  <h4>Create a new folder</h4>
  <p>Click on the folder you want to be the parent of the new folder. Click on the folder action <code>Add new</code>, write the name of the new folder and press the key <kbd>↵</kbd>.</p>
  <h4>Rename a folder</h4>
  <p>Click on the folder you want to rename. Click on the folder action <code>Rename</code>, write the new name of the new folder and press the key <kbd>↵</kbd>.</p>
  <h4>Remove a folder</h4>
  <p>Click on the folder you want to remove. Click on the folder action <code>Remove</code>. Please remember that all <strong>the documents stored in this folder will be also removed</strong>.</p>
</div>
<div class="one-third-col">
  {% include message.html message='<strong>What is a document?</strong>&nbsp;Any fragment of text. It can be plain text or have one of the formats (PDF, HTML, XML, etc.) defined here: <a title="Input types" href="/ioformats.html#input-types">input types</a>'%}
  {% include message.html message='You can <strong>expand or collapse</strong> folders using the arrows on the left of the folder names.'%}
</div>

<div class="two-third-col">
  <h3>Upload content</h3>
  <p>To <strong>upload</strong> content, please select the folder you want to upload content to, and click on {% include inline-image.html name="add-content-button.png" width="70" %}. Once clicked, a modal menu is displayed.</p>
  <p>The different input types accepted are described here: <a href="/ioformats.html#input-types">Input types</a></p>
</div>
<div class="one-third-col">
  {% include image.html name="editor-upload-box.png" caption="Upload menu where you can select how to import content" %}
</div>
<div class="two-third-col">
  <h4>Upload pre-annotated documents</h4>
  <p>If you have pre-annotated documents, you can upload them directly to tagtog. You will need these two files:</p>

  <p class="list-item"><span class="list-item-1"></span><strong>The file with the text content</strong>. The file type should be one of our supported <a title="tagtog - Input types" href="ioformats.html#input-types">input types</a>.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>The file with the annotations</strong>. Currently, the only supported format for pre-annotated content is the <code><a title="tagtog - ann.json format" href="/anndoc.html#ann-json">ann.json</a></code>.</p>
  <p><strong>Please remember to name both files the same, except for the extension</strong>. For example: <code>mydoc.pdf</code> and <code>mydoc.ann.json</code>. You can upload multiple pre-annotated documents in a single request. For example, 5 text files and 5 annotation files.</p>
  <p>Please check the <a title="tagtog - API" href="/API_documents_v1.html">API</a> for more options as replacing existing annotations.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can upload multiple pre-annotated documents at the same time. For example, 5 text files and 5 annotation files.'%}
</div>

<div class="two-third-col">
  <h4>Advanced options</h4>
  <h5>Upload files with predefined document labels</h5>
  <p>If you have document labels defined in your project, you can pre-annotate these labels for the document you want to upload. This is very handy if you have metadata (e.g. time stamp, type of document, industry, severity, etc.) available you want to have <strong>readily available for your annotators or your ML model</strong>.</p>
  <p>For example, let's say your model uses <a title="tagtog - project - webhooks" href="projects.html#webhooks">Webhooks</a> to generate predictions once a document is uploaded. If the user has pre-annotated this document before, your model has valuable information to generate these predictions based on the pre-annotations. Language can significantly vary between departments, contexts, industries, time, etc., therefore you have an opportunity here to pick this info and to generate better predictions accordingly.</p>
  <p>If there are <a title="tagtog - Project requirements" href="projects.html#requirements">Requirements</a> set for the document labels, these conditions should be met upon content upload.</p>
  <p>Using the <a title="tagtog - API" href="/API_documents_v1.html#import-annotated-documents-post">API</a> you can automatically pre-annotate documents uploading together the content and the <code><a href="anndoc.html#ann-json">ann.json</a></code> file with the annotations.</p>
</div>
<div class="one-third-col">
  {% include image.html name="preann-doclabels.png" caption="Predefining document labels before uploading the file" %}
  {% include message.html message='If you upload multiple files at the same time, the predefined document labels will apply to all the files.'%}
</div>
<div class="two-third-col">
  <h5>Define a name</h5>
  <p>Input types such as plain text, don't have a name associated. In this case, or for regular files, you might want to define your own name for the document. Here you can define a name. The extension attached for plain text is <code>.txt</code>, for files, their original extension.</p>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h5>Format</h5>
  <p>Select <code>Auto</code> to let tagtog decide which is the best format (<a href="/ioformats.html#input-types">default formats</a>).</p>
  <p>If you want to force tagtog to represent the content using a specific format, you can select it here. For example, you can import plain text and set the format as <code>formatted</code> to clean and format the input.</p>
</div>
<div class="one-third-col">
  {% include message.html message='Using Markdown you can also use <a href="tagtog-blocks">tagtog blocks</a> to build a customized annotation layout for your project! E.g. question answering datasets, chatbot training, tweets, etc.'%}
</div>
<div class="two-third-col">
  <h5>Distribute to a group of users</h5>
  <p>If <a href="projects.html#task-distribution">Task Distribution</a> is enabled, you can select to which users you want to assign the documents to import. If one or more users are selected, the automatic task distribution settings are override for this import request.</p>
  <p>The list of selectable users matches the list of members specified in the Task Distribution settings.</p>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h3>Remove a document</h3>
    <p>You can remove a document on the web editor view or in the document list view by clicking on the remove button {% include inline-image.html name="editor-doc-remove.PNG" %}.</p>
    <p>To <strong>remove documents in batch</strong>, you can use the <a title="Search - web app" href="/search.html#remove-documents-in-batch">search bar</a> or the <a title="API - Delete" href="/API_documents_v1.html#delete-documents-delete">API for batch removal</a>.</p>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h3>Manually confirmed documents</h3>
  <p>In the document list view, each document has a check mark, when it is green, it means the document is confirmed.</p>
  <p>Manually confirmed documents are those with the <strong><code>master</code> version confirmed</strong>. Depending on the project, it can also mean that the annotations have been reviewed by a human, and they can be used as ground truth.</p>
  <p>To confirm documents is helpful to keep the progress of the annotation tasks. If <a href="projects.html#task-distribution" title="task distribution">task distribution</a> is active, a number will appear together with the confirm check mark. This number indicates the number of users that have confirmed their version of the annotations. When you hover with your mouse, the list of users who confirmed their version will show up.</p>
</div>

<div class="one-third-col">
  {% include message.html message="If you are training a model within tagtog, only those documents marked as confirmed are used as <strong>training data</strong> for your machine learning model."%}
  {% include message.html message='Using the API, you can also <a href="/API_documents_v1.html#search-documents-in-a-project-get">retrieve which documents are complete</a>.' %}
</div>

<div class="two-third-col">
  <h3>Export/Import documents</h3>
  <p>When you import the settings of a project into another project, the content (the documents and their annotations) is not imported.</p>
  <p>If you want to export documents from one project and import them into another project, you should follow the next steps in the GUI or API.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h4>GUI</h4>
  <h5>One by one</h5>
  <p>Download the original document + the annotations and import them into the new project. The caveat of this method is that, from the GUI, you can only import annotations in the <code>master</code> version</p>. Use the API if you want to export/import also the annotations from the members of the original project.
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-1">1</span><strong>Download the original document</strong>. Open the document. In the toolbar, <a href="webeditor.html#view-output-mode">select the option to download</a> the <code>original</code> file.</p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Download the annotations</strong>. In the toolbar, <a href="webeditor.html#view-output-mode">select the option to download</a> the annotations in <a href="anndoc.html#ann-json"><code>ann.json</code> format</a>.</p>
</div>
<div class="one-third-col">
  {% include message.html message="From the GUI, if you upload an annotation file along with the content, only the <code>master</code> version gets annotated."%}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import the original document and the annotations</strong>. Go to the new project, select the folder where you want to import the pre-annotated document and <a href="documents.html#upload-pre-annotated-documents">upload both files</a> (original document + annotations) using the content panel. You can also import multiple pairs of original document + annotations.</p>
</div>
<div class="two-third-col">
  <h5>Download as a ZIP</h5>
  <p>Download all your content (<a href="anndoc.html#plain-html">plain.html</a> + annotations) at once or download a filtered subset.</p>
  <p>If you want to download only a subset of documents and annotations, you can use <a href="search-queries.html">search queries</a> to filter your documents.</p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-1">1</span><strong>Download a ZIP file</strong>. <a href="projects.html#downloads">Download all your content or a filtered list</a>. Please take into consideration that the original document is not stored in the ZIP file, but only its HTML representation (plain.html).</p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Import the original documents and the annotations</strong>. Go to the new project, select the folder where you want to import the pre-annotated documents and <a href="documents.html#upload-pre-annotated-documents">upload pairs of files</a> (original document or plain.html + annotations) using the content panel.</p>
</div>


<div class="two-third-col">
  <h4>API</h4>
  <p>Download the original document and the annotations and import them into the new project.</p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-1">1</span><strong>Download the the original documents</strong>. Use a document id to download the original file: <a href="API_documents_v1.html#examples-get-the-original-document-by-document-id">Examples: get the original document by document id</a>, or iterate over a the API result of a search query: <a href="API_documents_v1.html#examples-search-using-search-queries">Examples: search using search queries</a>. For example, you can use the wildcard <code>*</code> to obtain all the document ids of a project.</p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Download the annotations</strong>. Use the document id to download the annotations. The same document has multiple annotation versions. You can download the <code>master</code> version: <a href="API_documents_v1.html#examples-get-the-annotations-of-a-document-by-document-id">Examples: get the annotations of a document by document id</a>, or you can download the version from a project member: <a href="API_documents_v1.html#examples-get-the-members-annotations-of-a-document-by-document-i">Examples: get the member's annotations of a document by document id</a></p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import the original documents and the annotations</strong>. You can upload in the same request multiple pairs of original document + annotations: <a href="API_documents_v1.html#examples-import-a-list-of-pre-annotated-files">Examples: import a list of pre-annotated files</a>.</p>
</div>