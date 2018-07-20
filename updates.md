---
layout: page
title: Updates
sidebar_link: true
id: updates
---

Here is the versioned list of all the new features, fixes, and other changes. [tagtog Cloud](https://www.tagtog.net) runs always on the latest version. If you are running **tagtog On-Premises**, make sure to [update to the latest version](on_premises_README.html) to make the most of your experience.

Have feedback? :heart: Report bugs and/or suggest improvements on our [:point_right:GitHub issues page:point_left:](https://github.com/tagtog/tagtog-doc/issues).

## ## 3.2018-W29.1-SNAPSHOT 📑

<ul class="updates">
  <li class="new">Now you can choose whether <a title="tagtog - pre-annotations" href="/webeditor.html#pre-annotations">pre-annotations</a> (i.e. the automatic annotations that are created while manually annotating) are <strong>case sensitive or not</strong>.</li>
  <li class="doc">Improved reporting of parsing errors in API uploads</li>
</ul>

---

## 3.2018-W29.0 🇫🇷
_2018-07-18_

<ul class="updates">
  <li class="new">The maximum upload size on the cloud, was augmented from 2MB up to 5MB 📈</li>
  <li class="fix">Some improvements in the management of on-premises licenses</li>
  <li class="doc">Simplified pricing information</li>
</ul>

---

## 3.2018-W28.3 🇧🇪
_2018-07-13_

<ul class="updates">
  <li class="new"><a title="Annotation types" href="/webeditor.html#annotation-types">Relations</a> are now supported between entities from different paragraphs or sections 🔛!</li>
  <li class="fix">The uploading of documents has been fixed so that special characters such as "#" are accepted in the filenames</li>
  <li class="fix">Fixed memory leak that happened when annotating with dictionaries with some specially-charactered files, often PDFs</li>
  <li class="fix">Fixed bug that caused not using re-confirmed documents for ML training</li>
  <li class="new">Support for on-premises license updates</li>
</ul>

---

## 3.2018-W28.2 🕵️‍♀️
_2018-07-10_

<ul class="updates">  
  <li class="fix">Fixed the problem that users could not edit <a title="Annotation types" href="/webeditor.html#annotation-types">Entity Labels</a></li>
  <li class="new">The modal menu to set <a title="Annotation types" href="/webeditor.html#annotation-types">Entity Labels</a> is now scrollable and supports a long list of labels</li>
</ul>

---

## 3.2018-W28.0 🥅

<ul class="updates">  
  <li class="new">Support for <b>proxies on-premises</b> 🕵️‍♀️</li>
  <li class="fix">Fixed an interface bug affecting <b>Internet Explorer</b>, that blocked importing new documents</li>
</ul>

---

## 3.2018-W26.0 ⚽️

### Webhooks

<ul class="updates">
  <li class="new">You can now choose the new <code>tagtogID</code> (pseudo-)format in your <b>webhooks</b> to POST the updated document's id</li>
  <li class="new">You can now delete webhooks 😉</li>
  <li class="fix"><b>Webhooks</b> are now also triggered on new document uploads that have <i>no annotations</i></li>
  <li class="del">The formats <code>docJSON</code> and <code>PubAnnotation</code> were removed from the possible <b>webhooks</b>' payload. We might review this decision.</li>
</ul>

### More!

<ul class="updates">  
  <li class="new">API call to get a JSON map of the annotations legend, <i>anntasks ids → names</i>. For a sample call, check your project's <kbd>Downloads</kbd> page.</li>
  <li class="fix">Fixed a bug that prevented the training of ML models for entities that had associated dictionaries (specifically created through the interface).</li>
  <li class="doc">This new page of release notes was created 🤩</li>
</ul>
