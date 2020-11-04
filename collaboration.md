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
      <td><span markdown="1">Usually they set the project up and track it. Can read all user's annotations and can edit them. They can edit `master`'s and their own annotations. Moreover, they can edit all project's settings. All permissions are active for this role. By default, the user that creates a project becomes its admin. <a title="tagtog - permissions" href="collaboration.html#permissions">More details</a>.</span></td>
    </tr>
    <tr>
      <td><code>reviewer</code></td>
      <td><span markdown="1">They review and approve the annotators' annotations. They can read all user's annotations and can edit them. They can edit `master`'s and their own annotations. Moreover, they can edit some settings, see the project metrics, and use the API. <a title="tagtog - permissions" href="collaboration.html#permissions">More details</a>.</span></td>
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
     It can be very handy especially when you have many users in the system. Then you can add a whole teams
     to projects, delete them from projects, define permission for all team members and so on. For now, it's 
     only available for <a href="on_premises_README.html">OnPremises</a>. For more details, please go <a href="on-premises-sysadmin.html#teams-management">here</a>.</p>
</div>

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
  <p class="numbered-item"><span class="number-6">6</span><strong>Review</strong>. <code>Reviewer</code> (or <code>Admin</code>) checks which documents are ready for review (via GUI in the <i><a href="/metrics.html#documents">metrics panel > documents</a></i> or <a title="tagtog - Search for confirmed documents" href="search-queries.html#search-confirmed-documents">by using a search query</a>). <code>Reviewer</code> moves the user's annotations to the <code>master</code> version (ground truth), review, and make the required changes. <code>Reviewers</code> should click on the <i>Confirm</i> button in the <code>master</code> version to indicate that the review is completed and the document is ready for production.</p>
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
  <p class="numbered-item"><span class="number-6">6</span><strong>Adjudication</strong>. <code>Reviewers</code> (or <code>Admins</code>) check which documents are ready for review (via GUI in the <i><a href="/metrics.html#documents">metrics panel > documents</a></i> or <a title="tagtog - Search for confirmed documents" href="search-queries.html#search-confirmed-documents">via search query</a>). For a document, <code>Reviewers</code> merge the users' annotations (<a title="tagtog - Automatic adjudication based on IAA" href="collaboration.html#automatic-adjudication-based-on-iaa">automatic adjudication</a>) to the <code>master</code> version (ground truth). <code>Reviewers</code> review the merged annotations and they should click on the <i>Confirm</i> button in the <code>master</code> version to indicate that the review is completed.</p>
</div>
<div class="one-third-col">
  {% include message.html message="As an alternative, <code>reviewers</code> could review each member's annotations, move to <code>master</code> one of them and apply any potential change directly on <code>master</code>." %}
</div>


<div class="two-third-col">
  <h2>Quality Management</h2>
  <p>Here you will learn how to <strong>track the quality</strong> of your project in real time.</p>
  <h3>IAA (Inter-Annotator Agreement)</h3>
  <p>The <a title="Wikipedia - Inter-rater_reliability" href="https://en.wikipedia.org/wiki/Inter-rater_reliability">Inter-Annotator Agreement (IAA)</a> gauges the quality of your annotation project, that is the degree of consensus among your annotators. If all your annotators make the same annotations independently, it means your guidelines are clear and your annotations are most likely correct. <strong>The higher the IAA, the higher the quality</strong>.</p>

  <p>In tagtog, each annotator can annotate the same piece of text separately. <strong>The percentage agreement is measured as soon as two different <em>confirmed</em>✅ annotation versions for a same document exist; i.e., at least one member's and master annotations are confirmed, or 2 or more members' annotations are confirmed</strong>. These scores are <a href="IAA-calculation-methods">calculated</a> <strong>automatically</strong> in tagtog for you. You can <a title="tagtog - Project's members" href="projects.html#members">add members to your project</a> at <i>Settings > Members</i>.</p>

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
<div class="two-third-col">
  <h3>Adjudication</h3>
  <p> When different users annotate the same documents, as a result, there are multiple annotation versions. <strong>Adjudication is the process to resolve inconsistencies among these versions before promoting a version to master</strong>. tagtog supports automatic adjudication. </p>
  <h4>Automatic adjudication based on IAA</h4>
  <p>Do you need first more information about what IAA (inter-annotator agreement) is. Read here: <a title="tagtog - inter-annotator agreement" href="collaboration.html#iaa-inter-annotator-agreement">inter-annotator agreement</a> ? </p>
  <p>It follows a merging strategy based on <strong>choosing the available-best user for each annotation task</strong>, i.e. choosing the annotations from the user with the highest IAA for a specific annotation task (regarding the <a title="tagtog - IAA calculation methods" href="IAA-calculation-methods">exact_v1 metric</a>; for all documents).</p>
  {% include image.html caption="In this example SME A has the highest IAA for task A and SME B for task B. The result are the annotations for task A by SME A plus the annotations from task B by SME B" name="automatic_adjudication.png" %}
  <p>In the background, tagtog creates an IAA ranking of all annotators for each specific task. In that ordered ranking,
  the chosen annotator is the first one, which has annotations made for the document to merge.</p>
  <p>Also, a ranking of the best overall annotators as an average of all IAAs is calculated. If there are no best overall annotators, this means there is no IAA at all calculated for the project. If the IAA is not calculated for a specific IAA, its best annotator is defaulted to the available-best overall annotator.</p>
  <p>Currently this adjudication process is only available in the user interface (no through API), in the toolbar of the annotation editor (<a title="tagtog - manage annotation versions" href="webeditor.html#manage-annotation-versions">Manage annotation versions</a>{% include inline-image.html name="editor-toolbar-import-ann.PNG" width="28" %}). </p>
  <p>If you want to know more about the adjudication process and when it makes sense to use an automatic process, take a look at this blog post: <a title="Jorge Campos at Medium - The adjudication process in collaborative annotation" href="https://medium.com/@jorgecp/the-adjudication-process-in-collaborative-annotation-61623c46b700?source=friends_link&sk=41adf0909b87899133ac3ef87fa88ccf">The adjudication process in collaborative annotation</a></p>
  <p>If you want to see a step-by-step example for setting up automatic adjudication, check out this post: <a title="tagtog at Medium - Automatic adjudication based on the inter-annotator agreement" href="https://medium.com/@tagtog/automatic-adjudication-based-on-the-inter-annotator-agreement-a62f49be7bcf">Automatic adjudication based on the inter-annotator agreement</a></p>
</div>
<div class="one-third-col">

</div>
