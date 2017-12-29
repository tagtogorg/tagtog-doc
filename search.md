# Web app

You can find the search bar in the main toolbar from the web app.

![Search Bar](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/searchbar.png)

If you click on the arrow on the right side the advance search panel shows up.

![Advance search](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/advancesearch.png)

## Search box

If you type in the search box any term it will retrieve all documents that contain that string. For more advance ways of searching or concept search you can use the syntax described [here](https://github.com/tagtog/tagtog-doc/wiki/search-parameter), it is valid for the web app and the API. 

You can also use the advance search panel to perform more advance search queries in a more friendly way.

## Advance search

### Annotation complete
Find which documents have been already marked as confirmed or which not.

### Entity type
Find which documents contain at least one annotation from the entity type selected from the dropdown menu.

>Tip: there is a 'none' option. You can use it to find which documents are not annotated, i.e. don't have any annotation.

### Normalization

Just start typing one of the names of the entity you are looking for. For example:

![Search by normalization](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/search_normalization.png)

This will help you find all the documents that contain at least one entity normalized to that name. In the case of this picture all documents containing entities with the name: minivan, people carrier, etc.

### Document ID

Documents such as biomedical have usually associated an id (e.g. PubMed articles). Type the id in order to find matching documents. You can also use wildcard characters as in the example below:

![Search by Document ID](https://raw.githubusercontent.com/tagtog/tagtog-doc/master/resources/docIdsearch.png)


