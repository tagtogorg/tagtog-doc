---
layout: page
title: Quick tutorials
sidebar_link: true
id: quick_tutorials
notoc: true
---

Know what you can do withe tagtog with the following tutorials. Moreover, we publish other tips on our [🗞 Medium blog](https://medium.com/@tagtog).


<div class="two-third-col" markdown="1">

## [How to annotate scans for NLP](https://tagtog.medium.com/how-to-annotate-scans-for-nlp-7333ad4bab3a?source=friends_link&sk=ca708d310fee15aa4573dfafe11bfe95)

Learn how to integrate an external OCR software into tagtog, including [fully-functioning java code](https://github.com/tagtog/java-ocr-amazon-textract-searchable-pdf) to:

1. OCR scans calling the APIs of Amazon Textract
2. Uplaod the resulting text-embedded PDFs into tagtog (to do there the labeling)

</div>
<div class="one-third-col">
  <div vertical-align="center"><img width="80%" src="/assets/img/tutorials/2021-04-27-scans-OCR-PDF.png"></div>
</div>

<div class="two-third-col">
  <h2><a title="Connect your NLP models to tagtog using webhooks" href="https://tagtog.medium.com/connect-your-nlp-models-to-tagtog-using-webhooks-13d422ae4dff">Connect your NLP models to tagtog using webhooks</a></h2>
  <p>When you finish this tutorial, you will understand:</p>
  <p class="list-item"><span class="list-item-1"></span>What is a webhook.</p>
  <p class="list-item"><span class="list-item-2"></span>How to connect your model to tagtog (or other services) using webhooks</p>
  <p class="list-item"><span class="list-item-3"></span>How to test webhooks locally</p>
  <p class="list-item"><span class="list-item-4"></span>How using webhooks will make the training of your model more accessible</p>
</div>
<div class="one-third-col">
  {% include image.html width="80%" name="webhook_icon.png" %}
</div>

<div class="two-third-col">
  <h2><a title="Integrating tagtog and spaCy: a simple example" href="https://tagtog.medium.com/integrating-tagtog-and-spacy-16fb0addeea1">Integrating tagtog and spaCy: a simple example</a></h2>
  <p>This tutorial uses the spaCy library to automatically generate NER (Named-Entity Recognition) annotations and display these annotations directly in tagtog.</p>
</div>
<div class="one-third-col">
  {% include image.html name="SpaCy_logo.png" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Build powerful annotation layouts with tagtog blocks" href="https://medium.com/@tagtog/build-powerful-annotation-layouts-with-tagtog-blocks-5ae2a1268917">Build powerful annotation layouts with tagtog blocks</a></h2>
  <p>As part of the flavored Markdown used in tagtog, you can create blocks with custom styles/layout. As we all know, annotating data can be a tedious task, and a more attractive content can be key to keep your team engaged. Using Markdown you can use the new tagtog blocks to build a customized annotation layout for your project! E.g. question answering datasets, chatbot training, tweets, etc.</p>
</div>
<div class="one-third-col">
  {% include image.html name="chatbot.png" %}
</div>

<div class="two-third-col">
  <h2><a title="Jorge Campos at Medium - The adjudication process in collaborative annotation" href="https://medium.com/@jorgecp/the-adjudication-process-in-collaborative-annotation-61623c46b700?source=friends_link&sk=41adf0909b87899133ac3ef87fa88ccf">The adjudication process in collaborative annotation</a></h2>
  <p>If multiple annotators work on the same data, as a result, there are multiple annotation versions. We define adjudication as the process to resolve inconsistencies among these versions before a version is promoted to the gold standard. This process is manual, semi-automatic or automatic. Learn the differences and when to use each of them.</p>
</div>
<div class="one-third-col">
  {% include image.html name="automatic_adjudication.png" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Poor Inter-Annotator Agreement: what to do?" href="https://medium.com/@tagtog/poor-inter-annotator-agreement-what-to-do-6980e90ce7ee">Poor Inter-Annotator Agreement: what to do?</a></h2>
  <p>There may be several reasons why your annotators do not agree on the annotation tasks. It is important to mitigate these risks as soon as possible by identifying the causes. Discover how to prevent a low Inter-Annotator Agreement.</p>
</div>
<div class="one-third-col">
  {% include image.html name="iaa-matrix.png" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Automatic adjudication based on the inter-annotator agreement" href="https://medium.com/@tagtog/automatic-adjudication-based-on-the-inter-annotator-agreement-a62f49be7bcf">Automatic adjudication based on the inter-annotator agreement</a></h2>
  <p>When multiple annotators produce annotations for the same data,  tagtog chooses the annotations from the available-best annotator for each annotation task. Check out step by step how to setup this process.</p>
</div>
<div class="one-third-col">
  {% include image.html name="automatic_adjudication_2.jpg" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - How to rank & review your annotators" href="https://medium.com/@tagtog/how-to-rank-review-your-annotators-4a814c941ac3">How to rank & review your annotators</a></h2>
  <p>Some useful tips and suggestions that may be useful for anyone who is managing a team of annotators. tagtog allows users to filter documents based on whether a given user has confirmed them (or any user has confirmed them). This feature, despite it may not look like such a big deal, it can be used for many different things. In this post we discuss some of the applications 🚀.</p>
</div>
<div class="one-third-col">
  {% include image.html name="annteam.jpeg" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Annotating Images & Markdown" href="https://medium.com/@tagtog/annotating-images-markdown-e14a6fbd4df4?source=friends_link&sk=79fdc6e586739aebf1fc1fec06391f83">Annotating Images & Markdown</a></h2>
  <p>tagtog gives support to annotate Markdown files. Therefore images, nested lists, or code blocks are fully supported. This opens many new possibilities for annotation. This article focuses on three.</p>
</div>
<div class="one-third-col">
  {% include image.html name="img-annotation.png" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Finding Pokemon names in text using dictionaries and tagtog" href="https://medium.com/@tagtog/finding-pokemon-names-in-text-using-dictionaries-and-tagtog-140ac43d65e1">How to build a very simple pipeline to recognize Pokémon names using a dictionary</a></h2>
  <p>Dictionaries are simple controlled vocabularies, and yet a powerful resource when you have a well-defined list of items you want to recognize in text, especially if those items are identified with different names. Learn how to use them and when to use them with a practical example.</p>
</div>
<div class="one-third-col">
  {% include image.html name="pokemon.png" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Overlapping text annotations" href="https://medium.com/@tagtog/overlapping-text-annotations-19d7ac5b247a">Learn how overlapping text annotations can help you train a model more efficiently</a></h2>
  <p><strong>Overlapping annotations</strong> increase the flexibility and allow you to make the most out of your data. Learn how to use them and in which scenarios.</p>
</div>
<div class="one-third-col">
  {% include image.html name="overlapped_cropped.png" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Train your AI models with tagtog" href="https://medium.com/@tagtog/how-to-train-your-ai-models-with-tagtog-5a2beaa12eb">Learn how you can use webhooks to train a model</a></h2>
  <p><strong>Webhooks</strong> can be used to notify your AI model when you have labelled new data in tagtog, so it can be <strong>retrained and improve its performance</strong></p>
</div>
<div class="one-third-col">
  {% include image.html name="webhooks_tutorial.png" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - Train and deploy a custom ML model to recognize dates in text in 5 minutes" href="https://medium.com/@tagtog/train-and-deploy-a-custom-ml-model-to-recognize-dates-in-text-in-5-minutes-a17d604be5f9">Train and deploy a custom ML model to recognize dates in text in 5 minutes</a></h2>
  <p>Learn how to create and use an <strong>custom ML model from scratch just by using some text annotations</strong>. We are going to show you how to build a model that extracts dates in text. All will take 5 minutes of your time.</p>
</div>
<div class="one-third-col">
  {% include image.html name="calendar.jpg" %}
</div>

<div class="two-third-col">
  <h2><a title="tagtog at Medium - A short introduction to tagtog, text annotation made easy" href="https://medium.com/@tagtog/a-short-introduction-to-tagtog-text-annotation-made-easy-a8de243c2c3f">A short introduction to tagtog, text annotation made easy</a></h2>
  <p>tagtog is a collaborative text annotation platform to find, create, and maintain NLP datasets efficiently. Accessible on the Cloud and On-Premises. Find a quick introduction in this article.</p>
</div>
<div class="one-third-col">
  {% include image.html name="pdfanno.jpeg" %}
</div>

<div class="two-third-col">
  <h2><a title="Demo of tagtog, in Video!" href="https://medium.com/@tagtog/demo-of-tagtog-in-video-2821293cb382">Demo of tagtog, in Video! 🎥</a></h2>
  <p>Learn the core of tagtog comfortably, grab some 🍿 and <a href="https://www.youtube.com/watch?v=2G3Eqci9YgE&t=2s">watch the movie</a>.</p>
</div>
<div class="one-third-col">
  <a href="https://www.youtube.com/watch?v=2G3Eqci9YgE&t=2s">{% include image.html name="tutorials/demo_youtube_video.png" %}</a>
</div>