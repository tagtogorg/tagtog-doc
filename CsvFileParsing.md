---
layout: page
title: CSV (and TSV) file input parsing
sidebar_link: false
id: CsvFileParsing
version: 2.0
toc: false
---

Current format version: `{{ page.version }}`

You can import CSV (comma-separated values) and TSV (tab-separated values) files onto tagtog 😻. This also means, you can easily **import any excel sheet** onto tagtog 📊.

### How it's parsed

An imported file is parsed as follows:

* **The first row is considered the header**. Each column represents a section in tagtog, and the header gives
the title for each.

  Optionally, if the first row starts with the character `#`, then no titles will be created. Please note that still the first row (the header) must exist.

* **Each subsequent row represents a document**. Each column represents a paragraph in a section in tagtog,
whose header is given by the corresponding header column.

  Content rows with a different number of columns than the header's are allowed. In case the row has less columns, everything remains equal.
If the row has more columns than the header's, then a stub title for the column section is created with
the pattern: `"Column-#{columnNumber}"`. Of course, if *no titles* header was chosen, then no titles will be added
in the documents.

_☝️ Note_: the imported file must have _at least_ 2 rows: 1 for the header and the other for the first document.
 Each subsequent row is another document.

_✌️ Note_: **double quotes, commas, tabs, and even new lines are accepted**. This means that CSV/TSV files exported from spreadsheets applications are accepted. Special characters (e.g. newlines) are accepted as long as they are wrapped in double quotes. If we want to import the double quote character itself when the text is already quoted, then the quote has to be doubled, like in this example:

```csv
"this is one cell value with comma (,), new lines
and ""double quote""
inside"
```

---

#### Example

How the parsing works is best explained with an example 🙂. Say you start with an excel
file (or numbers file on macOS) like the following:

<img src="assets/img/csv/example_excel.png" alt="Example excel" width="40%"/>

<br/>
You can save the file as CSV:

<img src="assets/img/csv/save_as_csv.png" alt="Save as CSV" width="40%"/>

<br/>
The file will look like this in a text editor:

<img src="assets/img/csv/example_text_editor.png" alt="CSV in text editor" width="30%"/>

<br/>
Uploading that CSV file, will result in 6 documents on tagtog:

<img src="assets/img/csv/6_parsed_documents.png" alt="Upload CSV file" width="100%"/>

<br/>
And, for example, the first document (the last on the list) will look like this:

<img src="assets/img/csv/first_document.png" alt="tagtog document presentation" width="15%"/>

Note that the headers are in bold, and the paragraphs are in regular font.

Also note how the upload preserves new lines, commas, and quotes from the original spreadsheet source.
