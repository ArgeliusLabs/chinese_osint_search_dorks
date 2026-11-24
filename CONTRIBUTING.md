# Contributing

Corrections to translations, source links, record-status interpretations, and observed portal behavior are welcome. Use [issues](https://github.com/ArgeliusLabs/chinese_osint_search_dorks/issues) for reports and pull requests for proposed changes. Follow the [guide's scope](guide.md#1-scope-ethics-and-safety).

## Supply enough evidence to review a change

- Identify the section and the proposed replacement wording.
- For a translation, include the minimum necessary Chinese text, an English gloss, context, and a primary source when available.
- For a query or portal report, include the exact benign query or URL, date/time with timezone, engine/interface, browser/API/script method, language, login status, and network region if known.
- Separate the observed response from a suspected cause. HTTP errors, visible challenges, login requirements, and an accessible search with no match are different outcomes. Do not infer geographic blocking, a protection vendor, or browser accessibility from a status code alone.
- Cite evidence that supports the specific claim. Disclose commercial affiliation and study limitations; avoid generalizing a single sample or provider to all Chinese records.
- Remove tokens, cookie values, credentials, and unnecessary personal data from attachments. Do not bypass access controls to produce evidence.

## Update validation records

[data/validation.json](data/validation.json) is the source for the generated [validation register](docs/validation.md). The register is selective; an absent example has not been validated by this repository.

- `documented`: relevant provider documentation was checked; no live result is implied.
- `observed`: a dated live test has a recorded query (for operators), context, and actual observation. It is not a guarantee of completeness or future behavior.
- `untested`: no supporting live test is recorded; notes can explain a reported issue or unsupported format without treating it as reproduced.

Keep unperformed checks null. Record dates only for work actually performed. Preserve dated historical observations when replacing a record, for example in the changelog or an issue with supporting evidence.

After editing the JSON, regenerate the Markdown:

```text
python scripts/render_validation.py
```

Do not hand-edit the generated register. Do not update the guide's editorial-review date to imply every portal was retested.

## Run the offline checks

Use Python 3.12 or later; no third-party packages are required. From the repository root:

```text
python scripts/render_validation.py --check
python scripts/check_docs.py
python -m unittest discover -s tests -v
```

The documentation checker covers the Markdown conventions used here: case-sensitive relative paths, heading anchors, reference links, footnotes, and closed fences. It is not a complete CommonMark parser. The workflow uses read-only repository permissions and performs no live portal requests.

Check changed external links manually and report the outcome. Do not make a transient timeout, account requirement, or anti-bot response a build failure or label a site dead on that basis. Record the URL, check time, client context, response, and any uncertainty in an issue or validation record.

## Teaching materials and reuse

Keep fictional records prominently labeled, use visibly synthetic identifiers, and distinguish scenario dates from actual observation timestamps. Queries in the [worked exercise](examples/procurement/README.md) are illustrative and must not be represented as executed searches. Keep [template field definitions](templates/README.md), example CSV columns, and the walkthrough consistent.

By submitting material, confirm that you can contribute it under the repository's [CC BY 4.0 license](LICENSE). Credit adapted material and contributors, link original sources, and summarize material changes in [CHANGELOG.md](CHANGELOG.md).
