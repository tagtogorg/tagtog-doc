[< Back to index](../tagtog-doc)



# Accepted input formats

* TOC
{:toc}

## Files

You can upload files you have on your computer. Formats accepted:

* **.xml**
  * [NCBI Journal Publishing Tag Set](http://jats.nlm.nih.gov/publishing/) (versions JATS 1.0 and NLM 2.x and 3.0). This includes all [PLOS journals](http://www.plos.org/) or [F1000Research articles](http://f1000research.com/).
  * [BioMed Central format](http://www.biomedcentral.com/about/xml). This includes all articles in [BioMed Central](http://www.biomedcentral.com/), [ChemistryCentral](http://www.chemistrycentral.com/), or [SpringerOpen](http://www.springeropen.com/), among others.
* **.txt** any plain text file (article sections are not recognized).
* **.pdf** (sections are not recognized. Currently, the text content is just stripped out.).
* **.html** (sections are not recognized. Currently, the text content is just stripped out.).

## Bundle files
* ~~**.tar.gz** bundle of files with accepted format~~ coming soon!
* ~~**.zip**. bundle of files with accepted format~~ coming soon!

## Raw
* **Text**: plain text, just copy and paste the text you want to analyze.
* **PMID** (PubMed Id): [PubMed](https://www.ncbi.nlm.nih.gov/pubmed) is a free online database of references on life sciences. Each record in the PubMed database is assigned a special number to identify it. This is the PMID. Any PMID is only a number, e.g. [`12781165`](https://www.ncbi.nlm.nih.gov/pubmed/12781165). It also accepts inputs as: `PMID12781165 `. You can introduce a list of documents separated by comma and each of them will be uploaded. e.g. `25821226,12781165`. You can find this id at the bottom of the document at PubMed.
* **PMCID** (PubMed Central Id): [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)® (PMC) is a free archive of biomedical and life sciences journal literature at the U.S. National Institutes of Health's National Library of Medicine (NIH/NLM). Each record in the PubMed Central database is assigned a special number to identify it. This is the PMCID. Any PMCID is a number plus the `PMC `prefix, e.g. [`PMC165443`](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC165443/). You can introduce a list of documents separated by comma and each of them will be uploaded. e.g. `PMC165443,PMC165213`. You can find this id usually at the top of the document at PubMed Central. This feature relies on PubMed provider.
* **URL**: web address pointing to a web resource or document. e.g. `http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000245.v1.p1`. This is an experimental feature and you may find visualization problems depending on the web resource being analyzed.
