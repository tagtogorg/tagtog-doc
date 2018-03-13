---
layout: page
title: Search engine
sidebar_link: true
id: search
---
<div class="two-third-col">
  <p>Traditional search is built around string matching. tagtog uses your annotated data to create a <strong>semantic layer</strong> allowing users to perform queries across their documents using concepts, labels and other metadata. This augmentation of the search functionality makes easier to discover patterns or find actionable insights. This is a major benefit when you have built a model that annotates text automatically and you want to grasp the intelligence of the data processed.</p>
  <p>This search engine can be used through the user interface or the API. Learn <a href="/search-queries.html">how to build queries</a> and make the most of the concept search.</p> 
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h2>Web app</h2>
  <p>You can find the search bar in the main toolbar from the web app. Here you type <a href="/search-queries.html">search queries</a>.</p>
  {% include image.html name="searchbar.png" %}
</div>
<div class="one-third-col">

</div>
<div class="two-third-col">
  <h3>Advance search</h3>
  <p>You can access the advance search panel by clicking on the arrow on the right side of the search box. This panel uses the data from your project settings (dictionaries included) to automatically create search queries in a friendly way.</p>
  {% include image.html name="advancesearch.png" %}
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h4>Annotation complete</h4>
  <p>Find which documents have been already marked as confirmed or which not.</p>
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h4>Entity Type</h4>
  <p>Find which documents contain at least one annotation from the entity type selected from the dropdown menu.</p>
</div>
<div class="one-third-col">
  {% include message.html message="<strong>Tip</strong>: there is a <code>none</code> option. You can use it to find which documents are not annotated, i.e. don't have any annotation." %}
</div>
<div class="two-third-col">
  <h4>Normalization</h4>
  <p>Just start typing the first 3 characters of one of the names of the entity you are looking for. All the possible entities gathered across all your dictionaries will show up. Click on one of the items to display the search query on the normalization text box and, when you are ready, just click on the Search button {% include inline-image.html name="search-button.png" width="28" %} to retrieve all the documents that contain at least one entity normalized to that name. In the case of the picture below, all documents containing entities with the name: minivan, people carrier, etc.</p>
  <p>The search results are paginated. If your query retrieves a long list of results, you will find a <code>Load more</code> link at the bottomo of the list. Just click it to load more results.</p>
  {% include image.html name="search_normalization.png" caption=""%}
</div>
<div class="one-third-col">
  {% include message.html message="The normalization search engine finds names and IDs across all your dictionaries. You don't need to know the entity type, just one of the names of the concept you are looking for." %}
</div>
<div class="two-third-col">
  <h4>Document ID</h4>
  <p>Documents such as biomedical articles have usually associated an id (e.g. PubMed articles). Type the id in order to find matching documents in the pool. You can also use wildcard characters as in the example below.</p>
  {% include image.html name="docIdsearch.png" caption=""%}
</div>
<div class="one-third-col">
  {% include message.html message='Check <a href="/API.html#idtype-parameter">here</a> the available ID types.' %}
</div>

<div class="two-third-col">
  <h2>API</h2>
  <p>You can also search using the API. You can use it <a href="/#index-your-data">directly as your search interface</a> or simply augment your existing engine. Discover everything you can do checking the <a href="/API.html#search-documents-in-a-project-get">documentation</a>.</p>
</div>
<div class="one-third-col">
</div>
