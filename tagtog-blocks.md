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
  <br>
  <p markdown="1">Check the [align add-ons](tagtog-blocks#align-blocks) for more ideas.</p>
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
  {% include image.html name="taskblock.png" caption="A sample annotation guidelines with an example and a task for the annotators to validate their learning. Afterward, their annotations can be reviewed by a third person to track annotator's progress. Please notice in this example that you can combine <a href='MarkdownFileParsing.html#supported'>Markdown</a> and tagtog blocks." %}
</div>

<div class="one-third-col">

</div>

<div class="two-third-col">
  <h3>Meta information</h3>
  <p>Sometimes you need to add meta information to other blocks or parts of your document. This contextual information might be important for the annotation task. For example: timestamps, specific ids, etc. or any other piece of information associated to the block. </p>
  <p markdown="1">Meta blocks are not explicitly linked to other blocks, they are stand alone blocks. Therefore, meta blocks won't auto align with the blocks they refer to.</p>
  <p markdown="1">This block is not annotatable, and users cannot create any manual annotations.</p>
  <p>Code: <code>meta</code></p>
  <p>Block to define meta information.</p>

  <p>Example:</p>
  <div markdown="1">
    ```meta left
    12/11/2020 14:44:30
    ```
    ```human
    Good morning. I cannot login to my account. I see a connection error. Is your site down?
    ```
    ```meta right
    12/11/2020 14:44:35
    ```
    ```bot
    Thank you for your question. According to our status records, our site is now up and running. Can you please check again?
    ```
  </div>
  {% include image.html name="metablock.png" caption="We add the timestamp to each interaction human/bot. This information can be useful for the annotator to better understand the context. In this case, as human/bot interactions are aligned to left/right respectfully, we also added the <code>left</code> and <code>right</code> add-ons to align the meta information." %}
</div>

<div class="one-third-col">

</div>

<div class="two-third-col">
  <h3>Miscellaneous</h3>

  <h4>Quotes</h4>
  <p>Layout to display quotes.</p>
  <p>Code: <code>quote</code></p>
  <p>Block to define quotes.</p>

  <p>Example:</p>
  <div markdown="1">
    ```quote
    It is easy to hate and it is difficult to love. This is how the whole scheme of things works. All good things are difficult to achieve, and bad things are very easy to get.

    Confucius
    ```
  </div>
  {% include image.html name="quote_block.png" caption="Confucius quote. Notice the content of any block uses the <a href='ioformats.html#input-formats'><code>verbatim</code> format</a>. Therefore, all spaces, line breaks, etc. are respected." %}


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

</div>

<div class="two-third-col">
  <h2>Add-ons</h2>
  <p>Use them to modify blocks. The add-on codes come after the block code. For example: <code>tweet attention</code>, <code>tweet</code> being the name of the block, and <code>attention</code> the name of the add-on.</p>
  <h3>Attention</h3>
  <p markdown="1">This add-on marks a block with a warning to indicate the annotator to pay special attention. For example, to illustrate that this block contains critical information or it is a source of annotation conflicts.</p>
  <p markdown="1">Code: `attention`</p>

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
{% include message.html message="Tip: one block can have more than one add-on. For example: <code>task no-annotatable attention</code>"%}
</div>

<div class="two-third-col">
  <h3>Not annotatable</h3>
  <p>This add-on marks a block as not annotatable. This is useful if you don't want annotators to annotate specific parts of your document (e.g. tasks or information for annotators). Manual annotation is not possible for blocks with this add-on.</p>
  <p markdown="1">Code: `no-annotatable`</p>
  <p>Example:</p>
  <div markdown="1">
    ```task no-annotatable
    Please annotate the law provisions
    ```
    ```textbox
    The obligation to comply with European legislation derives ultimately from membership of the European Union. However, European Directives may be transposed into domestic law in different ways. This is well illustrated by the European Directive on Unfair Terms in Consumer Contracts (93/13 EEC). The first attempt to implement the Directive in domestic law showed a distinct lack of imagination, using the ‘copy out’ technique. The provisions of the Directive were simply repeated, mostly verbatim, in a statutory instrument: the Unfair Terms in Consumer Contracts Regulations 1994 (SI 1994/ 3159). The ‘copy out’ approach creates many problems as there is no attempt to integrate the measure with the existing domestic law on the subject.  These issues of integration were not addressed when the 1994 Regulations were replaced by a new statutory instrument with the same name but a different date in 1999 (SI 1999/2083).
    ```
  </div>
  {% include image.html name="noannotatable.png" caption="In this example, the user cannot annotate the content in the task block" %}
</div>
<div class="one-third-col">
<br>
{% include message.html message="Please notice that this add-on won't prevent the visualization of already existing annotations (e.g. via automatic annotations)."%}
</div>

<div class="two-third-col">
  <h3>Layout</h3>
  <p>This collection of add-ons are useful to align your blocks. For example, to align a block to the left/right or to create a multi-columns layout.</p>
</div>
<div class="two-third-col">
  <h4>Align blocks</h4>
  <p>Use this add-on to align a block to the left/right.</p>
  <p markdown="1">Codes: `left` / `right`</p>
  <p>Example:</p>
  <div markdown="1">
    ```tweet left
    The NHS has published its phase 3 implementation plan in response to the Covid-19 pandemic, including patient-initiated follow ups, the addressing of NHS inequalities and mental health planning.
    ```
    ```textbox right
    Where can I find an update?
    ```
    ```textbox right
    Well done!
    ```
    ```tweet left
    The economic impact of COVID19 on the hotel industry is the worst we have ever faced. The hotel industry is expected to lose more than fifty percent of its total revenue in 2020.
    ```
    ```textbox right
    This is the end
    ```
    ```textbox right
    We need support!!
    ```
    ```textbox right
    It is not only affecting the hotel industry. Look to the restaurants.
    ```
  </div>
  {% include image.html name="alignblocks.png" caption="In this example, tweet blocks are aligned to the left and comments for those tweets to the right" %}
</div>
<div class="one-third-col">
  <br>
  {% include message.html message="<code>left</code> or <code>right</code> add-ons will make the block <strong>float</strong>. Be aware that this state can conflict with other floating elements such as the multi-column add-ons or human/bot blocks."%}
</div>

<div class="two-third-col">
  <h4>Multi-column</h4>
  <p markdown="1">tagtog blocks supports a **grid of 12 columns**. Use these add-ons to create a **multi-column layout**. You can create horizontal groups of columns forming rows. Currently, the add-ons for grid columns are:</p>
  <p markdown="1">Codes: `col-*`</p>
  <p class="list-item" markdown="1"><span class="list-item-1"></span>`col-6`: for **two-column layout**. Each block takes up 6 grid columns. 2 blocks will require the whole 12 (6*2) grid columns.</p>
  <p class="list-item" markdown="1"><span class="list-item-2"></span>`col-4`: for **three-column layout**. Each block takes up 4 grid columns. 3 blocks will require the whole 12 (4*3) grid columns.</p>
  <p class="list-item" markdown="1"><span class="list-item-3"></span>`col-3`: for **four-column layout**. Each block takes up 3 grid columns. 4 blocks will require the whole 12 (3*4) grid columns.</p>

  <p>Example:</p>
  <div markdown="1">
    ```task col-6
    当时管原惠庆长老怀着对祖庭的崇高敬意，从寺中摘了一把枣子带回日本，经过精心培育，长成了一棵枣树。(常书鸿， 李承仙， 《五台名刹画沧桑》)
    ```
    ```textbox col-6
    Then Master Sugehara had a deep respect for Zuting, picked a handful of dates from the Monastery, took back to Japan, after careful cultivation, grew into a big date tree.
    ```
    ```task col-6
    我买了六只钢笔，一共三十元，拿回家一看，都是用过了的。
    ```
    ```textbox col-6 attention
    I bought six pens which cost me thirty yuan. When I took them home, I found they were second-hand.
    ```
  </div>
  {% include image.html name="col_6_block.png" caption="In this example, the two-column layout (<code>col-6</code>) is used for a translation task. The text to translate is on the left column, the text translated is on the right column. The annotator annotates the translation of the annotated text. In addition, the translation in the second row was marked with the <code>attention</code> add-on to warn the user of a potential issue with this translation." %}
  <br>
  <br>
  <p>Example:</p>
  <div markdown="1">
    ```task col-3
    我买了六只钢笔，一共三十元，拿回家一看，都是用过了的。
    ```
    ```textbox col-3
    wo mai le liu-zhi gang-bi, yi-gong san-shi-yuan, na hui-jia yi-kan, dou-shi yong guo de le.
    ```
    ```textbox col-3
    I bought six pens, altogether thirty yuan, took home and had a look, all used.
    ```
    ```textbox col-3
    I bought six pens which cost me thirty yuan. When I took them home, I found they were second-hand.
    ```
  </div>
  {% include image.html name="col_3_block.png" caption="In this example, the four-column layout (<code>col-3</code>) is used for another translation task. The text to translate (in Chinese) is on the first column, on the second column we fid the Chinese pinyin version, on the third column we find the word-for-word English translation, and on the last column we find the acceptable English translation. The second and third column facilitate the work of the translator/annotator." %}

  <br>
  <br>

  <p>Example:</p>
  <div markdown="1">
    ```question col-6
    What type of authority are ambulatory care pharmacists given in the U.S. federal health care system?
    ```
    ```answer col-6
    Full independent prescribing authority
    ```
    ```question col-6
    In what states are pharmacist clinicians given prescriptive and diagnostic authority?
    ```
    ```answer col-6
    North Carolina and New Mexico
    ```
  </div>
  {% include image.html name="col_6_block_qa.png" caption="In this example, the 2-column layout (<code>col-6</code>) is used for a QA task. Questions on the left column, and answers on the right column." %}


</div>
<div class="one-third-col">
  {% include message.html message="You can create multiple rows of columns to create an experience closer to <strong>tables</strong>. Each row starts at the same height. See the example."%}
</div>

<div class="two-third-col">
  <h4>Align text within blocks</h4>
  <p markdown="1">Using this add-on you can align the text within your blocks to left/center/right.</p>
  <p markdown="1">Codes: `txtleft` / `txtcenter` / `txtright` </p>

  <br>

  <p>Example:</p>
  <div markdown="1">
    ```question col-6
    What type of authority are ambulatory care pharmacists given in the U.S. federal health care system?
    ```
    ```answer col-6 txtright
    Full independent prescribing authority
    ```
    ```question col-6
    In what states are pharmacist clinicians given prescriptive and diagnostic authority?
    ```
    ```answer col-6 txtright
    North Carolina and New Mexico
    ```
  </div>
  {% include image.html name="col_6_block_qa_txtright.png" caption="In this example, the 2-column layout is used for a QA task. Questions on the left column, and answers on the right column. On the answer columns, the text is aligned to the right." %}


</div>

<div class="two-third-col">
  <h3>Colors</h3>
  <h4>Background color</h4>
  <p>Using these add-ons you can set/overwrite the background color of a block. Currently, there is a set of predefined colors.</p>
  <p>Available codes:</p>
  <p class="list-item" markdown="1"><span class="list-item-1" style="background: #454545;"></span>Black: `colblack`</p>
  <p class="list-item" markdown="1"><span class="list-item-2" style="background: #fddbdb;"></span>Red: `colred`</p>
  <p class="list-item" markdown="1"><span class="list-item-3" style="background: rgb(214, 255, 176)"></span>Green: `colgreen`</p>
  <p class="list-item" markdown="1"><span class="list-item-4" style="background: rgb(250, 252, 150)"></span>Yellow: `colyellow`</p>
  <p class="list-item" markdown="1"><span class="list-item-5" style="background: rgb(196, 246, 255)"></span>Blue: `colblue`</p>
  <p class="list-item" markdown="1"><span class="list-item-6" style="background: #fcfcfc; border: 1px solid #aba8a8;"></span>White: `colwhite`</p>

  <h4>Text color</h4>
  <p>Using these add-ons you can set/overwrite the color of the text in a block. The default color is black. Currently, there is a set of predefined colors.</p>
  <p>Available codes:</p>
  <p class="list-item" markdown="1"><span class="list-item-1" style="background: #b94b18;"></span>Red: `txtred`</p>
  <p class="list-item" markdown="1"><span class="list-item-2" style="background: #189b44;"></span>Green: `txtgreen`</p>
  <p class="list-item" markdown="1"><span class="list-item-3" style="background: #fcfcfc; border: 1px solid #aba8a8;"></span>White: `txtwhite`</p>

  <br>
  <br>
  <p>Example: dark mode for fake news</p>
  <div markdown="1">
    ```textbox colblack txtwhite attention
    The law would instantly transform all martial arts instructors into criminal felons. This includes instructors who teach kickboxing, BJJ, Krav Maga, boxing and even Capoeira.

    It would also criminalize all firearms training classes, including concealed carry classes. It would even criminalize a father teaching his own son how to use a hunting rifle.

    Specifically, the law says that a person “is guilty of unlawful paramilitary activity” (a class 5 felony) if that person:
    “Assembles with one or more persons for the purpose of training with, practicing with, or being instructed in the use of any firearm, explosive, or incendiary device, or technique capable of causing injury or death to persons…”

    The phrase “technique capable of causing injury or death to persons” covers all forms of martial arts and self-defense training, including Krav Maga, BJJ, boxing and other contact martial arts such as Tae Kwon Do or Tai Chi.

    Under the proposed law, all forms of self-defense training, including hand-to-hand martial arts training, would be considered “paramilitary activity,” even if the training consists of private classes involving just one instructor and one student. That’s because every form of martial arts training imparts skills which could be used to cause injury to other persons.

    In fact, according to the language of the law, just “one” person learning such arts is a felony crime, which means that watching a DVD on Krav Maga would be a felony crime.
    ```
  </div>
  {% include image.html name="color_block.png" caption="In this example, a <code>textbox</code> uses the add-ons <code>colblack</code> and <code>txtwhite</code> to customize the colors of the block. In this example, the annotator labels specific fragments that identify this news as fake news. It has also been marked with the add-on <code>attention</code> to highlight that this news might be fake." %}
  <h3>Fonts</h3>
  <p>Use these add-ons to customize the font of your block.</p>
  <h4>Font family</h4>
  <p>Set/overwrite the font family of a block. Currently, there is one predefined font.</p>
  <p>Available codes:</p>
  <p class="list-item" markdown="1"><span class="list-item-1"></span>Courier (typewriter/machine): `txtmachine`. Example: <span style="font-family: Courier">This is a piece of meta information</span>.</p>
</div>
<div class="one-third-col">
  {% include message.html message="You can create multiple rows of columns to create an experience closer to <strong>tables</strong>. Each row starts at the same height. See the example."%}
</div>

<div class="two-third-col">
  <h2>Combining blocks</h2>
  <p markdown="1">You can combine tagtog blocks and also combine it with other [markdown content](MarkdownFileParsing.html#supported).</p>
  <p>Example:</p>
  <div markdown="1">
    ## Fake news detection: identifying fake news

    1. Is the story unbelievable?
        If it’s so incredible that you cannot believe it, you shouldn’t.  Alternatively, if is confirms your worst nightmares, you should research it deeper to find supporting or contradictory evidence.

    2. Does the story match the headline?
        This is an example of clickbait used to pass biased or fake news to unsuspecting readers.

    3. What is the timing of the story?
        If the article is describing things that will happen, you should be skeptical.  You should also double-check that this isn’t an old story.  Many sites take stories or pictures from a few years ago and revamp them to fit in with a headline from a current date.

    4. Is the story attacking a generic enemy?
        Good reporting will not make generalizations and will be specific about who they are criticizing.  Be skeptical for vague references, such as the left or Washington.

    5. Is there only one incredible fact?
        If the story tries to prove or disprove something  based on only one encompassing fact, treat it as a warning sign.  Look for supporting evidence and links to reputable news outlets.

    6. Who is accountable for this information?
        All media is vulnerable to mistaken facts and news.  However, reputable news sources take accountability for their stories.  Biased and fake news outlets often do not take the same steps towards accountability, even going as far as giving fake contact information.

    ## Tasks

    ### Tweet annotation

    ```task
    Review the predictions from these two models. Leave only those annotations that represent a false statement.
    ```

    ```tweet col-6
    We at Snapchat are now legally authorized to give photos and other evidence associated with an open court case if requested by legal authorities. If you would wish to opt. out of this option tag #teamsnapchat on your snap story so that we know who wish to be left out of our option panel. Deadline is September 5th. Happy Snapping.
    - Snapchat team
    ```
    ```tweet col-6
    We at Snapchat are now legally authorized to give photos and other evidence associated with an open court case if requested by legal authorities. If you would wish to opt. out of this option tag #teamsnapchat on your snap story so that we know who wish to be left out of our option panel. Deadline is September 5th. Happy Snapping.
    - Snapchat team
    ```

    ### Image classification in news

    ```task
    Does this image represent this news? Please set the document label "isImageTrue" to "Yes", "Not sure" or "No"
    ```

    ```textbox col-6
    Last Tuesday people from Madrid left their cities due to the imminent declaration of state of emergency. The Spanish government plans to impose a 15-day state of emergency in the region of Madrid on Friday, a week after a court struck down the previous measures aimed to curb the spread of coronavirus.
    October 12, 2020, Madrid
    ```

    ![This is an image](https://mypictures/traffic-jam.jpg)

  </div>

  {% include image.html name="fakenews_example_blocks.png" caption="This example shows how to combine components from the Markdown specification and tagtog blocks. In this case, we implemented a flow to review model predictions for fake news in a human-in-the-loop process." %}

</div>
<div class="one-third-col">
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Caveats</h2>
    <p class="list-item" markdown="1"><span class="list-item-1"></span>tagtog blocks cannot be nested within each other. For example, you cannot create a `task` block inside a `textbox` block.</p>
    <p class="list-item" markdown="1"><span class="list-item-2"></span>While you can combine any tagtog block or add-ons together (e.g. `task` + `question left warning` + `textbox right`), be aware that some of these have a predefined style that might conflict visually with other blocks.</p>
  </div>
  <div class="one-third-col">
  </div>

  <div class="two-third-col">
    <h2>Suggestions</h2>
    <p>Do you have any other suggestions, feedback or requests? Write us at <a href="mailto:support@tagtog.net">support@tagtog.net</a></p>
  </div>
  <div class="one-third-col">
  </div>
</div>
