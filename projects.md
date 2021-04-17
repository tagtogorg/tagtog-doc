---
layout: page
title: Projects
sidebar_link: true
id: projects

tagtog_domain: https://www.tagtog.net
---

<div class="two-third-col">
  <p>A project is a collection of documents and rules to annotate documents manually or automatically.</p>

  <h2>Create a new project</h2>

  <p>Once you have signed up and you have a user account, you are ready to <a href="{{page.tagtog_domain}}/-new">create a new project</a>.</p>

  <p class="numbered-item"><span class="number-1">1</span>Set the <strong>name</strong> for your project.</p>
  <p class="numbered-item"><span class="number-2">2</span>Set an optional <strong>description</strong> for your project. Moreover, each project has a <a href="#guidelines">Guidelines section</a> where you can go into detail about the characteristics of your project.</p>
</div>


<div class="two-third-col">
  <h2>Project settings</h2>
  <p>If you selected some machines when you created your project, you probably want to start importing text to tagtog. Otherwise, you need to configure the project's settings either to annotate manually or automatically.</p>
</div>
<div class="one-third-col">

</div>

<div class="page-subsection">
  <div class="two-third-col">
    <h3>Guidelines</h3>
    <p>You can write the <strong>annotation guidelines</strong> for you or your team. It should define what and how to manually annotate. The more clear it is, the better the annotations and the training data you can generate.</p>
  </div>
  <div class="one-third-col">
    {% include image.html name="settings-guidelines.PNG" %}
  </div>
  <div class="two-third-col">
    <p>Clicking on <code>Edit</code> you turn on the mode to edit the guidelines. Clicking on <code>View</code> you are on the preview mode and you can see the results of your changes. Once it is ready, just save it {% include inline-image.html name="save-guidelines.PNG" width="30" %}.
    </p>
    <p>Only users with <strong>admin role</strong> (or a custom role with enough <a href="collaboration.html#permissions" title="tagtog - Permissions">permissions</a>) can edit the guidelines.</p>
  </div>
  <div class="one-third-col">
    <div class="message">
      You can enrich the guidelines using <a alt="Markdown" href="https://commonmark.org/help/">Markdown</a>
    </div>
  </div>
</div>


<div class="page-subsection">
  <div class="two-third-col">
    <h3>Annotatable sections</h3>
    <p>Here you select which sections you want to manually or automatically annotate in supported scientific papers (papers should be imported in XML format. <a title="tagtog - XML supported input types" href="ioformats.html#files">Here</a> is the list of supported XML formats). The available sections are: <code>Title</code>, <code>Abstract</code>, <code>Introduction & Background</code>, <code>Materials & Methods</code>, <code>Results, Conclusion & Discussion</code>, <code>Other</code>. The sections not selected will be grayed out in the editor and manual annotations disabled.</p>
    <p>You can also select how to annotate <code>Figures & Tables</code> as in <code>always</code>, <code>never</code> or <code>section-dependant</code>.</p>
    <p>To <strong>disable manual annotation</strong>, uncheck each section. Users will be able to read text in the editor as usual, however manual annotation won't be possible.</p>
  </div>
  <div class="one-third-col">
    {% include image.html name="settings-annotatables.PNG" %}
    <div class="message">
      Annotatable settings are only specific to scientific articles. If you are not planning to import this type of documents, make sure <code>All</code> option is selected.
    </div>
  </div>
</div>
<div class="page-subsection">
  <div class="two-third-col">
    <h3>Entities</h3>
    <p>Here you should define what type of information you want to annotate manually or automatically. Meaning, which type of information you want to identify or annotate in text. You achieve this by defining <code>Entity Types</code> (a.k.a. Entity Classes).</p>
    {% include image.html name="settings-entities-types.PNG" caption="You define entity types from the user interface"%}
  </div>
  <div class="one-third-col">
    <div class="message">
      <strong>What is an entity?</strong>&nbsp; a named entity is a real-world object, such as persons, locations, organizations, products, etc. Examples of named entities include Barack Obama, New York City, Volkswagen Golf, or anything that can be named. Entities are instances of <code>Entity Types</code> (e.g., New York City is an instance of a City, wheel is an instance of a Vehicle part).
    </div>
    <div class="message">
      <strong>Accessibility tip</strong>: use colors that are easy to distinguish. Keep in mind color blind users.
    </div>
    <div class="message">
      The name for an Entity type should contain only letters, numbers, or underscores, and must start with a letter. Minimum length: 2 characters. Maximum length: 24 characters.
    </div>
  </div>
  <div class="two-third-col">
    <p>You must add one or more entity types. Each entity is defined by a <code>name</code>, <code>description</code> (optional) and <code>color</code>. For example in the project in the picture above we want to extract vehicle information and for that we have created entity types to annotate vehicle parts (<code>vehiclePart</code>), vehicle types, (<code>vehicleType</code>) and vehicle model (<code>vehicleModel</code>). In order to easily identify the entities in the text, we will assign to each entity type a color.</p>
  </div>
  <div class="one-third-col">

  </div>
</div>
<div class="page-subsection">
  <div class="two-third-col">
    <h3>Dictionaries</h3>
    <p>As soon as you create one entity type, this will appear in the <code>Dictionaries</code> panel. Each entity type can have associated one or more dictionaries (<a href="/dictionary-format.html">Dictionary format</a>). From here you can upload, replace or download dictionaries.</p>
    {% include image.html name="settings-dictionaries.PNG" caption="Once you have created a dictionary, you can upload/replace or download the dictionary file"%}
    <p>As an example of dictionary, let's use the entity type <code>vehicleModel</code>. For example, <code>Volkswagen Golf 7</code>, <code>Golf Mk7</code> and <code>Golf VII</code> all identify the same canonical or unique object, this object can be identified with an ID, e.g.: <code>VWGOLF7</code>. Let's create our entry in the dictionary:</p>
    <div class="highlight">
      VWGOLF7&emsp;Volkswagen Golf 7&emsp;Golf Mk7&emsp;Golf VII
    </div>
  </div>
  <div class="one-third-col">
    <div class="message">
      <strong>What is a dictionary?</strong> A simple list of terms with their synonyms. E.g. the model <code>Volkswagen Golf 7</code> is also known as <code>Golf Mk7</code>. This list facilitates NER, i.e. the <strong>automatic extraction of entities</strong> in text and their normalization. The <strong>normalization</strong> of entities is the process to identify a canonical unambiguous reference to an entity. <a href="/dictionary-format.html">Dictionary format</a>.
    </div>
  </div>
  <div class="two-third-col">
    <p>When you create a dictionary, you don't need to cover cases as plural, tenses, etc. tagtog uses the dictionary entries and applies <strong>grammar rules</strong> to identify potential entities doing such modifications for you.</p>
    <p>In order to upload a dictionary, you first need to create a dictionary. Click on <code>New Dictionary</code> under the entity type name and Save it. Two options will show up: <code>Download Dictionary</code> and <code>Upload Dictionary</code>.</p>
  </div>
  <div class="one-third-col">
    {% include message.html message="The process of normalization <strong>facilitates the retrieval of information</strong>, e.g. How many error reports mention the vehicle <code>Golf Mk7</code>?" %}
  </div>
  <div class="two-third-col">
  <p><strong>Upload/Replace</strong>: you can use this option to upload a dictionary file. If the file was uploaded previously, it will be replaced with the new dictionary. Once you uploaded a dictionary, all new text imported is annotated automatically following the dictionary rules.</p>
  </div>
  <div class="one-third-col">
  </div>
  <div class="two-third-col">
    <p><strong>Download</strong>: you can use this option to download the dictionary being used in tagtog to your computer. This is very useful to make large edit operations and later replace the existing dictionary.</p>
    <p>Dictionaries are <strong>automatically updated</strong> if a user adds new normalizations using the web editor. <a href="/webeditor.html#update-dictionary-from-annotation-editor">More information</a>.</p>
  </div>
  <div class="one-third-col">
  </div>
</div>

<div class="page-subsection">
  <div class="two-third-col">
    <h3>Relations</h3>
    <p>You can <strong> annotate relations</strong> in text. For that you must first create a new <code>Relation Type</code> by clicking the <code>New Relation Type</code> button. After just choose two Entity Types, those types you want to identify relations for. Optionally you can add a <code>description</code> for the relation. For example, a new relation type between vehicle parts and vehicle models.</p>
  </div>
  <div class="one-third-col">
    {% include image.html name="settings-new-relation-type.PNG"%}
  </div>
  <div class="two-third-col">
    <p>Currently you cannot extract relations in text automatically. However, as a workaround, you can extract the entities automatically and based on the distance in text, infer a relation.</p>
  </div>
  <div class="one-third-col">
    <div class="message">
      From the moment you define a relation in settings, you can start annotating relations in text.
    </div>
  </div>
</div>

<div class="page-subsection">
  <div class="two-third-col">
    <h3>Document labels</h3>
    <p>These are tags (labels) that you associate to the <em>whole</em> document. This is useful for text classification / categorization (e.g. sentiment analysis).</p>
    <p>To create a new Document Label, click on the button <code>New Document Label</code>. Then, write a <code>name</code> for the label (required), <code>type</code> (required), and <code>description</code> (optional).</p>
    <p>You can create different types of Document Labels:</p>
    <table style="width:100%">
      <tr>
        <th>Type</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><code>boolean</code></td>
        <td>The simplest label. Basically you mark the document as <code>True</code> or <code>False</code> for a specific condition. e.g. should this customer request go to the technical department? Yes or No.</td>
      </tr>
      <tr>
        <td><code>string</code></td>
        <td>One or more words describing a document. This is particularly handy whether you don't have a specific list of options or if you do, it might change often. e.g. which disease is related to this clinical profile? You can also use the <code>string</code> type to attach any meta information, e.g.: comments, URLs, json data, etc.</td>
      </tr>
      <tr>
        <td><code>enum</code></td>
        <td>list of options which can describe a document. <strong>In this case, the options must be written in the description of the label separated by commas</strong>. e.g. an error's severity could be broken down as: low, medium, high, critical. </td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
    <div class="message">
      <strong>What is a document label?</strong> An attribute assigned to a fragment of text (document). This attribute makes a reference to the whole text and not just to a text span or entity.
    </div>
    <div class="message">
      The name for a Document Label should contain only letters, numbers, or underscores, and must start with a letter. Minimum length: 3 characters. Maximum length: 24 characters.
    </div>
  </div>
  <div class="two-third-col">
    {% include image.html name="settings-doclabel.png" caption="Example: setting a document label of <code>enum</code> type."%}
  </div>
  <div class="one-third-col">
    <div class="message">
      <strong>Tip</strong>: document labels are very useful for text classification or intent detection. You can use document labels to train a machine learning model and generate these automatically.
    </div>
  </div>
</div>

<div class="page-subsection">
  <div class="two-third-col">
    <h3>Entity labels</h3>
    <p>Labels used to add attributes to existing entities. It is usual some attributes make sense only to some entity types (e.g. gender for person, not for city), you can assign an entity label to one specific entity type or all entity types.</p>
    <p>To create a new Entity Label, click on the button <code>New Document Label</code>. Then, write a <code>name</code> for the label (required), <code>type</code> (required), <code>entity type</code> you want to assign the label to (required), and a <code>description</code> (optional).</p>
    <p>You can create different types of Entity Labels:</p>
    <table style="width:100%">
      <tr>
        <th>Type</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><code>boolean</code></td>
        <td>The simplest label. Basically you mark an entity as <code>True</code> or <code>False</code> for a specific condition. e.g. if you are dealing with financial reports, you can annotate organization names and add an attribute <code>Bankruptcy</code> with value <code>True</code> to those organizations going bankrupt. You can later train a model that identifies in text companies that went bankrupt.</td>
      </tr>
      <tr>
        <td><code>string</code></td>
        <td>One or more words describing an entity. This is particularly handy whether you don't have a specific list of options or if you do, it might change often. e.g. you can add comments to entities.</td>
      </tr>
      <tr>
        <td><code>enum</code></td>
        <td>list of options to describe an entity. In this case the options should be <strong> written in the description of the label separated by commas</strong>. e.g. if you are processing CVs you could add an entity label to the entities identifying skills. This enum entity label <code>skill type</code> have the values <code>soft skill</code> and <code>hard skill</code>.</td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
    {% include message.html message="<strong>What is an entity label?</strong> An attribute assigned to an entity." %}
    {% include message.html message="The name for an Entity Label should contain only letters, numbers, or underscores, and must start with a letter. Minimum length: 3 characters. Maximum length: 24 characters." %}
  </div>
  <div class="two-third-col">
    {% include image.html name="settings-entitylabel.PNG" caption="Setting two entity labels. The first with the <code>enum</code> type can be only set for entities with the type <code>VehiclePart</code>. The second with the <code>string</code> type can be set for all entity types. "%}
    <p><strong>By default, the new entity labels will be assigned to all entity types</strong>. Otherwise, you can choose or filter an entity type from the list of entity types.</p>
    <p>Once saved, you can start using them on the web editor. When you add a label to an entity, <strong>remember that only those labels related to the entity type of the entity will show</strong>.</p>
    <p>Soon you will be able to generate entity labels automatically within tagtog.</p>
  </div>
  <div class="one-third-col">
    <div class="message">
      <strong>Tip</strong>: an entity itself contains information as entity type, text, etc. Entity labels are useful to add additional attributes to entities.
    </div>
  </div>
</div>

<div class="page-subsection">
  <div class="two-third-col">
    <h3>Webhooks</h3>
    <h4>What is a webhook?</h4>
    <p>A webhook is a notification mechanism that allows your system to receive events from a different service in real-time. Event notifications are sent via HTTP POST requests to an endpoint defined by you.</p>
    <p>Think of it as an SMS notification. You make a change to your bank account details (event), and you receive an SMS asking you for confirmation (event notification). When you opened your bank account, you gave your phone number (endpoint), so they know how to reach you.</p>
    <h4>Webhooks in tagtog</h4>
    <p>The webhooks are useful to integrate your system or models with tagtog. You can define webhooks to notify automatically an external system right after a specific action was performed using tagtog GUI or API.</p>
    <p>Only users with the role <code>admin</code> (or a custom role with enough <a href="collaboration.html#permissions" title="tagtog - Permissions">permissions</a>) can see/edit these project settings.</p>
    <p>In tagtog, there are two events that trigger an event notification:</p>
    <p class="list-item"><span class="list-item-1"></span>Import new document: an event notification is sent once a user uploads a document. Use this notification, for example, to annotate the document using your models and push the annotated document back to tagtog.</p>
    <p class="list-item"><span class="list-item-2"></span>Save a document: an event notification is sent once a user saves a document. Use this notification, for example, to get the annotations done by your team and add them to your training data.</p>
    <table style="width:100%">
      <tr>
        <th>Event</th>
        <th>Description</th>
        <th>Source</th>
      </tr>
      <tr>
        <td>Import new document</td>
        <td>A notification is sent when the user uploads a document.</td>
        <td><code>GUI</code> and <code>API</code></td>
      </tr>
      <tr>
        <td>Save document</td>
        <td>A notification is sent when the user saves a document.</td>
        <td><code>GUI</code> and <code>API</code> (<a href="/train-your-own-models.html#how-to-upload-annotated-documents">update annotations via API</a>)</td>
      </tr>
    </table>
    <p>When any of those events are triggered, we'll send a <strong>HTTP POST payload</strong> to the webhook's configured End Point URL.</p>
    <p>We also send information in the delivery <strong>HTTP headers</strong> for you to better process the event:</p>
    <table style="width:100%">
      <tr>
        <th>Header</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><code>X-tagtog-onPushSave-source</code></td>
        <td>Source of the event. Possible values: <code>GUI</code>, <code>API</code></td>
      </tr>
      <tr>
        <td><code>X-tagtog-onPushSave-status</code></td>
        <td>Type of event. Possible values: <code>created</code>, <code>updated</code></td>
      </tr>
    </table>
    <p>This is the required information to configure a webhook:</p>
    <table style="width:100%">
      <tr>
        <th>Field</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>End Point</td>
        <td>URL pointing to the external system</td>
      </tr>
      <tr>
        <td>Format</td>
        <td>Format of the payload to be sent to the End Point. Currently you can select:
          <ul>
            <li><code>ann.json</code> (<a href="/anndoc.html#ann-json">docs</a>). <code>application/json</code></li>
            <li><code>tagtogID</code> (simple json object like: <code>{"owner": "...", "project": "...", "tagtogID": "...document id related to the event..."}</code>). <code>application/json</code></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>Only GUI trigger</td>
        <td>Check it if you want only GUI changes to trigger the webhook. Leave it unchecked if you want that both, API and GUI changes, trigger the webhook.</td>
      </tr>
      <tr>
        <td>Authentication</td>
        <td><p><code>None</code> no authentication</p>
          <p><code>Basic</code> <a href="https://en.wikipedia.org/wiki/Basic_access_authentication">Basic access authentication</a></p>
          <p><code>NTLMv2</code> (Windows) <a href="https://en.wikipedia.org/wiki/NT_LAN_Manager#NTLMv2">NT LAN Manager v2</a></p></td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
    <div class="message">
      Webhooks can be used to <strong>train your own machine learning models</strong>. You can learn how in this <a href="https://medium.com/@tagtog/how-to-train-your-ai-models-with-tagtog-5a2beaa12eb">tutorial</a>.
    </div>
  </div>
  <div class="one-third-col">
    {% include image.html name="settings-webhook.PNG" %}
  </div>
  <div class="two-third-col">
    <h4>How to test webhooks locally?</h4>
    <p markdown="1">To easily expose your app externally, you can use [ngrok](https://ngrok.com). This tool forwards the incoming requests to your local app. If you are using our Cloud, this tool will make easier for tagtog.net to reach your app.</p>
    <h4>A full example</h4>
    <p markdown="1">In this step-by-step guide you will find a end-to-end example in Python about how to connect your models to tagtog using webhooks: [Connect your NLP models to tagtog using webhooks](https://tagtog.medium.com/connect-your-nlp-models-to-tagtog-using-webhooks-13d422ae4dff). Here you can find the GitHub repository: [demo-webhooks](https://github.com/tagtog/demo-webhooks)</p>
  </div>

</div>
<div class="page-subsection">
  <div class="two-third-col">
    <h3>Annotations</h3>
    <h4>Pre-selections</h4>
    <p markdown="1">Here you can decide the **default settings** for: [pre-selections, pre-deselections](webeditor.html#pre-selections), and their case sensitivity. You can always [change these settings on the web editor toolbar for a specific document](webeditor.html#pre-selections-1).</p>
  </div>

  <div class="two-third-col">
    <h4>Machine Learning (tagtog ML)</h4>
    <p>Each time you press the button {% include inline-image.html name="editor-confirm-button.PNG" width="80" %} in the annotation editor, <strong>a tagtog ML model gets trained in the background with all the confirmed project documents</strong>. Next time you upload a new document, this model will predict new annotations based on the training data. You can remove or add new annotations to continue training the model and get more accurate results.</p>
    <p>If activated, tagtog machine learning will start annotating automatically from the first document confirmed. <strong>No deployments or complex configurations are required</strong>, just by annotating you can train a use a tagtog machine learning model.</p>
    <p>If you don't want to use tagtog machine learning, deactivate this option.</p>
    <p>More information on how <a title="tagtog - machine learning" href="/machine-learning.html">tagtog ML</a> works.</p>
  </div>
  <div class="one-third-col">
    <div class="message">Automatic annotations with <strong>dictionaries</strong> will work with machine learning either activated or deactivated</div>
  </div>
  <div class="two-third-col">
    <h4>PDF</h4>
    <p>Check this option to annotate directly over the native PDF document. This web interface only works with PDF files. If this option is unchecked, only the plain text stripped from the PDF is annotatable.</p>
    <p>Take into consideration that if the PDF file is imported with the option unchecked, only the plain text version will be available for annotation. If you import the file with this option checked, both versions will be available: the native PDF annotation and the plain text annotation when the option is unchecked.</p>
    <p>Find more information of the PDF annotation tool <a title="tagtog - PDF annotation tool" href="/pdf-annotation-tool.html">here</a>.</p>
  </div>
  <div class="one-third-col">
    <div class="message">This feature is only available in some plans. Check the <a title="tagtog - plans" href="https://tagtog.net/-plans">available features for each plan</a>.</div>
  </div>
</div>

<div class="page-subsection">
  <div class="two-third-col">
    <h3>Members</h3>
    <p>In this panel, project admins (or a custom role with enough <a href="collaboration.html#permissions" title="tagtog - Permissions">permissions</a>) can invite and manage project members. All added project members will be able to collaborate in the same project-scoped annotation task. <a href="/collaboration.html">See for more info about roles and collaborative annotation</a>.</p>

    {% include image.html name="settings/members-b.png" width="80%" caption="Invite other users to collaborate in your project." %}
  </div>
  <div class="one-third-col">
    <p class="message" markdown="1">**Tip:** you can also manage your project members with the [members API](API_settings_v1.html#members-management).</p>
  </div>

  <div class="two-third-col">
  <h4>Add members & teams to your project</h4>

  <p>To <strong>add a new member</strong>: 1) simply write the tagtog username, or their email associated to their tagtog account, or any email address (for those who don't have an account in tagtog yet) in the input box, 2) choose the role, and 3) click on <kbd>Add Member</kbd>. Once added, those emails who don't have an account at tagtog yet, will receive a link to create an account and join the project. Already existing users will receive an email notification.</p>

  <p>To <strong>add a new <a href="on-premises-sysadmin.html#teams-management">team</a> (and its users/members)</strong>: just write the team's name in the input box, and add it. Everything works the same as when adding individual members.</p>
  </div>

  <div class="two-third-col">
  <h4>Update members & teams in your project</h4>

  <p>At any time, you can change the role of an individual member or of an entire team. To do so, just click on the member/team's role, and select in the shown dropdown the desired new role.</p>

  {% include image.html name="settings/members-update-b.png" width="80%" caption="You can change the roles of individual members and entire teams." %}

  <p>When you change the role of a team, you change the role of all its users. Additionally, if desired, you can change the role of the team users independently. This will allow you to set all the team's users to share some equal role (say <em>"curator"</em>), but a few of them, which might have different roles (say <em>"supercurator"</em>).</p>

  {% include image.html name="settings/members-update-team-b.png" width="60%" caption="You can also change the role of the team's users independently." %}

  </div>


  <div class="two-third-col">
  <h4>Delete members & teams from your project</h4>

  <p>To delete an existing project member (or project team) just click on its associated removal button <kbd>x</kbd>. You will be asked in a 2nd-step dialog to confirm that you do want to delete the project member.</p>

  <p>Important: <strong>the removal of project members/teams cannot be undone!</strong> Please make sure you have downloaded their annotations before, or that you have merged their annotations into the <code>master</code> version.</p>

  {% include image.html name="settings/members-delete.png" width="80%" caption="Delete existing project members." %}
  </div>


  <div class="two-third-col">
    <h4>Task distribution</h4>
    <p>With this feature, you can <strong>automatically distribute (assign) uploaded documents to selected project members</strong>. For example, if you choose 2 annotators, every uploaded document will be randomly assigned to 2 annotators; that is, every document will have to be annotated by at least 2 annotators. You can choose between different flows to annotate documents in your group. Find <a title="tagtog - Annotation flows" href="collaboration.html#annotation-flows">here</a> the options.</p>

    <p markdown="1">Annotating the same document by 2 or more members is recommended to increase the overall **quality of your annotation project**. Using it, tagtog compares the annotations from different annotators to calculate their level of agreement (<a title="tagtog - Inter-annotator agreement" href="collaboration#iaa-inter-annotator-agreement">inter-annotator agreement</a> or IAA) automatically, a good indicator of quality. For more information about quality management at tagtog, go <a title="tagtog - Quality Management" href="collaboration.html#quality-management">here</a>.</p>

    <br>

    {% include image.html name="settings/members-task-distribution.png" width="85%" caption="Task Distribution: assign documents to your labelers as soon they are uploaded." %}

    <p>To start task distribution, first you need to enable the feature. Then:</p>
    <p class="numbered-item"><span class="number-1">1</span><strong>Select the members you want to distribute documents to</strong> (the system only distributes documents to these users).</p>
    <p class="numbered-item"><span class="number-2">2</span><strong>Select the number of annotators per document</strong> (how many of the selected users will annotate each document).</p>
    <br>
    <p>To keep track of the project quality, even if you set the task distribution as one annotator per document (each document is assigned to a different annotator), tagtog automatically tries to allocate 5% of your documents to two annotators to calculate IAA.</p>
    <p><strong>By default, task distribution is turned off</strong>. This means that uploaded documents do not get distributed. When task distribution is not active, members see the <a href="collaboration.html#annotation-versions"><code>master</code> version</a> automatically when they open a document. Once the task distribution is active (number of annotators per document is 1 or more), members will see their own version of the annotations when they open a document.</p>
    <p><strong>When task distribution is active, project members see by default the special search <a href="search-queries.html#filter-todo"><code>filter:TODO</code></a></strong> (in the tab <em>Documents</em>). This view lists the documents that have not been confirmed yet by the logged annotator.</p>
  </div>
  <div class="one-third-col">
    <div class="message">
      <strong>Only new documents are distributed automatically</strong>. If you want to distribute existing documents, you should reimport them.
    </div>
    <div class="message">
      The number of annotators per document is limited to the number of users selected to annotate.
    </div>
    <div class="message">
      Using the <strong>API</strong> with the <a title="tagtog - API documents - Import" href="API_documents_v1.html#import-and-annotate-text">parameter <code>distributeToMembers</code></a>, you can override who exactly you want to distribute a specific document to.<br>
      Using the <strong>website</strong>, you can also override the Task Distribution settings <a href="documents.html#distribute-to-a-group-of-users">on the upload advanced menu</a>.
    </div>
  </div>
 </div>

 <div class="page-subsection">
  <div class="two-third-col">
    <h3>Requirements</h3>
    <p>Here you can set data requirements for your annotation tasks. These are enforced by tagtog to ensure your annotations comply with your data quality policies.</p>
    <p>Only users with the role <code>admin</code> can see/edit these project settings.</p>
    <p>There are different types of requirements available:</p>
    <h4>Required labels on file upload</h4>
    <p>You can <a title="Upload files with predefined document lables" href="documents.html#upload-files-with-predefined-document-labels">upload files with predefined document labels</a>. By default, no document label is selected. You can select one or more document labels if you want to ensure that always a file is uploaded using the GUI, these labels are defined.</p>

  </div>
  <div class="one-third-col">
    <div class="message">
      This is a new section. Soon we will add more requirement types to help you manage quality. Stay tuned!
    </div>
  </div>
</div>



<div class="page-subsection">
  <div class="two-third-col">
    <h3>Admin</h3>
    <p>Only users with the role <code>admin</code> can see/edit these project settings.</p>
    <h4>Export settings</h4>
    <p>Export the project's settings (entity types, relation types, entity labels, document labels, etc.) as a JSON file to reuse as a template on new projects.</p>
    <h4>Import settings</h4>
    <p>Import another project's settings. <strong>This will overwrite your current settings and remove all your project's documents</strong>. This should be applied solely on new projects.</p>
    <h4>Edit Project Description</h4>
    <p>You can change the description of your project at any moment. Just type the new description and click on Save.</p>
    <h4>Change Privacy Settings</h4>
    <p>Switch your <a title="tagtog - Public projects" href="projects.html#public-projects">public project</a> to <a title="tagtog - Private projects" href="projects.html#private-projects">private project</a> or the other way around.</p>
    <h4>Remove a project</h4>
    <p>To remove a project, go to its <i>Settings > Admin</i>. Click on the <code>Delete Project</code> button. Please notice that removing a project will remove all the documents within the project.</p>

  </div>
  <div class="one-third-col">
    {% include image.html name="DeleteProjectBtn.png" caption="Delete the project" %}
    <div class="message">
      You cannot remove projects for which you are not the <strong>admin</strong>.
    </div>
  </div>
</div>


<div class="two-third-col" markdown="1">

## Downloads

Your project has also a tab _"Downloads"_ to... download stuff 😉. Depending on your role in the project, and whether the project is public or private, you will see different actionable buttons.

In particular, with the button `Download All Documents (and their annotations)` you can **download as a Zip file** all your project's documents and their annotations (in [anndoc format](anndoc)). This button is available only to project admins in private projects. It is available to all logged-in users in public projects. Moreover, an analogous button `Download as Zip` is present in all document searches and folders (_"Documents"_ tab) to download as Zip the subset of documents that match the search.

In this section, you can also download a CSV file with the annotation status of your documents. This report lists in one column the document ids and in a second column the status of their `master` version (`true` if confirmed, `false` if not confirmed).

Other download actions are also available, including a reference to [download documents using the API](API_documents_v1), and [exporting the annotations legend](API_settings_v1.html#annotations-legend).

</div>
<div class="one-third-col">
{% include image.html name="projects/download-as-zip.png" caption="Download all project documents or a searched subset as Zip" %}
</div>

<div class="two-third-col" >
  <h2>Privacy</h2>
  <p>Projects in tagtog are either public or private. You can change your private project to public or your public project to private in the <a href="projects.html#admin" title="tagtog - Admin settings">Admin Settings</a> of your project.</p>
  <h3>Public projects</h3>
  <p>Public projects {% include inline-image.html name="globe.png" width="20" %} are <strong>open projects</strong>. Share your data with the entire world (Cloud) or across your organization (OnPremises). Give to your dataset <strong>transparency and visibility</strong>. It is also a good opportunity to attract other people to collaborate with you to build or maintain open datasets. In public projects: </p>
  <p class="list-item"><span class="list-item-1"></span>Anyone can see its documents and annotations (read-only).</p>
  <p class="list-item"><span class="list-item-2"></span>Only registered users can download documents or annotations using the UI or the <a href="API_documents_v1.html" title="tagtog - API docs">API</a>.</p>
  <p class="list-item"><span class="list-item-3"></span>Only the project members can make changes.</p>
  <h3>Private projects</h3>
  <p>In private projects {% include inline-image.html name="lock.png" width="20" %}, documents and annotations are kept private:</p>
  <p class="list-item"><span class="list-item-1"></span>Each private project is only visible to its members.</p>
  <p class="list-item"><span class="list-item-2"></span>Only project members can make changes.</p>


</div>
<div class="one-third-col">
  {% include message.html message="For <strong>OnPremises</strong> installations, only those users with accounts in the tagtog instance can see or download documents or annotations from public projects. Only the members of the project can perform changes." %}

  {% include message.html message='The default <strong>license</strong> for public projects is <a title="Creative Commons - Creative Commons: Attribution 4.0 International (CC BY 4.0)" href="https://creativecommons.org/licenses/by/4.0/">Creative Commons: Attribution 4.0 International (CC BY 4.0)</a>. You can always change it directly in the guidelines of your project.' %}
</div>
