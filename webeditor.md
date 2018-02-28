---
layout: page
title: Annotation editor
sidebar_link: true
---

<div class="page-section">
  <div class="two-third-col">
    <h2>Introduction</h2>
    <p>The core of tagtog the text annotation editor for data augmentation. This editor is designed to make the user feel comfortable annotating text. We have created a minimalistic user interface to interfere as less as possible in the reading experience to increase annotator focus and the efficiency during annotation tasks.</p>
    <p>The annotation editor is used to <strong>manually annotate text</strong> or/and <strong>train a machine learning model to automatically annotate text</strong>.</p>
    <p>This web editor includes features as automatic annotations, overlapping text annotations or full-text annotation, that reduce significantly the time required to annotate text.</p>

    {% include image.html name="editor-mainview.PNG" caption="tagtog annotation editor"%}
  </div>
  <div class="one-third-col">
    <div class="message">
      The editor is part of a <strong>web app</strong>. You don't need anything else than a web browser to use it. If you are using an <strong>on-premises</strong> version, contact the internal administrator of the application to understand how to access the app. If you are using the <strong>Cloud</strong> version, just go to <a href="https://tagtog.net">tagtog.net</a>.
    </div>
    <div class="message">
      By protecting the reading experience the tool is more accesible. This is specially important when you involve <strong>subject matter experts</strong> in your annotation projects.
    </div>
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Type of annotations</h2>
    <p>You can annotate at text span level or at document level. Let's take a look to the type of annotaitons you can create using tagtog:</p>
    <table style="width:100%">
      <tr>
        <th>Annotation type</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>Entity</td>
        <td>Span of text representing a named entity. It can be any span: a part of a word, a word, a sentence or a group of words. Each entity belongs to one or more entity classes (e.g. Barack Obama is <code>person</code> and <code>politic</code>).</td>
      </tr>
      <tr>
        <td>Normalization</td>
        <td>Id assigned to a named entity. These annotations help in <strong>disambiguation</strong>. Normalization or canonicalization is the process for assigning an id or unique name to data that has more than one possible representation. For example an <code>air filter</code> in automotive can make reference to a <code>cabin air filter</code> or a <code>engine air filter</code>. With tagtog you can assign the correct reference to the entity. Each entity can have assigned one or more Ids (e.g. Id from Wikipedia, and an Id from your internal database).</td>
      </tr>
      <tr>
        <td>Entity label</td>
        <td><p>Label (boolean, string, enum) assigned to a named entity. Each entity can have assigned one or more labels.</p>
        <p>Let's say you are extracting technical issues from reports in a CRM. When annotating those reports, you can add extra information to those entities (technical issues), for example severity. You can use this metadata to build a statistical model that retrieves the severity given a particular technical issue in a specific context.</p></td>
      </tr>
      <tr>
        <td>Relation</td>
        <td><p>Relation between two named entities. Each relation belong to one specific relation type (e.g. BRCA2 <code>gene</code> is located <code>is_located</code> on the chromosome 13 <code>location</code>).</p>
        <p>Currently tagtog supports bidirectional relationships (A relates to B, and B relates to A) to connect two entities. If you want to connect more than two entities you need to create more than one relation.</p>
        <p>In order to set or see relations, remember you need first to define at least one Relation Type in <i>Settings - Relations</i>. Otherwise the option to See or Add relations in the menu will be disabled.</p></td>
      </tr>
      <tr>
        <td>Document label</td>
        <td><p>Label (boolean, string, enum) assigned to a document or text. One or more labels can be assigned to a document. These annotations help in <strong>text or intent classification</strong>.</p>
        <p>For example, if you are classifying emails in order to dispatch them to different departments, you can create a document label (enum) and classify emails as, for example, <code>sales</code>, <code>technical support</code> or <code>legal</code>. You can use the labeled data to train a text classifier model and classify emails automatically.</p></td>
      </tr>
    </table> 
  </div>
  <div class="one-third-col">
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Hotkeys map</h2>
    <p>If you hover the mouse on the icon <kbd>hotkeys</kbd> the list of hotkeys is displayed.</p>
    <table style="width:100%">
      <tr>
        <th>Hotkey</th>
        <th>Description</th>
      </tr>
      <tr>
        <td class="centered"><kbd>[</kbd></td>
        <td>Previous document in the pool</td>
      </tr>
      <tr>
        <td class="centered"><kbd>]</kbd></td>
        <td>Next document in the pool</td>
      </tr>
      <tr>
        <td class="centered"><kbd>s</kbd></td>
        <td>Save document</td>
      </tr>
      <tr>
        <td class="centered"><kbd>r</kbd></td>
        <td>Start relation (only available when the annotation menu is visible)</td>
      </tr>
      <tr>
        <td class="centered"><kbd>d</kbd></td>
        <td>Delete annotation (only available when the annotation menu is visible)</td>
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
      <p>Each annotation is highlighted with a color. The color depends on each Entity Type. The font color adapts to the highlight color so it is easier to read.</p>
      {% include image.html name="editor-annotations.PNG" caption="In green the gene names, in red the mutations" %}
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <h5>Create new text annotations</h5>
      <p>A new text annotation is done by highlighting text. Position your cursor at the beginning of the text you want to highlight. Press and hold your primary mouse button (commonly the left-button). While holding the mouse button, drag the cursor to the end of the text and let go of the mouse button. Once completed, all text from the beginning to the end should be highlighted using the same Entity Type used in the previous text annotation.</p>
      <p>If you <strong>double-click</strong> you will annotate the word you clicked.</p>
      <p>If you try to annotate a word that starts or ends in <i>space</i>, the space won't be annotated.</p>
    </div>
    <div class="one-third-col">
      <div class="message">
        The maximum length of a text annotation is <code>180</code> characters.
      </div>
    </div>
    <div class="two-third-col">
      <h5>Overlapped text annotations</h5>
      <p>Just create a new annotation that is contained within the span of existing one or that only overlaps part of it. Overlapped annotations will be still recognizable while not disturbing you from reading the text.</p>
      {% include image.html name="editor-contained-ann.PNG" caption="Example of contained annotation, <code>arginine 551</code> is contained in <code>arginine 551 to lysine</code>" %}
      {% include image.html name="editor-overlapped-ann.PNG" caption="Example of overlapped annotation, <code>mutation of CARM1's</code> overlaps with <code>CARM1's automethylation</code>" %}
    </div>
    <div class="one-third-col">
      <div class="message">
        You cannot annotate text starting in a paragraph and ending in a second paragraph.
      </div>
      <div class="message">
        More on overlapping annotations in this <a href="https://medium.com/@tagtog/overlapping-text-annotations-19d7ac5b247a">blog post</a>.
      </div>
    </div>
    <div class="two-third-col">
      <h5>Pre-annotations</h5>
      <p>Pre-annotations are automatic annotations created upon the creation or removal of other equal annotation. These annotations are created while annotating and make easier annotator's life as potential candidates for new/to-remove annotations are identified.</p>
      <table style="width:100%">
        <tr>
          <th>Pre-annotation type</th>
          <th>Description</th>
        </tr>
        <tr>
          <td>Pre-selection</td>
          <td>Equal entities that are annotated upon manual annotation. E.g. if you annotate <code>HER2</code> as Entity Type "Gene", all occurrences of the string "HER2" will be annotated as Entity Type <code>Gene</code>. Pre-selections are visualized with a yellow border and the background color of the Entity Type. If you click on one of these pre-annotations, the pre-annotation will turn into a regular annotation.
          {% include image.html name="editor-pre-selection2.PNG" width="250"%}</td>
        </tr>
        <tr>
          <td>Pre-deselection</td>
          <td>Equal entities that are removed upon manual removal, e.g. if you remove an existing annotation with the text "HER2" and Entity Type <code>Gene</code>, all annotations with the text "HER2" with the same Entity Type will be pre-deselected. Pre-deselections are visualized with a yellow border and white background color. If you click on one of these pre-deselections, the annotation will be removed.
          {% include image.html name="editor-pre-deselection.PNG" width="250" %}</td>
        </tr>
      </table>
    </div>
    <div class="one-third-col">
      <div class="message">
        From the editor you can choose if the pre-selections or pre-deselections are activated or deactivated. You can also change the default of these settings at project level in <i>Project - Settings</i>.
      </div>
    </div>
    <div class="two-third-col">
      <h5>Annotation Menu</h5>
      <p>By clicking on the primary mouse button (commonly the left-button) on a text annotation, you display the <strong>annotation menu</strong>.</p>
      <p>These are the actions you can perform:</p>
      <table style="width:100%">
        <tr>
          <th>Action</th>
          <th>Hotkey</th>
          <th>Description</th>
        </tr>
        <tr>
          <td>Delete</td>
          <td class="centered"><kbd>d</kbd></td>
          <td>Delete annotation</td>
        </tr>
        <tr>
          <td>Add relation</td>
          <td class="centered"><kbd>r</kbd></td>
          <td><p>Start a relation if a Relation Type is defined for the Entity Type of this entity. Once the relation is initializated, you can see highlighted the annotations you can relate your entity. Other annotations are faded to indicate that you cannot relate the entity to these.</p>
          <p>Click on one of the available entities to set the relation. From that moment, both entities will be connected. Both entities will this icon on the top {% include inline-image.html name="relation-bidirectional-icon.png" width="20" %}</p></td>
        </tr>
        <tr>
          <td>See relations</td>
          <td class="centered">-</td>
          <td>See the relations this entity is part of.</td>
        </tr>
        <tr>
          <td>Change Type</td>
          <td class="centered">-</td>
          <td>Change the Entity Type of an entity. If you hover the mouse, the list of possible Entity Classes will show up.</td>
        </tr>
        <tr>
          <td>Normalizations</td>
          <td class="centered"><kbd>↵</kbd></td>
          <td><p>Each dictionary created for the entity type will appear as an input box. If the box is not empty, the entity is normalized to that value.</p>
          <p>If you type at least <code>3</code> characters a list of recommended dictionary entries will appear. To select a normalization simply choose an entry and press the <kbd>↵</kbd> key or click the ↵ icon.</p></td>
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
  <div class="page-subsection">
    <div class="two-third-col">
      <h3>Toolbar</h3>
      <p>The toolbar is located on the top of the document area. From it you can perform these actions:</p>
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <h4>Original source {% include inline-image.html name="editor-original-source.PNG" width="18" %}</h4>
      <p>In case the document or text comes from a known provider, clicking this link you access to the original source.</p>
      <p>For example, if you upload a PubMed document by PubMedId, tagtog understands the source. Clicking on this button you will go to the paper in Pubmed.</p>
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <h4>Annotations from other users</h4>
      <p>Click on the user list to show all the project members. Click on the one you are interested and the document annotated by that user will be displayed in the document area.</p>
      <p>Depending on your permissions you are able to edit or not the different versions of the annotations. A locker icon {% include inline-image.html name="editor-member-locker.png" width="15" %} indicates that your permissions on that version are read-only.</p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-members.PNG" width="150"%}
    </div>
    <div class="two-third-col">
      <h4>Import annotations from other versions</h4>
      <p>You may want to start from the annotations of other user or import your annotations to the <code>master</code> version. For such cases, you can use the import option {% include inline-image.html name="editor-toolbar-import-ann.PNG" width="28" %} in the toolbar.</p>
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
      </table>      
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-copy-annotations.png" width="300" %}
    </div>
    <div class="two-third-col">
      <h4>Pre-annotations</h4>
      <p>Here you can select if pre-selections or pre-deselections are activated or deactivated.</p>
      <p>Each time you load a new document, the default settings from <i>Settings-Annotations</i> will apply. The changes in this menu won't change these default values and only will affect the current document. There are two options: pre-selections and pre-deselections. You can find more information about pre-annotations HHHHERE.
    </p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-pre-annotations.png" width="300" %}
    </div>
    <div class="two-third-col">
      <h4>Save a document</h4>
      <p>Each time a change is made in the document (e.g. new annotation or relation added), the Save button will turn into green to indicate there are changes to save. Click the button {% include inline-image.html name="editor-save-button.png" width="50" %} to save the changes. </p>
    </div>
    <div class="one-third-col">
      <div class="message">The on-premises version has the possibility of <strong>auto-save</strong>. Each change is saved automatically upon the action.</div>
    </div>
    <div class="two-third-col">
      <h4>Confirm a document</h4>
      <p>Usually annotators confirm the document once the <strong>annotations has been reviewed</strong>. This is used to indicate that this document can be used as training data for AI or that all annotations has been reviewed by a human. </p>
      <p>To confirm a document click on the button with the icon {% include inline-image.html name="editor-confirm-button.PNG" width="80" %}</p>
      <p>Once you have confirmed a document, many actions are disabled. You can undo the confirm action by clicking again the button. It is a toggle button.</p>
    </div>
    <div class="one-third-col">
      <div class="message">If you have <code>Machine Learning</code> activated in Settings, each time you confirm a document, a <strong>model will be trained automatically</strong> in the background together with all the previously confirmed documents.</div>
    </div>
    <div class="two-third-col">
      <h4>View / output mode</h4>
      <p>Here you can select which way you want to display or export the annotated document.</p>
      <p>Annotated documents can be exported in various formats: <a href="">output formats</a></p>
      <p><code>tagtog Web Editor</code> refers to the visualizatoin of the annotated document in the annotation editor.</p>
      <br/>
      <h4>Clear annotations</h4>
      <p>Click on the button with the icon {% include inline-image.html name="editor-clean.PNG" width="20" %} to remove all the annotations in the current document. This won't remove the document. </p>
      <br/>
      <h4>Remove document</h4>
      <p>Click on the button with the icon {% include inline-image.html name="editor-doc-remove.PNG" width="20" %} to remove the document from the document pool.</p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-view.PNG" width="250"%}
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Document navigator</h4>
      <p>These are two buttons, each with an arrow pointing to left and right. If you click on the button with the left arrow, the previous document in the pool will be loaded. If you click on the button with the right arrow, the next document in the pool will be loaded.</p>
    </div>
    <div class="one-third-col">
      <div class="message">
        There are hotkeys available: <kbd>[</kbd> for previous document, <kbd>]</kbd> for next document.
      </div>
    </div>
  </div>
  <div class="page-subsection">
    <div class="two-third-col">
      <br/>
      <h2>Sidebar</h2>
      <p>The way the sidebar is displayed changes depending on how you configured your project. These are the components you can find: </p>
    </div>
    <div class="one-third-col">
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Document labels</h4>
      <p>If you have any document label configured at _Settings-Document Labels_ they will appear in this section in the side bar. Here the user can define the value of a document label for the current document. Once a change is made, you can save the document as usual.</p>
      <p>Clicking on the icon {% include inline-image.html name="editor-clean.PNG" width="20" %} you reset the label to the default value <code>?</code></p>
    </div>
    <div class="one-third-col">
      {% include image.html name="editor-doc-label.PNG" width="300" %}
    </div>
    <div class="two-third-col">
      <br/>
      <h4>Entity tally</h4>
      <p>The entity tally displays statistics for each entity type in the current document.</p>
      <p>On the top of this section you find a summary with the number entities annotated and the entities not normalized. E.g. {% include inline-image.html name="editor-tally-headline.PNG" width="190"%}</p>
      <br/>
      {% include image.html name="editor-tally-icons.png" width="600" caption="Entities are classified under Entity types. For each type some statistics are displayed: number of entities, manual annotated entities, automatic annotated entities, normalized entities" %}
      <br/>
      <p>To digest the status of the annotated entities as fast as possible and to reduce the noise of repeated annotations, you can group entities by:</p>
      <table style="width:100%">
        <tr>
          <th>Group by</th>
          <th>Description</th>
        </tr>
        <tr>
          <td>Normalization <code>default</code></td>
          <td><p>Group annotations by normalization. Very useful to understand which concepts are annotated in the current document.</p>
          <p>Entities not normalized are highlighted to spot them at a glance.</p>
          <p>Clicking on the icon {% include inline-image.html name="editor-tally-roll-down.PNG" width="20"%} you expand a view with each single annotation.</p></td>
        </tr>
        <tr>
          <td>Text</td>
          <td>Group annotations by text. It is very common that in the same text, the same entity is repeated multiple times. Sometimes it is better to understand that only two unique entities have been identified in this text, e.g. gene <code>BRCA2</code> and gene <code>HER2</code> insted of getting the total number of annotations, included repeated ones.</td>
        </tr>
        <tr>
          <td>No group</td>
          <td>Entities are not grouped. They will appear one by one in the same order they appear in text. This is very handy if you need to review each single annotation. <span class="soon">Soon we will enable hotkeys so you can navigate this menu fast and easily</span>.</td>
        </tr> 
      </table>
    </div>
    <div class="one-third-col">
      <div class="message">
        <strong>What is an unique entity?</strong> a group of entity with the same Entity Type and text.
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
      <br/>
      <h4>Relation tally</h4>
      <p>It keeps the count of the relations defined in the current document. In this section you can <strong>remove</strong> existing relations, clicking on the button {% include inline-image.html name="editor-clean.PNG" width="20" %}</p>
      <p>This tally only appears if you have relation types defined at <i>Settings-Relations</i>.</p>
    </div>
    <div class="one-third-col">
      <div class="message">
        If you click in a relation, the document area <strong>scroll to highlight the entities related</strong> in the text.
      </div>
      {% include image.html name="editor-relation-tally.PNG" width="230" %}
    </div>
  </div>
</div>
