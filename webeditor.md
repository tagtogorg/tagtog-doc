[< Back](../tagtog-doc)


# Web editor

* TOC
{:toc}


The web editor is designed to annotate text while making comfortable to read it, thus improving the annotation task efficiency. It is used to manually **annotate text** or train a machine to automatically annotate text. If you train a machine to annotate text, you eventually are **identifying relevant information in text**.

This is a **web app**, so you don't need anything else than a web browser to use it. If you are using an **on-premises** version, contact the internal administrator of the application to understand how to access the app. If you are using the **Cloud** version, just go to [https://tagtog.net](https://tagtog.net).

![tagtog web editor](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-mainview.PNG)

The _web editor view_ is mainly divided into:

* Document area
* Toolbar
* Sidebar

## Document area

The text is displayed in the document area. There you can read and annotate.

### Text annotations

Once a piece of text is annotated, it becomes an entity. In tagtog you can operate with entities and do things as normalize them, relate them, etc.

Each annotation is highlighted with a color. The color depends on each Entity Type. The font color adapts to the highlight color so it is easier to read. In the example below, in green the gene names, in red the mutations.

![Editor - text annotations](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/editor-annotations.PNG)

#### Create new text annotations

A new text annotation is done by highlighting text. Position your cursor at the beginning of the text you want to highlight. Press and hold your primary mouse button (commonly the left-button). While holding the mouse button, drag the cursor to the end of the text and let go of the mouse button. Once completed, all text from the beginning to the end should be highlighted using the same Entity Type used in the previous text annotation. 

If you **double-click** you will annotate the word you clicked.

If you try to annotate a word that starts or ends in _space_, the space won't be annotated.

You can create **overlapped annotations**. Just create a new annotation that is contained within an existing one or that only overlaps part of it. Overlapped annotations will be still recognizable while not disturbing you from reading the text.

Below an example of contained annotation, `arginine 551` is contained in `arginine 551 to lysine`.

![editor - contained annotation](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-contained-ann.PNG)

Below an example of overlapped annotation, `mutation of CARM1's` overlaps with `CARM1's automethylation`.

![editor - overlapped annotation](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-overlapped-ann.PNG)

You cannot annotate text starting in a paragraph and ending in a second paragraph.

> The maximum length of a text annotation is `180` characters.

##### Pre-annotations

Annotations that are created automatically upon adding/removing an annotation. Those only works if the pre-select or pre-deselect options are enabled in the toolbar.

* **Pre-select**: check it if you want that all equal entities are annotated upon manual annotation, e.g. if you annotate "HER2" as Entity Type "Gene", all occurrences of the string "HER2" will be annotated as Entity Type "Gene". Pre-selections are visualized with a fluorescent border and the background color of the Entity Type. If you click on one of these pre-annotations, the pre-annotation will turn into a regular annotation. 

***

![editor - pre-selection](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-pre-selection2.PNG)

***

* **Pre-deselect**: check it if you want to remove all equal entities upon manual removal (it only operates on confirmed entities, not pre-selected), e.g. if you remove an existing annotation with the text "HER2" and Entity Type "Gene", all annotations with the text "HER2" with the same Entity Type will be pre-deselected. Pre-deselections are visualized with a fluorescent border and white background color. If you click on one of these pre-deselections, the annotation will be removed.

***

![editor - pre-deselection](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-pre-deselection.PNG)

***

#### Annotation menu
By clicking on the primary mouse button (commonly the left-button) on a text annotation, you display the **annotation menu**. 

![Editor - annotation menu](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-menuann.PNG)

From here you can:

* **Delete** (hotkey: `d`): delete annotation.
* **Add relation** (hotkey: `r`): start a relation if a Relation Type is defined for the Entity Type of this entity.
* **See relations**: see the relations this entity is part of.
* **Change Type**: change the Entity Type of an entity. If you hover the mouse, the list of possible Entity Classes will show up.
* **Normalizations**: at the bottom of the annotation menu you can see the normalizations.

#### Relations

Currently tagtog supports bidirectional relationships (A relates to B, and B relates to A) to connect only two entities. If you want to connect more than two entities you need to create more than one relation.

In order to set or see relations, remember you need first to define at least one Relation Type in _Settings - Relations_. Otherwise the option to See or Add relations in the menu will be disabled.

##### Add a new relation

You can start a relation using the annotation menu (option `Add Relation`). The relation will start in this annotation. After clicking this option, only will be visible the annotations with an Entity Type that can held a relation with the Entity Type of the first annotation. Rest will be faded. Click on one of the available entities to set the relation. From that moment, both entities will be connected. Both entities will have an icon with two arrows ![Icon for relations](https://github.com/tagtog/tagtog-doc/raw/master/resources/relation-bidirectional-icon.PNG)

##### See Relations

Once an entity is part of one or more relations, you can see these by clicking this option in the annotation menu (option `See Relations`)

##### Remove Relation

You can remove relations in the Relation Tally in the Side bar. You cannot remove relations from the annotation menu.

#### Normalizations

Each dictionary you have defined at _Settings-Dictionaries_ allows you to normalize entities. For more information check the documentation about [normalizations](Projects-documentation#dictionaries) at Project Settings. You can see the normalizations of each entity opening its annotation menu, bottom. 

Each dictionary associated to the Entity Type of the entity will display a text box. If the text box is not empty, the entity is normalized to that value. Otherwise, the entity is not normalized.

You can always change the normalization of an entity if there is an existing dictionary for the related Entity Type. Just click on the text box and start typing, after the three first characters a list of possible normalizations will show up in case there are any. When you click on any of them, just click on ↵ or just pressing `Enter`.

In case you want to remove a normalization, just remove any character in the normalization text box and click on ↵ or just press `Enter`

## Toolbar

### Original source

In case the document or text comes from a known provider, clicking this link you access to the original source. 

For example, if you upload a PubMed document by PubMedId, tagtog understands the source. Clicking on this button you will go to this paper in Pubmed.

### Annotations from other users

In tagtog you can collaborate with other users to annotate faster or improve the quality of annotations. Each user has a version of the annotations for a single document, e.g. _UserA _can have 20 annotations, _UserB_ can have 5 different annotations on the same exact document. In addition to these versions, each document has a `master `version which is usually treated as the final/official version.

#### See annotations from other users.

Click on the user list to show all the users. Click on the one you are interested and the annotations done by that user will show up in the document area.

Depending on your permissions you are able to edit or not the different versions of the annotations. A locker icon on the right side of the username indicates that your permissions on that version are read-only.

![Editor - members](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-members.PNG)

#### Import annotations from other versions

You may want to start from the annotations of other user or import your annotations to `master`. You can use the import option in the toolbar: ![Editor - import annotations](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/editor-toolbar-import-ann.PNG)

If you click on that option, a list of actions shows up:

* **Copy to master**: replace master's annotation with the annotations displayed. 
* **Copy to mine**: replace your annotations with the annotations being displayed.

![Editor - Copy annotations](https://github.com/tagtog/tagtog-doc/blob/master/resources/editor-copy-annotations.PNG?raw=true)

### Pre-annotations

The defaults in this menu will follow the settings in _Settings-Annotations_. The changes in this menu won't change these defaults and only will affect the current document. There are two options: pre-selections and pre-deselections. You can find more information about pre-annotations [here](Web-editor#pre-annotations).

### Save

Each time a change is made in the document (e.g. new annotation or relation added), the Save button will turn green to indicate there are changes to save. Click the button ![Editor - Save document](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-save-button.PNG) to save the changes. 

If you accidentally leave the page without saving the changes you will be prompted with a message so you can confirm.

### Confirm

Usually users confirm the document one the annotations has been reviewed. This is sometimes used to indicate that this document can be used as training data for AI or that all annotations has been reviewed by a human.

To confirm a document click on the button with the icon ![Editor - Confirm document](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-confirm-button.PNG)

Once you have confirmed a document, many of the actions cannot be done anymore. You can undo the confirm action by clicking again in the button. This is a toggle button.

### View / output mode

![Editor - View/output](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-view.PNG)

The visualization in the web editor is just one of many tagtog supports. Additionally, you can display the document in the following formats:

* **ann.json**: more information in the [https://github.com/tagtog/tagtog-doc/wiki/ann.json](official doc for this format)
* **TSV**: more information in the [https://www.tagtog.net/-doc/formats/outFullTsv_v0_2](official doc for this format)
* **PubAnnotation**: more information in the [http://www.pubannotation.org/docs/annotation-format/](official doc for this format)
* **BioC**: more information in the [http://bioc.sourceforge.net/](official doc for this format)
* **docJSON**: only available for some users. Documentation not available.
* **html**: you can see the document in HTML. No annotations provided within this format.
* **text**: you can see the document in plain text. No annotations provided within this format.

### Clear annotations

Click on the button with the icon ![Editor - Clean annotations](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-clean.PNG) to remove all the annotations in the current document. This won't remove the document. 

### Remove documents

Click on the button with the icon ![Editor - Remove document](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-doc-remove.PNG) to remove the current document from the document pool.

### Pool navigator

These are two buttons, each with an arrow pointing to left and right. If you click on the button with the left arrow, the previous document in the pool will be loaded. If you click on the button with the right arrow, the next document in the pool will be loaded.

### Hotkeys map

If you hover the mouse on the icon with the text `hotkeys` the list of hotkeys is displayed.

* `[` : previous document in the pool
* `]` : next document in the pool
* `s` : save document
* `r` : start relation (only available when the annotation menu is visible)
* `d` : delete annotation (only available when the annotation menu is visible)

## Side bar
The side bar is placed on the right side of the screen and it is mainly used to display statistics of the current document.

### Document labels
If you have any document label configured at _Settings-Document Labels_ you will find this section in the side bar. Here the user can define the document label for the current document. Once a change is made, you can save the document as usual.

![Editor - document labels](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-doc-label.PNG)

### Entity tally

![editor - entity tally](https://github.com/tagtog/tagtog-doc/raw/master/resources/editor-entity-tally.PNG)

It keeps the count of the entities you are annotating in the current document.

On the top of this section you find a summary with the number entities annotated, the number of unique entities, and the entities unidentified (i.e. not normalized). 

> **What is an unique entity?** a group of annotations with the same Entity Type and same text.

Below this summary you find a list of unique entities annotated.

If you hover the mouse on the counter, it will show you how many of these annotations were done manually and how many automatically.

If you click on any of the items, the document area will move to the annotation in the document. The border of the annotation displayed will wider than usual so it is easier to spot.

### Relation tally

You will only see content here if you have relation types defined at _Settings-Relations_.

It keeps the count of the relations defined in the current document. In this section you can also remove existing relations, clicking on the button `X`.

![Editor - relation tally](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/editor-relation-tally.PNG)

If you click on a relation on this section, the document area will move to the first annotation related. The border of both annotations will be wider than usual so they are easier to spot.

