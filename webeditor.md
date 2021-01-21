---
layout: page
title: Annotation editor
sidebar_link: true
id: webeditor
toc: true
---

<div class="page-section">
  <div class="two-third-col">
    <h2>Introduction</h2>
    <p>The core of tagtog the text annotation editor for data augmentation. This editor is designed to make the user feel comfortable annotating text. We have created a minimalist user interface to interfere as little as possible in the reading experience to increase annotator's focus and the efficiency during annotation tasks.</p>
    <p>The annotation editor is used to <strong>manually annotate text</strong> or/and <strong>train a machine learning model to automatically annotate text</strong>. By enabling automatic annotations you can build <a href="/#what-can-you-achieve">awesome stuff</a> you didn't think of at first.</p>
    <p>This web editor includes features as automatic annotations, <a href="https://medium.com/@tagtog/overlapping-text-annotations-19d7ac5b247a" title="Medium - Overlapping text annotations, gain flexibility">overlapping text annotations</a> or support for full-text articles, that reduce significantly the time required to annotate text.</p>

    {% include image.html name="editor-mainview-described.jpg" caption="tagtog annotation editor with text span annotations, entity labels, normalizations and document labels. The editor is mainly divided into: Document area, Folders, Toolbar and Sidebar. "%}
  </div>
  <div class="one-third-col">
    {% include image.html name="robot.ann.svg" width=300 %}
    <div class="message">
      The editor is part of a <strong>web app</strong>. You don't need anything than a web browser to use it. If you are using an <strong>on-premises</strong> version, contact the internal administrator of the application to understand how to access the app. If you are using the <strong>Cloud</strong> version, just go to <a href="https://tagtog.net">tagtog.net</a>.
    </div>
    <div class="message">
      By protecting the reading experience the tool is more accessible. This is specially important when you involve <strong>subject matter experts</strong> in your annotation projects.
    </div>
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Annotation types</h2>
    <p>You can annotate at text span level or at document level. Let's take a look to the type of annotations you can create using tagtog:</p>
    <table style="width:100%">
      <tr>
        <th>Annotation type</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>Entity</td>
        <td>Span of text representing a named entity. <strong>It can be any span</strong>: a part of a word, a word, a sentence or a group of words. Each entity belongs to one or more entity classes (e.g. Barack Obama is <code>person</code> and <code>politic</code>). Overlapped annotations are supported. <a href="#create-new-text-annotations">More</a>.</td>
      </tr>
      <tr>
        <td>Normalization</td>
        <td>Id assigned to a named entity. These annotations help in <strong>disambiguation</strong>. Normalization or canonicalization is the process for assigning an id or unique name to data that has more than one possible representation. This process is supported by <a href="/projects.html#dictionaries">dictionaries</a>. For example an <code>air filter</code> in automotive can make reference to a <code>cabin air filter</code> or an <code>engine air filter</code>. With tagtog you can assign the correct reference to the entity. Each entity can have assigned one or more Ids (e.g. Id from Wikipedia, and an Id from your internal database).</td>
      </tr>
      <tr>
        <td>Entity label</td>
        <td><p><strong>Label (<code>boolean</code>, <code>string</code>, <code>enum</code>) assigned to a named entity</strong>. Each entity can have assigned one or more labels.</p>
        <p>Let's say you are extracting technical issues from reports in a CRM. When annotating those reports, you can add extra information to those entities (technical issues), for example severity. You can use this metadata to build a statistical model that retrieves the severity given a particular technical issue in a specific context.</p></td>
      </tr>
      <tr>
        <td>Relation</td>
        <td><p>Relation <strong>between two named entities</strong>. Each relation belong to one specific relation type (e.g. BRCA2 <code>gene</code> is located <code>is_located</code> on the chromosome 13 <code>location</code>).</p>
        <p>Currently tagtog supports bidirectional relationships (A relates to B, and B relates to A) to connect two entities. If you want to connect more than two entities you need to create more than one relation.</p>
        <p>In order to set or see relations, remember you need first to define at least one Relation Type in <i>Settings > Relations</i>. Otherwise the option to See or Add relations in the menu will be disabled.</p>
        <p>Relations are supported between entities from different paragraphs or sections.</p></td>
      </tr>
      <tr>
        <td>Document label</td>
        <td><p>Label (<code>boolean</code>, <code>string</code>, <code>enum</code>) assigned to a document or text. One or more labels can be assigned to a document. These annotations help in <strong>text or intent classification</strong>.</p>
        <p>For example, if you are classifying emails in order to dispatch them to different departments, you can create a document label (enum) and classify emails as, for example, <code>sales</code>, <code>technical support</code> or <code>legal</code>. You can use the labeled data to train a text classifier model and classify emails automatically.</p></td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
    {% include message.html message="Text annotation in tagtog is <strong>flexible</strong>, tagtog supports the annotation of any text span: parts of words, words, sentences, etc. On the top of that you can create annotations overlapping text spans, or load pre-annotated data with these annotations." %}
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Hotkeys map</h2>
    <p>At the top-right corner of the editor, you find a <kbd>hotkeys</kbd> icon. If you hover the mouse on this icon, the list of hotkeys is displayed.</p>
    <table style="width:100%">
      <tr>
        <th>Hotkey</th>
        <th>Description</th>
        <th>Availability</th>
      </tr>
      <tr>
        <td class="centered"><kbd>[</kbd></td>
        <td>Previous document in the folder</td>
        <td>Any document</td>
      </tr>
      <tr>
        <td class="centered"><kbd>]</kbd></td>
        <td>Next document in the folder</td>
        <td>Any document</td>
      </tr>
      <tr>
        <td class="centered"><kbd>s</kbd></td>
        <td>Save document</td>
        <td>Any document</td>
      </tr>
      <tr>
        <td class="centered"><kbd>r</kbd></td>
        <td>Start Document Review</td>
        <td>Any document</td>
      </tr>
      <tr>
        <td class="centered"><kbd>t</kbd></td>
        <td>Start a new relation</td>
        <td>Any document. Only when the annotation menu is visible or in Document Review mode.</td>
      </tr>
      <tr>
        <td class="centered"><kbd>d</kbd></td>
        <td>Delete annotation </td>
        <td>Any document. Only when the annotation menu is visible or in Document Review mode.</td>
      </tr>
      <tr>
        <td class="centered"><kbd>l</kbd></td>
        <td>Show entity labels</td>
        <td>Any document. Only when the annotation menu is visible or in Document Review mode.</td>
      </tr>
      <tr>
        <td class="centered"><kbd>ctrl+c</kbd> or <kbd>command+c</kbd></td>
        <td>Copy annotation text</td>
        <td>Any document. Only when the annotation menu is visible or in Document Review mode.</td>
      </tr>
      <tr>
        <td class="centered"><kbd>q</kbd></td>
        <td>Previous page</td>
        <td>Only for paginated documents as PDFs</td>
      </tr>
      <tr>
        <td class="centered"><kbd>w</kbd></td>
        <td>Next page</td>
        <td>Only for paginated documents as PDFs</td>
      </tr>
      <tr>
        <td class="centered"><kbd>z</kbd></td>
        <td>Zoom in</td>
        <td>Only for paginated documents as PDFs</td>
      </tr>
      <tr>
        <td class="centered"><kbd>x</kbd></td>
        <td>Zoom out</td>
        <td>Only for paginated documents as PDFs</td>
      </tr>
      <tr>
        <td class="centered"><kbd>ctrl+f</kbd> or <kbd>command+f</kbd></td>
        <td>Search in the text of a document</td>
        <td>Only for paginated documents as PDFs</td>
      </tr>
      <tr>
        <td class="centered"><kbd>ctrl</kbd> or <kbd>command</kbd></td>
        <td>Annotate the whole paragraph. Hold the key and click on the paragraph to annotate it. </td>
        <td>Supported by all formats except for paginated documents.</td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Components</h2>
    <p>The editor is mainly divided into: <strong>Document area</strong>, <strong>Toolbar</strong> and <strong>Sidebar</strong>.</p>
  </div>
  <div class="one-third-col">

  </div>
  <div class="page-subsection">
    <div class="two-third-col">
      <h3>Document area</h3>
      <p>The text is displayed in the document area. There you can read and annotate text.</p>
      <h4>Text annotations</h4>
      <p>Once a piece of text is annotated, it becomes an entity. In tagtog you can operate with entities and do things as normalize them, relate them, etc.</p>
      <p>The background color of each annotation depends on the color picked for the Entity Type. The font color changes based on the background color so the contrast is appropriate to read.</p>
      <br/>
      {% include image.html name="editor-annotations.PNG" caption="In green the gene names, in red the mutations. Font color change depending on the entity background color" %}
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <h5>Create new text annotations</h5>
      <p>A new text annotation is created by <strong>highlighting text with the mouse</strong>. Position the cursor at the beginning of the text you want to highlight. Press and hold your primary mouse button (commonly the left-button). While holding the mouse button, drag the cursor to the end of the text and let go of the mouse button. Once completed, all the text from the beginning to the end should be highlighted using the same Entity Type used in the previous text annotation. Currently the only way to change the entity type used for new annotations is by first changing the entity type of existing annotation.</p>
      <p><strong>Tips & tricks</strong>:</p>
      <ul>
        <li>If you <strong>double-click</strong>, you annotate the word clicked.</li>
        <li>If you try to annotate a word that starts or ends in <i>space</i>, the <strong>space</strong> won't be annotated.</li>
        <li>Press and hold the <kbd>ctrl</kbd> or <kbd>command</kbd> key to <strong>annotate a whole paragraph</strong>. Simply hold the key and click on the paragraph to annotate it.</li>
      </ul>
    </div>
    <div class="one-third-col">
      {% include image.html name="annotate.paragraph.gif" caption="Annotating paragraphs with one click" %}
    </div>
    <div class="two-third-col">
      <h5>Overlapping text annotations</h5>
      <p>Just create a new annotation that is contained within the span of existing one or that only overlaps part of it. Overlapping text annotations are recognizable at a glance while not disturbing you from reading the text.</p>
      {% include image.html name="editor-contained-ann.PNG" caption="Example of contained annotation, the car make <code>Toyota</code> is contained in the model <code>Toyota Corolla</code>" %}
      {% include image.html name="editor-overlapped-ann.PNG" caption="Three entities annotated, two annotations are overlapping" %}
      {% include image.html name="editor-same-span-ann.png" caption="Sample of customer feedback. Two annotations (first in pink, second in yellow) within the same span representing a vehicle part and the failing part." %}
      <br>
    </div>
    <div class="one-third-col">
      {% include message.html message="You cannot annotate text starting in a paragraph and ending in a second paragraph." %}
      {% include message.html message='More on overlapping annotations in this <a href="https://medium.com/@tagtog/overlapping-text-annotations-19d7ac5b247a">blog post</a>.' %}
    </div>
    <div class="two-third-col">
      <h5>Pre-annotations</h5>
      <p>Automatic annotations created upon the manual creation or removal of other <strong>equal annotation</strong> (same entity type and same text). These type of annotations increase annotator's <strong>efficiency</strong> as potential candidates for new/to-remove annotations are automatically identified.</p>
      <p>Currently, pre-annotations don't work in the <a href="pdf-annotation-tool.html" title="tagtog - PDF annotation tool">PDF annotation tool</a>.</p>
      <table style="width:100%">
        <tr>
          <th>Pre-annotation type</th>
          <th>Description</th>
        </tr>
        <tr>
          <td>Pre-selection</td>
          <td><p>Equal entities that are annotated <strong>upon manual annotation</strong>. E.g. if you annotate <code>HER2</code> as Entity Type <code>Gene</code>, all occurrences of the string "HER2" will be annotated as Entity Type <code>Gene</code>. Pre-selections are visualized with a yellow border and the background color of the Entity Type. If you click on one of these pre-annotations, the pre-annotation will turn into a regular annotation.</p>
          {% include image.html name="editor-pre-selection2.PNG" width="250"%}
          <p>In addition, if you add/remove a normalization or entity label for this entity, this change will propagate to all pre-annotated occurrences.</p>
          </td>
        </tr>
        <tr>
          <td>Pre-deselection</td>
          <td><p>Equal entities that are removed <strong>upon manual removal</strong>, e.g. if you remove an existing annotation with the text "HER2" and Entity Type <code>Gene</code>, all annotations with the text "HER2" with the same Entity Type will be pre-deselected. Pre-deselections are visualized with a yellow border and white background color. If you click on one of these pre-deselections, the annotation will be removed.</p>
          {% include image.html name="editor-pre-deselection.PNG" width="250" %}</td>
        </tr>
      </table>
      <p>You can choose whether pre-annotations are <strong>case sensitive</strong> or not. As other properties from pre-annotations, this setting can be change both from the editor and/or at project level: <i>Settings > Annotations</i>.</p>
    </div>
    <div class="one-third-col">
      {% include message.html message="From the editor you can choose whether the pre-selections or pre-deselections are activated or deactivated. You can also change the <strong>default</strong> of these settings at project level in <i>Settings > Annotations</i>." %}
      {% include message.html message="You can turn on/off <strong>case sensitivity</strong> for pre-annotations" %}
    </div>
    <div class="two-third-col">
      <h5>Annotation Menu</h5>
      <p>By clicking on the primary mouse button (commonly the left-button) on a text annotation, you display the <strong>annotation menu</strong>.</p>
      <p>These are the actions you can perform:</p>
      <table style="width:100%">
        <tr>
          <th>Action</th>
          <th>Hotkey</th>
          <th>Available in read-only mode</th>
          <th>Description</th>
        </tr>
        <tr>
          <td>Delete</td>
          <td class="centered"><kbd>d</kbd></td>
          <td>No</td>
          <td>Delete annotation</td>
        </tr>
        <tr>
          <td>Labels</td>
          <td class="centered">-</td>
          <td>Yes, read-only</td>
          <td>Go to the entity labels menu</td>
        </tr>
        <tr>
          <td>Permalink</td>
          <td class="centered">-</td>
          <td>Yes</td>
          <td>Show a dialog box with a permalink for the annotation.</td>
        </tr>
        <tr>
          <td>Add relation</td>
          <td class="centered"><kbd>r</kbd></td>
          <td>No</td>
          <td><p>Start a relation if a Relation Type is defined for the Entity Type of this entity. Once the relation is initialized, you can see highlighted the annotations you can relate your entity to. Other annotations are faded to indicate that you cannot relate the entity to these.</p>
          <p>Click on one of the available entities to set the relation. From that moment, both entities will be connected. Both entities will display this icon on the top {% include inline-image.html name="relation-bidirectional-icon.PNG" width="20" %}.</p></td>
        </tr>
        <tr>
          <td>See relations</td>
          <td class="centered">-</td>
          <td>Yes</td>
          <td>See the relations this entity is part of.</td>
        </tr>
        <tr>
          <td>Change Type</td>
          <td class="centered">-</td>
          <td>No</td>
          <td><p>Change the Entity Type of entity. If you hover the mouse on this menu item, the list of possible Entity Types and their descriptions will show up. This list is sorted alphabetically. The first item is always selected by default and you can change to this entity type by clicking or pressing <kbd>↵</kbd>.</p>
          <p>You can filter the entity types by name or description. Just type in the searchbox and the entity types with matching description or name will be listed. The list is navigable by keyboard. Move with <kbd>↑</kbd> <kbd>↓</kbd> and select with <kbd>↵</kbd>.</p>
          <p>A change of entity type can affect the properties of the entity. Normalizations will be removed and only common entity labels will be preserved.</p></td>
        </tr>
        <tr>
          <td>Copy text</td>
          <td class="centered"><kbd>ctrl+c</kbd> or <kbd>command+c</kbd></td>
          <td>Yes</td>
          <td>Copy the text of the annotation to the clipboard.</td>
        </tr>
        <tr>
          <td>Normalizations</td>
          <td class="centered"><kbd>↵</kbd></td>
          <td>Yes, read-only</td>
          <td><p>Each <a href="/projects.html#dictionaries">dictionary</a> created for the entity type will appear as an input box. If the box is not empty, the entity is normalized to that value.</p>
          <p>If you type at least 3 characters, a list of recommended dictionary entries will appear. To select a normalization simply choose an entry. Otherwise you can type a new value. Each time you type or you select a value, the normalization is stored in the data model.</p>
          <p>Press the <kbd>+</kbd> button to add the value in the input box as a new entry for the dictionary. Instead of clicking the button, while you type a value, you can simple click the <kbd>↵</kbd>. If the entry is correctly added to the dictionary, a checkmark will show up during 1 second.</p></td>
        </tr>
      </table>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-menuann.PNG" %}
      <div class="message">
        You can <strong>remove relations</strong> in the Relation Tally in the Side bar. You cannot remove relations from the annotation menu.
      </div>
    </div>
  </div>
  <div class="two-third-col">
    <h5>Update dictionary from annotation editor</h5>
    <p>If you are using dictionaries, you can <strong>updated them upon manual normalization</strong>. If you add a new normalization and you click on the <kbd>+</kbd> button, this will either add a new entry to the dictionary or update an existing entry with a new term. By design, the dictionary won't be updated when a normalization is removed.</p>
    <p>You can always download the most updated version of a dictionary at <i>Settings > Dictionaries</i>.</p>
  </div>
  <div class="one-third-col">
    {% include message.html message="tagtog triggers automatically asynchronous calls to update dictionaries when a new normalization is added. You don't need to save the document to update a dictionary." %}
  </div>
  <div class="two-third-col">
    <h5>Permalinks</h5>
    <p>You can create permalinks for annotated entities. Just click on the entity and click the <code>Permalink</code> entry in the annotation menu. You can copy and share it. When opened, the link points exactly to the annotation, the document editor will scroll to highlight the annotation properly.</p>
  </div>
  <div class="one-third-col">
    {% include message.html message="A permalink looks like this example: <code>https://tagtog.net/demo/test/pool/a7Kiphm8zanJ9q-text?p=0&i=0&ann=s14v1|e_14|428,434</code>" %}
  </div>
  <div class="page-subsection">
    <div class="two-third-col">
      <h3>Toolbar</h3>
      <p>The toolbar is located on the top of the document area. From it you can perform these actions:</p>
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <h4>Original source {% include inline-image.html name="editor-original-source.PNG" width="18" %}</h4>
      <p>In case the document or text comes from a known provider, clicking this link you access the original source.</p>
      <p>For example, if you upload a PubMed document by PubMedId (PMID), tagtog understands the source. Clicking on this button you will go to the article in Pubmed.</p>
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <h4>Annotations from other users</h4>
      <p>Click on the user list to show all the project members. Click on the one you are interested, the version of the annotations for that user will be displayed on the document area.</p>
      <p>Depending on your permissions you are able to edit or not the different versions of the annotations. A locker icon {% include inline-image.html name="editor-member-locker.PNG" width="15" %} indicates that your permissions on that version are read-only.</p>
      <p>If you are a project admin, you will be able to see which of the members have already confirmed the document in the member list</p>
      <p><a href="/collaboration.html">More information on multi-user annotation</a></p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-members.PNG" width="150"%}
    </div>
    <div class="two-third-col">
      <h4>Manage annotation versions</h4>
      <p>You might want to start from the annotations of other user or replace the <code>master</code> version with the annotations of a specific user. If different users have annotated the same documents, tagtog also supports an <strong>automatic adjudication process</strong> to compose the final version of the annotations based on the agreement among users. For such cases, you can use the options available {% include inline-image.html name="editor-toolbar-import-ann.PNG" width="28" %} in the toolbar.</p>
      <p>If you click on that option, a list of actions shows up:</p>
      <table style="width:100%">
        <tr>
          <th>Action</th>
          <th>Description</th>
        </tr>
        <tr>
          <td>Copy to master</td>
          <td>Replace master's annotations version with the version displayed in the document area.</td>
        </tr>
        <tr>
          <td>Copy to mine</td>
          <td>Replace your annotations with the version displayed in the document area.</td>
        </tr>
        <tr>
          <td>Merge Annotations</td>
          <td>Automatic adjudication process that merges all the member's annotations into <code>master</code>. This adjudication is based on the <a title="tagtog - inter-annotator agreement" href="collaboration#iaa-inter-annotator-agreement">inter-annotator agreement</a> (IAA) and it is explained in detail here: <a title="tagtog - Automatic adjudication based on IAA" href="collaboration.html#automatic-adjudication-based-on-iaa">Automatic adjudication based on IAA</a>.</td>
        </tr>
      </table>
      <p>The availability of these options depends on the role permissions. <a href="/collaboration.html">More information on multi-user annotation</a></p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-copy-annotations.PNG" width="300" %}
    </div>
    <div class="two-third-col">
      <h4>Pre-annotations</h4>
      <p>Here you can select whether pre-selections or pre-deselections are activated or deactivated. You can also turn on/off case sensitivity.</p>
      <p>Each time you load a new document, the default settings from <i>Settings > Annotations</i> will apply. The changes in this menu won't change these default values and only will affect the current document. There are two types of pre-annotations: pre-selections and pre-deselections. You can find more information about pre-annotations <a href="#pre-annotations">here</a>.
    </p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-pre-annotations.PNG" width="300" %}
    </div>
    <div class="two-third-col">
      <h4>Save a document</h4>
      <p>Each time a change is made in the document (e.g. new annotation or relation added), the Save button will turn into green to indicate there are changes to save. Click the button {% include inline-image.html name="editor-save-button.png" width="50" %} to save the changes. </p>
    </div>
    <div class="one-third-col">
      <div class="message">The on-premises version has the possibility of <strong>auto-save</strong>. Each change is saved automatically upon action.</div>
    </div>
    <div class="two-third-col">
      <h4>Confirm a document</h4>
      <p>Usually users confirm the document once the <strong>annotations has been reviewed</strong>. This is used to indicate that this document can be used as training data for AI, or simply that all annotations has been reviewed by a human. There are different <a href="/collaboration.html#annotation-flows-task-distribution">annotation flows</a> you can use for your project.</p>
      <p>To confirm a document click on the button with the icon {% include inline-image.html name="editor-confirm-button.PNG" width="80" %}</p>
      <p>Once you have confirmed a document, many actions are disabled. You can undo the Confirm action by clicking again the button. It is a toggle button.</p>
    </div>
    <div class="one-third-col">
      <div class="message">If you have <code>Machine Learning</code> activated in Settings, each time you confirm a document, a <strong>model will be trained automatically</strong> in the background together with all the previously confirmed documents.</div>
    </div>
    <div class="two-third-col">
      <h4>View / output mode</h4>
      <p>Here you can select which way you want to display or <strong>export</strong> the annotated document.</p>
      <p>Annotated documents can be exported in various formats: <a href="/ioformats.html#output-formats">output formats</a></p>
      <p><code>tagtog Web Editor</code> refers to the visualization of the annotated document in the annotation editor.</p>
      <br/>
      <h4>Remove annotations</h4>
      <p>Click on the button with the icon {% include inline-image.html name="editor-doc-remove.PNG" width="20" %} and select the option <code>Remove annotations</code>to delete all the annotations in the current document. This won't remove the document.</p>
      <br/>
      <h4>Remove document</h4>
      <p>Click on the button with the icon {% include inline-image.html name="editor-doc-remove.PNG" width="20" %} and select the option <code>Remove document</code>to remove the document from the folder.</p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-view.PNG" width="250"%}
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Document navigator</h4>
      <p>Each button with an arrow pointing to left and right. If you click on the button with the left arrow, the previous document in the folder will be loaded. If you click on the button with the right arrow, the next document in the folder will be loaded.</p>
      <p>Under the document navigator, you can find the document index. This will give you an idea of where you are and how much work is left.</p>
    </div>
    <div class="one-third-col">
      <div class="message">
        There are hotkeys available: <kbd>[</kbd> for previous document, <kbd>]</kbd> for next document.
      </div>
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Page navigator</h4>
      <p>If the document is paginated, the toolbar has a controller to navigate across the pages. For example, in PDF documents. <a title="PDF annotation tool" href="pdf-annotation-tool.html#document-navigation">More information</a>.</p>
    </div>
    <div class="one-third-col">
    </div>
  </div>
  <div class="page-subsection">
    <div class="two-third-col">
      <br/>
      <h2>Sidebar</h2>
      <p>The sidebar <strong>appearance changes depending on how you configured your project</strong>. It will only display those actionable items for those entity types, entity labels, document labels or relations used in the project.</p>
      <p>You can <strong>show/hide</strong> the sidebar by clicking on the arrow {% include inline-image.html name="chevron.png" width="20" %} near the top of the sidebar.</p>
      <p>These are the components you can find in the sidebar:</p>
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Document labels</h4>
      <p>If you have any document label configured at <i>Settings > Document Labels</i> they will appear in this section in the side bar. Here the user can define the value of a document label for the current document. Once a change is made, you can save the document as usual.</p>
      <p>The list of document labels is <strong>sorted alphabetically</strong>.</p>
      <p>Clicking on the icon {% include inline-image.html name="editor-clean.PNG" width="20" %} you reset the label to the default value <code>?</code></p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-doc-label.PNG" width="300" %}
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Entity tally</h4>
      <p>The entity tally displays a summary for the entities annotated in your current document.</p>
      <p>On the top of this section you find some statistics with the number entities annotated and the entities not normalized. E.g. {% include inline-image.html name="editor-tally-headline.PNG" width="190"%}. Below the header, you can find a summary for the entities annotated in the current document. For example:</p>
      <br/>
      {% include image.html name="editor-tally-icons.png" width="600" caption="Entities are classified under Entity types. For each type some statistics are displayed: number of entities, manual annotated entities, automatic annotated entities, normalized entities" %}
      <br/>
      <p markdown="1">If you **click on an entity, the entity is highlighted in the text and the [Document Review](webeditor.html#document-review) starts** with this entity. If you click again on the entity, you get out the Document Review mode</p>
      <p>To quickly digest the status of the annotated entities, you can:</p>
      <p class="list-item"><span class="list-item-1"></span><strong>Group</strong> entities</p>
      <p class="list-item"><span class="list-item-2"></span><strong>Filter</strong> entities</p>
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <h5>Group entities</h5>
      <p>Classify entities in different groups.</p>
      <table style="width:100%">
        <tr>
          <th>Group by</th>
          <th>Description</th>
        </tr>
        <tr>
          <td><code>Normalization</code></td>
          <td><p>Group annotations by normalization. Very useful to understand which concepts are annotated in the current document. This option doesn't appear if you don't have dictionaries associated to your project.</p>
          <p>Entities not normalized are highlighted to spot them at a glance.</p>
          <p>Clicking on the icon {% include inline-image.html name="editor-tally-roll-down.PNG" width="20"%} you expand a view with the information of each single annotation.</p></td>
        </tr>
        <tr>
          <td><code>Text</code></td>
          <td>Group annotations by text. It is very common that in the same text, the same entity is repeated multiple times. Sometimes it is better to understand that only two unique entities have been identified in this text, e.g. gene <code>BRCA2</code> and gene <code>HER2</code> instead of getting the total number of annotations, included repeated ones.</td>
        </tr>
        <tr>
          <td><code>Entity label</code></td>
          <td>Group annotations by entity label. Check whether annotations have been labeled or not. Check the list of annotations labeled with a particular entity label.</td>
        </tr>
        <tr>
          <td><code>No group</code></td>
          <td>Entities are not grouped. They will appear one by one, in the same order they appear in the text. This is very handy if you need to review each single annotation. <span class="soon">Soon we will enable hotkeys so you can navigate this menu fast and easily</span>.</td>
        </tr>
      </table>
    </div>
    <div class="one-third-col">
      <div class="message">
        <strong>tagtog remembers your last grouping choice</strong>. If you select a specific way of grouping entities. The next time you open a new document or login to tagtog, the same grouping option will be selected by default.
      </div>
    </div>
    <div class="two-third-col">
      {% include image.html name="normalization_diagram.png" width="600" caption="Entities grouped by normalization. If you click on any of the annotations listed, the annotation will be highlighted in the text of the document area." %}
    </div>
    <div class="one-third-col">
      <div class="message">
        All menus in the entity tally are <strong>collapsible</strong>, if you click in an annotation, the document area <strong>scroll to highlight the annotation</strong> in the text.
      </div>
    </div>
    <div class="two-third-col">
      <h5>Filter entities</h5>
      <p markdown="1">You can **display entities that meet certain criteria**.</p>
      <p markdown="1">You decide whether you want to **apply the filter only to the entity tally or extend the scope to the document**. To control this functionality, there is an _Apply to document_ switch available:  {% include inline-image.html name="filter-scope.png" width="" %}</p>
      <p class="list-item" markdown="1"><span class="list-item-1"></span>**Off**: show the resulting entities only in the entity tally. Only those entities meeting the filter criteria are listed.</p>
      <p class="list-item" markdown="1"><span class="list-item-2"></span>**On**: show the resulting entities in the entity tally, and in the document. In the entity tally, only those entities meeting the filter criteria are listed. In the document, these entities are visible, the rest are hidden (visually almost transparent).</p>
       {% include image.html name="filter-scope-document.png" caption='Example of a filter applied to a document. Notice that the entities filtered out are hidden (visually almost transparent). In this example, the document is styled using <a href="tagtog-blocks.html#question-answering">tagtog blocks</a>.' %}
      <p>You can filter entities by the following properties:</p>
      <table style="width:100%">
        <tr>
          <th>Filter by</th>
          <th>Description</th>
        </tr>
        <tr>
          <td><code>Entity type</code></td>
          <td><p>Select one or more entity types to display entities that belong to one of those entity types.</p><p>This filter only shows up when there are two or more entity types defined in the project.</p>
          </td>
        </tr>
        <tr>
          <td><code>Entity text</code></td>
          <td><p>Display entities which text includes the search query.</p> <p>This filter only shows up when there is at least one entity type defined in the project.</p></td>
        </tr>
        <tr>
          <td><code>Entity label</code></td>
          <td><p>Select one or more entity labels to display only entities with all those labels.</p> <p>This filter only shows up when there is at least one entity label defined in the project.</p></td>
        </tr>
        <tr>
          <td><code>Entity label value</code></td>
          <td><p>Type the value of an entity label to only display those entities with at least one entity label with that value. As there can be a large number of entities, the match is exact.</p><p>As you type, a list of recommended values appears in a drop down menu. This list is generated using fuzzy search against the possible values of those entity labels with type <code>enum</code>.</p><p>This filter only shows up when there is at least one entity label defined in the project.</p></td>
        </tr>
         <tr>
          <td><code>Entity probability</code></td>
          <td>
            <p>All the entities with a probability lower than the value indicated in the range slider will be selected. The idea is that you can focus on the entities with low probability. This filter doesn't take into consideration the probability of other annotation tasks within the entity (e.g. entity labels, normalizations, relationships).</p>
            <p>This filter only shows up when there is at least one entity type defined in the project.</p>
          </td>
        </tr>
      </table>
      <p markdown="1">To **reset the filter** to the default values, there are two options:</p>
      <p class="list-item" markdown="1"><span class="list-item-1"></span>**Reset each filter property independently**: click on a {% include inline-image.html name="editor-clean.PNG" width="20" %} icon near the property.</p>
      <p class="list-item" markdown="1"><span class="list-item-2"></span>**Reset all filter properties**: if the filter is active, an option to reset the whole filter shows up on the top of the filter.</p>
    </div>
    <div class="one-third-col">
      <div class="message">
        To <strong>remove a filter</strong>, just click on the cross on the right side of the filter.
      </div>
      <div class="message">
        You can <strong>combine groups and filters</strong> to gain flexibility.
      </div>
      <div class="message">
        <strong>tagtog remembers whether you want to extend the filter scope to the document or not</strong>. If you turn on/off the switch, the next time you open a new document or login to tagtog, the same option will be selected by default.
      </div>
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Relation tally</h4>
      <p>It keeps the count of the relations defined in the current document. In this section you can <strong>remove</strong> existing relations, clicking on the button {% include inline-image.html name="editor-clean.PNG" width="20" %}.</p>
      <p>This tally only appears if you have relation types defined at <i>Settings > Relations</i>.</p>
    </div>
    <div class="one-third-col">
      <div class="message">
        If you click in a relation, the document area <strong>scroll to highlight the entities related</strong> in the text.
      </div>
      {% include image.html name="editor-relation-tally.PNG" width="230" %}
    </div>
  </div>
  <div class="page-subsection">
    <div class="two-third-col">
      <br/>
      <h2>Document Review</h2>
      <p>If you want to review a set of entities from your document, you can use the Document Review mode:</p>
      <p class="numbered-item"><span class="number-1">1</span><span markdown="1">Using the [filter](webeditor.html#filter-entities), select the entities you want to review. For example: review all the entities under 0.7 probability threshold.</span></p>
      <p class="numbered-item"><span class="number-2">2</span><span markdown="1">Press the [hotkey](webeditor.html#hotkeys-map) <kbd>r</kbd> to start the Document Review from the first entity. Alternatively, you can click on an entity in the Entity tally to start from that entity. Use <kbd>↑</kbd> and <kbd>↓</kbd> to navigate across the matching entities. For each entity, using hotkeys, you can perform the following actions:</span>
      <table style="width:100%">
        <tr>
          <th>Hotkey</th>
          <th>Description</th>
        </tr>
        <tr>
          <td class="centered"><kbd>d</kbd></td>
          <td>Delete entity</td>
        </tr>
        <tr>
          <td class="centered"><kbd>l</kbd></td>
          <td>Show/Edit entity labels</td>
        </tr>
        <tr>
          <td class="centered"><kbd>t</kbd></td>
          <td>Add relation</td>
        </tr>
        <tr>
          <td class="centered"><kbd>command+c</kbd> <kbd>ctrl+c</kbd></td>
          <td>Copy entity text</td>
        </tr>
      </table>
      </p>
      <p>Click on an entity in the text or press <kbd>ESC</kbd> to exit the Document Review mode.</p>
      <br/>
      {% include image.html name="documentReview.gif" caption="Document Review. In this example, we first filter the entities by text, and next, we review the resulting items performing some actions with the keyboard (change entity labels, creating a relationship, and removing the last entity)" %}
    </div>
    <div class="one-third-col">
      <div class="message">
        The Document Review <a href="webeditor.html#group-entities">ungroups</a> (<code>No Group</code>) the entities automatically to easily navigate across entities ordered by their position in the document.
      </div>
    </div>
  </div>
  <div class="page-subsection">
    <div class="two-third-col">
      <br/>
      <h2>Folders</h2>
      <p>Folders can be accessed from the document pool or the web editor. You can find the folders panel of the left side of the editor. <a title="Folders - tagtog.net" href="documents.html#folders">More information about folders</a>.</p>
    </div>
    <div class="one-third-col">
    </div>
  </div>
</div>
