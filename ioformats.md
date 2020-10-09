---
layout: page
title: Inputs & Outputs
sidebar_link: true
id: formats
toc: true
---

<div class="page-section">
  <h2>Input types</h2>
  <p>This is the type of content you can import to tagtog.</p>
  <div class="two-third-col">
    <table style="width:100%">
      <tr>
        <th>Input type</th>
        <th>Description</th>
        <th>Default <code>format</code></th>
      </tr>
      <tr>
        <td>Text</td>
        <td>Plain text.</td>
        <td><code>verbatim</code></td>
      </tr>
      <tr>
        <td>File</td>
        <td><a href="#files">See below for the supported file types</a></td>
        <td>See below for the default formats for each file type. You can import one or more files in a single request.</td>
      </tr>
      <tr>
        <td>URL</td>
        <td>Web address pointing to any website (e.g. <code>http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000245.v1.p1</code>) or resource (e.g. <code>https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf</code>).</td>
        <td><p><a href="#files">See below the default format that is associated to the file type</a> of the file the URL is pointing to.</p> E.g. if the URL points to a text file or a PDF file, the text file or PDF file is imported to tagtog and the default format used accordingly. If the URL points to an HTML file, the text is stripped from the HTML content and imported to tagtog. The format used is the default format for the <code>html</code> file type.</td>
      </tr>
      <tr>
        <td>PMID</td>
        <td><a href="https://www.ncbi.nlm.nih.gov/pubmed">PubMed</a> is a free online database of references on life sciences. Each record in the PubMed database is assigned a special number to identify it. This is the PMID. Any PMID is only a number, e.g. <code><a href="https://www.ncbi.nlm.nih.gov/pubmed/12781165">12781165</a></code>. It also accepts inputs as: <code>PMID12781165</code>. You can introduce a list of documents separated by comma and each of them will be uploaded. e.g. <code>25821226,12781165</code>. You can find this id at the bottom of the document at PubMed.</td>
        <td>Bio XML format</td>
      </tr>
      <tr>
        <td>PMCID</td>
        <td><a href="https://www.ncbi.nlm.nih.gov/pmc/">PubMed Central®</a> (PMC) is a free archive of biomedical and life sciences journal literature at the U.S. National Institutes of Health's National Library of Medicine (NIH/NLM). Each record in the PubMed Central database is assigned a special number to identify it. This is the PMCID. Any PMCID is a number plus the <code>PMC</code> prefix, e.g. <code><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC165443/">PMC165443</a></code>. You can introduce a list of documents separated by comma and each of them will be uploaded. e.g. <code>PMC165443,PMC165213</code>. You can find this id usually at the top of the document at PubMed Central. This feature relies on the availability of the PubMed provider.</td>
        <td>Bio XML format</td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
    <div class="message">
      All input types can be imported through the <strong>user interface</strong> or the <strong>API</strong>.
    </div>
  </div>
  <div class="two-third-col">
    <h3>Files</h3>
    <p>You can import files to tagtog. Following are the supported file types.</p>
    <table style="width:100%">
      <tr>
        <th>File extension</th>
        <th>Description</th>
        <th>Default <code>format</code></th>
      </tr>
      <tr>
        <td><code>txt</code></td>
        <td>Any plain text file</td>
        <td><code>verbatim</code></td>
      </tr>
      <tr>
        <td><code>md</code> (Markdown)</td>
        <td><p><span markdown="1">Any Markdown file, supporting a subset of the CommonMark spec. [Go to documentation](MarkdownFileParsing).</span></p>
            <p>Using Markdown you can also use <a href="tagtog-blocks">tagtog blocks</a> to build a customized annotation layout for your project! E.g. question answering datasets, chatbot training, tweets, etc.</p>
        </td>
        <td><code>markdown</code></td>
      </tr>
      <tr>
        <td><code>pdf</code></td>
        <td><span markdown="1">Two variants are possible: **NativePDF** (supported on Cloud-Large and On-Premises ML only) to annotate directly on top of the PDF, and **Simple** to annotate on a stripped out plain text representation of the PDF.</span></td>
        <td><p>Native PDF format if native PDF is activated </p><p>Simple PDF format if native PDF is not activated</p></td>
      </tr>
      <tr>
        <td><code>html</code></td>
        <td>Sections are not recognized. Currently, the text content is just stripped out.</td>
        <td>HTML format</td>
      </tr>
      <tr>
        <td><code>csv</code> and <code>tsv</code></td>
        <td><span markdown="1">[Go to documentation](CsvFileParsing).</span></td>
        <td>CSV format or TSV format</td>
      </tr>
      <tr>
        <td>source code files</td>
        <td>Supported programming language extensions include: <code>.c, .coffee, .cpp, .cs, .css, .diff, .go, .h, .java, .js, .jsx, .less, .log, .m, .matlab, .mm, .patch, .php, .pl, .py, .python, .r, .rb, .sass, .scala, .sh, .shell, .sql, .swift, .ts, .tsx, .vb</code></td>
        <td><code>markdown</code></td>
      </tr>
      <tr>
        <td><code>xml</code></td>
        <td><p><a href="http://jats.nlm.nih.gov/publishing/">NCBI Journal Publishing Tag Set</a> (versions JATS 1.0 and NLM 2.x and 3.0). This includes all <a href="http://www.plos.org/">PLOS journals</a> or <a href="http://f1000research.com/">F1000Research articles</a>.</p>
            <p><a href="http://www.biomedcentral.com/about/xml">BioMed Central format</a>. This includes all articles in <a href="http://www.biomedcentral.com/">BioMed Central</a>, <a href="http://www.chemistrycentral.com/">ChemistryCentral</a>, or <a href="http://www.springeropen.com/)">SpringerOpen</a>, among others.</p>
        </td>
        <td>Bio XML format</td>
      </tr>
    </table>
    </div>
    <div class="one-third-col">
      <div class="message">
        All input types can be imported through the <strong>user interface</strong> or the <strong>API</strong>.
      </div>
      <div class="message">
        The format is <strong>automatically recognized</strong> by the file extension; no other parameter is needed.
      </div>
    </div>
    <div class="two-third-col">
      <h4>Bundle files</h4>
      <table style="width:100%">
        <tr>
          <th>File extension</th>
          <th>Description</th>
        </tr>
        <tr>
          <td><code>tar.gz</code></td>
          <td><span class="soon">tarball gzip. Bundle of files with accepted format.</span> Coming soon.</td>
        </tr>
        <tr>
          <td><code>zip</code></td>
          <td><span class="soon">zip file. Bundle of files with accepted format.</span> Coming soon</td>
        </tr>
      </table>
    </div>

  <div class="one-third-col">

  </div>
  <div class="two-third-col">
    <h2>Input formats</h2>
    <p>If there is no format specified, the default format for the content imported is used.</p>
    <p>In the API, use the <a href="API_documents_v1.html#import-annotated-documents-post"><code>format</code> parameter</a> to set the format. In the GUI, open the Advanced options under the upload panel to select a format. In both ways, you explicitly "force" tagtog to represent the content by the format selected.</p>
    <p>Below you find the different formats. There are formats that are used when you import <strong>only content</strong>, and other formats that you should use when you import <strong>pre-annotated</strong> content. The latter is useful if you want to import documents that were annotated outside tagtog (for example by your own machine learning model) or you want to update the annotations for a specific document.</p>
    <table style="width:100%">
      <tr>
        <th>Content</th>
        <th>Format</th>
        <th>Description</th>
      </tr>
      <tr>
        <td rowspan="3">Only content</td>
        <td><code>verbatim</code></td>
        <td>Parsed as already pre-formatted. <strong>No transformation is done at all to the given content</strong>. This is ideal, for instance, for files that contain arbitrary indentation or white spaces. It creates one single block with the whole the content. It is the simpler option if you are dealing with plain text or simple text files. <a href="API_documents_v1.html#examples-send-plain-text-as-verbatim">Example</a>.</td>
      </tr>
      <tr>
        <td><code>markdown</code></td>
        <td>The content is expected to follow the <a href="MarkdownFileParsing.html">markdown syntax</a>. The content will be formatted and visualized as markdown (e.g. you can include images, different sections, lists, code blocks, etc.).</td>
      </tr>
      <tr>
        <td><code>formatted</code></td>
        <td><p>The <strong>content is formatted and cleaned</strong>. For example, for each paragraph, one content part is created . Ideal if your content has different discourse units. For example: chat bots conversations.</p>
        <p>Up to the tagtog version <a href="updates.html#32020-w301-">3.2020-W30.1</a> this was the default mode when a user imported plain text. If using the API, you want to pre-annotate with annotations created in this period of time, please use <code>formatted-plus-annjson</code>. See below.</p></td>
      </tr>
      <tr>
        <td rowspan="5">Pre-annotated content</td>
        <td><code>default-plus-annjson</code></td>
        <td><p>Use it if you are importing pre-annotated documents (content + <code>ann.json</code>) and you want the <strong>content to be recognized using the default format</strong>.</p><p>For example to import pre-annotated PDFs, plain text or markdown files.</p><p>Choose this option if you are not sure which format to use when sending pre-annotated documents.</p><p><a title="tagtog - How to upload annotated documents?" href="API_documents_v1.html#examples-import-pre-annotated-plain-text-file">Example</a></p></td>
      </tr>
      <tr>
        <td><code>verbatim-plus-annjson</code></td>
        <td><p>Analogous to <code>default-plus-annjson</code>, and complimentary to the <code>verbatim</code> format. Use it if you are sending pre-annotated content (content + <code>ann.json</code>) and you want to force the content to be recognized with the <code>verbatim</code> format.</p></td>
      </tr>
      <tr>
        <td><code>formatted-plus-annjson</code></td>
        <td><p>Analogous to <code>default-plus-annjson</code>, and complimentary to the <code>formatted</code> format. Use it if you are sending pre-annotated content (content + <code>ann.json</code>) and you want the content to be recognized with the <code>formatted</code> format (instead of the default).</p><p><a href="API_documents_v1.html#examples-import-pre-annotated-formatted-text">Example</a></p></td>
      </tr>
      <tr>
        <td><code>nativepdfv1-plus-annjson</code></td>
        <td><p>Analogous to <code>default-plus-annjson</code>, and complimentary to the <code>nativepdfv1</code> format. Use this format when you have old annotations you want to import to tagtog, and these were created using the <a href="pdf-annotation-tool.html">PDF native editor</a>.</p>
        <p>You can verify which format was originally used in the <code>plain.html</code> file. If you don't have access to this information, assume that any native PDF annotations generated up to the <a href="updates.html#32020-w282-">3.2020-W28.2</a> version should use this format.</p></td>
      </tr>
      <tr>
        <td><code>anndoc</code></td>
        <td>Use the <a href="anndoc.html">anndoc format</a> to import a pre-annotated <code>plain.html</code> (<code>plain.html</code> + <code>ann.json</code>). <a title="tagtog - How to upload annotated documents?" href="API_documents_v1.html#replace-annotations-of-existing-document-post">Example</a>.</td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">
    <div class="message">
      In the GUI, it is not necessary to specify a pre-annotated format, it is recognized automatically that you are importing content + annotations.
    </div>
  </div>




</div>


<div class="page-section">
  <h2>Output formats</h2>
  <div class="two-third-col">
    <p>Find below the available output formats in tagtog. Some of these outputs are available through the GUI and others through the API.</p>
  </div>
  <div class="two-third-col">
    <table>
      <tr>
        <th>Format</th>
        <th>Description</th>
        <th>Type</th>
        <th>GUI</th>
        <th>API</th>
      </tr>
      <tr>
        <td><code>ann.json</code></td>
        <td>This is the official format for annotations. It supports all the annotation tasks in tagtog. <a title="tagtog - ann doc" href="/anndoc.html">Documentation</a>.</td>
        <td>Only annotations</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>entitiestsv</code></td>
        <td>Tabulated annotation format, with both plain content and annotations. It closely resembles the output by the Stanford NER tool. <a href="/EntitiesTsv">Documentation</a>.</td>
        <td>Content + annotations</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>entitiesonlyclassestsv</code></td>
        <td>Tabulated annotation format, with both <em>partial</em> plain content and annotations. Similar to <code>entitiestsv</code>. The non-labeled text is not included, and it supports <a href="webeditor.html#overlapping-text-annotations">overlapping entities</a>. <a href="/EntitiesOnlyClassesTsv">Documentation</a>.</td>
        <td>Only annotations</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>plain.html</code>, <code>html</code>, <code>xml</code></td>
        <td>This is the official representation of the content imported. Any piece of text/document you import to tagtog is converted to plain content and the annotation offsets always refer back to this format. No annotations provided within this format, only content. <a href="anndoc.html#plain-html">Documentation</a>.</td>
        <td>Only content</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>txt</code></td>
        <td>Plain text. No annotations provided within this format, only content.</td>
        <td>Only content</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>orig</code>, <code>original</code></td>
        <td>The originally submitted file (e.g. the original html or pdf document that was imported to tagtog).</td>
        <td>Only content</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>visualize</code></td>
        <td>This is the default value. Choose to visualize the document resource returning the web page directly (<code>web</code> or <code>web-editor-only</code> if the User Agent is a recognized browser and a tagtog project information was given, i.e. web, or, respectively, no tagtog project was given, i.e., <code>web-editor-only</code>) or otherwise return the <code>weburl</code> (typically, the User Agent will be a command line program).</td>
        <td>Visualization</td>
        <td class="centered">✅</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>web</code></td>
        <td>Visual representation of the document and its annotations on the tagtog web interface (HTML page).</td>
        <td>Visualization</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>web-editor-only</code></td>
        <td>Analogously as <code>web</code>, yet without the information of a tagtog project, i.e., only the document editor layout. Useful in case you want to create iFrames in your web app.</td>
        <td>Visualization</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>weburl</code></td>
        <td>URL of the annotated document at tagtog web interface.</td>
        <td>Visualization</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>csv</code></td>
        <td>List of the project's documents and the status of their <code>master</code> (ground truth) annotation version. Currently, it only works with a search query (i.e. with the API parameter <code>search</code>).</td>
        <td>Search</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
      </tr>
      <tr>
        <td><code>null</code></td>
        <td>Special output to signify that no document output is desired. A JSON response of the request will be returned instead. For example, when importing a document:
<div markdown="1">
```javascript
{
  "ok":1 //number of documents successfully changed,
  "errors":0 //number of documents with errors,
  "items": //list of documents changed
  [
    { "origid":"text",
      "names":["text.txt"],
      "tagtogID":"aOM6EFIvULWc6J.7MAYQB3V2sF84-text",
      "result":"created"}
  ],
  "warnings":[]
}
```
<p>You can use this parameter, for example, if you need the API to return you the id of each document imported.</p>
</div>
        </td>
        <td>Operation result</td>
        <td class="centered">❌</td>
        <td class="centered">✅</td>
      </tr>
    </table>
    <p>All output formats are returned in their latest format versions. The output format versions cannot be chosen.</p>
  </div>
  <div class="two-third-col">
    <h2>Other formats?</h2>
    <p markdown="1">We are currently experimenting with other formats to ease your work. [Stay tuned :smirk::bird:](https://twitter.com/tagtog_net).</p>
  </div>
</div>
