---
layout: page
title: Metrics
sidebar_link: true
id: metrics
---

  <div class="two-third-col">
    <p>Metrics to track the progress of your project and the health of your data. Metrics are split into different sections:</p>
    <h3>Overview</h3>
    <p>A simple overview of your project's settings and members.</p>
  </div>
  <div class="one-third-col">
  </div>
  <div class="two-third-col">
    <h3>Inter-Annotator Agreement</h3>
    <p>You can read all about the Inter-Annotator Agreement (IAA) <a title="tagtog docs - IAA" href="collaboration.html#iaa-inter-annotator-agreement">here</a>.</p>
  </div>
  <div class="one-third-col">
  </div>
  <div class="two-third-col">
    <h3>Documents</h3>
    <p>The following charts are available:</p>
    <p class="list-item"><span class="list-item-1"></span><strong>Confirmed VS Not Confirmed documents</strong>. It gives you a general idea of the progress in your project. Please notice that this chart only show data from the master version of the annotations.</p>
    <p class="list-item"><span class="list-item-2"></span><strong>Annotated VS Not Annotated documents</strong>. Annotated documents are those with at least one annotation of any kind (document label, entity, etc.). Not annotated documents are those with no annotations.</p>

  </div>
  <div class="one-third-col">
    {% include message.html message="Notice that most of the metrics below are extracted <strong>using only the master version</strong> of the annotations. The versions used are indicated on the top of each metric." %}
    {% include image.html name="annotated.metric.png" caption="Example of Annotated VS Not Annotated documents. The master and the users' versions of the annotations have been used to calculate this metric."%}
  </div>
  <div class="two-third-col">
    <h3>Entities</h3>
    <p>The following charts are available:</p>
    <p class="list-item"><span class="list-item-1"></span><strong>Entity type distribution</strong>. Number of entities across all your documents, by entity type.</p>
    <p class="list-item"><span class="list-item-2"></span><strong>Entity type distribution across documents</strong>. Number of documents annotated with entities of specific entity type.</p>
    <p>An entity type misrepresented or concentrated in a small sample of documents might lead to bias or incorrect predictions. Take action to improve the health of your data</p>
  </div>
  <div class="one-third-col">
    {% include image.html name="entity.distribution.metric.png" caption="Example of Entity type distribution metric. Hold the mouse pointer to see the number of entities and percentage."%}
  </div>
  <div class="two-third-col">
    <h3>Normalizations</h3>
    <p>The following charts are available:</p>
    <p class="list-item"><span class="list-item-1"></span><strong>A chart per dictionary</strong>. It shows the number of documents annotated with specific normalizations (i.e. unique ids).</p>
    <p>A normalization concentrated in a small sample of documents can lead to a misrepresented normalization and eventually to bias or incorrect predictions.</p>
  </div>
  <div class="one-third-col">

  </div>
  <br>
  <br>
  <br>
  <div class="two-third-col">
    <h3>Document labels</h3>
    <p>The following charts are available:</p>
    <p class="list-item"><span class="list-item-1"></span><strong>Document labels distribution across documents</strong>. Number of documents with an specific document label set.</p>
    <p class="list-item"><span class="list-item-2"></span><strong>A chart per document label</strong>. For the `boolean` or `enum` types, this chart represents the distribution of possible values across the documents of your project. For the `string` type, due to its non-finite nature, this chart represents the top values across the documents of your project.</p>
    <p>A misrepresentation of a document label or any of their possible values might impact the health of your data. Pay special attention to the representation of the values from your labels, it can lead to bias or incorrect predictions.</p>
  </div>
  <div class="one-third-col">
    {% include image.html name="doclabel.metric.png" caption="Example of document label metric. In this case, the type of the label is <code>string</code> and the top values are represented." %}

    {% include message.html message="Currently, there are no metrics for relations or entity labels" %}
  </div>