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
  <p>tagtog comes with a set of predefined user roles. Here you find a summary description of the roles. In the <a title="tagtog - permissions" href="collaboration.html#permissions">permissions</a> section just below you will find a detailed list of the permissions for these roles.</p>
  <table style="width:100%">
    <tr>
      <th>Role</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>admin</code></td>
      <td><span markdown="1">Usually they set the project up and track it. Can read all users' annotations and can edit them. They can edit `master`'s and their own annotations. Moreover, they can edit all project's settings. All permissions are active for this role. By default, the user that creates a project becomes its admin. <a title="tagtog - permissions" href="collaboration.html#permissions">More details</a>.</span></td>
    </tr>
    <tr>
      <td><code>reviewer</code></td>
      <td><span markdown="1">They review and approve the annotators' annotations. They can read all users' annotations and can edit them. They can edit `master`'s and their own annotations. Moreover, they can edit some settings, see the project metrics, and use the API. <a title="tagtog - permissions" href="collaboration.html#permissions">More details</a>.</span></td>
    </tr>
    <tr>
      <td><code>supercurator</code></td>
      <td>In addition to the regular annotator routine, they can perform some privileged tasks. They can edit <code>master</code>'s and their own annotations. They can read the settings of the project, see the project metrics, and use the API. <a title="tagtog - permissions" href="collaboration.html#permissions">More details</a>.</td>
    </tr>
    <tr>
      <td><code>curator</code></td>
      <td><span>Regular annotators. They can edit their own annotations. They cannot edit <code>master</code>'s annotations, but can export master into their annotations. They cannot see the metrics of the project nor use the API. <a title="tagtog - permissions" href="collaboration.html#permissions">More details</a>.</span></td>
    </tr>
    <tr>
      <td><code>reader</code></td>
      <td><span>Perfect for those users that only want to consume the production annotations and check the progress. Can only read <code>master</code>'s annotations. They can see the metrics of the project. <a title="tagtog - permissions" href="collaboration.html#permissions">More details</a>.</span></td>
    </tr>
  </table>

</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h3>Create custom roles</h3>
  <p>Depending on your <a href="https://www.tagtog.net/-plans" title="tagtog - plans">plan</a>, you can create custom roles and define their permissions. Read <a title="tagtpg - sysadmin panel - roles and permissions" href="on-premises-sysadmin.html#roles-and-permissions">how to manage and create custom roles</a>.</p>
</div>

<div class="one-third-col">
</div>



<div class="two-third-col">
  <h2>Permissions</h2>
    <p>tagtog role-based access control helps you manage what users can do in a project, and what areas they have access to. You can find below the permissions available in tagtog. Each role has a set of permissions associated.</p>
    <table style="width:150%">
      <tr>
        <th>Realm</th>
        <th>Component</th>
        <th>Permission</th>
        <th>Description</th>
        <th>Reader</th>
        <th>Curator</th>
        <th>Supercurator</th>
        <th>Reviewer</th>
        <th>Admin</th>
      </tr>
      <tr>
        <td rowspan="16">settings</td>
        <td rowspan="2">Guidelines</td>
        <td><code>canReadGuidelinesConf</code></td>
        <td><span>Read access for Settings - Guidelines</span></td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditGuidelinesConf</code></td>
        <td><span>Write access for Settings - Guidelines</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Annotation Tasks</td>
        <td><code>canReadAnnTasksConf</code></td>
        <td><span>Read access for all annotation tasks, namely: Document Labels, Entities, Dictionaries, Entity Labels, and Relations</span></td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditAnnTasksConf</code></td>
        <td><span>Write access for all annotation tasks, namely: Document Labels, Entities, Dictionaries, Entity Labels, and Relations</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Requirements</td>
        <td><code>canReadRequirementsConf</code></td>
        <td><span>Read access for Settings - Requirements</span></td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditRequirementsConf</code></td>
        <td><span>Write access for Settings - Requirements</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Annotatables</td>
        <td><code>canReadAnnotatablesConf</code></td>
        <td><span>Read access for Settings - Annotatables</span></td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditAnnotatablesConf</code></td>
        <td><span>Write access for Settings - Annotatables</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Annotation</td>
        <td><code>canReadAnnotationsConf</code></td>
        <td><span>Read access for Settings - Annotations</span></td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditAnnotationsConf</code></td>
        <td><span>Write access for Settings - Annotations</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Webhooks</td>
        <td><code>canReadWebhooksConf</code></td>
        <td><span>Read access for Settings - Webhooks</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditWebhooksConf</code></td>
        <td><span>Write access for Settings - Webhooks</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Members</td>
        <td><code>canReadMembersConf</code></td>
        <td><span>Read access for Settings - Members</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditMembersConf</code></td>
        <td><span>Write access for Settings - Members</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Admin</td>
        <td><code>canReadAdminConf</code></td>
        <td><span>Read access for Settings - Admin</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditAdminConf</code></td>
        <td><span>Write access for Settings - Admin</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
      </tr>

      <tr>
        <td rowspan="7">documents</td>
        <td rowspan="2">Content</td>
        <td><code>canCreate</code></td>
        <td><span>Rights to import documents to the project</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canDelete</code></td>
        <td><span>Rights to remove documents from the project</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="1">Own version</td>
        <td><code>canEditSelf</code></td>
        <td><span>Write access to the own version of the annotations</span></td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Master version</td>
        <td><code>canReadMaster</code></td>
        <td><span>Read access to the master version of the annotations</span></td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditMaster</code></td>
        <td><span>Write access for the master version of the annotations (ground truth)</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="2">Others' versions</td>
        <td><code>canReadOthers</code></td>
        <td><span>Read access to every project member's versions of the annotations</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canEditOthers</code></td>
        <td><span>Write access to every project member's versions of the annotations</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td rowspan="3">folders</td>
        <td rowspan="3"></td>
        <td><code>canCreate</code></td>
        <td><span>Rights to create folders</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canUpdate</code></td>
        <td><span>Rights to rename existing folders</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>canDelete</code></td>
        <td><span>Rights to delete existing folders</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td>dictionaries</td>
        <td></td>
        <td><code>canCreateItems</code></td>
        <td><span>Rights to add items to the dictionaries using the editor</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td>metrics</td>
        <td></td>
        <td><code>canRead</code></td>
        <td><span>Read access to the metrics of the project (metrics tab) or the metrics for annotation tasks in a document (e.g. IAA)</span></td>
        <td class="centered">✅</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td>API</td>
        <td></td>
        <td><code>canUse</code></td>
        <td><span>Users with this permission can use the API. Users with this permission can see the output formats in the UI</span></td>
        <td class="centered">❌</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
    </table>

</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h2>Teams</h2>
  <p>tagtog comes with a feature to define teams of users to simplify and speed up your collaboration.
     It allows you to group users into teams so you don't have to add each user to a project separately.
     It can be very handy especially when you have many users in the system. Then you can add whole teams
     to projects, delete them from projects, define permission for all team members and so on. For now, it's
     only available for <a href="on_premises_README.html">OnPremises</a>. For more details, please go <a href="on-premises-sysadmin.html#teams-management">here</a>.</p>
</div>

<div class="one-third-col">
</div>


<div class="two-third-col">
  <h2>Annotation versions</h2>
  <p><strong>Each user has an independent version of the annotations for each single document</strong>. For instance, UserA could have 20 entities; UserB could have 5 different entities on the same exact document. <strong>In addition, each document has a <code>master</code> version</strong> which is usually treated as the final/official version (ground truth).</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h2>Annotation flows &amp; Task Distribution</h2>
  <p>There are different ways you can organize your annotation tasks. These are the most common:</p>
</div>



<div class="two-third-col">
  <br/>
  <h4>Annotators annotate directly on the <code>master</code> version (ground truth). No review.</h4>
  <p>This is the simplest flow and there is no review step. Make this choice if you are working alone, or if you trust your annotators' annotations or if time is a constraint. <strong>This is the project's default</strong>. Here, for simplicity, we explain the flow using the default roles.</p>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
  <p class="numbered-item"><span class="number-1">1</span><strong>Add users to your project</strong>. As a project's <code>admin</code>, go to <i>Settings &#8594; Members</i> to add members to your project.</p>
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here, the <code>admin</code> or <code>reviewer</code> writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can create the guidelines at <i>Settings &#8594; Guidelines</i>' %}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Import text</strong>. The default roles <code>admin</code>,  <code>supercurator</code>, and <code>reviewer</code> can import the documents to be annotated by the group. Any project member can see these documents.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>Distribute documents among annotators</strong>. Either let users annotate non-yet-confirmed documents, or otherwise, for example, manually assign document ids to each user.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Each user annotates only the <code>master</code> version of the assigned documents. Once a document is annotated, the user marks the annotations as completed by clicking the <i>Confirm</i> button. For example, <code>admin</code> or <code>reviewer</code> can track the progress in the <a href="metrics.html#documents">metrics of the project</a>.</p>
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
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here, the <code>admin</code> or <code>reviewer</code> writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Distribute documents among annotators</strong>. The project <code>admin</code> goes to <i>Settings &#8594; Members</i>, enables <a href="projects.html#task-distribution">task distribution</a>, selects who to distribute documents to, and selects <strong>1 annotator per document</strong>.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>Import text</strong>. The default roles <code>admin</code>, <code>supercurator</code>, and <code>reviewer</code> can import the documents to be annotated by the group. Any project member can see these documents. In addition, each annotator will see a TODO list with the documents assigned to them, and not confirmed by them yet.</p>
</div>
<div class="one-third-col">
  {% include message.html message='When you import text (via GUI or API), you can <a href="documents.html#distribute-to-a-group-of-users">define manually to which members you want to distribute the documents to</a>.' %}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Users annotate their version of the annotations for the documents assigned. Once completed, users mark their version as completed by clicking on the <i>Confirm</i> button.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can always assign a document to more than one user. Check out <a href="#documents-are-automatically-distributed-multiple-annotators-per">this annotation flow</a> for details.' %}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-6">6</span><strong>Review</strong>. <code>Reviewer</code> (or <code>Admin</code>) checks which documents are ready for review (via GUI in the <a href="documents.html#document-list-item">Document list</a>, in Metrics <i><a href="/metrics.html#documents">metrics panel > documents</a></i>, or <a title="tagtog - Search for confirmed documents" href="search-queries.html#search-confirmed-documents">by using a search query</a>). <code>Reviewer</code> moves the user's annotations to the <code>master</code> version (ground truth), review, and make the required changes. <code>Reviewers</code> should click on the <i>Confirm</i> button in the <code>master</code> version to indicate that the review is completed and the document is ready for production.</p>
</div>
<div class="one-third-col">
  {% include message.html message='If the Review step was not required, users could annotate directly on the <code>master</code> version. When ready, users should mark the annotations of each document as completed by clicking on the <i>Confirm</i> button.' %}
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
  <p class="numbered-item"><span class="number-2">2</span><strong>Create clear guidelines</strong>. Here, the <code>admin</code> or <code>reviewer</code> writes what is to be annotated and which type of annotations to use. Clear and complete guidelines are key to align all project members.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Distribute documents among annotators</strong>. The project <code>admin</code> goes to <i>Settings &#8594; Members</i>, enables <a href="projects.html#task-distribution">task distribution</a>, selects who to distribute documents to, and selects <strong>2 or more annotators per document</strong>.</p>
</div>
<div class="one-third-col">
  {% include message.html message='From the overlapping documents among annotators, the IAA can be computed. Note that even when only <a href="#documents-are-automatically-distributed-one-annotator-per-docume">one annotator is assigned per document</a>, a small sample of documents is randomly chosen by tagtog to always be able to compute the IAA.' %}
</div>


<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>Import text</strong>. The default roles <code>admin</code>, <code>supercurator</code>, and <code>reviewer</code> can import the documents to be annotated by the group. Any project member can see these documents. In addition, each annotator will see a TODO list with the documents assigned to them, and not confirmed by them yet.</p>
</div>
<div class="one-third-col">
  {% include message.html message='When you import text (via GUI or API), you can <a href="documents.html#distribute-to-a-group-of-users">define manually to which members you want to distribute the documents to</a>.' %}
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-5">5</span><strong>The group starts annotating</strong>. Users annotate their version of the annotations for the documents assigned. Once completed, users mark their as completed by clicking on the Confirm button.</p>
</div>

<div class="two-third-col">
  <p class="numbered-item"><span class="number-6">6</span><strong>Adjudication</strong>. <code>Reviewers</code> (or <code>Admins</code>) check which documents are ready for review (via GUI in the <a href="documents.html#document-list-item">Document list</a>, in the <i><a href="/metrics.html#documents">metrics panel > documents</a></i> or <a title="tagtog - Search for confirmed documents" href="search-queries.html#search-confirmed-documents">via search query</a>). For a document, <code>Reviewers</code> merge the users' annotations (<a title="tagtog - Automatic adjudication based on IAA" href="collaboration.html#automatic-adjudication-based-on-iaa">automatic adjudication</a>) to the <code>master</code> version (ground truth). <code>Reviewers</code> review the merged annotations and they should click on the <i>Confirm</i> button in the <code>master</code> version to indicate that the review is completed.</p>
</div>
<div class="one-third-col">
  {% include message.html message="As an alternative, <code>reviewers</code> could review each member's annotations, move to <code>master</code> one of them and apply any potential change directly on <code>master</code>." %}
</div>


<div class="two-third-col">
  <h2>Quality Management</h2>
  <p>Here you will learn how to <strong>track the quality</strong> of your project in real time.</p>
</div>
<div class="two-third-col">
  <h3>IAA (Inter-Annotator Agreement)</h3>
  <p>The <a title="Wikipedia - Inter-rater_reliability" href="https://en.wikipedia.org/wiki/Inter-rater_reliability">Inter-Annotator Agreement (IAA)</a> gauges the quality of your annotation project, that is the degree of consensus among your annotators. If all your annotators make the same annotations independently, it means your guidelines are clear and your annotations are most likely correct. <strong>The higher the IAA, the higher the quality</strong>.</p>

  <p markdown="1">In tagtog, each annotator can annotate the same piece of text separately. <strong>The percentage agreement is measured as soon as two different <em>confirmed</em>✅ annotation versions for a same document exist; i.e., at least one member's and master annotations are confirmed, or 2 or more members' annotations are confirmed</strong>. These scores are <a href="IAA-calculation-methods">calculated</a> <strong>automatically</strong> in tagtog for you ([IAA calculation methods](IAA-calculation-methods)). You can <a title="tagtog - Project's members" href="projects.html#members">add members to your project</a> at <i>Settings > Members</i>.</p>

  <p>If your project has activated <a href='#annotation-flows' title='tagtog - Automatic Task Distribution'>Automatic Task Distribution</a>, tagtog will distribute the same documents to a set of annotators to calculate the IAA right away. Even if you set the task distribution as one annotator per document (each document is assigned to a different annotator), tagtog automatically tries to allocate 5% of your documents to two annotators to calculate IAA. Otherwise, if you want to control this process manually, the only requirement is that more than one annotator annotates the same documents. Using task distribution, you can manually assign a document to a specific set of annotators - <a href='#annotation-flows' title='tagtog - Automatic Task Distribution'>More information</a>.</p>
</div>
<div class="one-third-col">
  {% include message.html message="Note that having a high IAA doesn’t strictly mean that the annotations are correct. It just means that the annotators are following the guidelines with a similar understanding." %}
  {% include message.html message="All the metrics measure the IAA in <a href='https://en.wikipedia.org/wiki/F1_score' title='Wikipedia - F1 Score'>F1</a>." %}
</div>
<div class="two-third-col">
  <h4>IAA at the project level</h4>

  <p>To go to the IAA results, open your project and click on the <strong>Metrics</strong> section. Results are split into annotation types (entity types, entity labels, document labels, normalizations and relations). Each annotation type is divided into annotation tasks (e.g. Entity types: Entity type 1, Entity type 2; Document labels: document label 1, document label 2, etc.). <strong>For each annotation task, scores are displayed as a matrix</strong>. <strong>Each cell represents the agreement pair for two annotators</strong>, being 100% the maximum level of agreement and 0% the minimum.</p>
  <p>The agreement percentage near the title of each annotation task represents the average agreement for this annotation task.</p>
  {% include image.html caption="<strong>Inter-annotator agreement matrix</strong>. It contains the scores between pairs of users. For example, Vega and Joao agree on the 87% of the cases. Vega and Gerard on the 47%. This visualization provides an overview of the agreement among annotators. It also helps find weak spots. In this example we can see how Gerard is not aligned with the rest of annotators (25%, 47%, 35%, 18%). A training might be required to have him aligned with the guidelines and the rest of the team. On the top left we find the annotation task name, id and the agreement average (59,30%)." name="iaa-matrix.png" %}
</div>

<div class="one-third-col">
  {% include message.html message="Note that for a large amount of documents the IAA results might be cached." %}

  {% include message.html message="Only those <a href='collaboration.html#roles'>roles</a> with the <a href='collaboration.html#permissions'>permission</a> to read the project metrics (metrics > <code>canRead</code>) can see the IAA values." %}
</div>

  <div class="two-third-col">


  <h4>IAA at the document level</h4>
  <p markdown="1">tagtog would calculate the agreement if at least two users confirmed their document version. The values are shown on the **sidebar**, near each annotation task. Each value represents the **agreement of the annotation/s for this task in a specific document**. The agreement is calculated only using the annotations from confirmed versions.</p>

  <p markdown="1">Only those [roles](collaboration.html#roles) with the [permission](collaboration.html#permissions) to read the project metrics (metrics > `canRead`) can see the IAA values. This is ideal for `reviewers`, where they need to assess the quality of the annotations before accepting them. Suppose a user's role has this permission (e.g., default roles such as `supercurator`, but not `curator`). In that case, this user also sees the IAA values at the document level for their annotations. While this can increase the annotation bias in some scenarios, it also creates an exciting use case where the users can understand their annotations' quality and spot not intended errors.</p>

  <p markdown="1">If you click on any of these IAA values, a modal dialog shows up with the **list of annotation tasks and the respective IAA values**. In this way, you see all the information in one place, and it is easier to compare and identify problems.</p>

  <p markdown="1">To easily understand the IAA values, imagine you see a 70% IAA near to a document label. It means the value selected by this user was also selected by 70% of all users who confirmed this document. You can find a more detailed example below:</p>

  {% include image.html caption="In this example, you see Kevin's annotations." name="IAA-document-level-content.png" %}

  {% include image.html caption="On the sidebar, you find the IAA values for this document. You can observe that Kevin's agreement with the rest of users who already confirmed their version is 100% for the entity types <code>identifier</code> and <code>argument</code>. However, the value selected for the entity label <code>category</code> ('SEC') has not been selected by any of the other users (agreement 0%). For the relation specified, only half of the users agree with him (agreement: 50%). This information should give you an oversight of  Kevin's annotations quality for this specific document" name="IAA-document-level-sidebar.png" %}

  {% include image.html caption="By clicking on any of the IAA values, a modal dialog shows a summary with all the annotation tasks and their respective IAA for this specific document" name="IAA-document-level-summary.png" %}


</div>
<div class="one-third-col">
  {% include message.html message="IAA values at document level only are displayed in confirmed versions" %}

  {% include message.html message="Only those <a href='collaboration.html#roles'>roles</a> with the <a href='collaboration.html#permissions'>permission</a> to read the project metrics (metrics > <code>canRead</code>) can see the IAA values at document level." %}
</div>

<div class="two-third-col">
  <h4>What can I do if IAA is low?</h4>
  <p>There may be several reasons why your annotators do not agree on the annotation tasks. It is important to mitigate these risks as soon as possible by identifying the causes. If you find such an scenario we recommend you to review the following:</p>
  <p class="list-item"><span class="list-item-1"></span><strong>Guidelines are key</strong>. If you have a large group of annotators not agreeing on a specific annotation task, it means your guidelines for this task are not clear enough. Try to provide representative examples for different scenarios, discuss boundary cases and remove ambiguity. Remember you can attach pictures or screenshots to the guidelines.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>Be specific</strong>. If annotation tasks are too broadly defined or ambiguous, there is room for different interpretations, and eventually disagreement. On the other hand, <strong>very rich and granular tasks can be difficult</strong> for annotators to annotate accurately. <strong>Depending on the scope of your project, find the best trade-off between high specific annotations and affordable annotations</strong>.</p>
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

<div class="two-third-col" markdown="1">

### Adjudication (Merging)

When different users annotate the same document, as a result, there are **different annotation versions**. **Adjudication is the process to resolve inconsistencies among these versions before promoting a version to master**. In other words, the different annotators' versions are **merged** into one (using various strategies). This is also called **aggregation**.

tagtog supports manual adjudication and automatic adjudication. The adjudication methods presented below are available both from the user interface and [via the API](API_documents_v1.html#merge-the-annotations-of-a-document-automatic-adjudication). For the user interface, in the toolbar of the annotation editor, you find these options under (<a title="tagtog - manage annotation versions" href="webeditor.html#manage-annotation-versions">Manage annotation versions</a>{% include inline-image.html name="editor-toolbar-import-ann.PNG" width="28" %}).

<div class="img-with-caption">
  <img src="/assets/img/editor/toolbar/adjudication-merging-actions.png" width="40%" alt="Screenshot: tagtog adjudication / merging button actions" />
  <p>Manual &amp; Automatic Adjudication Actions available on the tagtog document editor.</p>
</div>

  <h4>Manual adjudication</h4>
  <p>A user with the role reviewer or a role with similar permissions (e.g., supercurator) promotes a user version to master using the adjudication option Copy to master. If required, the reviewer can manually change master to ammend any of the user's annotations.</p>
  <p>Alternatively, the reviewer can use one of the automatic adjudication methods explained below and then apply the required changes to master.</p>
</div>

<div class="two-third-col">
  <h4>Automatic adjudication</h4>
  <p markdown="1">Based on your quality requirements, you might want to automate to some extent the review of the annotations. In case more than one user is annotating each document, you can use the automatic adjudication methods to obtain a master version by merging all users' versions for a given document. Notice that a user with the required permissions can still edit master after the adjudication (e.g. role `reviewer`). Therefore, you can either fully automate the review process or accelerate it by only reviewing master rather than each user version.</p>
  <p>Let's explore the different strategies for automatic adjudication.</p>

  <div class="img-with-caption" align="center">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/rf7Za0NBpqA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>

</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h5>Automatic adjudication based on: IAA</h5>
  <p>For each single annotation task, this method promotes to master the annotations of the user with the best <a title="tagtog - inter-annotator agreement (IAA)" href="collaboration#iaa-inter-annotator-agreement">IAA</a> (using the calculation <a title="tagtog - IAA calculation methods" href="IAA-calculation-methods">exact_v1 metric</a>; for all documents).</p>
  <p>The goal is to have in master the <strong>available-best annotations for each annotation task</strong>. That is the reason why this adjudication method is also know as adjudication by Best Annotators</p>
  {% include image.html caption="In this example, SME A (Subject-Matter Expert A) has the highest IAA for task A and SME B for task B. The result are the annotations for task A by SME A plus the annotations from task B by SME B" name="automatic_adjudication.png" %}
  <p>tagtog continuosly computes the IAA values for each annotation task. If there is not enough information to compute the IAA for an specific task, then tagtog, only for that task, promotes to master the annotations of the user with the highest IAA in the project.</p>

  <p>If you want to know more about the adjudication process and when it makes sense to use an automatic process, take a look at this blog post: <a title="Jorge Campos at Medium - The adjudication process in collaborative annotation" href="https://medium.com/@jorgecp/the-adjudication-process-in-collaborative-annotation-61623c46b700?source=friends_link&sk=41adf0909b87899133ac3ef87fa88ccf">The adjudication process in collaborative annotation</a></p>
  <p>If you want to see a step-by-step example for setting up automatic adjudication, check out this post: <a title="tagtog at Medium - Automatic adjudication based on the inter-annotator agreement" href="https://medium.com/@tagtog/automatic-adjudication-based-on-the-inter-annotator-agreement-a62f49be7bcf">Automatic adjudication based on the inter-annotator agreement</a></p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h5>Automatic adjudication by: Union</h5>
  <p markdown="1">This method promotes to master **all the annotations from all the confirmed users' versions**.</p>
    {% include image.html caption="In this example, user A's version and user B's version are merged using the Union method. All the annotations from user A and user B are promoted to master." name="adjudication-union.png" %}
  <p markdown="1">**If an annotation is repeated in two or more versions**, only one of the ocurrences is promoted to master. However, this ocurrence will have different properties in comparison to the original annotation.</p>
  <p markdown="1">Find below how this method generates the resulting `master` version:</p>

  <table style="width:100%">
    <tr>
      <th>Component</th>
      <th>Description</th>
      <th>ann.json location</th>
    </tr>
    <tr>
      <td>Probability</td>
      <td><p markdown="1">The average of probabilities of all the occurrences. For example, if three users confirmed their annotation version and only two users have this annotation on their version, tagtog will promote the annotation to master with a probability of 2/3.</p></td>
      <td><p markdown="1">`confidence.prob`</p></td>
    </tr>
    <tr>
      <td>User list</td>
      <td><p markdown="1">It is composed by all the users that have this annotation in their version.</p></td>
      <td><p markdown="1">`confidence.who`</p></td>
    </tr>
    <tr>
      <td>Entity Labels and Normalizations</td>
      <td><p markdown="1">If an entity is common to all versions, but not the entity label values or normalizations, the result of Union is one entity with the entity label/normalization value set using the first version's value. For example, suppose user A has selected the value `1` for the entity label `category`, user B has selected the value `2` for this label, and user C has selected value `3`. The value of the entity label for this entity in `master` is `1`.</p></td>
      <td><p markdown="1">`entity.fields` or `entity.normalizations`</p></td>
    </tr>
    <tr>
      <td>Relations</td>
      <td><p markdown="1">Each different relation is promoted to `master`.</p></td>
      <td><p markdown="1">`relations`</p></td>
    </tr>
    <tr>
      <td>Document Labels</td>
      <td><p markdown="1">Value is set using the first version's value</p></td>
      <td><p markdown="1">`metas`</p></td>
    </tr>
  </table>

</div>

<div class="one-third-col">
</div>

<div class="two-third-col">
  <h5>Automatic adjudication by: Intersection</h5>
  <p markdown="1">This method promotes to master all the annotations **common in all the confirmed users' versions**.</p>
  <p markdown="1">The Intersection method is the strictest adjudication method because to promote an annotation to master, all the users should agree on that annotation.  It is recommended for environments where annotations play a critical role and where incorrect annotations might have a considerable impact.</p>
  {% include image.html caption="In this example, user A's version and user B's version are merged using the Intersection method. Only the annotations that are in both versions are promoted to master." name="adjudication-intersection.png" %}
  <p markdown="1">Find below how this method generates the resulting `master` version:</p>
  <table style="width:100%">
    <tr>
      <th>Component</th>
      <th>Description</th>
      <th>ann.json location</th>
    </tr>
    <tr>
      <td>Probability</td>
      <td><p markdown="1">Because the annotations promoted the master are common to all the versions, the probability is always `1` (100%).</p></td>
      <td><p markdown="1">`confidence.prob`</p></td>
    </tr>
    <tr>
      <td>User list</td>
      <td><p markdown="1">Because the annotations promoted the master are common to all the versions, all the users who confirmed their version at the moment of the adjudication are in this list.</p></td>
      <td><p markdown="1">`confidence.who`</p></td>
    </tr>
    <tr>
      <td>Entity Labels and Normalizations</td>
      <td><p markdown="1">If an entity is common to all versions, but not the entity label values or normalizations, the result of Intersection is the entity with no entity labels or normalizations set. For example, suppose user A has selected the value `1` for the entity label `category`, user B has selected the value `2` for this label, and user C has selected value `3`. The entity label for this entity in `master` is not set.</p></td>
      <td><p markdown="1">`entity.fields` or `entity.normalizations`</p></td>
    </tr>
    <tr>
      <td>Relations</td>
      <td><p markdown="1">Only the relations (and their entities) common to all the versions are promoted to master. If any of the entities composing the relation is not promoted to master for not meeting the adjudication method criteria, then the relation is not promoted.</p></td>
      <td><p markdown="1">`relations`</p></td>
    </tr>
    <tr>
      <td>Document Labels</td>
      <td><p markdown="1">Value is only set if all the users agree on the same value.</p></td>
      <td><p markdown="1">`metas`</p></td>
    </tr>
  </table>

</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h5>Automatic adjudication by: Majority Vote</h5>
  <p markdown="1">For each single annotation, this method promotes it to master **only if it was annotated by over 50% of the annotators**.</p>
  {% include image.html caption="In this example, the versions of user A, user B and user C are merged using the Majority Vote method. Only the annotations that are common in more than 50% (majority) of the versions are promoted to master. For example, the annotation for the task C (red) on the top left has been selected by user A and user B, therefore they form majority (2 out of 3, or over 66%) and this annotation is promoted to master. On the contrary, those annotations that have not been selected by the majority, are not promoted to master." name="adjudication-vote.png" %}
</div>
<div class="two-third-col">
  <p markdown="1">Find below how this method generates the resulting `master` version:</p>
  <table style="width:100%">
    <tr>
      <th>Component</th>
      <th>Description</th>
      <th>ann.json location</th>
    </tr>
    <tr>
      <td>Probability</td>
      <td><p markdown="1">tagtog only promotes to master those annotations that more than 50% (majority) of the users have in their version. This means, the probability of any annotation promoted to master will be over `0.5` (50%).</p></td>
      <td><p markdown="1">`confidence.prob`</p></td>
    </tr>
    <tr>
      <td>User list</td>
      <td><p markdown="1">It is composed by all the users that have this annotation in their version.</p></td>
      <td><p markdown="1">`confidence.who`</p></td>
    </tr>
    <tr>
      <td>Entity Labels and Normalizations</td>
      <td><p markdown="1">Suppose an entity is common to all versions, but the values for an entity label or normalization are different. If the same value has been chosen by 50% or less of the users, the Majority Vote method results in the entity with no entity label or normalization set. If more than 50% of the users choose the same value, then the entity label or normalization is set using that value. For example, suppose user A has selected the value `1` for the entity label `category`, user B has selected the value `1` for this label, and user C has selected value `2`. The entity label for this entity in `master` is set to `1`.</p></td>
      <td><p markdown="1">`entity.fields` or `entity.normalizations`</p></td>
    </tr>
    <tr>
      <td>Relations</td>
      <td><p markdown="1">Only the relations (and their entities) common to more than 50% of the versions are promoted to master. If any of the entities composing the relation is not promoted to master for not meeting the adjudication method criteria, then the relation is not promoted.</p></td>
      <td><p markdown="1">`relations`</p></td>
    </tr>
    <tr>
      <td>Document Labels</td>
      <td><p markdown="1">Value is only set if more than 50% of the users agree on the same value.</p></td>
      <td><p markdown="1">`metas`</p></td>
    </tr>
  </table>
</div>
<div class="one-third-col">
  {% include message.html message="If an annotation is shared by exactly 50% of the versions, the annotation is not promoted to <code>master</code>. The value must be _over 50%_ for the promotion." %}
</div>
<div class="two-third-col">
  <h3>Conflict resolution</h3>
  <p markdown="1">When you start an annotation project, you will want your annotators to align with your project guidelines. Depending on the project, this might be challenging for the first few iterations when annotators might not adhere to the guidelines or resolve the annotation tasks differently. During this process, we recommend approaching these differences via conflict resolution:</p>
  <p class="numbered-item" markdown="1"><span class="number-1">1</span>Upload a set of documents. Each annotator will annotate each of the documents.</p>
  <p class="numbered-item" markdown="1"><span class="number-2">2</span>Using the [GUI](webeditor.html#manage-annotation-versions) or the API, select automatic adjudication by Union to move all the users' annotations to `master`.</p>
  <p class="numbered-item" markdown="1"><span class="number-3">3</span>The user taking care of the conflict resolution goes to the master version and [**filter the annotations by probability**](webeditor.html#filter-entities). Any probability under 100% will show the annotations that have a conflict, i.e., not all the users agreed on the annotation. For example, if you set the filter to 99%, it will show you all the annotations that less than 99% of the annotators annotated). You probably want to filter for many annotators using a lower probability (e.g., less than 70%).</p>
</div>
<div class="two-third-col">
  <p class="numbered-item" markdown="1"><span class="number-4">4</span>Go over each annotation with your team to understand what went wrong.  Update the guidelines to avoid this issue in the future.</p>
</div>
<div class="one-third-col">
  {% include message.html message='You can use the <a href="webeditor.html#document-review">Document Review</a> feature to navigate the conflicts by keyboard' %}
</div>

