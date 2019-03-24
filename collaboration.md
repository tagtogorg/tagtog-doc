---
layout: page
title: Multi-user annotation
sidebar_link: true
id: collaboration
---
<div class="two-third-col">
  <p>tagtog is a multi-user tool. Collaborate with other users to annotate faster and improve the quality of your annotations.</p>
  <p>It supports different roles as annotator. Each user can annotate their own copy of the text, facilitating the review process and measurement of inter-annotator agreement (IAA).</p>
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
      <td><span markdown="1">Can read all user's annotations, but cannot edit them. They can edit `master`'s and their own annotations. Moreover, they can [edit the project's settings](#admin-role).</span></td>
    </tr>
    <tr>
      <td><code>supercurator</code></td>
      <td>They can edit <code>master</code>'s and their own annotations.</td>
    </tr>
    <tr>
      <td><code class="soon">curator</code></td>
      <td><span class="soon">Can edit their own annotations. They cannot edit <code>master</code>'s annotations, but can export master into their annotations.</span> Coming soon.</td>
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
      <td>Members</td>
      <td>Add or remove members to the project</td>
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
  <p><strong>Each user has an independent version of the annotations for each single document</strong>. For instance, UserA could have 20 entities; UserB could have 5 different entities on the same exact document. <strong>In addition, each document has a <code>master</code> version</strong> which is usually treated as the final/official version.</p>
</div>
<div class="one-third-col">
</div>




<div class="two-third-col">
  <h2>Annotation flows</h2>
  <p>There are different ways you can organize your annotation tasks. These are the most common:</p>
</div>



<div class="two-third-col">
  <br/>
  <h4>Annotators annotate directly on the <code>master</code> version. No review.</h4>
  <p>This is the simplest flow and there is no review step. Make this choice if you are working alone, or if you trust your annotators' annotations or if time is a constraint. <strong>This is the project's default</strong>.</p>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
  <p class="numbered-item"><span class="number-1">1</span><strong>Add users to your project</strong>. As a project's <code>admin</code>, go to <i>Settings &#8594; Members</i> to add members to your project.</p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here the admin writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can create the guidelines at <i>Settings &#8594; Guidelines</i>' %}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import text</strong>. Admins and supercurators can import the documents to be annotated by the group. Any project member can see these documents.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>Distribute documents among annotators</strong>. Either let users annotate non-yet-confirmed documents, or otherwise, for example, manually assign document ids to each user.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Each user annotates only the <code>master</code> version of the assigned documents. Once a document is annotated, the user marks the annotations as completed by clicking the Confirm button. <code>admin</code>'s can check the progress in the document list view.</p>
</div>




<div class="two-third-col">
  <br/>
  <h4>Documents are automatically distributed; one annotator per document</h4>
  <p>Make this choice if the annotation task is simple or if time is a constraint. If you assign each document to only one annotator, the quality of the annotations depends on the assigned user.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-1">1</span><strong>Add users to your project</strong>. As a project's <code>admin</code>, go to <i>Settings &#8594; Members</i> to add members to your project.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here the admin writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import text</strong>. Admins and supercurators can import the documents to be annotated by the group. Any project member can see these documents.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>Distribute documents among annotators</strong>. As a project's <code>admin</code>, go to <i>Settings &#8594; Members</i> and select <strong>1 annotator per document</strong>. Additionally, choose whether the project's owner should be assigned documents to annotate or not.</p>
</div>
<div class="one-third-col">
  {% include message.html message="The <em>project's owner</em> is the user who created the project. This is always an <code>admin</code>." %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Users annotate their version of the annotations for the documents assigned. Once completed, the user mark her/his version as completed by clicking on the Confirm button.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can always assign a document to more than one user. Check out <a href="#documents-are-automatically-distributed-multiple-annotators-per">this annotation flow</a> for details.' %}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-6">6</span><strong>Review</strong>. Admins review the annotated documents and if ready, import the user's annotations to the <code>master</code> version (final version). If the annotations were not Confirmed yet, admins should click on the Confirm button in the <code>master</code> version to indicate that the review is completed.</p>
</div>
<div class="one-third-col">
  {% include message.html message='If the Review step was not required, users could annotate directly on the <code>master</code> version. When ready, users should mark the annotations of each document as completed by clicking on the Confirm button.' %}
</div>










<div class="two-third-col">
  <br/>
  <h4>Documents are automatically distributed; multiple annotators per document</h4>
  <p>This flow is ideal for those projects requiring high-quality annotations and complex annotation tasks (specific skills required, divergent interpretations, etc.).</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-1">1</span><strong>Add users to your project</strong>. As a project's <code>admin</code>, go to <i>Settings &#8594; Members</i> to add members to your project.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here the admin writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import text</strong>. Admins and supercurators can import the documents to be annotated by the group. Any project member can see these documents.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>Distribute documents among annotators</strong>. As a project's <code>admin</code>, go to <i>Settings &#8594; Members</i> and select <strong>2 annotators or more per document</strong>. Additionally, choose whether the project's owner should be assigned documents to annotate or not.</p>
</div>
<div class="one-third-col">
  {% include message.html message='From the repeated documents ammong annotators, the IAA can be computed. Note that even when only <a href="#documents-are-automatically-distributed-one-annotator-per-docume">one annotator is assigned per document</a>, a small sample of documents is randomly chosen by tagtog to always be able to compute the IAA.' %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Users annotate their version of the annotations for the documents assigned. Once completed, the user mark her/his version as completed by clicking on the Confirm button.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-6">6</span><strong>Review</strong>. Admins review the annotated documents and if ready, import the user' annotations to the <code>master</code> version (final version). If the annotations were not Confirmed yet, admins should click on the Confirm button in the <code>master</code> version to indicate that the review is completed.</p>
</div>
