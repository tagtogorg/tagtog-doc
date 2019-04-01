---
layout: page
title: PDF annotation tool
sidebar_link: true
id: pdfann
toc: true
---
<div class="page-section">
  <div class="two-third-col">
    <h2>Introduction</h2>

    <p>The Portable Document Format, or PDF is one of the most popular file formats. <strong>PDFs are everywhere</strong>.</p>
    <blockquote>PDF has become a de facto global standard for more secure and dependable information exchange since Adobe published the complete PDF specification in 1993. Both government and private industry have come to rely on PDF for the volumes of electronic records that need to be more securely and reliably shared, managed, and in some cases preserved for generations.</blockquote>
    <p>— An excerpt from the <a title="Adobe - Document management — Portable document format" href="https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf">ISO 32000-1 standard</a></p>
    <p>As you can imagine, if you work with text, sooner or later you will need to deal with PDFs. However, it's still a format that causes headaches for people trying to add or extract knowledge to/from them. That's why we have built a PDF annotation tool integrated within tagtog. Our goal is to <strong>facilitate the processing of PDFs for entity/relations extraction, document classification,manual annotation and other tasks</strong>.</p>

  </div>
  <div class="one-third-col">
    {% include image.html name="icon-pdf.png" width=150 %}
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>How does it look?</h2>

    <p>It is the same web interface as in tagtog, but annotating directly over the native PDF :book:</p>
    <p>You can annotate any text in the PDF: captions, text in images, figures, tables, etc. Just make sure the text is not an image itself.</p>
    <br>

    {% include image.html name="pdf-annotation.jpg"  caption="Annotate titles, figures, tables, forms, etc." %}

  </div>
  <div class="one-third-col">
  <br><br>
  {% include image.html name="front-pdf-annotation.jpg" caption="Beautiful and engaging for annotators" %}
  </div>
  <div class="two-third-col">
    <h3>Document navigation</h3>
    <p>You can navigate by just <strong>scrolling</strong> with your mouse or clicking on the arrows on the toolbar. {% include inline-image.html name="pdf-navigation.png" width="100" %} If you want to go to a specific page, just write the page number in the page text box and press enter <kbd>↵</kbd>. The page navigation will float when you scroll down a document to allow you change the page at any moment.</p>
  </div>
  <div class="one-third-col">

  </div>
</div>


<div class="page-section">
  <div class="two-third-col">
    <h2>Annotations</h2>
    <p>tagtog uses two different measures to locate annotations done over native PDFs. Both are contained in each annotation:</p>
    <p class="list-item"><span class="list-item-1"></span><strong>Text offsets</strong>. Each annotation is located using the start offset of its text in reference to the beginning of the page containing the annotation. In order to do that, we transform each page of the PDF into text and save the result in the <code><a title="tagtog - ann.doc - plain.html format" href="anndoc.html#plain-html">plain.html format</a></code>. We use this file as a reference to calculate the offset of the annotations. You can <a title="tagtog - web editor - view output mode" href="webeditor.html#view-output-mode">download and use this file</a> to share a common interface with tagtog. Offsets take into account the reading order of elements such as tables or columns.</p>
    <p class="list-item"><span class="list-item-2"></span><strong>Coordinates</strong>. Each annotation is located using the coordinates of the bounding box containing the annotation. Currently, each annotation uses a pair of coordinates (X, Y) corresponding to the top-left of the first character of the annotation and the bottom-right of the last character of the annotation. In order to facilitate translation, <strong>coordinates are expressed in Points(pt)</strong>. 1pt is equal to exactly 1/72th of an inch. The coordinates system has its 0,0 position in the top left of each page.</p>
  </div>
  <div class="one-third-col"></div>
</div>


<div class="page-section">
  <div class="two-third-col">
    <h2>How does it help you?</h2>
    <p>Processing PDF files is a painful process full of tears. To solve this, we have built a PDF annotation tool. This is how it can help you:</p>
    <p class="list-item"><span class="list-item-1"></span><strong>Annotate over the PDF</strong>. Annotate directly over the native PDF layout. PDF files contain figures, pictures, tables, etc. Stripping only the text, you destroy part of the original context reducing the global understanding of the document.</p>
    <p class="list-item"><span class="list-item-2"></span><strong>Train your own models easily</strong>. Annotate native PDFs; then use them to train your ML models as easily as if they were plain texts! :open_mouth: Find below how and forget about processing PDFs yourself.</p>
    <p class="list-item"><span class="list-item-3"></span><strong>Fully integrated</strong>. The PDF annotation tool is a web component fully integrated with tagtog. Annotate relations, document labels, entity labels, etc.</p>
    <p class="list-item"><span class="list-item-4"></span><strong>Annotate any text</strong> Sometimes image captions are important, text in tables is critical, etc. Don't miss this important source of knowledge, now you can annotate these and any other text that you find in the PDF.</p>
  </div>
  <div class="one-third-col">
    <div class="message">
      Annotators love to annotate using the PDF layout, this is the way they are used to work! :sparkling_heart:
    </div>
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Training your model to process PDF files</h2>
    <p class="numbered-item"><span class="number-1">1</span><strong>Annotate using the PDF annotation tool</strong>. Import a PDF and annotate it using the native layout.</p>
    <p class="numbered-item"><span class="number-2">2</span><strong>Download the plain text and annotations</strong>. Use the <a title="tagtog - API - Get existing documents" href="API_documents_v1.html#get-existing-documents-get">API</a> or <a title="tagtog - web editor - view output mode" href="webeditor.html#view-output-mode">user interface</a> to download both: the <code><a title="tagtog - ann.json format" href="anndoc.html#ann-json">ann.json</a></code> with the annotations and the <code><a title="tagtog - plain.html format" href="anndoc.html#plain-html">plain.html</a></code> with the plain text. The offsets from the annotations refer to the plain text.</p>
    <p class="numbered-item"><span class="number-3">3</span><strong>Train your model</strong>. Use the annotations and the plain text to train your model.</p>
    <p class="numbered-item"><span class="number-4">4</span><strong>Import new PDFs with the annotations from your model</strong>. Import the PDFs to tagtog and download the plain texts using the API or user interface, use this easy to digest text as an input for your model. Now <a title="tagtog - API - Import annotated documents" href="API_documents_v1.html#import-annotated-documents-post">push the resulting annotations</a> to tagtog. <a title="tagtog - Train your own models" href="train-your-own-models.html">More information</a>.
    You can automate this process using <a title="tagtog - project - webhooks" href="projects.html#webhooks">Webhooks</a>, so each time a PDF is imported, you get automatically the plain.html file, the annotations are generated right away and pushed to tagtog. </p>
    <p class="numbered-item"><span class="number-5">5</span><strong>Continuosly train your model</strong>. Annotators review the annotations from your model over the native PDF layout and correct them. You can use the new <code>ann.json</code> files to update your model and increase the accuracy of your predictions over time.</p>

  </div>
  <div class="one-third-col">
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>How to activate this feature?</h2>
    <p><strong>By default this feature is turned off</strong>. You can change this setting differently for each project. To activate this feature follow <a title="tagtog - Activate PDF native tool" href="projects.html#pdf">these instructions</a>.</p>
  </div>
  <div class="one-third-col">
    <div class="message">The PDF annotation tool is only available in some plans. Check the <a title="tagtog - plans" href="https://tagtog.net/-pricing">available features for each plan</a>.</div>
  </div>
</div>

<div class="page-section">
  <div class="two-third-col">
    <h2>Caveats</h2>
    <p class="list-item"><span class="list-item-1"></span>You cannot create an annotation with one piece in one page and the other piece in the next page. The main constraint is that the PDF footer interferes when creating an annotation across two pages.</p>
    <p class="list-item"><span class="list-item-2"></span>Currently, <a title="tagtog - preannotations" href="webeditor.html#pre-annotations">pre-annotations</a> are not available with this new layout.</p>
  </div>
  <div class="one-third-col">
  </div>
</div>
