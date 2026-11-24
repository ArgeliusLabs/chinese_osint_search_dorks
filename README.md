# China Web OSINT Search Dorks

**A bilingual field guide to Baidu, Chinese-language query pivots, public records, and verification — published by [Argelius Labs](https://argeliuslabs.com).**

China-focused web research depends on Chinese names, identifiers, terminology, and document conventions. Company registries, procurement awards, court and enforcement data, regulatory penalties, patents, and disclosures often surface through Chinese-language queries and official portals that English-language searches miss.

This repository is a practical, bilingual playbook for doing that work well and lawfully.

## 📖 Read the guide

**→ [`guide.md`](guide.md)** — the full field guide (28 sections).

Every Chinese query, keyword, and operator is paired with an English translation, so you can use it whether or not you read Chinese.

## Start here

1. Read [scope and safety](guide.md#1-scope-ethics-and-safety), then the [core workflow](guide.md#3-a-practical-china-osint-workflow).
2. Complete the [offline procurement exercise](examples/procurement/README.md): three fictional bilingual notices, a worked evidence log, and an answer key.
3. Copy the [evidence-log template](templates/README.md) for your own work.
4. Check the [validation register](docs/validation.md) before relying on an operator or portal. Documentation checks and live observations are labeled separately.

For a compact vocabulary reference, use the [cheat sheet](guide.md#25-quick-reference-cheat-sheet). The [JSON validation records](data/validation.json) are available for reuse; they cover selected patterns, not every query in the guide.

## What's inside

- A repeatable workflow: resolve the canonical Chinese identity, pivot on one Chinese term at a time, constrain by source and file type, then move from search engines to primary portals.
- Baidu search syntax and how it differs from Google — with honest caveats about what each operator actually does.
- Ready-to-use "dork" libraries for corporate ownership, listed-company disclosures, people and biographies, government and regulatory records, procurement and tenders, litigation and enforcement, IP and standards, technical footprint, locations, and social platforms.
- A map of official, high-value Chinese source portals (registries, courts, procurement, IP, securities, standards, maps).
- Verification discipline: a source hierarchy, status words that change a record's meaning, common analytical traps, an evidence-log template, and preservation/integrity steps.
- Troubleshooting, classroom exercises, a quick-reference cheat sheet, and a briefing-slide summary.

## Who it's for

OSINT students, investigators, journalists, researchers, analysts, due-diligence teams, and technical professionals doing lawful research on information that is intentionally public.

## ⚠️ Read this first

This is **open-source intelligence** material — it covers information intentionally made public. It does **not** teach bypassing access controls, credential hunting, scraping in violation of law or terms, or collecting private personal data without a lawful purpose.

It is **educational material and not legal advice**, and is **not affiliated with or endorsed by any government, agency, search engine, or platform** named within it. Researching Chinese entities can carry legal exposure for *you* as the collector — including under China's Data Security Law, PIPL, and Counter-Espionage Law — depending on the subject, your location, and what you do with the data. See **[Section 1 of the guide](guide.md#1-scope-ethics-and-safety)** before you start.

## License

Released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license — see [`LICENSE`](LICENSE). You may share and adapt the material, including commercially, with attribution.

## Contributing & contact

Issues and pull requests are welcome — corrections to translations, dead links, and changed portal behavior are especially valuable. Read [CONTRIBUTING.md](CONTRIBUTING.md) for evidence requirements and local checks. Contact us through [repository issues](https://github.com/ArgeliusLabs/chinese_osint_search_dorks/issues), or learn more at [argeliuslabs.com](https://argeliuslabs.com).

## Maintenance

Search engines and official portals change. Before relying on a specific operator or link, test it against the live interface. The guide's editorial-review date describes content review; each [validation record](docs/validation.md) separately states its documentation check and live-test status. Untested behavior is not certified by a document revision.

Repository checks run offline in GitHub Actions and can be run locally with Python 3.12 or later:

```text
python scripts/render_validation.py --check
python scripts/check_docs.py
python -m unittest discover -s tests -v
```

These checks cover documentation consistency and validation data, not live search results or portal availability. See the [changelog](CHANGELOG.md) for changes and contribution credits.

---

© Argelius Labs · [argeliuslabs.com](https://argeliuslabs.com) · *China Web OSINT Search Dorks* is provided for educational use under CC BY 4.0.

