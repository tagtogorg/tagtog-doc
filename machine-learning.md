---
layout: page
title: Machine Learning
sidebar_link: true
id: ml
---

<div class="two-third-col">
  <br>
  <p><strong>Two of the main barriers to Machine Learning are deployment and scaling</strong>. Deploying manually models requires time and engineering resources. Scaling the usage of these models requires a powerful infrastructure, the effort to maintain it and cost control. With tagtog, this complexity is transparent to users. <strong>We take care of the training mechanisms, the deployment and the handling of usage spikes</strong>. You only focus on problem solving using the web editor to indicate what you want to recognize in text. This will be the training data tagtog learns from. All without writing any code, empowering experts in any field to train and use machine learning models.</p>
</div>
<div class="one-third-col">
  {% include image.html name="robot.drone.svg" width=500 %}
  
</div>

<div class="two-third-col">
  <p>One of the advantages using tagtog is the possibility of annotating text automatically using machine learning (ML) :bookmark_tabs: Why is this important? Automatic annotations are just insights on the top of the text. You can leverage intelligence in different scenarios:</p>
  <p class="list-item"><span class="list-item-1"></span>tagtog annotates text automatically using custom or pre-trained ML models. This means you can <strong>automate</strong> processes to find relevant insights automatically. E.g. analyze customer feedback on real time.</p>
  <p class="list-item"><span class="list-item-2"></span>Automatic annotations can <strong>boost annotator performance</strong>. Documents are pre-annotated by ML models and annotators only need to correct wrong predictions. tagtog learns from feedback and provide with more accurate results with each iteration.</p>
  <p class="list-item"><span class="list-item-3"></span><strong>Index your data</strong>. Use automatic annotations to augment your data and improve discoverability (e.g. augment records with mutation mentions using standard names, easier to find). You can either import the results into your own system or use the <a href="/API.html#search-documents-in-a-project-get" title="Search API">Search API</a> to find suitable records across the data imported.</p>
</div>
<div class="one-third-col">
  {% include message.html message='tagtog with machine learning capabilities is offered on the tagtog <strong>Cloud or On-premises</strong> (<a title="tagtog plans" href="https://www.tagtog.net/-pricing">plans</a>). You can install it within your infrastructure or any public cloud (AWS, Google, Azure, etc.).' %}
</div>

<div class="two-third-col">
  <h2>How does it work?</h2>
  <p>In tagtog, training data means annotations in any of <a title="Text annotation types supported by tagtog" href="/webeditor.html#annotation-types">supported types</a>. You annotate, you train :pencil2: tagtog is implemented using <strong>semi-supervised learning algorithms</strong> that reduce the volume of training data required. One of the strongest points is the ability of models to <strong>learn continuously and adaptively</strong> to incrementally take into account different scenarios but still being able to re-use and retain useful knowledge and skills during time.</p>

  {% include image.html name="diagram_ml_small.svg" caption="Training flow" %}

  <br/>

  
</div>
<div class="one-third-col">
  {% include message.html message='<strong>What is semi-supervised learning?</strong> Traditional models use only labeled data to train. Labeled instances however are often difficult or expensive to obtain, as they require experienced human annotators. Meanwhile, unlabeled data may be easy to collect but harder to use for training.  Semi-supervised learning uses large amount of unlabeled data, together with the labeled data, to build better models. In practice, semi-supervised learning requires less human effort and gives higher accuracy. <a title="Semi-Supervised Learning Literature Survey. Xiaojin Zhu, Computer Sciences TR 1530, University of Wisconsin – Madison." href="http://pages.cs.wisc.edu/~jerryzhu/pub/ssl_survey.pdf">More information</a>' %}
</div>
<div class="two-third-col">
  <br/> 
  <p>To train a ML model follow the next steps: </p>
  
  <p class="numbered-item"><span class="number-1">1</span><a title="tagtog docs - create a project" href="/projects.html#creating-a-project">Create a project</a>, define one or more <a title="tagtog docs - entity types" href="/projects.html#entities">entity types</a> and import a document (if you have pre-annotated documents you can import them too).</p> 
  <br>
</div>
<div class="one-third-col">
  {% include message.html message="Currently automatic annotations are only available for Name Entity Recognition." %}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-2">2</span><strong>Annotate the text with the entities you want to extract automatically</strong>. When you have finished annotating, use the <strong>Confirm</strong> button to tell tagtog these annotations are ready to be used as training data. When you click this button, in the background, the custom model is being trained and deployed automatically using all the confirmed annotations in your project. The process is <strong>very fast</strong> and you can immediately annotate other documents automatically using this model.</p>
  {% include image.html name="annotate_date.gif" caption="Example of document where dates are being annotated"%}
</div>
<div class="one-third-col">
  {% include message.html message='<strong>Machine learning is active by default</strong>. You can deactivate it at <i>Settings > Annotations</i>. Please notice that this only will deactivate the automatic annotations provided by ML. Automatic annotations provided by dictionaries are independent and always active.' %}
 
 {% include message.html message="Machine learning only trains with the <strong>master</strong> version of your documents." %}
</div>  
<div class="two-third-col">
  <p class="numbered-item"><span class="number-3">3</span><strong>Use the model</strong>. When you import new documents using the interface or the <a title="tagtog - API documentation" href="/API.html">API</a>, they are automatically annotated by the custom ML model.</p>
</div>
<div class="one-third-col">
  {% include message.html message='To facilitate automation, models are also accessible as a highly-reliable <strong><a title="tagtog - API documentation" href="/API.html">API</a></strong>.' %}
</div>
<div class="two-third-col">
  <p class="numbered-item"><span class="number-4">4</span><strong>Continuous learning</strong>. Were any automatic annotations wrong? was important information not annotated? something new to teach? No problem. Just remove/edit the wrong annotations and add those that are missing. Click on the Confirm button. Again all the confirmed documents are used to retrain the model with your new findings.</p>
</div>
<div class="one-third-col">
  {% include message.html message="<strong>While a model is being retrained, the previous version of the model is fully available to process requests</strong>. In this way we guarantee your model is always accessible. Once the new version of the model has been trained and deployed, it replaces the previous version." %}
</div>

<div class="two-third-col">
  <p>Follow this <strong><a title="tagtog at Medium - Train and deploy a custom ML model to recognize dates in text in 5 minutes" href="https://medium.com/@tagtog/train-and-deploy-a-custom-ml-model-to-recognize-dates-in-text-in-5-minutes-a17d604be5f9">hands-on quick tutorial</a></strong> to understand how easily you can train custom models.</p>
</div>
<div class="one-third-col">
  
</div> 

<div class="two-third-col">
  <h2>Continuous learning</h2>
  <p>tagtog smoothly update your custom prediction models with the changes in your annotations. Each time you confirm the annotations of one of your documents, the model is trained with all your confirmed documents used as training data. There are two ways you can retrain your model iteratively:</p>
  <p class="list-item"><span class="list-item-1"></span><strong>On top of previously learned knowledge</strong>. You just need to import new documents, edit the wrong predicted annotations or add new ones and click on Confirm. Your model has been retrained using this new knowledge.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>Changing historical data</strong>. Yes! this is possible. Your documents are indexed within your project. You just need to go to the document you want modify (even if it was used previously for training), toggle the Confirm button to allow the changes and make the required changes. Once finished, click the Confirm button again and voilà, your model is trained and deployed including these changes. Usually you want to perform similar changes across the documents of your project, use the <a title="tagtog-docs - Search" href="/search.html">search</a> engine to find the documents to modify.</p>

</div>
<div class="one-third-col">

</div>


<div class="two-third-col">
  <h2>ML annotations and dictionary annotations</h2>
  <p>Machine learning and <a title="tagtog-doc - Dictionaries" href="/projects.html#dictionaries">dictionary</a> annotations are annotated automatically. <strong>They can work independently or combined.</strong></p>
  <p>When a ML model is trained, it uses the data from your dictionaries as a feature.</p>
  <p>Currently, the normalization of entities can be only done with dictionaries. ML annotates entities, but it doesn't normalize them. If you combine both mechanisms ML will annotate and dictionaries will normalize.</p>
</div>
<div class="one-third-col">

</div>


