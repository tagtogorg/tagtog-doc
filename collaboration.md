---
layout: page
title: Multi-user annotation
sidebar_link: true
id: collaboration
---
<div class="two-third-col">
  <p>tagtog is a multi-user tool. Collaborate with other users to annotate faster and improve the quality of your annotations.</p>
  <p>It supports different roles as annotator or admin. Each user can annotate their own copy of the text, facilitating the review process and measurement of inter-annotator agreement.</p>
</div>
<div class="one-third-col">
  {% include message.html message="Both, Cloud and On-premises versions allow multi-user annotation." %}
</div>

<div class="two-third-col">
<h2>Roles</h2>
  <table style="width:100%">
    <tr>
      <th>Role</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>admin</code></td>
      <td>The user who created the project. This user can read other user's annotations, but cannot edit them. They can import into master any user's annotations.</td>
    </tr>
    <tr>
      <td><code>supercurator</code></td>
      <td>Users invited as collaborators to a project who only can see their annotations and <code>master</code>'s. They can edit <code>master</code>'s annotations and export these into their annotations.</td>
    </tr>
    <tr>
      <td><code class="soon">curator</code></td>
      <td><span class="soon">Users invited as collaborators to a project who only can edit their own annotations. They cannot edit <code>master</code>'s annotations, but can export master into their annotations.</span> Coming soon.</td>
    </tr>
    <tr>
      <td><code class="soon">reader</code></td>
      <td><span class="soon">Users invited as collaborators to a project. They cannot edit any annotations. They can only read <code>master</code>'s annotations.</span> Coming soon.</td>
    </tr>
  </table>
  <h5>Admin role</h5>
  <table style="width:100%">
    <tr>
      <th>Component</th>
      <th>Privileges</th>
    </tr>
    <tr>
      <td>Master annotations</td>
      <td>Replace master annotations using the annotations from other project member.</td>
    </tr>
    <tr>
      <td>Guidelines</td>
      <td>Edit project guidelines.</td>
    </tr>
    <tr>
      <td>Entities</td>
      <td>Edit or create entity types.</td>
    </tr>
    <tr>
      <td>Document labels</td>
      <td>Edit or create document labels</td>
    </tr>
    <tr>
      <td>Entity labels</td>
      <td>Edit or create entity labels</td>
    </tr>
    <tr>
      <td>Dictionaries</td>
      <td>Edit or create dictionaries</td>
    </tr>
    <tr>
      <td>Annotatables</td>
      <td>Edit options under the Annotatables settings</td>
    </tr>
    <tr>
      <td>Annotations</td>
      <td>Edit options under the Annotations settings</td>
    </tr>
    <tr>
      <td>Project</td>
      <td>Delete project</td>
    </tr>
  </table>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h2>Annotation versions</h2>
  <p><strong>Each user has a version of the annotations for each single document</strong>. E.g. UserA can have 20 annotations, UserB can have 5 different annotations on the same exact document. In addition to these versions, each document has a <code>master</code> version which is usually treated as the final/official version.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h2>Annotation flows</h2>
  <p>There are different ways you can organize your annotation tasks. These are the most common:</p>
  <br/>
  <h4>Each annotator annotates each document</h4>
  <p>This flow is ideal for those projects requiring high-quality annotations and complex annotation tasks (specific skills required, divergent interpretations, etc.).</p>
  <p class="numbered-item"><span class="number-1">1</span><strong>Add users to your project</strong>. Once you create a project, you become its <code>admin</code>. Go to <i>Settings > Members</i> to add members to your project. Currently, each project member is added as <code>supercurator</code>.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here the admin writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can create the guidelines at <i>Settings > Guidelines</i>' %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import text</strong>. Any project member can import the documents to be annotated by the group. Any project member can see these documents.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>The group starts annotating</strong>. Users annotate their version of the annotations. When the annotations' version of a document is complete, the user mark her/his version as completed by clicking the Confirm button. Each user will do the same when their version is completed.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>Review</strong>. The admin can review every annotation version for each document and check whether they are completed or not. The admin can import any of these versions to <code>master</code> (final version) and mark this version as completed by clicking the Confirm button to indicate the annotations for this document are reviewed and ready.</p>
</div>
<div class="one-third-col">
  {% include message.html message='The admin can use annotation versions to calculate the <a href="https://corpuslinguisticmethods.wordpress.com/2014/01/15/what-is-inter-annotator-agreement/">Inter-annotator agreement</a>' %}
</div>

<div class="two-third-col">
  <br/>
  <h4>Documents to annotate are distributed among annotators</h4>
  <p>Make this choice if the annotation task is simple. If you assign each document to only one annotator, the quality of the annotations depends on the user assigned. </p>
  <p class="numbered-item"><span class="number-1">1</span><strong>Add users to your project</strong>. Once you create a project, you become its <code>admin</code>. Go to <i>Settings > Members</i> to add members to your project. Currently, each project member is added as <code>supercurator</code> role.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here the admin writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can create the guidelines at <i>Settings - Guidelines</i>' %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import text</strong>. Any project member can import the documents to be annotated by the group. Any project member can see these documents.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
<br>
  <p class="numbered-item"><span class="number-4">4</span><strong>Distribute documents among annotators</strong>. You can, for example, assign document ids to each user. </p>
</div>
<div class="one-third-col">
  {% include message.html message="Currently you need to distribute documents among users manually. Coming soon a fully automated mechanism will dispatch the documents among users automatically." %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Users annotate their version of the annotations for the documents assigned. Once completed, the user mark her/his version as completed by clicking the Confirm button.</p>
</div>
<div class="one-third-col">

  {% include message.html message='You can always assign a document to more than one user. Check out <a href="#each-annotator-annotates-each-document">this annotation flow</a> for details.'%}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-6">6</span><strong>Review</strong>. Admin reviews the annotated documents and if ready, import the user annotations to the <code>master</code> version (final version). To indicate the annotations for this document are reviewed, admin clicks the Confirm button in the <code>master</code> version.</p>
</div>
<div class="one-third-col">
  {% include message.html message='If the Review step is not required, the annotator can annotate directly on the <code>master</code> version. When ready, the user marks the annotations of each document as completed by clicking the Confirm button. Check <a href="/collaboration.html#documents-to-annotate-are-distributed-among-annotators-no-review">this flow</a>.' %}
</div>

















<div class="two-third-col">
  <br/>
  <h4>Documents to annotate are distributed among annotators. No review.</h4>
  <p>Make this choice if time is a constraint and you trust the annotations to be produced. This is the simplest flow and there is no review step.</p>
  <p class="numbered-item"><span class="number-1">1</span><strong>Add users to your project</strong>. Once you create a project, you become its <code>admin</code>. Go to <i>Settings > Members</i> to add members to your project. Currently, each project member is added as <code>supercurator</code> role.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here the admin writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can create the guidelines at <i>Settings - Guidelines</i>' %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import text</strong>. Any project member can import the documents to be annotated by the group. Any project member can see these documents.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
<br>
  <p class="numbered-item"><span class="number-4">4</span><strong>Assign each document to one annotator</strong>. To identify a document you use the document id. </p>
</div>
<div class="one-third-col">
  {% include message.html message="Currently you need to distribute documents among users manually. Coming soon a fully automated mechanism will dispatch the documents among users automatically." %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Each user annotates only the <code>master</code> version of the assigned documents. Once a document is annotated, user marks the annotations as completed by clicking the Confirm button. <code>admin</code> can check the progress in the document pool.</p>
</div>
<div class="one-third-col">
</div>
