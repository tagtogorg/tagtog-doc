---
layout: page
title: Inputs & Outputs
sidebar_link: true
id: formats
toc: true
---

<div class="page-section">
  <h2>Input formats</h2>
  <div class="two-third-col">
    <h3>Raw</h3>
    <table style="width:100%">
      <tr>
        <th>Input type</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>Text</td>
        <td>Plain text.</td>
      </tr>

      <tr>
        <td>File</td>
        <td><a href="#files">See below for the supported formats</a></td>
      </tr>

      <tr>
        <td>URL</td>
        <td>Web address pointing to any website. e.g. <code>http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000245.v1.p1</code>. This is an experimental feature and you may find errors rendering the text depending on the HTML being analyzed.</td>
      </tr>

      <tr>
        <td>PMID</td>
        <td><a href="https://www.ncbi.nlm.nih.gov/pubmed">PubMed</a> is a free online database of references on life sciences. Each record in the PubMed database is assigned a special number to identify it. This is the PMID. Any PMID is only a number, e.g. <code><a href="https://www.ncbi.nlm.nih.gov/pubmed/12781165">12781165</a></code>. It also accepts inputs as: <code>PMID12781165</code>. You can introduce a list of documents separated by comma and each of them will be uploaded. e.g. <code>25821226,12781165</code>. You can find this id at the bottom of the document at PubMed.</td>
      </tr>
      <tr>
        <td>PMCID</td>
        <td><a href="https://www.ncbi.nlm.nih.gov/pmc/">PubMed Central®</a> (PMC) is a free archive of biomedical and life sciences journal literature at the U.S. National Institutes of Health's National Library of Medicine (NIH/NLM). Each record in the PubMed Central database is assigned a special number to identify it. This is the PMCID. Any PMCID is a number plus the <code>PMC</code> prefix, e.g. <code><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC165443/">PMC165443</a></code>. You can introduce a list of documents separated by comma and each of them will be uploaded. e.g. <code>PMC165443,PMC165213</code>. You can find this id usually at the top of the document at PubMed Central. This feature relies on the availability of the PubMed provider.</td>
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
    <p>You can import files to tagtog. Following are the supported formats.</p>

    <h4>Default-distinguish format by file extension</h4>

    <p>The format is automatically recognized by the file extension; no other parameter is needed.</p>

    <table style="width:100%">
      <tr>
        <th>File extension</th>
        <th>Description</th>
      </tr>

      <tr>
        <td><code>txt</code></td>
        <td>Any plain text file</td>
      </tr>

      <tr>
        <td><code>md</code> (Markdown)</td>
        <td><span markdown="1">Any markdown file, supporting a subset of the CommonMark spec. [Go to documentation](MarkdownFileParsing).</span></td>
      </tr>

      <tr>
        <td><code>pdf</code></td>
        <td><span markdown="1">Two variants are possible: **NativePDF** (supported on Cloud-Large and On-Premises ML only) to annotate directly on top of the PDF, and **Simple** to annotate on a stripped out plain text representation of the PDF.</span></td>
      </tr>

      <tr>
        <td><code>html</code></td>
        <td>Sections are not recognized. Currently, the text content is just stripped out.</td>
      </tr>

      <tr>
        <td><code>csv</code> and <code>tsv</code></td>
        <td><span markdown="1">[Go to documentation](CsvFileParsing).</span></td>
      </tr>

      <tr>
        <td>source code files</td>
        <td>Supported programming language extensions include: <code>.c, .coffee, .cpp, .cs, .css, .diff, .go, .h, .java, .js, .jsx, .less, .log, .m, .matlab, .mm, .patch, .php, .pl, .py, .python, .r, .rb, .sass, .scala, .sh, .shell, .sql, .swift, .ts, .tsx, .vb</code></td>
      </tr>

      <tr>
        <td><code>xml</code></td>
        <td><p><a href="http://jats.nlm.nih.gov/publishing/">NCBI Journal Publishing Tag Set</a> (versions JATS 1.0 and NLM 2.x and 3.0). This includes all <a href="http://www.plos.org/">PLOS journals</a> or <a href="http://f1000research.com/">F1000Research articles</a>.</p>
            <p><a href="http://www.biomedcentral.com/about/xml">BioMed Central format</a>. This includes all articles in <a href="http://www.biomedcentral.com/">BioMed Central</a>, <a href="http://www.chemistrycentral.com/">ChemistryCentral</a>, or <a href="http://www.springeropen.com/)">SpringerOpen</a>, among others.</p></td>
      </tr>

      <tr>
        <td>Annotation input formats</td>
        <td><a href="#annotation-input-formats">See below</a></td>
      </tr>      
    </table>


    <h4>Distinguish format by given <code>format</code> parameter</h4>

    <p>Currently only available via API, use the <a href="API_documents_v1.html#import-annotated-documents-post"><code>format</code> parameter</a> to "force" the format.</p>

    <table style="width:100%">
      <tr>
        <th>Format</th>
        <th>Description</th>
      </tr>

      <tr>
        <td><code>verbatim</code></td>
        <td>ANY file that will be parsed as already pre-formatted. No transformation is done at all to the given content. This is ideal, for instance, for files that contain arbitrary indentation or white spaces. <a href="API_documents_v1.html#examples-send-plain-text-as-verbatim">Example</a>.</td>
      </tr>

      <tr>
        <td>Annotation input formats</td>
        <td><a href="#annotation-input-formats">See below</a></td>
      </tr>      
    </table>


  </div>
  <div class="one-third-col">
    <div class="message">
      All input types can be imported through the <strong>user interface</strong> or the <strong>API</strong>.
    </div>
  </div>


  <div class="two-third-col">
    <h3>Bundle files</h3>
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


</div>
<div class="page-section">
  <h2>Annotation input formats</h2>
  <div class="two-third-col">
    <p>You can import files with annotations. This is useful if you want to import documents that were annotated outside tagtog (for example by your own machine learning model) or you want to update the annotations for a specific document.</p>
    <table style="width:100%">
      <tr>
        <th>Format</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><code>anndoc</code></td>
        <td><p>Use the <a href="anndoc.html">anndoc format</a> to upload the via API both, the <code>plain.html</code> and its annotations <code>ann.json</code>). <a title="tagtog - How to upload annotated documents?" href="API_documents_v1.html#replace-annotations-of-existing-document-post">Example</a>.</p></td>
      </tr>
      <tr>
        <td><code>default-plus-annjson</code></td>
        <td><p>To upload via API both: text (TXT files, PDF, etc. Check the <a href="ioformats.html#input-formats">input formats</a>) and its annotations <code>ann.json</code>. <a title="tagtog - How to upload annotated documents?" href="API_documents_v1.html#import-annotated-documents-post">Example</a>.</p></td>
      </tr>
      <tr>
        <td><code>verbatim-plus-annjson</code></td>
        <td><p>Analogous to <em>default-plus-annjson</em>, and complimentary to the <code>verbatim</code> format, use this format to parse any given file as <em>verbatim</em> accompanied with its annotation file (with ann.json extension). <a href="API_documents_v1.html#examples-import-pre-annotated-verbatim-text">Example</a>.</p></td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">

  </div>
</div>

<div class="page-section">
  <h2>Output formats</h2>
  <br/>
  <div class="two-third-col">
    <table style="width:100%">
      <tr>
        <th>Format</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><code>ann.json</code></td>
        <td>Only annotations. <a title="tagtog - ann doc" href="/anndoc.html">Official documentation</a></td>
      </tr>
      <tr>
        <td><code>plain.html</code>, <code>html</code>, <code>xml</code></td>
        <td>No annotations provided within this format, only content.</td>
      </tr>
      <tr>
        <td><code>txt</code></td>
        <td>Plain text. No annotations provided within this format, only content.</td>
      </tr>
      <tr>
        <td><code>entitiestsv</code></td>
        <td><a href="/EntitiesTsv">EntitiesTsv documentation</a> (annotation format, with both plain content and annotations)</td>
      </tr>
      <tr>
        <td><code>entitiesonlyclassestsv</code></td>
        <td><a href="/EntitiesOnlyClassesTsv">EntitiesOnlyClassesTsv documentation</a> (annotation format, with both <em>partial</em> plain content and annotations)</td>
      </tr>

      <tr>
        <td><code>pubannotation</code></td>
        <td><span class="soon"><a href="http://www.pubannotation.org/docs/annotation-format/">Official documentation</a></span> (annotation format, with both plain content and annotations) Coming soon</td>
      </tr>
    </table>
  </div>
  <div class="one-third-col">

  </div>
  <div class="two-third-col">
    <h2>Other formats?</h2>

    <p markdown="1">We are currently experimenting with other formats to ease your work. [Stay tuned :smirk::bird:](https://twitter.com/tagtog_net).</p>
  </div>

</div>
