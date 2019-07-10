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
      <td><span class="soon">Can edit their own annotations. They cannot edit <code>master</code>'s annotations, but can export master into their annotations.</span></td>
    </tr>
    <tr>
      <td><code>reader</code></td>
      <td><span>They cannot edit any annotations nor change anything in the project. They can only read <code>master</code>'s annotations.</span></td>
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
  <h2>Annotation flows &amp; Task Distribution</h2>
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


<div class="two-third-col">
  <h2>Quality Management</h2>
  <p>Here you will learn how to <strong>track the quality</strong> of your project in real time.</p>
  <h3>IAA (Inter-Annotator Agreement)</h3>
  <p>The <a title="Wikipedia - Inter-rater_reliability" href="https://en.wikipedia.org/wiki/Inter-rater_reliability">Inter-Annotator Agreement (IAA)</a> gauges the quality of your annotation project, that is the degree of consensus among your annotators. If all your annotators make the same annotations independently, it means your guidelines are clear and your annotations are most likely correct. <strong>The higher the IAA, the higher the quality</strong>.</p>
  <p>In tagtog, each annotator can annotate the same piece of text separately. <strong>The percentage agreement is only measured when 2 or more annotators annotate the same text and confirm their respective versions</strong>. These scores are calculated <strong>automatically</strong> in tagtog for you. You can <a title="tagtog - Project's members" href="projects.html#members">add members to your project</a> at <i>Settings > Members</i></p>
  <p>To go to the IAA results, open your project and click on the <strong>Metrics</strong> section. Results are split into annotation types (entity types, entity labels, document labels, normalizations and relations). Each annotation type is divided into annotation tasks (e.g. Entity types: Entity type 1, Entity type 2; Document labels: document label 1, document label 2, etc.). <strong>For each annotation task, scores are displayed as a matrix</strong>. <strong>Each cell represents the agreement pair for two annotators</strong>, being 100% the maximum level of agreement and 0% the minimum.</p>
  <p>The agreement percentage near the title of each annotation task represents the average agreement for this annotation task.</p>
  {% include image.html caption="<strong>Inter-annotator agreement matrix</strong>. It contains the scores between pairs of users. For example, Vega and Joao agree on the 87% of the cases. Vega and Gerard on the 47%. This visualization provides an overview of the agreement among annotators. It also helps find weak spots. In this example we can see how Gerard is not aligned with the rest of annotators (25%, 47%, 35%, 18%). A training might be required to have him aligned with the guidelines and the rest of the team. On the top left we find the annotation task name, id and the agreement average (59,30%)." name="iaa-matrix.png" %}
</div>
<div class="one-third-col">
  {% include message.html message="If your project has activated <a href='#annotation-flows' title='tagtog - Automatic Task Distribution'>Automatic Task Distribution</a>, tagtog will distribute some annotators with the same documents and calculate right away the IAA. Otherwise, if you want tagtog to produce IAA metrics, you can organize your annotators to annotate the same subsample of documents." %}

  {% include message.html message="Note that having a high IAA doesn’t strictly mean that the annotations are correct. It just means that the annotators are following the guidelines with a similar understanding." %}

  {% include message.html message="All the metrics measure the IAA in <a href='https://en.wikipedia.org/wiki/F1_score' title='Wikipedia - F1 Score'>F1</a>." %}

  {% include message.html message="Note that for a large amount of documents the IAA results might be cached." %}
</div>

<div class="two-third-col">
  <h4>What can I do if IAA is low?</h4>
  <p>There may be several reasons why your annotators do not agree on the annotation tasks. It is important to mitigate these risks as soon as possible by identifying the causes.  If you find such an scenario we recommend you to review the following:</p>
  <p class="list-item"><span class="list-item-1"></span><strong>Guidelines are key</strong>. If you have a large group of annotators not agreeing on a specific annotation task, it means your guidelines for this task are not clear enough. Try to provide representative examples for different scenarios, discuss boundary cases and remove ambiguity. Remember you can attach pictures or screenshots to the guidelines.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>Try to be specific</strong>. If annotation tasks are too broadly defined or ambiguous, there is room for different interpretations, and eventually disagreement. On the other hand, <strong>very rich and granular tasks can be difficult</strong> for annotators to annotate accurately. <strong>Depending on the scope of your project, find the best trade-off between high specific annotations and affordable annotations</strong>.</p>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <p class="list-item"><span class="list-item-3"></span><strong>Test reliability</strong>. Before start annotating large amounts of data, it is good to make several assessments with a sample of the data. Once the team members have annotated this data, check the IAA and improve your guidelines or train your team accordingly.</p>
  <p class="list-item"><span class="list-item-4"></span><strong>Train</strong>. Make sure you train appropriately members joining the annotation project. If you find annotators that do not agree with most of members from the team, check the reasons, make your guidelines evolve and train them further.</p>
  <p class="list-item"><span class="list-item-5"></span><strong>Check how heterogeneous is your data</strong>. If your data/documents are very different from each other either in complexity or structure, a larger effort would be required to stabilize the agreement. We recommend to split the data into homogeneous groups.</p>
</div>
<div class="one-third-col">
  {% include message.html message="You can create a separate project with the same setup as your production project and <strong>perform tests</strong>. If you bring someone aboard, you can have them annotate the test documents already annotated by the team and check the level of agreement. To train your team, you can add new documents and check the team agreement." %}
</div>
