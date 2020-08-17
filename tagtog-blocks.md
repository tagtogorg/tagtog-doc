---
layout: page
title: tagtog blocks
sidebar_link: false
id: tagtogBlocks
toc: true
---

<div class="two-third-col">
  <h2>What are tagtog blocks?</h2>
  <p>As part of the <a href="MarkdownFileParsing">flavored Markdown used in tagtog</a>, you can create blocks with <strong>custom styles/layout</strong>. As we all know, annotating data can be a tedious task, and a <strong>more attractive content</strong> can be key to keep your team engaged.</p>
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h2>How to use tagtog blocks?</h2>
  <p>You can add blocks to your content in two ways:</p>
  <p class="list-item"><span class="list-item-1"></span>Import to your project a <strong><code>.md</code> (Markdown) file</strong> with one or more tagtog blocks. You can use the <a href="API_documents_v1.html#examples-import-a-markdown-file">API</a> or the <a href="documents.html#upload-content">GUI</a>.</p>
  <p class="list-item"><span class="list-item-2"></span>Copy or write the blocks <strong>directly in the <a href="documents.html#upload-content">+Content</a> menu</strong> and set the format as Markdown in the advanced options.</p>
  <p>tagtog blocks are Markdown code blocks. For example, you can add a textbox code block as follows:</p>
  <div markdown="1">
    ```textbox
    Hello, I'm a textbox block.
    ```
  </div>

</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h2>Block types</h2>
  <h3>Text box</h3>
  <p>Code: <code>textbox</code></p>
  <p>This block draws a circled box around the content.</p>

  <p>Example:</p>

  <div markdown="1">
    ```textbox
    In the U.S. federal health care system (including the VA, the Indian Health Service, and NIH) ambulatory care pharmacists are given full independent prescribing authority. In some states such North Carolina and New Mexico these pharmacist clinicians are given collaborative prescriptive and diagnostic authority. In 2011 the board of Pharmaceutical Specialties approved ambulatory care pharmacy practice as a separate board certification.

    The official designation for pharmacists who pass the ambulatory care pharmacy specialty certification exam will be Board Certified Ambulatory Care Pharmacist and these pharmacists will carry the initials BCACP.
    ```
  </div>

   {% include image.html name="textbox.png" caption="textbox tagtog block" %}
</div>
<div class="one-third-col">
</div>
<div class="two-third-col">
  <h3>Chatbot</h3>
  <p>If you combine this layout with the tagtog annotation capabilities, you could perform chatbot annotation tasks such as:</p>
  <p class="list-item"><span class="list-item-1"></span>Entity annotation</p>
  <p class="list-item"><span class="list-item-2"></span>Intent classification</p>
  <p class="list-item"><span class="list-item-3"></span>Create relations between entities</p>
  <p class="list-item"><span class="list-item-4"></span>Attach attributes to entities</p>
  <p class="list-item"><span class="list-item-5"></span>Context classification</p>
  <p class="list-item"><span class="list-item-6"></span>Overlapping annotations (e.g. entity within intent)</p>
</div>
<div class="two-third-col">
  <h4>Bot</h4>
  <p>Code: <code>bot</code></p>
  <p>Block for the chatbot interaction.
human for the human interaction</p>
  <h4>Human</h4>
  <p>Code: <code>human</code></p>
  <p>Block for the human interaction.</p>

  <p>Example:</p>

  <div markdown="1">
    ```human
    Hi, how are you today?
    ```
    ```bot
    I'm good. How are you? Do you have a favorite food? Mine is lobster!
    ```
    ```human
    Doing well, my favorite food is cake. I just bought one because I got promoted at work!
    ```
    ```bot
    Congratulations on the promotion! What kind of work do you do? I work in software.
    ```
    ```human
    Thanks so much! I just want to make my parents proud! I'm an engineer.
    ```
    ```bot
    I'm sure they will be very proud of you. What type of engineering do you work in?
    ```
    ```human
    I'm an environmental engineer. What is it like to work in software?
    ```
    ```bot
    It can be a lot of work, but it is very rewarding. Do you enjoy your job?
    ```
    ```human
    I love it! it's very important to protect the environment.
    ```
    ```bot
    That's great! Do you have any hobbies? I like to play tennis in my spare time.
    ```
    ```human
    I'm not very coordinated so I don't play sports… I do like to play the guitar, though!
    ```
    ```bot
    That's awesome! I've always wanted to learn how to play an instrument. What kind of music do you play?
    ```
    ```human
    Mostly alternative rock!
    ```
    ```bot
    That's cool! I like alternative rock as well. What are some of your favorite bands?
    ```
    ```human
    I like Modest Mouse and the Smashing Pumpkins.
    ```
  </div>

   {% include image.html name="chatbot.png" caption="Example of a conversation between a human and Facebook BlenderBot chatbot" %}
</div>

<div class="one-third-col">
{% include message.html message='You can combine <code>bot</code> and <code>human</code> blocks equally.'%}
</div>

<div class="two-third-col">
  <h3>Question/Answering</h3>
  <p>Perfect for question answering datasets.</p>
  <h4>Question</h4>
  <p>Code: <code>question</code></p>
  <p>Block for questions.</p>
  <h4>Answer</h4>
  <p>Code: <code>answer</code></p>
  <p>Block for answer.</p>

  <p>Example:</p>
  <div markdown="1">
    ```textbox
    In the U.S. federal health care system (including the VA, the Indian Health Service, and NIH) ambulatory care pharmacists are given full independent prescribing authority. In some states such North Carolina and New Mexico these pharmacist clinicians are given collaborative prescriptive and diagnostic authority. In 2011 the board of Pharmaceutical Specialties approved ambulatory care pharmacy practice as a separate board certification.

    The official designation for pharmacists who pass the ambulatory care pharmacy specialty certification exam will be Board Certified Ambulatory Care Pharmacist and these pharmacists will carry the initials BCACP.
    ```
    ```question
    Q1: What type of authority are ambulatory care pharmacists given in the U.S. federal health care system?
    ```
    ```answer
    A1: full independent prescribing authority
    ```
    ```question
    Q2: In what states are pharmacist clinicians given prescriptive and diagnostic authority?
    ```
    ```answer
    A2: North Carolina and New Mexico
    ```
    ```question
    Q3: When was ambulatory care pharmacy approved as its own certification?
    ```
    ```answer
    A3: 2011
    ```
  </div>
  {% include image.html name="question_answering.png" caption="SQuAD like dataset sample. On the document, we see at the top the paragraphs supporting the questions. Below, question/answer pairs (Q1-A1, Q2-A2, Q3-A3)." %}
</div>



<div class="one-third-col">
  {% include message.html message='You can combine blocks of different types, for example <code>textbox</code> and <code>question</code>. You also can repeat blocks in the same document, for example, multiple <code>question</code> and <code>answer</code> blocks together.'%}
</div>



<div class="two-third-col">
  <h3>Tweets</h3>
  <p>Useful to annotate tweets (please notice that we are not using iFrames to load original tweets from Twitter).</p>
  <p>Code: <code>tweet</code></p>
  <p>Block for tweets.</p>

  <p>Example:</p>
  <div markdown="1">
    ```tweet
    The NHS has published its phase 3 implementation plan in response to the Covid-19 pandemic, including patient-initiated follow ups, the addressing of NHS inequalities and mental health planning.
    ```
    ```tweet
    The economic impact of COVID19 on the hotel industry is the worst we have ever faced. The hotel industry is expected to lose more than fifty percent of its total revenue in 2020.
    ```
    ```tweet
    The World Bank Group's FY20 financial statements are out, highlighting the strength of the World Bank Group's financial position, the strong demand for financing including due to COVID19, and the continued backing from shareholders and capital markets.
    ```
  </div>
  {% include image.html name="tweetblock.png" caption="Example about how to annotate and to classify Tweets with tagtog. A more engaging layout than raw plain text." %}
</div>

<div class="one-third-col">
  {% include message.html message='You can <a title="Annotating Images & Markdown in tagtog" href="https://medium.com/@tagtog/annotating-images-markdown-e14a6fbd4df4">use images</a> along with the tweets to create a more contextual content'%}
</div>

<div class="two-third-col">
  <h3>Tasks</h3>
  <p>Specially at the beginning of an annotation project, it is important to guide the annotator through the whole annotation flow. Usually, a set of guidelines are put together, annotators read through them and they try to label some documents following these rules. Why not to combine theory and practice?</p>
  <p>Code: <code>task</code></p>
  <p>Block to define a task for the annotators.</p>

  <p>Example:</p>
  <div markdown="1">
    ## Interactive guidelines

    Welcome to the interactive guidelines for our medical annotation project.

    #### Basic rules:

    * The annotator must select the concept codes that better cover the meaning of the clinical concept.
    * The annotator must select the fewest number of codes that, together, better covers the meaning of the clinical concept.
    * If there is a doubt, don't annotate.

    #### Example

    ```textbox
    Complicated fracture of third rib
    ```

    This text could be annotated with the following codes:
    1. |255302009| Complicated.
    2. |706922007| Complicated fracture of bone.
    3. |125605004| Fracture of bone. If annotators are more literal this code could be full coverage. However, other could see the next code as more appropriate and also use the score "inferred coverage".
    4. |20274005|   Fracture of one rib.
    5. |25888004|   Bone structure of third rib (body structure).

    ```task
    Explore the different combinations below, click on each annotated entity and see which codes were assigned to it.
    ```

    1,3,5
    ```textbox
    Complicated fracture of third rib
    ```
    2,5
    ```textbox
    Complicated fracture of third rib
    ```
    This would be the best annotation group, because it has a fully coverage and it also has a fewer number of codes
    #### Your task
    ```task
    Now it is your turn! Annotate this sentence to fully cover its content.
    ```
    ```textbox
    other complications of unspecified head injuries
    ```
  </div>
  {% include image.html name="taskblock.png" caption="A sample annotation guidelines with an example and a task for the annotators to validate their learning. Afterward, their annotations can be reviewed by a third person to track annotator's progress." %}
</div>

<div class="one-third-col">
  {% include message.html message=""%}
</div>





<div class="two-third-col">
  <h3>Miscellaneous</h3>
  <h4>Lyrics</h4>
  <p>Layout to display lyrics.</p>
  <p>Code: <code>lyrics</code></p>
  <p>Block to define lyrics.</p>

  <p>Example:</p>
  <div markdown="1">
    ```lyrics
    [Verse 1]
    Now I've heard there was a secret chord
    That David played, and it pleased the Lord
    But you don't really care for music, do ya?
    It goes like this, the fourth, the fifth
    The minor fall, the major lift
    The baffled king composing "Hallelujah"

    [Chorus]
    Hallelujah, Hallelujah
    Hallelujah, Hallelujah

    [Verse 2]
    Your faith was strong but you needed proof
    You saw her bathing on the roof
    Her beauty and the moonlight overthrew ya
    She tied you to a kitchen chair
    She broke your throne, and she cut your hair
    And from your lips she drew the Hallelujah

    [Chorus]
    Hallelujah, Hallelujah
    Hallelujah, Hallelujah
    ```
  </div>
  {% include image.html name="lyrics.png" width="400" caption="Lyrics from Leonard Cohen - Hallelujah" %}

  <h4>Poems</h4>
  <p>Layout to display poems.</p>
  <p>Code: <code>poem</code></p>
  <p>Block to define a poem.</p>


  <p>Example:</p>
  <div markdown="1">
    ```poem
    Caminante, son tus huellas
    el camino y nada más;
    Caminante, no hay camino,
    se hace camino al andar.
    Al andar se hace el camino,
    y al volver la vista atrás
    se ve la senda que nunca
    se ha de volver a pisar.
    Caminante no hay camino
    sino estelas en la mar.
         - Antonio Machado -
    ```
  </div>
  {% include image.html name="poem.png" width="400" caption="A poem from Antonio Machado" %}
</div>

<div class="one-third-col">
  {% include message.html message=""%}
</div>

<div class="two-third-col">
  <h2>Add-ons</h2>
  <p>Use them to modify blocks. The add-on code is added after the block code. For example: <code>tweet attention</code> , <code>tweet</code> being the name of the block, and <code>attention</code> the name of the add-on.</p>
  <h3>Attention</h3>
  <p>This add-on marks a block with a warning to indicate the annotator to pay special attention. For example, to illustrate that this block contains critical information or it is a source of annotation conflicts.</p>
  <p>Example:</p>
  <div markdown="1">
    ```bot
    Hello, how can I help you?
    ```
    ```human attention
    I want to report a theft of my account not foreseen 2 days ago, I doubt very much to recover it. However, if it is possible to suspend it, it would be definitely better.
    ```
    ```bot
    Please let me know your username
    ```
  </div>
  {% include image.html name="chatattention.png" caption="A warning icon appears on the top right of the block to indicate that the annotator should focus on this item." %}
</div>
<div class="one-third-col">
</div>

<div class="two-third-col">
  <h2>Suggestions</h2>
  <p>Do you have any other suggestions or requests? Write us at <a href="mailto:support@tagtog.net">support@tagtog.net</a></p>
</div>
<div class="one-third-col">
</div>
