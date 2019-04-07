---
layout: page
title: anndoc format
sidebar_link: true
version: 2.0
id: anndoc
toc: true
---

<div class="two-third-col">
  <p><code>anndoc</code> is a standoff format for document annotations consisting of two files:</p>
  <table style="width:100%;">
    <tr>
      <th>File</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>ann.json</code></td>
      <td>Annotations-only, part of the format.</td>
    </tr>
    <tr>
      <td><code>plain.html</code></td>
      <td>Content-only, part of the format.</td>
    </tr>
  </table>



</div>
<div class="one-third-col">
  {% capture version %}<strong>Version</strong>: <code>{{ page.version }}</code>{% endcapture %}
  {% include message.html message=version %}
</div>


<div class="two-third-col">
  <h3><code>ann.json</code></h3>
  <p>An <code>ann.json</code> can represent the 5 annotation types listed below. Each annotation type is identified by a prefix and an id (e.g. <code>e_1</code>). This value is unique in a project and cannot be changed.</p>
  <table style="width:100%;">
    <tr>
      <th>Prefix</th>
      <th>Name</th>
    </tr>
    <tr>
      <td class="centered"><code>m_</code></td>
      <td>Meta (a.k.a. Document Label)</td>
    </tr>
    <tr>
      <td class="centered"><code>e_</code></td>
      <td>Entity type (a.k.a Entity class)</td>
    </tr>
    <tr>
      <td class="centered"><code>r_</code></td>
      <td>Relation</td>
    </tr>
    <tr>
      <td class="centered"><code>f_</code></td>
      <td>Field (a.k.a. Entity Label)</td>
    </tr>
    <tr>
      <td class="centered"><code>n_</code></td>
      <td>Normalization</td>
    </tr>
  </table>

</div>
<div class="one-third-col">
  {% include message.html message="The names of the annotation types are not used in this format. E.g. entity type <code>gene</code> has the id <code>e_1</code>. <code>e_1</code> will be used in this format, not <code>gene</code>" %}
</div>


<div class="two-third-col">
  <h4>Properties</h4>
  <p>Let's take a deeper look at the format.</p>
  <table style="width:100%;">
    <tr>
      <th>Property</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>annotatable</code></td>
      <td>Array of document <code>partId</code>'s (relative to the <code>plain.html</code>). Indicates what document parts can be annotated. Document parts are identified by an id. Example: <code>s3s1f1p2</code> (section 3, subsection 1, figure 1, paragraph 2).
      <p><code>s</code>section or subsection, <code>h</code>header, <code>p</code>paragraph, <code>f</code>figure</p>
      </td>
    </tr>
    <tr>
      <td><code>anncomplete</code></td>
      <td>Boolean value indicating whether the document's annotations are complete. The user sets this value from the user interface and depending on them, "complete" may mean that the document has been reviewed, or simply it has been annotated.</td>
    </tr>
    <tr>
      <td><code>sources</code></td>
      <td><p>Array of collection sources that this documents can be associated to. E.g. a URL with the source of the text.</p>
      <p>Common current uses are to have the sources: ORIG (for the original source of the document) and PMID (for PubMed).</p></td>
    </tr>
    <tr>
      <td><code>metas</code></td>
      <td>Map object with Document labels (also known as metas) set in the document. Each meta describes the value and the confidence of the annotation.</td>
    </tr>
    <tr>
      <td><code>entities</code></td>
      <td>Array of entities annotated in the document. Entities are relative to a part (typically paragraph or header) of the <code>plain.html</code>.
        <p><code>classId</code> entity type id (a.k.a. entity class id)</p>
        <p><code>offsets</code>entitiy's offsets relative to the part of text. Support for entities spanning divided words like "North America" in "North and South America". The whole text is encoded within the array. Note that the end offset is implicitly defined as <code>start</code> + <code>text.size</code></p>
        <p><code>confidence</code> each entity has a <code>confidence</code> object attached to represent the probability of this annotation.</p>
      </td>
    </tr>
    <tr>
      <td><code>fields</code></td>
      <td>Map object with Entity Labels (also known as fields) attached to an entity.</td>
    </tr>
    <tr>
      <td><code>normalizations</code></td>
      <td><p>Map object with the normalizations attached to an entity (also known as fields).</p>
          <p>The <code>source</code> object defines the dictionary used (<code>name</code>) and the <code>id</code> the entity is normalized to.</p>
          <p><code>recname</code> is the first or most recommended name of the normalized entity.</p>
          <p><code>confidence</code> each normalization has a <code>confidence</code> object attached to represent the probability of this annotation.</p>
      </td>
    </tr>
    <tr>
      <td><code>relations</code></td>
      <td><p>Array of relations (of entities) annotated in the document. Note that <code>type</code> and <code>directed</code> properties are already defined by this relation's type. They may be deleted in the future. However, so far they are here written explicitly to make this file's annotations as self-contained as possible.</p>
      <p><code>classId</code> relation type (a.k.a. relation class) id</p>
      <p><code>type</code> <code>linked</code>, <code>part-of</code>, <code>anaphora</code> or user-defined.</p>
      <p><code>directed</code> boolean value indicating the direction of the relation. <code>true</code> if A->B or B<-A, <code>false</code> if A<->B</p>
      <p><code>entities</code> identifies the entities related converting their partId + offsets to a hash string. Format: <code>partId|e_id|start,end</code>. E.g. <code>["s1p1|e_1|9,17", "s1p1|e_3|55,62"]</code> For the moment we expect relations of 2 entities only (that is, no 3 or more). However, the array format is flexible to support more in the future.</p>
      <p><code>connectingWords</code> the connecting words tell whether there is evidence that some words, typically verbs, supports the argument that the entities are related. This can be `null` if none.</p>
      <p><code>confidence</code> each relation has a <code>confidence</code> object attached to represent the probability of this annotation.</p>
      </td>
    </tr>
    <tr>
      <td><code>confidence</code></td>
      <td><p><code>state</code> can be empty (manual annotation) or have the following values: <code>pre-added</code> (automatic annotation or pre-annotation -preselected-), <code>pre-removed</code> (pre-annotation -predeselected-).</p>
      <p><code>who</code> string array. Each string represents who performed the annotation. Possibly multiple actors, prefixed by either <code>ml:</code> (automatic annotation or pre-annotation) or <code>user:</code> (manual annotation).</p>
      <p><code>prob</code> aggregated probability between all actors.</p>
      </td>
    </tr>
    <tr>
      <td><code>source</code></td>
      <td><p><code>name</code> source's name. E.g. Wikipedia</p>
          <p><code>id</code> unique id within source. E.g. Barack_Obama</p>
          <p><code>url</code> url of id. E.g. <a href="https://en.wikipedia.org/wiki/Barack_Obama">https://en.wikipedia.org/wiki/Barack_Obama</a></p>
      </td>
    </tr>
  </table>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
<div markdown="1">
```javascript
{   //v{{ page.version }}

    "annotatable": {
        "parts": [string...] //Array of of partId's
    },
    "anncomplete": boolean,

    "sources": [
        { //Source prototype
            "name": string,
            "id": string, // `null` for unknown
            "url": string // `null` for unknown or not given
        }, ...
    ],

    // Map object with Document Labels
    "metas": {
        "m_<uniq>": {
            "value": boolean/number/string,
            "confidence": { //Confidence prototype
                "state": string, //in {"", "pre-added", "pre-removed"} ; "" or null == regular state
                "who": [string...], //prefixed by either "ml:" (machine learning) or "user:"
                "prob": double //in [0, 1] -- aggregated probability between all actors;
            }
        }, ...
    },

    // Array of entities annotated in the document
    "entities": [
        {
            "classId": "e_<uniq>",

            "part": string,

            "offsets": [{"start": int, "text": string}, ...],

            "confidence": Confidence,

            //Map object with Entity labels
            "fields": {
                "f_<uniq>": {
                    "value": string,
                    "confidence": Confidence
                }, ...
            },

            //Map object with Document Labels
            "normalizations": {
                "n_<uniq>": {
                    "source": Source,
                    "recName": string,
                    "confidence": Confidence
                }, ...
            }
        }
    ],

    //Array of relations annotated in the document
    "relations": [
        {
            "classId": "r_<uniq>",
            "type": string, //in standards={linked, part-of, anaphora} or user-defined
            "directed": boolean, //true if A->B or B<-A, false if A<->B
            "entities": [string, string], //entities related hashed
            "connectingWords": [{"start": int, "text": string}, ...],
            "confidence": Confidence
        }
    ]
}
```
</div>
</div>
<div class="one-third-col">
</div>


<div class="two-third-col">
<h3><code>plain.html</code></h3>
<p>This part of the <code>anndoc</code> format covers only the content, not the annotations. It's written in <a href="https://www.w3.org/TR/html-polyglot/" title="Polyglot Markup: A robust profile of the HTML5 vocabulary">polyglot markup</a> (XML-compatible HTML5). There are no special semantics other that every text element (paragraph, header, ...) has a unique id. These ids are used as a reference by the annotations file.</p>
</div>
<div class="one-third-col">
  {% include message.html message="Every time you import a file or text into tagtog, the input content is <strong>converted</strong> to this format." %}
</div>
<div class="two-third-col">
<p>Find below an example of a <code>plain.html</code> file representing the content of a document.</p>
<div markdown="1">
```html
<!DOCTYPE html >
<html id="4ae5a3ffbd0e0d5b74c5790d0f6e0954:1471-2229-8-71" data-origid="1471-2229-8-71" class="anndoc" data-anndoc-version="2.0" lang="" xml:lang="" xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta charset="UTF-8"/>
    <meta name="generator" content="com.jmcejuela.bio.BioMedCentralArticleParser_v0_2$"/>
    <meta name="dcterms.source" content="http://www.biomedcentral.com/1471-2229/8/71"/>
    <title>4ae5a3ffbd0e0d5b74c5790d0f6e0954:1471-2229-8-71</title>
  </head>
  <body>
    <article>
      <section data-type="title">
        <h2 id="s1h1">Expression of cell wall related genes in basal and ear internodes of silking brown-midrib-3, caffeic acid O-methyltransferase (COMT) down-regulated, and normal maize plants</h2>
      </section>
      <section data-type="abstract">
        <h2 id="s2h1">Abstract</h2>
        <div class="subsections">
          <section data-type="">
            <h3 id="s2s1h1">Background</h3>
            <div class="content">
              <p id="s2s1p1">Silage maize is a major forage and energy resource for cattle feeding, and several studies have shown that lignin content and structure are the determining factors in forage maize feeding value. In maize, four natural brown-midrib mutants have modified lignin content, lignin structure and cell wall digestibility. The greatest lignin reduction and the highest cell wall digestibility were observed in the brown-midrib-3 (bm3) mutant, which is disrupted in the caffeic acid O-methyltransferase (COMT) gene.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s2s2h1">Results</h3>
            <div class="content">
              <p id="s2s2p1">Expression of cell wall related genes was investigated in basal and ear internodes of normal, COMT antisens (AS225), and bm3 maize plants of the INRA F2 line. A cell wall macro-array was developed with 651 gene specific tags of genes specifically involved in cell wall biogenesis. When comparing basal (older lignifying) and ear (younger lignifying) internodes of the normal line, all genes known to be involved in constitutive monolignol biosynthesis had a higher expression in younger ear internodes. The expression of the COMT gene was heavily reduced, especially in the younger lignifying tissues of the ear internode. Despite the fact that AS225 transgene expression was driven only in sclerenchyma tissues, COMT expression was also heavily reduced in AS225 ear and basal internodes. COMT disruption or down-regulation led to differential expressions of a few lignin pathway genes, which were all over-expressed, except for a phenylalanine ammonia-lyase gene. More unexpectedly, several transcription factor genes, cell signaling genes, transport and detoxification genes, genes involved in cell wall carbohydrate metabolism and genes encoding cell wall proteins, were differentially expressed, and mostly over-expressed, in COMT-deficient plants.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s2s3h1">Conclusion</h3>
            <div class="content">
              <p id="s2s3p1">Differential gene expressions in COMT-deficient plants highlighted a probable disturbance in cell wall assembly. In addition, the gene expressions suggested modified chronology of the different events leading to cell expansion and lignification with consequences far beyond the phenylpropanoid metabolism. The reduced availability of monolignols and S units in bm3 or AS225 plants led to plants also differing in cell wall carbohydrate, and probably protein, composition. Thus, the deficiency in a key-enzyme of the lignin pathway had correlative effects on the whole cell wall metabolism. Furthermore, the observed differential expression between bm3 and normal plants indicated the possible involvement in the maize lignin pathway of genes which up until now have not been considered to play this role.</p>
            </div>
          </section>
        </div>
      </section>
      <section data-type="">
        <h2 id="s3h1">Background</h2>
        <div class="content">
          <p id="s3p1">Since shortly after its introduction into Europe, maize has been recognized to be an excellent forage plant and is now the most important annual forage crop in Northern Europe. Despite the fact that maize silage provides roughage with high energy content, large genetic variations in cell wall digestibility have been established between maize genotypes [1]. The lignified grass cell wall is a composite material with cellulose microfibrils, an amorphous matrix consisting of hemicelluloses (mainly glucurono-arabinoxylans) with very little pectins, and phenolics. Phenolics are comprised of lignins, which are essential for the structural integrity of tissues and impart hydrophobicity to vascular elements. They also are comprised of cell wall-linked p-coumaric (pCA) ferulic, and diferulic acid derivatives. Lignins are the only cell wall component resistant to micro-organism degradation. Hence, lignin content is a primary factor involved in cell wall digestibility variation. In addition, lignin variable structure and the intensity of cross-linkages between cell wall components also have variable depressive effects on cell wall carbohydrate degradation by microorganisms in the cow rumen. [2-4]. The lignin pathway begins after the shikimate pathway with the deamination of L-phenylalanine into cinnamic acid. Successive steps including hydroxylation and methylation on the aromatic ring lead to production of three monolignols (p-hydroxyphenyl, coniferyl, and syringyl alcohols). The latter are polymerized into lignins, giving rise to the three p-hydroxyphenyl (H), guaiacyl (G) and syringyl (S) monomeric units. In the maize lignin pathway, caffeic acid O-methyltransferase (COMT) is specifically involved in methylation of 5-hydroxy-coniferaldehyde into sinapaldehyde.</p>
          <p id="s3p2">Besides the reddish brown pigmentation of the leaf midrib and stalk pith associated with lignified tissues, brown-midrib (bm) mutants of maize were early distinguished by their lower lignin content and modified lignin structure [5-7]. Among the four non-allelic bm mutants, bm3 exhibits the strongest phenotype and was early considered to be a powerful model in cell wall digestibility improvement and lignification studies [8-12]. Compared with normal hybrids, cell wall digestibility of isogenic bm3 genotypes was increased by about 9 percentage points [1]. Correlatively, and based on several experiments with lactating cows [13-15], the intake of bm3 silage by dairy cows was always higher than the intake of normal silage (1.5 to 2.5 kg DM per day). A higher milk yield of cows fed bm3 hybrids was also reported in most experiments. Every time this trait was recorded, an increase in body weight was also observed in cattle fed with bm3 silage. However, the bm3 mutation has adverse effects on agronomic traits such as lower biomass yield and higher susceptibility to lodging and diseases, especially in early maize genetic backgrounds. As a consequence, only a few late maize hybrids are available for farmers on the US market [16-18].</p>
          <p id="s3p3">Since the precursory studies done from 1960 to 1970, extensive research has been devoted to maize bm3 plants in order to establish the key determining factors in their higher feeding value, with an in- depth description of their specific lignification patterns [2,19-21]. The lignin content of maize bm3 mutant plants is reduced by about 25 to 40 %, with a partly correlative reduced content of pCA esters by about 50 %. In the sixties, Kuc et al. [7] established that the frequency of S units was reduced in bm3 mutants, and they suspected the occurrence of additional not yet detected units. The thioacidolysis S/G ratio was shown to be reduced from 1.2 – 1.5 in normal plants to 0.2 – 0.5 in bm3 plants, and the additional units in lignins were identified as 5-hydroxyguaiacyl (5-OH-G) units [22]. The reduction in pCA esters thus appeared consistent with the preferential acylation of S units by p-coumaric acid [23-25]. The content of alkali-releasable FA in bm3 mature plants was not altered [2,26]. In younger plants, Marita et al. [27] obtained a greater amount of FA esterified to arabinoxylans in the bm3 cell walls. However, similar cross-linking between arabinoxylans (total FA dimers) was obtained.</p>
          <p id="s3p4">A nearly null COMT activity has been shown in maize bm3 plants [28-30]. Vignols et al. [29] and Morrow et al. [30] later established that bm3 mutants had an altered exon 2 of the COMT gene, with different events likely corresponding to different insertions/excisions of a transposable element. Down-regulation of COMT in maize gave plants with similar lignin patterns as observed in bm3 mutants [31,32]. In Arabidopsis, a lignin devoid of S units was observed due to a mutation in the gene encoding ferulate 5-hydroxylase (F5H) [33,34], while the Arabidopsis &quot;bm3&quot; mutant lacking the following COMT step in the pathway only had a reduced S content [35]. Only one COMT sequence is described in databases for maize, and a unique COMT in maize would seem to be the most probable hypothesis to date. The presence, even clearly reduced, of S units in bm3 lignins then raises a question about a substitutive pathway, and/or a substitutive OMT. In contrast to S unit content, normal ferulic acid content was observed in bm3 or AS225 plants, showing that COMT is very likely not involved in its biosynthesis. Ferulic acid biosynthesis in maize is still not clearly understood and different putative pathways have been discussed recently [36]. Based on the data of Nair et al. [37] with the ref1 mutant of Arabidopsis, ferulic acid could be produced in maize beyond the monolignol pathway. Ferulic acid could be derived from oxidation of the corresponding aldehyde, rather than acting as a precursor of this aldehyde.</p>
          <p id="s3p5">In contrast to phenolic compounds, only a few changes in cell wall carbohydrate characteristics were observed in bm3 plants. The cellulose content of bm3 maize was nearly the same as in normal plants, and the hemicellulose content was reported to be slightly or significantly higher in bm3 plants [20]. The composition of hemicelluloses also appeared to be little modified in bm3 plants. In plant stalks with just emerging tassels, Marita et al. [27,38] found a higher xylan content (as estimated by xylose) in bm3 mutants. Similarly, the xylan substitution with arabinose was a little lower in bm3 maize than in normal maize. A minor but significant decrease was also observed for rhamnose in bm3 plants [27].</p>
          <p id="s3p6">Little data is available on histological comparisons of normal and bm3 tissues. Based on scanning electron microscopy observations [39], the sclerenchyma of bm3 stem tissues appeared less dense, less rigid and less thick, with larger cell lumens than in normal plants. Moreover, the parenchyma of bm3 plants was more rapidly degraded in rumen fluid and the sclerenchyma walls were highly degraded and considerably thinned in bm3 plants. In contrast, the sclerenchyma of normal plants was little changed even after 72 hours of incubation in the rumen fluid.</p>
          <p id="s3p7">In a study devoted to a comparison of 144 cell wall gene expressions in 20-day-old normal and bm plants [40], only seven genes were differentially expressed in the bm3 mutant. The seven genes were all over-expressed except for the disrupted COMT. Gene expression was also investigated in young stems of three normal and bm3 lines. The latter were harvested 5 and 7 weeks after germination, with a micro-array containing nearly 12,000 ESTs [41,42]. Out of 865 candidate ESTs putatively involved in cell wall digestibility variation, only 53 were differentially expressed between bm3 and normal isogenic plants.</p>
          <p id="s3p8">The first objective of the present study was to investigate variations in expression of cell wall related genes in older and more lignified tissues of bm3, COMT down-regulated, and normal silking maize plants. Investigations were based on ear (young) and basal (old) internodes which differ in their physiological maturity. A second objective was to relate variation in gene expression to the previously described modifications in cell wall components, lignin content and structure of bm3 and COMT down-regulated plants. A third objective was to find new factors involved in maize cell wall lignification and assembly, in order to further improve forage maize feeding value. Expression studies were based on a macro-array specifically devoted to cell wall and lignification topics developed in CNRS-UPS Toulouse for such investigations [43].</p>
        </div>
      </section>
      <section data-type="">
        <h2 id="s4h1">Results and Discussion</h2>
        <div class="subsections">
          <section data-type="">
            <h3 id="s4s1h1">Lignin pathway gene expression in normal F2 basal and ear internodes of maize</h3>
            <div class="content">
              <p id="s4s1p1">Older and younger lignification stages were compared in basal and ear internodes of the F2 normal line. All genes known to be involved in constitutive monolignol biosynthesis had a higher expression in younger ear internodes, indicating their higher lignification activity, than in older basal internodes (data not shown). An expression at least three times higher was thus observed for genes encoding phenylalanine ammonia-lyases (PAL), cinnamate 4-hydroxylases (C4H), 4-coumarate:CoA ligases (4CL), caffeoyl-CoA O-methyltransferases (CCoAOMT), F5H, COMT, cinnamoyl-CoA reductases (CCR), cinnamyl and sinapyl alcohol dehydrogenases (CAD and SAD). Expressions of hydroxycinnamoyl transferases (HCT) and p-coumaroyl-shikimate/quinate 3'-hydroxylases (C3'H) genes were low, raising the possibility of other still unknown homolog genes involved in the pathway. Among the five maize CCoAOMT genes shown to be expressed in maize by Guillaumie et al. [43], the most expressed genes were CCoAOMT5 and CCoAOMT3 in ear and basal internodes, respectively. Previously described CCoAOMT2 [44] was the second most expressed gene in younger internodes and in older ones. Laccase genes were more expressed than peroxidase genes, and more expressed in older internodes, probably confirming the involvement of laccases in monolignol polymerization. However, three peroxidases, including ZmPox2 and ZmPox3, had a reverse expression pattern and were more expressed in younger tissues. These peroxidases could be assumed to be more specifically involved in the first steps of cell wall assembly.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s2h1">Lignin content and cell wall digestibility in COMT under-expressed and disrupted plants</h3>
            <div class="content">
              <p id="s4s2p1">Cell wall content was a little lower in AS225 basal internodes, which is likely related to a higher soluble carbohydrate content in this line. Lignin content, estimated as Klason lignin [45] in the cell wall part was reduced by 45 % in both F2bm3 and AS225 basal internodes, with a correlative average increase by 30 % in cell wall digestibility, estimated as in vitro neutral detergent fiber (NDF) digestibility [46].</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s3h1">Histochemical staining and lignin pattern alterations in bm3 or AS225 internodes</h3>
            <div class="content">
              <p id="s4s3p1">At silking + 30 days stage of plant growth, histological observations showed that xylem, sclerenchyma and parenchyma between vascular bundles were lignified. Internodal transverse sections stained with Maüle reagent, which enables to distinguish between S and G units, showed important differences between F2, AS225 and bm3 lines (Figure 1A–C). All lignified tissues in F2 plants exhibited a red coloration, showing the presence of S units, whereas in bm3 line both sclerenchyma and parenchyma between bundles had a brown coloration, underlying an absence of S units in both of these cell types. In AS225 plants, lignified parenchyma cells stained red, similar to F2 line, but sclerenchyma cells surrounding vascular bundles displayed an orangey color. This difference probably indicated a sclerenchyma-specific reduction of S units in AS225 line and highlighted the fact that using Adh1 promoter directs COMT down-regulation specifically in sclerenchyma tissues [31].</p>
              <figure data-origid="F1">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/figure/F1">Figure 1</a>
                <figcaption>
                  <h5 id="s4s3f1h1">Histochemical characterization of normal F2, AS225 and F2bm3 maize lines</h5>
                  <p id="s4s3f1p1">microscopy observations of transverse sections in bottom part of ear internode in silking +30 day-old plants stained with Maüle reagent (A-B). Light microscopy observations of transverse sections in bottom part of ear internode in silking plants stained with Wiesner reagent (D, F, H). UV illumination of ear internode bottom part in silking plants (E, G, I). Differences in coloration of lignified tissues between F2, AS225 and F2bm3 lines in the presence of Maüle reagent (A-C) are visible. Metaxylem vessels of ear internode transverse sections (D-I) of AS225 and F2bm3 plants also had a modified lignification (arrow). x = xylem; s = sclerenchyma; p = parenchyma; pp = protophloem; px = protoxylem; mx = metaxylem. Magnification bar was 100 μm (A-C) or 50 μm (D-I).</p>
                </figcaption>
              </figure>
              <p id="s4s3p2">At silking stage, Wiesner staining (Figure 1D, F and 1H) and UV-light (Figure 1E, G, I) observations of the bottom part of ear internode cross sections showed that protoxylem is lignified in all observed lines. Metaxylem vessels are lignified in F2 line but were only weakly lignified in bm3 plants and not lignified in AS225 plants.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s4h1">Lignin and phenylpropanoid pathway gene differential expression in bm3 or AS225 internodes</h3>
            <div class="content">
              <p id="s4s4p1">The expression of the COMT gene was, as expected, heavily reduced in COMT-disrupted and down-regulated plants. In younger lignifying tissues of the ear internode, COMT expression was reduced to a nearly null value in bm3 plants. Despite transgene, was driven only in sclerenchyma tissues of AS225 plants, COMT under-expression was reduced by 80 % in AS225 ear internodes (Table 1, Figure 2). COMT expression was reduced by 20–25 % in both bm3 and AS225 basal internodes (Table 1). More genes were differentially expressed in younger ear internodes than in older basal internodes. In addition, the pattern of gene deregulation was almost similar in bm3 and AS225 plants. However, a lower number of genes were differentially expressed in AS225 plants and their expressions were less modified than in bm3 plants. Disruption or down-regulation of COMT led to a differential expression of a limited number of genes related to the phenylpropanoid pathway, which were all over-expressed, except a PAL gene in bm3 plants. The small number of differentially expressed genes has also been observed in younger growing bm3 plantlets [40], illustrating a possible weak apparent co-regulation of lignin pathway genes at these developmental stages. Contrary results were obtained by Shi et al. [41] in a F2/F2bm3 comparison, with differentially expressed lignin pathway genes most often under-expressed in bm3 plants, except for two cytochrome P450 98A1 (C3'H) over-expressed genes. Observed differences could be related to variable stages of sampling and cropping conditions, and to a different set of investigated genes.</p>
              <figure class="table" data-origid="T1">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/table/T1">Table 1</a>
                <figcaption>
                  <h5 id="s4s4f1h1">Phenylpropanoid and lignin pathway genes differentially expressed in maize F2, F2bm3 and AS225 basal and ear internodes at silking stage.</h5>
                </figcaption>
              </figure>
              <figure data-origid="F2">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/figure/F2">Figure 2</a>
                <figcaption>
                  <h5 id="s4s4f2h1">RT-PCR expression analysis of three genes of phenylpropanoid and lignin pathway</h5>
                  <p id="s4s4f2p1">Transcripts of PAL (2161072.2.1, L77912), CCoAOMT3 (2591258.2.1, AY104670) and COMT (2192909.2.3, M73235) were detected by semi-quantitative RT-PCR in ear internodes from normal, bm3 and AS225 silking stage plants. 18S rRNA was used as a quantitative control.</p>
                </figcaption>
              </figure>
              <p id="s4s4p2">Besides the under-expressed COMT gene, the &quot;new&quot; CCoAOMT3 and CCoAOMT4 genes were over-expressed in young ear internodes, while the two currently known CCoAOMT1 and CCoAOMT2 were not differentially expressed (Table 1, Figure 2). CCoAOMT enzymes have a strict affinity for CoA-ester and have no or very little affinity on corresponding acids [36,47-49]. Consequently, it could not be considered that the two CCoAOMT substitute the missing COMT activity in the biosynthesis, of about a 40 % residual S content in bm3 plants [2]. The missing COMT activity was probably substituted by other OMT, whether they are over-expressed or not. Plausible candidates include ZRP4-like OMT. Several ZRP4-like OMT genes were indeed shown to be significantly expressed in stalk lignifying tissue [43], and their role is likely not limited to methylation of suberin sub-unit precursors as initially described by Held et al. [50]. Moreover, two ZRP4-like OMT genes were over-expressed in bm3 plantlets [40], including the AY108765 ZRP4-like OMT which also have a tendency to be over-expressed in ear internodes of bm3 silking plants with a ratio equal to 1.71. Unlike the under-expressed COMT, one F5H gene, whose encoded protein supplies COMT in its 5-hydroxy-coniferaldehyde substrate, has an increased expression in older internodes of bm3 and AS225 plants. However, this is not the case in younger ear internodes.</p>
              <p id="s4s4p3">A PAL/TAL gene, which encodes the entry enzyme of the phenylpropanoid pathway, had a greatly reduced expression in F2bm3 ear internodes and, to a lesser extent, in basal internodes. However, the expression was not reduced in AS225 internodes (Table 1, Figure 2). A low PAL expression was in agreement with the much lower lignin content of bm3 stalk tissues. In contrast to PAL, a C4H and a 4CL gene, whose encoded proteins catalyzed the following steps of the pathway, were over-expressed in bm3 young internodes. Also in contrast to PAL under-expression, a chorismate mutase was over-expressed in the youngest internodes of both bm3 and AS225 plants, upstream in the phenylpropanoid pathway. In the shikimic acid pathway, chorismate mutase is the enzyme which catalyzes the first committed step in phenylalanine and tyrosine biosynthesis [51,52]. This allows the intra-molecular rearrangement of the enolpyruvyl chain of chorismate to produce prephenate. The chorismate mutase/prephenate dehydratase gene over-expressed in the ear internode of bm3 possibly encoded a bifunctional chorismate mutase/prephenate dehydratase as observed by Fischer et al. [53], but its involvement as a precursor supplier for lignin biosynthesis is still unknown.</p>
              <p id="s4s4p4">The ZmPox2 peroxidase gene, whose encoded protein is involved in constitutive lignification [54], had an increased expression in bm3 and AS225 plants, especially in younger internodes. Simultaneously with the higher ZmPox2 expression, two laccase genes were similarly over-expressed in bm3 young internodes, and one in AS225 plants. These maize laccases were close orthologs to the poplar lac3 gene, whose down-regulation in poplar induced an important alteration of xylem fiber cell walls, with an increase in soluble phenolic compounds, especially in xylem parenchyma cells [55].</p>
              <p id="s4s4p5">According to Nair et al. [37], sinapic and probably ferulic acids in Arabidopsis derived from oxidation of the corresponding aldehydes, rather than acting as precursors of those aldehydes. A putative involvement of aldehyde dehydrogenase (ALDH) enzymes in maize ferulate biosynthesis has not yet been established. However, several ALDH genes are expressed in lignifying tissue [43] including the ALDH22A1 Arabidopsis ortholog [56,57] over-expressed in COMT deficient tissues, which was also the most expressed ALDH in normal internodes. While the lignin content of bm3 maize plants was greatly reduced, their content in ferulates released after alkaline hydrolysis was not modified or slightly increased [2].</p>
              <p id="s4s4p6">The maize chalcone flavonone isomerase (ZmCHI1), described in maize by Grotewold and Peterson [58], was over expressed in bm3 and AS225 internodes. CHI catalyzes conversion of chalcone, a yellow pigment synthesized downstream to the coumaroyl-CoA, into naringenin. CHI genes are regulated by MYB transcription factors [58-60], similarly to several other phenylpropanoid-related genes. Because ZmCHI1gene is not involved in the lignin pathway, its over-expression could be interpreted as a possible reaction against over-availability of monolignol precursors.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s5h1">Differential expression of transcription or regulation factor genes in bm3 or AS225 internodes</h3>
            <div class="content">
              <p id="s4s5p1">Several transcription or regulation factors, including one ATHB-8 HD-zip III, two Argonaute, and one Shatterproof MAD-box ortholog gene, were over-expressed in both ear and basal internodes of bm3 and, to a lesser extent, AS225 silking plants (Table 2). These transcription factors were not differentially expressed in bm3 plantlets. However, some of the transcription factors were under-expressed in bm1, bm2, and/or bm4 plantlets [40]. Homeodomain-leucine zipper (HD-Zip) III proteins are transcription factors which belong to a class of highly related proteins characterized by their expression in (pro)-vascular tissues. ATHB-8 HD-Zip proteins are positively regulated by auxin and promote vascular cell division and differentiation towards the formation of xylem and vascular tissue [61,62]. Argonaute genes are required for post-transcriptional gene silencing and RNA interference, and many of the miRNA which have thus far been identified in plants are predicted to target transcription factors involved in developmental processes [63,64]. An over-expression of an Argonaute gene, as observed in bm3 and AS225 deficient COMT plants, is considered to induce a higher repression of target genes. The simultaneous differential expression of Argonaute genes and the ATHB-8 HD-Zip gene could be related. The maize rolled leaf1 gene (rld1) indeed encodes a HD-ZIP III transcription factor, the expression of which is mediated by the miRNA Zmmir166 [65]. SHATTERPROOF (SHP1) MADS-box gene is involved, with SHP2, in lignification of valve margin cells adjacent to the dehiscence zone of Arabidopsis siliques [66]. The over-expressed maize SHP1 ortholog gene was the ZmZAG5 gene which has been described with ZmZAG3 [67,68] as an AGL6-like gene (agamous-like). Whether such a SHP maize ortholog could be involved in lignified tissue differentiation or more directly in lignification, is not yet known. However, its deregulation in bm3 and AS225 tissue could for the first time illustrate a relationship between this type of regulation factor and cell wall differentiation or lignification in grass plant stalks.</p>
              <figure class="table" data-origid="T2">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/table/T2">Table 2</a>
                <figcaption>
                  <h5 id="s4s5f1h1">Cell-wall-related transcription and regulation factor genes differentially expressed in maize F2, F2bm3 and AS225 basal and ear internodes at silking stage.</h5>
                </figcaption>
              </figure>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s6h1">Differential expression of genes related to auxin signaling and tissue patterning in bm3 or AS225 internodes</h3>
            <div class="content">
              <p id="s4s6p1">Several genes related to auxin signaling, and/or probably involved in vessel set up or tissue patterning, were over-expressed in basal or ear internodes of COMT deficient plants (Table 3). This occurrence probably indicated a feedback disorganization of tissues and cell wall assembly when the activity of the key COMT enzyme was missing.</p>
              <figure class="table" data-origid="T3">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/table/T3">Table 3</a>
                <figcaption>
                  <h5 id="s4s6f1h1">Cell-wall-related genes involved in auxin signaling and tissue patterning differentially expressed in maize F2, F2bm3 and AS225 basal and ear internodes at silking stage.</h5>
                </figcaption>
              </figure>
              <p id="s4s6p2">PINOID (PID) orthologous genes, of which one member was over-expressed in basal and ear bm3 internodes, and in ear AS225 internodes, encode serine/threonine protein kinases. PID genes are preferentially expressed in the vascular tissue of developing organs and in xylem parenchyma cells [69], and have been shown to be positive regulators of polar auxin transport [69-71]. The Emb30 gene of Arabidopsis, whose maize ortholog is over-expressed in basal internodes of bm3 and AS225 plants, is involved in the maintenance of polar auxin transport. In addition, the lack of Emb30 protein induced an irregular and discontinuous venation, with clustered or scattered tracheary elements [72,73]. The Emb30 gene encodes a guanine nucleotide exchange factor (GEF) on adenosine diphosphate (ADP)-ribolysation factor GTPase (ARF-GEF), which is involved in the targeted recycling of PIN1 putative auxin efflux carrier [74]. Its over-expression in bm3 and AS225 plants was likely a consequence of tissue assembly with a reduced amount of S units. In addition, one MONOPTEROS (MP) gene ortholog was over-expressed in bm3 ear internodes. The MP gene of Arabidopsis encodes a transcription factor of the auxin response factor (ARF) family, which is also involved in vascular cell differentiation [75,76]. The Arabidopsis recessive mutant &quot;CONTINUOUS VASCULAR RING&quot; (COV1) has a great increase in stem vascular tissue in of inter-fascicular regions [77]. Moreover, it has been established that cov1 affects vascular patterning by a mechanism which is not auxin-dependant [77]. In addition, cov1 mutants were shown to be defective in synthesis, transport, or perception of an inhibitor. The maize COV1 ortholog over-expression in bm3 ear lignifying internodes thus corresponded to a higher inhibition in lignified tissue formation, possibly illustrating a feed-back effect resulting from the low availability of S units.</p>
              <p id="s4s6p3">Cucumisins are serine protease of the subtilisin family [78]. Cucumisins are involved in the general protein turn-over as non-selective enzymes, but they also perform specific roles in the processing of precursor proteins to regulate growth and development by limited proteolysis [79]. The over-expressed maize cucumisin in bm3 and AS225 ear internodes was the closest ortholog to a zinnia (Zinnia elegans Jacq.) cucumisin expressed during xylogenesis [80]. Similarly, a subtilase (XSP1, At4g00230) has been identified from a xylem library of Arabidopsis [81]. The role of cucumisins in phenylpropanoid biosynthesis is still unknown. However, it is plausible that several cucumisins could function during autolysis of tracheary elements. A cucumisin gene deregulation in bm3 internodes could be in agreement with the lower stiffness of bm3 plant vessels.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s7h1">Differential expression of transport and detoxification genes in bm3 or AS225 internodes</h3>
            <div class="content">
              <p id="s4s7p1">Four genes involved in transport and detoxification processes were over-expressed in bm3 and/or AS225 internodes (Table 4). ATP-binding cassette (ABC) transporters are involved in different physiological functions such as cell signaling, transport of a broad range of substances across membranes and detoxification processes [82,83]. Given their ability to transport a diverse set of small molecules across membranes, and because several ABC transporters had similar expression profiles to known monolignol genes along the Arabidopsis growing stem, ABC transporters were assumed to be involved in the secretion of monolignols [52,82,84]. The maize ABC transporter over-expressed in internodes of maize bm3 plants could thus be considered as a monolignol transporter. Based on its under-expression in bm2 plantlets, it has been assumed to be preferentially involved in coniferyl alcohol transport [40].</p>
              <figure class="table" data-origid="T4">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/table/T4">Table 4</a>
                <figcaption>
                  <h5 id="s4s7f1h1">Cell-wall-related genes involved in transport and detoxification processes differentially expressed in F2, F2bm3 and AS225 basal and ear internodes at silking stage.</h5>
                </figcaption>
              </figure>
              <p id="s4s7p2">Maize bronze2-like genes encode glutathione S-transferases (GST). The latter are carrier proteins [85] which deliver anthocyanins from the biosynthesis site to the tonoplast membrane, where an appropriate ABC-type transporter moves the pigment into the vacuole [86]. Because several ABC transporters have a substrate preference for glutathione conjugates [82,83,87,88], a coupled activity could be assumed between the two over-expressed ZmGST17 and ZmGST22 and the over-expressed ABC transporter. The much reduced COMT activity and S unit formation could induce the accumulation of phenolic compounds that have to be delivered into the vacuole as a detoxification process.</p>
              <p id="s4s7p3">Plant glucosyltransferases belong to a multigene family, which are likely differentially regulated in different biosynthesis pathways and in response to a range of environmental stimuli. Glucosyltransferases have relative substrate specificity because of their extended plasticity towards metabolites of related structure [89]. They are involved in the biosynthesis of secondary plant metabolites and metabolization of xenobiotics. They are known in particular to have activity on both flavonoids and p-hydroxycinnamate derivatives. In addition, a grapevine UDP-glucose:flavonoid 3-O-glucosyltransferase, has been shown to be homolog to the maize bz1 encoded protein [90]. The role of the protein encoded by the differentially expressed UDP-glucosyltransferase-like gene is still unknown, but it could possibly be involved in detoxification and/or transport processes.</p>
              <p id="s4s7p4">The role of nodulin MtN21-like genes is not yet understood, but the presence of seven transmembrane domains and structural homologies with bacterial multidrug exporters might suggest a role in a transport function. The maize nodulin MtN21-like gene over-expressed in bm3 and/or AS225 internodes was found to be orthologous to a zinnia nodulin MtN21-like gene expressed during xylogenesis. Consequently, the maize nodulin MtN21-like gene is probably involved in transport of a component related to vascular tissue assembly.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s8h1">Differential expression of cell wall associated protein genes in bm3 or AS225 internodes</h3>
            <div class="content">
              <p id="s4s8p1">Several arabinogalactan proteins (AGP) and AGP-like proteins, which belong to a class of hydroxyproline-rich glycoproteins (HRGP), have been shown to be involved in plant xylogenesis [91-93]. Some of these proteins were thus highly preferentially expressed in differentiating xylem compared with phloem [93,94]. Out of the four genes encoding cell wall proteins which were differentially expressed in bm3 or AS225 internodes (Table 5), ZmRCP1 and ZmRCP2 showed especially high over-expression ratios (up to five times higher) in ear internodes. The large differential expression values in COMT deficient plants likely indicate that these AGP genes are relevant targets in understanding maize cell wall assembly.</p>
              <figure class="table" data-origid="T5">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/table/T5">Table 5</a>
                <figcaption>
                  <h5 id="s4s8f1h1">Cell-wall associated protein genes differentially expressed in maize F2, F2bm3 and AS225 basal and ear internodes at silking stage.</h5>
                </figcaption>
              </figure>
              <p id="s4s8p2">One glycine-rich protein (GRP) was the only investigated gene with an over-expression in bm3 internodes and an under-expression in AS225 internodes. This significant interaction could be related to the lack of complete isogenicity of F2 and AS225 genetic backgrounds, but also to the fact that COMT down-regulation in AS225 was directed specifically in sclerenchyma tissues. GRP genes encode a group of cell wall structural proteins which are particularly expressed in xylem tissues [95,96]. The differentially expressed GRP gene is the closest ortholog of the rice Osgrp-2 gene (AF010580) which possesses sequence elements conferring vascular-specific expression [97].</p>
              <p id="s4s8p3">The differentially expressed proline rich protein (PRP) was one of the rare genes significantly under-expressed in COMT-deficient ear internodes. PRP are considered to be structural components of the cell wall and are abundant in fibers and xylem [98]. Vignols et al. [99] have thus described the maize ZmPRP, which is expressed in vascular tissue, mainly in cells related to xylem development, but not in phloem cells. However, the differentially expressed PRP and ZmPRP are very different genes, with only 15 % identity. The protein encoded by the under-expressed PRP gene is a basic PRP, with 26 % of proline amino acid and a peptide signal allowing protein secretion in the cell wall. It also presents a six-times repeated PPVTGPP(KG)(P)VTYPP motif, which is different from the classic PRP motif [PPVX(K/T), with X being Y, H, or E]. This PRP, which is probably involved in cell wall formation, appeared to be an original and possibly new type of cell wall PRP.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s4s9h1">Differential expression of genes involved in nucleotide sugar interconversion and cell wall carbohydrate metabolism in bm3 or AS225 internodes</h3>
            <div class="content">
              <p id="s4s9p1">The nucleotide sugar interconversion pathway comprises a set of enzymatic reactions by which plants synthesize activated monosaccharides as precursor elements of cell wall polysaccharides [100]. Nucleotide sugars are thus substrates used for the elongation of carbohydrate chains by UDP-glycosyltransferase [101,102]. Cellulose is synthesized by an enzyme complex associated with the plasma membrane, using UDP-D-glucose as a precursor. While UDP-D-glucose is also a precursor of hemicelluloses, hemicellulose polysaccharides are formed in the Golgi apparatus and are exported to the external surface of the membrane in Golgi vesicles [103].</p>
              <p id="s4s9p2">Seven genes of the nucleotide sugar interconversion pathway, which belonged to five multigene families, were over-expressed in bm3 and/or AS225 plants (Table 6). Sucrose synthases catalyze a reversible reaction giving UDP-D-glucose from sucrose and uridine diphosphate (UDP). UDP-D-glucose dehydrogenases convert UDP-D-glucose into UDP-D-glucuronic acid (UDP-D-GlcA). UDP-D-GlcA is afterwards the substrate of UDP-D-GlcA decarboxylases, giving UDP-D-xylose, which is then converted into UDP-L-arabinose in a reversible reaction catalyzed by UDP-D-xylose 4-epimerases [102]. GDP-D-mannose 4,6-dehydratase catalyzes the irreversible conversion of GDP-D-mannose into 4-keto-6-deoxy-GDP-D-mannose, then allowing the synthesis of GDP-fucose [100,102]. In plant stalks with just emerging tassels, a decrease in mannose content has been observed in bm3 plants [27], which could be related to over-expression of GDP-D-mannose 4,6-dehydratase.</p>
              <figure class="table" data-origid="T6">
                <a href="http://www.biomedcentral.com/1471-2229/8/71/table/T6">Table 6</a>
                <figcaption>
                  <h5 id="s4s9f1h1">Nucleotide sugar and cell-wall carbohydrate metabolism genes differentially expressed in maize F2, F2bm3 and AS225 basal and ear internodes at silking stage.</h5>
                </figcaption>
              </figure>
              <p id="s4s9p3">Several genes involved in cell wall modification during cell growth and vascular element formation were differentially expressed between normal and COMT deficient plants (Table 6). Expansins are involved in the disruption of hydrogen bounds between cellulose microfibrils and cross-linking glycans in the cell wall. At least five different expansin genes are expressed in differentiating tracheary elements of zinnia. These genes were associated with the intrusive growth of protoxylem and with the differentiation of mesophyll cells into tracheary elements [80]. Xyloglucan endotransglycolase/hydrolases (XTH) and glucanases modify the structure of the cell wall so that it becomes more responsive to primary wall-loosening events [104,105]. Xyloglucan binds non-covalently to cellulose, coating and cross-linking adjacent cellulose microfibrils. The resulting network is considered to be the major tension-bearing structure in the primary wall [106]. Cleavage of xyloglucan chains by hydrolytic enzyme leads to rapid wall loosening, but also induces important risks of structural failure in the absence of concomitant reinforcement. XTH, capable of splitting and reconnecting xyloglucan molecules in a new position, help to satisfy the contradictory needs of growing and/or differentiating tissues [106]. Exo and endoglucanases are involved in specific degradation of cell wall β-glucans in auxin-mediated cell elongation [107,108]. ZmGnsN1, which was over-expressed in ear internodes of bm3 and AS225 plants, encodes an endo-1,3–1,4-β-D-glucanase first found in maize seedling growing tissues [107-109]. The two other over-expressed endoglucanases were ortholog to β-1,3-glucanase, which are also considered to be involved in hydrolysis of cell components and could be induced by hormone or wounding signals [110]. An exoglucanase was also overexpressed in bm3 internodes which has been shown to preferentially hydrolyze the non-reducing terminal glucosyl residue from 1,3-β-D-glucans [111].</p>
              <p id="s4s9p4">In maize, most hemicelluloses are arabinoxylans, with a few xyloglucans which are predominant in primary walls of dicotyledons. Xyloglucans have a backbone composed of β-1,4-glucose with up to 75% of the residues substituted with mono-, di-, or triglycosyl side chains. α-1,2-Xylosyl residues, linked to O6 of β-1,4-glucose, are partly further substituted by β-1,2-D-galactosyl. The latter can be further substituted by α-1,2-linked fucosyl residues [112]. This last step is catalyzed by xyloglucan fucosyltransferases and two genes encoding members of this multigene family were over-expressed in ear internodes of COMT deficient plants.</p>
              <p id="s4s9p5">Cell autolysis is a key event in tracheid formation. A maize gene ortholog to a pectate lyase (ZePel) expressed in the zinnia model system was found to be over-expressed in ear internodes of bm3 and AS225 plants. ZePel was strongly expressed at a very early stage of tracheary element induction, and was related to the presence of auxin. Moreover, in young zinnia stems, ZePel expression was associated with vascular bundles [113]. The over-expression of this gene in bm maize is likely an indication that this type of enzyme is involved in monocotyledon plant lignification.</p>
              <p id="s4s9p6">Two cellulose synthase genes were over-expressed in bm3 or AS225 internodes whereas no drastic modification was described in cellulose content in bm3 plants. Interestingly, ZmCesA-9 and ZmCesA-12 are respectively homolog to PtrCesA5 [114] and HvCesA8 [115] genes, highly expressed in developing xylem and stem undergoing significant secondary cell wall biosynthesis.</p>
            </div>
          </section>
        </div>
      </section>
      <section data-type="">
        <h2 id="s5h1">Conclusion</h2>
        <div class="content">
          <p id="s5p1">Disruption or down-regulation of COMT gene induced a correlative differential expression of only a few genes involved in the lignin pathway. These genes were all over-expressed, except for an under-expressed PAL gene. As a consequence, deregulation of maize COMT did not clearly highlight major co-regulation of lignin pathway genes. Similarly, no over-expressed phenylpropanoid related gene could explain that as much as 40 % of S units were still present in bm3 lignins, with no COMT expression. Syringyl alcohol thus probably resulted from methylation by other OMT which were sufficiently available. One ZRP4-like OMT gene, which was shown to be over-expressed in maize bm3 plantlets [40] and which also had a tendency to be over-expressed in the bm3 ear internode, could be a candidate for the replacement of the lacking 5-hydroxyconiferaldehyde methyltransferase activity.</p>
          <p id="s5p2">Differential gene expressions in bm3 and/or AS225 internodes highlighted a probable disturbance in cell wall assembly and/or a possibly modified chronology of the different events leading to cell expansion and lignification with consequences far beyond the phenylpropanoid metabolism. The reduced availability of monolignols and S units led to deeply different walls, with probably greater differences in carbohydrate composition than currently considered. During cell wall assembly, biosynthesis of phenylpropanoid, protein, and carbohydrate constituents appeared to be inter-dependent, and the deficiency in a key-enzyme of the lignin pathway had consequences on the expression of several genes involved in cell wall metabolism. Apart from a PRP gene in bm3 plants and a GRP gene in AS225 plants, all non-lignin-pathway differentially expressed genes were also over-expressed. Furthermore, the lower number of deregulated genes in AS225 plants than in bm3 plants could result, in addition to the difference in genetic background of the two progenies, from the sclerenchyma-limited expression of the COMT-antisens constructed gene.</p>
          <p id="s5p3">The differential expression of genes in COMT-deficient plants is likely an indicator of their involvement in cell wall assembly, and some of these genes are probably new relevant targets for silage and biofuel maize breeding. While the transcription factors involved in regulation of lignin biosynthesis and deposition in maize are not yet clearly understood, the differential expression of one ATHB-8 HD-zip III, two Argonaute, and one Shatterproof MAD-box orthologous genes between bm3 and normal plants could be the first evidence of their role in the cell wall metabolism. Similarly, maize COV1 ortholog could be assumed to be involved in lignified fiber tissue patterning. Finally, the comparison of gene expression in silking normal and bm3 plants highlighted the possible involvement in the constitutive lignin pathway of not yet considered genes, such as ZRP4-like OMT.</p>
        </div>
      </section>
      <section data-type="">
        <h2 id="s6h1">Methods</h2>
        <div class="subsections">
          <section data-type="">
            <h3 id="s6s1h1">Plant material and RNA extraction</h3>
            <div class="content">
              <p id="s6s1p1">The well known normal F2 line, originating from the Lacaune landrace, and its isogenic F2bm3 (7 backcrosses) were used with the COMT-AS (AS225) down regulated progeny previously described by Piquemal et al. [31] and Pichon et al. [116], which has only one backcross with the recurrent parent F2 (75 % of F2 genetic background). The use of the Adh1 promoter directed COMT down-regulation specifically in sclerenchyma tissues, as shown by Maüle staining [31]. Hence, there was a different topology of modified tissues between COMT down-regulated plants and bm3 COMT-disrupted mutant plants. Plants were cropped in a greenhouse during the spring of 2004 at Lusignan (France), in pots with a mix of sand and compost, and were fed with usual nutritive solution.</p>
              <p id="s6s1p2">Nine plants were harvested at silking stage, just before pollen shedding. The plants were divided into three pools of three plants each for transcriptome analysis. The first elongated basal internode and the internode below the node bearing the ear (ear internode) were sampled separately from each pool. Nodes and leaf sheaths were eliminated, and internodes were immediately frozen in liquid nitrogen. Total RNA was isolated from each set of frozen internodes (5 g) by a method adapted from Ragueh et al. [117]and developed in Guillaumie et al. [43]. Internodes of grasses elongate in acropetal staggered succession, with an intercalary meristematic zone at the base of each internode which remains active until the final stage of elongation [118,119]. The basal internode is then physiologically older than the ear internode, and its lignification is more advanced than the more newly extended and fully lignifying ear internode [120-122].</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s6s2h1">Histochemical Staining of Lignins</h3>
            <div class="content">
              <p id="s6s2p1">Stem sections were cut with a vibratome from silking stage plants and silking + 30 days plants grown in the greenhouse. Wiesner and Maüle reactions were performed according to standard protocols [123]. Sections were observed using an inverted microscope (Leitz DMRIBE, Leica Microsystems, Wetzlar, Germany) with bright-field optics or epifluorescence illumination. Images were registered using a CCD camera (Color Coolview, Photonic Science, Milham, UK) and characterized through image analysis (Image PRO-Plus, Media Cybernetics, Silver Spring, MD). Wiesner reagent specifically reacts with cinnamaldehyde side chains in lignins and underlines the presence of lignins with a pink coloration. Lignified cell walls of xylem appear blue under UV illumination.</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s6s3h1">Maize cell wall macro-array construction, membrane hybridization, and data analysis</h3>
            <div class="content">
              <p id="s6s3p1">The maize cell wall macro-array, which consists of gene-specific tags (GSTs) for 651 genes, was described in detail by Guillaumie et al. [43]. Spotted genes were chosen firstly as maize orthologs of genes expressed during secondary cell wall formation of zinnia (Zinnia elegans Jacq.) tracheary elements [80] and secondly from a keyword strategy developed from sequences previously described as involved in primary and secondary cell wall biosynthesis and assembly for all species throughout the plant kingdom. Maize orthologous genes were found from BLAST (blastn and tblastx) searches [124] performed against GenoPlante-Info databases [125].</p>
              <p id="s6s3p2">Membrane hybridizations and data analyses were achieved according to a protocol adapted from Pesquet et al. [80] and developed in Guillaumie et al. [43]. Each GST was diluted to a final concentration of 0.5 mg/ml and then denatured in 50% DMSO. Controls were added in separate 384-well plates. One plate included 384 Tris-EDTA, pH 8.0 (blank background control). Another plate had 30 NPT II fragments (a positive hybridization control), 20 pBluescript plasmids (unspecific hybridization control), and 18 ubiquitin fragments (positive control). All fragments were spotted onto a 20 × 20-cm Nytran SuPerCharge nylon membrane (Schleicher and Schuell, Keene, NH, USA) using a BioGrid spotting robot (BioRobotics) in a 4 × 4 grid organization. Each gene was spotted twice in two different membrane grids corresponding to four replicates. cDNA probes were synthesized according to Guillaumie et al. [43] from 10 μg of total RNA for each sample. Membranes were placed in a PhosphorImager cassette (Molecular Dynamics, Amersham- Pharmacia) for 72 h and scanned at 50 mm/pixel by a Storm 820 scanner (Amersham-Pharmacia).</p>
              <p id="s6s3p3">Data analysis was performed according to Pesquet et al. [80] and Guillaumie et al. [43]. Macro-array gridding and gene expression levels were measured with ImageQuant 5.0 software (Molecular Dynamics, Amersham-Pharmacia) using 4 × 4 grids. Three independent hybridizations, each corresponding to one of the three groups of ear or basal internodes, were performed for normal, AS225 and bm3 plants. Reproducibility of raw signal intensity values on the membrane was first verified inside each grid and between the two grids for each investigated gene. According to Pesquet et al. [80] and Guillaumie et al. [43], two threshold values were thus defined so that 95% of the ratios between raw values of two replicates would be within the 0.5–2.0 interval. Aberrant values giving ratios outside of this interval were discarded. Normalization was performed based on the blank background, unspecific hybridization and positive controls (Tris-EDTA pH8, pBluescriptII, ubiquitin and kanamycin-NPTII). Macro-array reproducibility was further investigated by comparing normalized spot intensity values from the three independent hybridizations performed on three independent membranes. As was developed for reproducibility within the membrane, the investigations on the threshold values showed that more than 95% of the ratio values between independent hybridizations were confined within a twofold limit. Out of range values were discarded and 96–99% of the ratios between replicates were found between the two 0.5–2.0 threshold values. Expression data were estimated as the average of normalized intensity signal values of replicates, and comparisons between F2bm3 or AS225 with the normal F2 line were based on expression value ratios. According to Pesquet et al. [80] and Guillaumie et al. [43], genes with more than a twofold expression ratio in F2bm3 or AS225 compared with F2 were considered as differentially expressed genes. In addition, a variance analysis based on elementary normalized signal intensity values, followed by a bilateral Student t test (risk levels of P &lt; 0.05), was performed. All genes that were considered differentially expressed were also validated by this statistical analysis. The normalized hybridization level under 3000 was similar to the macro-array blank value, and the minimal level of significant hybridizations was thus fixed to a normalized value equal to 6000. For each differentially expressed gene, the mRNA number was searched using a BLAST (blastn) program against all available mRNA sequences in NCBI database.</p>
              <p id="s6s3p4">In this investigation, only a subset of genes spotted on the MAIZEWALL macro-array was considered, in order to focus on lignin pathway, cell wall carbohydrate and cell wall protein genes and their transport and regulation factors. This subset thus comprised 105 phenylpropanoid genes, 44 transcription factor genes, 22 auxin related and tissue patterning genes, 33 transport and detoxification process associated genes, 18 cell wall protein genes, and 114 nucleotide sugar and cell wall carbohydrate genes. The exhaustive gene list has been given by Guillaumie et al. [43].</p>
            </div>
          </section>
          <section data-type="">
            <h3 id="s6s4h1">RT-PCR</h3>
            <div class="content">
              <p id="s6s4p1">Total RNA was isolated as described above. cDNA synthesis was conducted by incubating 1 μl of DNase-treated total RNA (1 μg/μl) with 2 μl of Oligo(dT)15 Primer (Promega, 500 μg/ml) and 15 μl of ultra-pure water for 5 min at 70°C and cooled down on ice for 5 min. 5 μl of Promega's MuMLVRT reverse transcriptase 5× buffer, 1.3 μl of 10 mM dNTP and 200 units of MuMLV-RT reverse transcriptase (Promega) were added to the denatured RNA and incubated at 37°C for 1 h. The reaction was stopped during 5 min at 70°C and then 5 min on ice. PCR was performed as follows: 95°C for 2 min, X cycles (15 cycles for 18S rRNA and 30 cycles for PAL, CCoAOMT3 and COMT) at 95°C for 30s, 55°C–60°C for 30s depending on primer couples, 72°C for 30s and final extension 2 min in a total volume of 25 μl with 12.5 μl of 2× Master Mix PCR (Promega), 1 μl of forward and reverse specific primers of each fragment (10 μM each), 9.5 μl of ultra-pure water and 1 μl cDNA product. Resulting PCR products were analyzed by electrophoresis and stained with Etbr. The PCR primer combinations for each gene were as follows: PAL (2161072.2.1, L77912) forward 5'-GGGGAGGAAATACGTGAAAA-3', reverse 5'-TTAGAAGGAATTGAGTACGC-3'; CCoAOMT3 (2591258.2.1, AY104670) forward 5'-CGTTCACGTCTGCCAGGT-3', reverse 5'-TTCACTCAAGCCCAGTTCG-3'; COMT (2192909.2.3, M73235): forward 5'-GCTTGCTTGGTCCTCGTATC-3', reverse 5'-TACTCGCACATGGCAGAGAC-3'; 18S rRNA: forward 5'-CATGTCAAATTTCACTGCTTCATC-3', reverse 5'-TGACCACCCAGCCATCCTT-3'. All primers were synthesized by MWG-BIOTECH (Ebersberg, Germany).</p>
            </div>
          </section>
        </div>
      </section>
      <section data-type="">
        <h2 id="s7h1">Abbreviations</h2>
        <div class="content">
          <p id="s7p1">4CL: 4-coumarate:CoA ligase, 5-OH-G: 5-hydroxyguaiacyl, ABC: ATP-binding cassette, AGL: Agamous like, AGP: arabinogalactan protein, ALDH: aldehyde dehydrogenase, ARF: ADP- ribolysation factor, AS225: COMT antisens, bm: brown-midrib, C3'H: p-coumaroyl-shikimate/quinate 3'-hydroxylases, C4H: cinnamate 4-hydroxylase, CAD: cinnamyl alcohol dehydrogenase, CCoAOMT: caffeoyl-CoA O-methyltransferase, CCR: cinnamoyl-CoA reductase, COMT: caffeic acid O-methyltransferase, COV: CONTINUOUS VASCULAR RING, CHI: chalcone flavonone isomerase, DM: dry matter, F5H: ferulate 5-hydroxylase, FA: ferulic acid, G: guaiacyl, GEF: guanine nucleotide exchange factor, GlcA: glucuronic acid, GRP: glycine-rich protein, GST: glutathion S-transferase, GSTs: gene specific tags, H: p-hydroxyphenyl, HCT: hydroxycinnamoyl transferase, HD-Zip: Homeodomain-leucine zipper, HRGP: hydroxyproline-rich protein, MP: Monopteros, NDF: neutral detergent fiber, PAL: phenylalanine ammonia-lyase, pCA: p-coumaric, PID: PINOID, S: syringyl, PRP: proline-rich protein, SAD: sinapyl alcohol dehydrogenase, SHP: Shatterproof, TAL: tyrosine ammonia-lyase, UDP: uridine diphosphate, XTH: Xyloglucan endotransglycolase/hydrolase.</p>
        </div>
      </section>
      <section data-type="">
        <h2 id="s8h1">Authors' contributions</h2>
        <div class="content">
          <p id="s8p1">SG conducted the research, designed the experiments, analyzed the data and drafted the manuscript together with YB. DG and MP coordinated the construction of the MaizeWall macro-array and contributed to the experimental design of this work. OB contributed to acquisition of expression data. YB coordinated the project, and coordinated together with J-PM the Génoplante ZmS3P2 and B5 projects in which this work was managed. All authors read and approved the final manuscript.</p>
        </div>
      </section>
    </article>
  </body>
</html>
```
</div>
</div>
<div class="one-third-col">

</div>
