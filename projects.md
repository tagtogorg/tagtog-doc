# Projects
A project is a collection of documents and rules to annotate documents manually or automatically. Create a new project is the starting point for each user.

## Create a project
1. Once you have signed up and you have a user account, you are **ready to create a new project**:

***

![Create a project](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/new-project.PNG)

***


2. You can now briefly **define your project**:

![Define a new project](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/define-new-proj.PNG)

* **Project name** (mandatory): choose a name for your project.
* **Description** (optional): what is the problem you are trying to solve? describe it briefly. It can help other users to understand your goal.
* **Domain**: tagtog has built-in some magic to process more effectively specific domains (e.g. biomedical). If the text you plan to analyze is not related to any of the domains in the list, please select the option `other`.
* **Language**: Right now only English is supported.
* **Entities**: We have some already built "machines" that can help you to identify relevant information (entities in this case) in the text from the scratch. Currently these are related to the biomedical field: GGP (Gene or Gene Product), Organism, Mutation, [SNOMED CT](https://en.wikipedia.org/wiki/SNOMED_CT) (Clinical Terms), Sequencing Platform. In the future there will be more connected to more domains.

## Configure a project

While defining a project, if you have [selected some entities](#create-a-project) to be extracted automatically, you may want start uploading text to get results right away. Otherwise, you need to configure its settings either to annotate manually or automatically. `Settings` can be found in the project bar under the project title:

![Project bar](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-bar.PNG)

Let's go over what you can configure under Settings:

### Guidelines
You can write the annotation guidelines for you or your team. It should define what and how manually annotate. More clear it is, better the annotations will be and better the training data you can provide with.

You can enrich the text using the [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)

***

![Setting Guidelines](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-guidelines.PNG)

***

Clicking on `Edit` you turn on the mode to edit the guidelines. Clicking on `View` you are on the preview mode and you can observe the result of your changes. Once it looks as you want it, you can save clicking on the save button ![Save guidelines](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/save-guidelines.PNG)

### Annotatable sections

> This section is specific to scientific papers. If you are not processing scientific papers, make sure `All` option is selected.

> If you want to **disable manual annotation** you can uncheck all the options. If every single option is unchecked you will be able to see text as usual in the editor, however the manual annotation won't be possible.

Here you select which sections you want to manually or automatically annotate in scientific papers. The available sections are: `Title`, `Abstract`, `Introduction & Background`, `Materials & Methods`, `Results, Conclusion & Discussion`, `Other`. The sections not selected will be grayed out in the editor and the manual annotations disabled.

You can also select how to annotate `Figures & Tables` as in `always`, `never` or `section-dependant`.

***

![Settings - Annotatables](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-annotatables.PNG)

***


### Entities

Here you should define what type of information you want to annotate manually or automatically. Meaning, which type of information you want to identify in text. You achieve this by defining `Entity Types`. 

> **What is an entity?** a named entity is a real-world object, such as persons, locations, organizations, products, etc. Examples of named entities include Barack Obama, New York City, Volkswagen Golf, or anything that can be named. Entities are instances of **Entity Types** (e.g., New York City is an instance of a city, wheel is an instance of a vehicle part).

You should add one or more entity types. Each entity is defined by a name, a description and a color. For example in the project in the picture below we want to extract vehicle information and therefore we have created entity types to annotate vehicle parts (`vehiclePart`), vehicle types, (`vehicleType`) and vehicle model (`vehicleModel`). In order to easily identify the entities in the text, we will assign to each entity type a color. It is recommended to use colors that are easy to distinguish. Keep in mind color blind people.

***

![Settings - Entity Types](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-entities-types.PNG)

***

### Dictionaries

As soon as you create one entity type, it will appear in the `Dictionaries` panel. **Each entity type can have associated one or more dictionaries**.

> **What is a dictionary?** A simple list of terms with their synonyms. E.g. the model `Volkswagen Golf 7` is also known as `Golf Mk7`. This list facilitates NER (Named Entity Recognition), i.e. the **automatic extraction of entities** in text and their normalization. The **normalization** of entities is the process to identify a canonical unambiguous referent to an entity. 

As an example of dictionary let's use the entity type `vehicleModel`. For example, `Volkswagen Golf 7`, `Golf Mk7` and `Golf VII` all identify the same canonical object, this object can be identify with an ID, e.g. : `VWGOLF7`. This could be an entry in the dictionary as simple as:

***

| VWGOLF7      | Volkswagen Golf 7  | Golf Mk7  |  Golf VII  |
| ------------ |:------------------:| ---------:|-----------:|

***

You can read [here](https://www.tagtog.net/-doc/formats/EntityDictionaryTsv_v0_1) the **format of dictionaries** you can upload to tagtog.

The process of normalization **facilitates the retrieval of information**, e.g. How many error reports mention the vehicle `Golf Mk7`?

tagtog applies grammar rules to identify potential entities as plurals, tenses, etc.

In order to upload a dictionary, click on `New Dictionary` under the entity type name and Save it. Two options will show up: `Download Dictionary` and `Upload Dictionary`.

***

![Settings - new dictionary](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/new-dictionary-upload.PNG)

***

* **Upload**: you can use this option to upload a [local dictionary file](https://www.tagtog.net/-doc/formats/EntityDictionaryTsv_v0_1) from your computer. If a dictionary file was uploaded previously, it will be replaced with the new dictionary. Once you have uploaded a dictionary, if you upload any text, in the web editor you can see how the **entities are identified automatically** :sunglasses:
* **Download**: you can use this option to download the dictionary being used in tagtog to your computer.

### Relations

You can **manually annotate relations** in text. For that you must first create a new `Relation Type` by clicking the `New Relation Type` button. Afterwards you should choose two `Entity Types`, those types you want to identify relations for. Optionally you can add a description for the relation. For example, below you can see a new relation type between vehicle parts and vehicle models.

***

![Settings - New Relation type](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-new-relation-type.PNG)

***

Once the relation type is created, you can manually annotate relations in the web editor.

> Currently you cannot extract relations in text automatically. However, as a workaround, you can extract the entities automatically and based on the distance in text infer a relation.

### Document labels

Document Labels are used to mark the documents or text you upload. It is another type of annotation, but affecting the whole document. This can be useful for intent detection, or machine training.

To create a new Document Label, click on the button `New Document Label`. Afterwards, write a name for the label (required), the type (required) and a description (optional)

You can create different types of Document Labels:
* **Boolean**: the simplest label. Basically you mark the document as true or false for a specific condition. e.g. should this customer request go to the technical department? Yes or No.
* **String**: one or more words describing a document. This is particularly handy if you don't have a specific list or if you do, it might change often. e.g. which disease is related to this clinical profile? 
* **Enum**: list of options which can describe a document. **In this case the options should be written in the description of the label**. e.g. severity of the error report could be low, medium, high or critical. 

You can see an example using the `enum` type below:

***
![Settings - new document label](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-doclabels.PNG)
***
Once saved, you can start using them in the web editor.

> Currently you cannot get document labels automatically. However, as a workaround, based on the entities extracted automatically you can infer the document label.

### Webhooks

You can define webhooks to notify an external system after an specific action in tagtog or [API](https://github.com/tagtog/tagtog-doc/wiki/API-documents-v0.1). These actions are: upload a new document and save a document.
* End Point URL: URL pointing to the external system
* Format: document format to be sent o the End Point. Currently you can select: [ann.json](ann.json), docJSON (used internally for some customers) and [PubAnnotation](http://pubannotation.org/)
* `Trigger only if change originates in the GUI` : if you check this option, the API changes won't create a call to the webhook. The call will be done only when a user uploads a new doc via web editor or saves it in the web editor.
* Authentication: 
  * None: no authentication
  * Basic: [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
  * NTLMv2 (Windows): [NT LAN Manager v2](https://en.wikipedia.org/wiki/NT_LAN_Manager#NTLMv2)

***

![Settings - webhook](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-webhook.PNG)

***

### Annotations

#### Pre-annotations
These are the annotations that are done automatically while you are manually annotating a document. For example, if you annote the gene: `BRA2` . All the mentions of `BRA2` in this text will be automatically annotated. In this panel you can decide which are the **default settings** for pre-annotations. You can always change these settings in the web editor for specific documents.
  * Pre-select: those annotations that will be **added** automatically upon creation of a new annotation.
  * Pre-deselect: those annotations that will be **removed** automatically upon removal of an existing annotation.

#### Machine Learning 
Each time you `Confirm` the annotations of a single document, a machine learning model is being trained with the annotations. Next time you upload a new document, this model can predict new annotations based on the learning. You can remove or add new annotations to continue training the machine and get more accurate results.
  * `Use machine learning for automatic annotations (dictionary annotations are independent and always activated)` : currently this option is experimental and we cannot guarantee it works as expected. 

### Members

In this panel you can invite users to your project so they can collaborate in the annotation tasks. Currently there are two roles:
* **admin**: the person who create the project
* **supercurator**: those you invite as collaborators.

To **add a new member** simply write his/her tagtog username in the text box and click on `Add Member`. Once added, they will receive an email notification.

![Settings - members](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/settings-members.PNG)

## Remove a project

To remove a project go to the list of projects (you can go easily clicking in the tagtog icon on the top left). Click the `Delete` option in the project card. 

You cannot remove projects for which you are not the `admin`.
