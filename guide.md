# China Web OSINT Search Dorks
## A Bilingual Field Guide to Baidu, Chinese-Language Query Pivots, Public Records, and Verification

> **Version:** 1.0  
> **Last reviewed:** 21 June 2026  
> **Publisher:** [Argelius Labs](https://argeliuslabs.com)  
> **Author:** [Add your name or handle]  
> **Contact:** [argeliuslabs.com](https://argeliuslabs.com) — or add a business email / repository issues link  
> **License:** Creative Commons Attribution 4.0 International (CC BY 4.0) — see [`LICENSE`](LICENSE)  
> **Audience:** OSINT students, investigators, journalists, researchers, analysts, due-diligence teams, and technical professionals  
> **Scope:** Lawful research using information intentionally available to the public

> [!IMPORTANT]
> **Disclaimer.** This guide is educational material published by Argelius Labs. It is **not legal advice**, and it is **not affiliated with, endorsed by, or connected to any government, agency, search engine, or platform** named within it. All product names, portal names, and trademarks belong to their respective owners. Laws, platform terms, and professional obligations vary by jurisdiction and assignment; you are responsible for ensuring your research is lawful where you operate and where the data resides. See [Section 1](#1-scope-ethics-and-safety) for scope, ethics, and your own legal exposure.

---

## Executive summary

China-focused web research works best when you stop treating the Chinese-language internet as a translated copy of the English-language web.

The most productive workflow is usually:

1. Find the target's **canonical Chinese name** and high-confidence identifiers.
2. Search the name in **Simplified Chinese**, then test Traditional Chinese, English, romanized names, abbreviations, and former names.
3. Combine the target with a **Chinese pivot term** such as `招聘` (**recruiting/jobs**), `中标公告` (**award notice**), `行政处罚` (**administrative penalty**), or `简历` (**résumé/biography**).
4. Narrow the query with a source domain, document type, title term, or exact identifier.
5. Run the same concept across **multiple search engines, platform-native searches, and official databases**.
6. Treat search results as leads—not proof—and verify important claims against primary records.

A reusable formula is:

```text
"[TARGET]" "[CHINESE PIVOT TERM]" site:[SOURCE DOMAIN] filetype:[FILE TYPE]
```

Example:

```text
"[目标公司全称]" "中标公告" site:ccgp.gov.cn filetype:pdf
```

**English translation:** `"[full legal company name]" "award notice"` limited to the China Government Procurement Network and PDF files.

The central lesson is simple:

> **Search in the language, terminology, platforms, identifiers, and document conventions used by the source ecosystem itself.**

---

## Contents

- [1. Scope, ethics, and safety](#1-scope-ethics-and-safety)
- [2. How to read the bilingual examples](#2-how-to-read-the-bilingual-examples)
- [3. A practical China OSINT workflow](#3-a-practical-china-osint-workflow)
- [4. Baidu search syntax and operator behavior](#4-baidu-search-syntax-and-operator-behavior)
- [5. Entity resolution: names, aliases, and identifiers](#5-entity-resolution-names-aliases-and-identifiers)
- [6. Corporate identity and ownership dorks](#6-corporate-identity-and-ownership-dorks)
- [7. Listed-company and securities-disclosure dorks](#7-listed-company-and-securities-disclosure-dorks)
- [8. People and professional-biography dorks](#8-people-and-professional-biography-dorks)
- [9. Government, regulatory, and licensing dorks](#9-government-regulatory-and-licensing-dorks)
- [10. Procurement, tenders, and contract dorks](#10-procurement-tenders-and-contract-dorks)
- [11. Litigation, court, and enforcement dorks](#11-litigation-court-and-enforcement-dorks)
- [12. Reports, PDFs, spreadsheets, and presentation dorks](#12-reports-pdfs-spreadsheets-and-presentation-dorks)
- [13. News, incidents, disputes, and reputation dorks](#13-news-incidents-disputes-and-reputation-dorks)
- [14. Supply-chain, customer, and partnership dorks](#14-supply-chain-customer-and-partnership-dorks)
- [15. Domains, apps, repositories, and technical-footprint dorks](#15-domains-apps-repositories-and-technical-footprint-dorks)
- [16. Patents, trademarks, software copyright, and standards](#16-patents-trademarks-software-copyright-and-standards)
- [17. Academic, research, and university dorks](#17-academic-research-and-university-dorks)
- [18. Locations, facilities, factories, and projects](#18-locations-facilities-factories-and-projects)
- [19. Chinese social and community-platform pivots](#19-chinese-social-and-community-platform-pivots)
- [20. Reposts, deleted pages, and archival pivots](#20-reposts-deleted-pages-and-archival-pivots)
- [21. Sensitive terms, warning banners, and filtered results](#21-sensitive-terms-warning-banners-and-filtered-results)
- [22. Official and high-value source map](#22-official-and-high-value-source-map)
- [23. Verification and analytical safeguards](#23-verification-and-analytical-safeguards)
- [24. Troubleshooting weak or noisy results](#24-troubleshooting-weak-or-noisy-results)
- [25. Quick-reference cheat sheet](#25-quick-reference-cheat-sheet)
- [26. Classroom exercises](#26-classroom-exercises)
- [27. Briefing-slide summary](#27-briefing-slide-summary)
- [28. Sources and further reading](#28-sources-and-further-reading)

---

# 1. Scope, ethics, and safety

This guide is about **open-source intelligence**, meaning information that is intentionally available to the public through search engines, public websites, official registries, public disclosures, media, academic sources, and public social platforms.

It does **not** teach or endorse:

- bypassing authentication, paywalls, access controls, CAPTCHAs, or technical restrictions;
- searching for or using passwords, private keys, tokens, API secrets, exposed databases, or credentials;
- exploiting vulnerable systems;
- impersonation, pretexting, harassment, stalking, or doxxing;
- collecting private home addresses, private phone numbers, family information, or other sensitive personal data without a legitimate and lawful purpose;
- bulk scraping that violates law, platform terms, or reasonable rate limits.

> [!IMPORTANT]
> Use organizational and professional contact details only when they are relevant to a legitimate research purpose. Do not turn public-source research into a mechanism for targeting private individuals.

Search results may expose information that was published accidentally. The fact that a search engine indexed something does not automatically make further access, use, redistribution, or exploitation appropriate. When you encounter credentials, highly sensitive personal data, or a clearly accidental exposure, stop, preserve only what is necessary for responsible reporting, and follow the applicable disclosure process.

This guide is educational and is not legal advice. Laws, platform rules, and professional obligations vary by jurisdiction and assignment.

## 1.1 Your own legal exposure when researching Chinese entities

Most OSINT guidance focuses on protecting the *subject's* privacy. Researching China-based entities adds a second concern that is easy to overlook: **your own legal exposure as the collector of the data.** The People's Republic of China has built out a body of law that can reach data-gathering activity even when each individual record was publicly accessible.

- **Data Security Law (DSL, in force since September 2021)** regulates the handling and cross-border transfer of "important data" and data affecting national security. Aggregating individually public records into a larger dataset, or moving Chinese-sourced data abroad, can fall within its scope.
- **Personal Information Protection Law (PIPL, in force since November 2021)** governs the processing of personal information of people in China and has extraterritorial reach. "It was public" is not, by itself, a complete defense to processing personal data at scale.
- **Counter-Espionage Law (revised, in force since July 2023)** broadened the definition of espionage and of "documents, data, materials, and items related to national security and interests." The boundaries are not precisely defined, which itself is a risk factor for anyone systematically collecting information about Chinese government bodies, state-owned enterprises, defense-linked entities, or critical infrastructure.

> [!CAUTION]
> The practical takeaway is not "do not research China." It is: understand that *who* you are, *where you operate*, *what entity you are looking at*, and *what you do with the data afterward* can change your legal risk profile. Risk is highest when the subject is government-, military-, or critical-infrastructure-linked, when you aggregate data into a dataset, and when you transfer Chinese-sourced data across borders. If your work is sensitive, commercial, or could be construed as adverse to a Chinese entity, get qualified legal advice for your jurisdiction and the assignment **before** you start collecting. This guide cannot give that advice.

## 1.2 Researcher operational security

These are general good-practice notes, not a guarantee of anonymity or safety:

- Separate your research identity from your personal accounts. Do not log into personal email, social, or cloud accounts in the same browser session you use to query Chinese portals.
- Expect many official and commercial portals (Tianyancha, Qichacha, court systems, some government sites) to require a Chinese mobile number, real-name verification, payment, or a CAPTCHA. Do not attempt to bypass these controls — note the access limitation in your evidence log instead.
- Be deliberate about where your traffic originates. Network location can change which results you see and may itself be relevant to the legal considerations above.
- Preserve evidence as you go (see Section 23), because pages can disappear and access can be revoked.
- If you are a journalist, NGO, academic, or investigator working on a sensitive subject, consult your organization's security and legal resources before fieldwork.

---

# 2. How to read the bilingual examples

Every Chinese query or keyword in this guide is paired with an English translation.

The main placeholders are:

| Chinese placeholder | English meaning |
|---|---|
| `[目标公司全称]` | `[full legal company name]` |
| `[目标公司简称]` | `[company short name or abbreviation]` |
| `[目标人物姓名]` | `[person's full name]` |
| `[目标机构名称]` | `[organization name]` |
| `[目标产品名称]` | `[product name]` |
| `[目标应用名称]` | `[app name]` |
| `[目标域名]` | `[domain name]` |
| `[统一社会信用代码]` | `[Unified Social Credit Identifier]` |
| `[证券代码]` | `[stock code]` |
| `[案号]` | `[case number]` |
| `[项目编号]` | `[project number]` |
| `[备案号]` | `[filing number]` |
| `[专利申请号]` | `[patent application number]` |
| `[商标注册号]` | `[trademark registration number]` |

In slide decks, people often write a conceptual query as:

```text
TARGET + 招聘
```

Here, `招聘` means **recruiting/jobs**. In an actual search box, use spaces rather than a literal plus sign unless the search engine specifically documents `+` behavior:

```text
"[目标公司全称]" 招聘
```

**English translation:** `"[full legal company name]" recruiting/jobs`.

## Search typography that matters

- Use a normal ASCII colon in operators: `site:gov.cn`, not `site：gov.cn`.
- Do not put a space after the colon: `site:gov.cn` is correct; `site: gov.cn` may fail.
- Start with straight quotation marks: `"exact phrase"`.
- Put a space before an exclusion minus and no space after it: `目标 -招聘` means **target, excluding recruiting/jobs**.
- Chinese search engines segment words algorithmically. Even quoted phrases can be rewritten or interpreted semantically, so inspect the actual results.
- If punctuation blocks a match, retry without punctuation or with alternate full-width and half-width forms.

---

# 3. A practical China OSINT workflow

## Step 1: Define the intelligence question

A weak task is “research this company.” A stronger task is:

- What is the company's exact registered identity?
- Who owns or controls it?
- Has it won government contracts?
- What public legal or regulatory history exists?
- Which facilities, subsidiaries, products, domains, or apps can be verified?
- Which claims are confirmed by primary sources, and which are only allegations or marketing statements?

A precise question determines which Chinese pivot terms and official databases matter.

## Step 2: Establish the canonical Chinese identity

Collect, where available:

- full registered Chinese name;
- official English name;
- Simplified Chinese and Traditional Chinese forms;
- former names;
- abbreviations and brand names;
- Unified Social Credit Identifier;
- stock code;
- official domain and ICP filing number;
- registered location;
- legal representative;
- relevant product, app, and subsidiary names.

Do not translate a legal entity name yourself and present the translation as official. An entity's official English name may differ from a literal translation. When no official English name is available, label your version as a transliteration or working translation.

## Step 3: Build an alias matrix

A compact alias matrix prevents missed results and mistaken identity:

| Variant type | Example format |
|---|---|
| Full Chinese legal name | `[目标公司全称]` — `[full legal company name]` |
| Chinese short name | `[目标公司简称]` — `[company abbreviation]` |
| Former name | `[曾用名]` — `[former name]` |
| English official name | Exact English form from an official disclosure |
| Romanized name | Pinyin or another documented romanization |
| Brand/product name | Chinese and English variants |
| Identifier | Unified Social Credit Identifier, stock code, filing number, case number, or project number |
| Domain/app | Root domain, mobile domain, app name, package name, or public account name |

For people, test surname-first and given-name-first romanization, spacing, hyphenation, initials, Chinese characters, and institutional affiliations.

## Step 4: Run a broad baseline query

```text
"[目标公司全称]"
```

**English translation:** exact full legal company name.

Record what the search engine associates with the entity before adding assumptions.

## Step 5: Add one pivot term at a time

```text
"[目标公司全称]" 股东
```

**English translation:** `"[full legal company name]" shareholders`.

```text
"[目标公司全称]" 中标公告
```

**English translation:** `"[full legal company name]" award notice`.

```text
"[目标公司全称]" 行政处罚
```

**English translation:** `"[full legal company name]" administrative penalty`.

Changing one variable at a time helps you understand which term produced the useful result.

## Step 6: Constrain by source or file type

```text
"[目标公司全称]" 行政处罚 site:gov.cn
```

**English translation:** `"[full legal company name]" administrative penalty`, limited to Chinese government domains.

```text
"[目标公司全称]" 年度报告 filetype:pdf
```

**English translation:** `"[full legal company name]" annual report`, limited to PDF files.

## Step 7: Search identifiers independently

Names collide; identifiers usually collide less.

```text
"[统一社会信用代码]"
```

**English translation:** exact Unified Social Credit Identifier.

```text
"[项目编号]"
```

**English translation:** exact project number.

```text
"[案号]"
```

**English translation:** exact case number.

Search an identifier by itself, then combine it with a name, location, or source domain.

## Step 8: Move from search engines to primary portals

A search engine is a discovery layer. Once you know the target's exact name or identifier, query the relevant official registry, procurement portal, court portal, stock-exchange disclosure system, patent database, or government website directly.

## Step 9: Repeat across indexes and native platform search

Run the same core query on Baidu, Google, Bing, another Chinese search engine, and the target platform's own search where lawful and available. Search engines have different coverage, ranking, filtering, and refresh cycles. Older comparative research found low overlap between Chinese search-engine result sets; the exact numbers are historical, but the operational lesson remains valid: **one index is never the whole web**.[^jiang-search]

## Step 10: Verify, preserve, and cite

For every important claim, capture:

- exact query;
- search engine or portal;
- date and time;
- result URL;
- publisher or issuing authority;
- publication date and effective date;
- original Chinese text;
- English translation;
- archived copy or screenshot when appropriate;
- confidence level and unresolved ambiguity.

---

# 4. Baidu search syntax and operator behavior

Baidu is a useful entry point into mainland Chinese web content and Baidu-hosted properties, but it is not simply “Google in Chinese.” Similar-looking operators do not guarantee identical behavior.

Baidu's official Advanced Search page provides controls for all words, an exact phrase, any word, excluded words, time, Simplified or Traditional Chinese, document format, title or URL position, and site restriction.[^baidu-advanced]

> [!CAUTION]
> Search behavior changes. Ranking systems may rewrite queries, ignore an operator, interpret a quoted phrase semantically, or show only a sample of indexed pages. Test each operator against the live results and avoid treating result counts as complete inventories.

## 4.1 Core Baidu query patterns

| Pattern | Purpose | Bilingual example | Reliability note |
|---|---|---|---|
| `"phrase"` | Request an exact phrase | `"[目标公司全称]"` — `"[full legal company name]"` | Common and available through Baidu Advanced Search, but exactness can vary in practice. |
| `-term` | Exclude a term | `"[目标公司全称]" -招聘` — company name excluding **recruiting/jobs** | Put a space before the minus and no space after it. |
| `site:domain` | Restrict to a site or domain | `"[目标公司全称]" site:gov.cn` — company name on Chinese government domains | Do not put a space after `site:`. A sparse result does not prove the site lacks the material. |
| `filetype:pdf` | Restrict by document type | `"[目标公司全称]" 年度报告 filetype:pdf` — company **annual report** PDFs | Try `pdf`, `doc`, `docx`, `xls`, `xlsx`, `ppt`, and `pptx` separately; coverage varies. |
| `intitle:term` | Request a term in the page title | `intitle:中标公告 "[目标公司全称]"` — title contains **award notice** plus the company name | Commonly observed; confirm that the result titles actually contain the term. |
| URL-position filter | Request a term in the URL | Use Baidu Advanced Search's URL-position option | Prefer the official Advanced Search control if `inurl:` behaves inconsistently. |
| Advanced Search UI | Combine fields without memorizing syntax | Baidu Advanced Search | Useful for date, language, file format, title, URL, and site filters. |

## 4.2 A disciplined operator-testing method

Suppose the baseline is:

```text
"[目标公司全称]" 中标公告
```

**English translation:** company name plus **award notice**.

Test these separately:

```text
"[目标公司全称]" 中标公告 site:ccgp.gov.cn
```

**English translation:** company name plus **award notice**, limited to the China Government Procurement Network.

```text
"[目标公司全称]" 中标公告 filetype:pdf
```

**English translation:** company name plus **award notice**, limited to PDFs.

```text
intitle:中标公告 "[目标公司全称]"
```

**English translation:** result title contains **award notice**, with the company name elsewhere in the result.

Then combine only the filters that visibly improve precision.

## 4.3 Operators are not evidence of completeness

A `site:` query is not an authoritative list of every indexed page. Google explicitly cautions that an indexed URL is not guaranteed to appear in a `site:` query; the same analytical caution should be applied to other engines.[^google-site]

Use `site:` to discover leads, not to prove absence.

## 4.4 Cross-engine strategy

Use the strongest documented features of each engine:

- **Baidu:** Chinese-language discovery, Baidu properties, official Advanced Search filters.
- **Google:** quotes, exclusions, `site:`, and `filetype:`; Google documents `site:` and `filetype:` and lists the file formats it can index.[^google-refine][^google-filetypes]
- **Bing:** documented Boolean operators and advanced keywords such as `site:`, `filetype:`, `ext:`, `intitle:`, and `url:`.[^bing-options][^bing-keywords]
- **Other Chinese indexes:** useful for coverage comparison, but test syntax rather than assuming Google-compatible behavior.
- **Platform-native search:** often necessary for Weibo, Zhihu, WeChat, Bilibili, Xiaohongshu, Douyin, and other partially indexed platforms.

## 4.5 What not to assume

Do not assume that:

- every Google operator works in Baidu;
- Baidu always has more results than Sogou or another Chinese engine;
- a result-count estimate is accurate;
- no results means no data exists;
- a warning banner proves that every result was removed;
- adding a platform name retrieves an archive;
- a cached snippet is current or correctly attributed.

Coverage is query-specific and changes over time.

---

# 5. Entity resolution: names, aliases, and identifiers

Entity resolution is the highest-value step in China OSINT. A perfect dork aimed at the wrong entity produces confident-looking nonsense.

## 5.1 Name-discovery keywords

| Chinese term | English translation | Use |
|---|---|---|
| `中文名` | Chinese name | Find a Chinese name associated with an English entity or person. |
| `英文名` | English name | Find an English name associated with a Chinese entity or person. |
| `全称` | full name | Find the complete legal or institutional name. |
| `简称` | abbreviation / short name | Find a common short form. |
| `曾用名` | former name | Find historical company or personal names. |
| `别名` | alias / alternate name | Find other names; verify carefully. |
| `品牌` | brand | Connect a product or brand to an entity. |
| `官网` | official website | Find a claimed official site; verify independently. |
| `主办单位` | operating or sponsoring entity | Especially useful in ICP filing and website-footer context. |
| `统一社会信用代码` | Unified Social Credit Identifier | High-value company identifier. |
| `备案号` | filing number | Website, app, or regulatory filing identifier, depending on context. |

## 5.2 Identity dorks

| Goal | Query template | English translation |
|---|---|---|
| Find a Chinese name | `"[English target name]" 中文名` | English target name plus **Chinese name** |
| Find a likely Chinese company | `"[English target name]" 中国公司` | English target name plus **Chinese company** |
| Find an English name | `"[目标公司全称]" 英文名` | full Chinese company name plus **English name** |
| Find a former name | `"[目标公司全称]" 曾用名` | full company name plus **former name** |
| Find an abbreviation | `"[目标公司全称]" 简称` | full company name plus **abbreviation/short name** |
| Find a claimed official site | `"[目标公司全称]" 官网` | full company name plus **official website** |
| Find a registered identifier | `"[目标公司全称]" 统一社会信用代码` | company name plus **Unified Social Credit Identifier** |
| Identify a domain operator | `"[目标域名]" 主办单位` | domain plus **operating/sponsoring entity** |
| Find an ICP record | `"[目标域名]" ICP备案` | domain plus **ICP filing** |
| Connect brand to company | `"[目标产品名称]" 公司` | product name plus **company** |
| Find a brand owner | `"[目标产品名称]" 商标` | product name plus **trademark** |
| Search an identifier | `"[统一社会信用代码]"` | exact Unified Social Credit Identifier |

## 5.3 High-value identifiers

| Chinese label | English meaning | Why it matters |
|---|---|---|
| `统一社会信用代码` | Unified Social Credit Identifier | Precise pivot across registry, procurement, regulatory, and contract records. |
| `注册号` | registration number | May appear in older company or trademark records; interpret by context. |
| `证券代码` | stock code | Links a listed company to exchange disclosures. |
| `案号` | case number | Precise court-record pivot. |
| `项目编号` | project number | Links tender, correction, award, contract, and acceptance records. |
| `备案号` | filing number | Can identify an ICP, app, or other filing; always note the filing type. |
| `专利申请号` | patent application number | Precise patent pivot. |
| `专利公开号` | patent publication number | Finds a published patent document. |
| `商标注册号` | trademark registration number | Precise trademark pivot. |
| `文号` | official document number | Useful for laws, government notices, approvals, and penalties. |

> [!TIP]
> When a name is common, search the exact identifier by itself first. Then combine it with a location, organization, or source domain.

## 5.4 Simplified, Traditional, and romanized variants

Mainland Chinese sources usually use Simplified Chinese. Hong Kong, Taiwan, Macau, overseas Chinese communities, and historical sources may use Traditional Chinese.

Two different things are at play here, and it helps to keep them separate:

- **Script conversion** changes the characters but not the word. `股东` becomes `股東`; the term is identical, just written in traditional characters.
- **Regional vocabulary** uses a *different word* for the same concept depending on locale. For "software," mainland and Hong Kong sources tend to write `軟件`, while Taiwan typically writes `軟體`. For "network/internet," `網絡` is the standard mainland/Hong Kong traditional form and `網路` is the typical Taiwan form.

When you widen a search, test both the straight traditional conversion **and** the regional synonym, because a Taiwan-hosted page may never contain the mainland word at all.

| Simplified (mainland) | Traditional conversion | Regional variant(s) | English translation |
|---|---|---|---|
| `股东` | `股東` | — | shareholder |
| `招标` | `招標` | — | tendering |
| `诉讼` | `訴訟` | — | litigation |
| `简历` | `簡歷` | — | résumé / biography |
| `软件` | `軟件` (mainland/HK) | `軟體` (Taiwan) | software |
| `网络` | `網絡` (mainland/HK) | `網路` (Taiwan) | network / internet |

For people, test:

- Chinese characters;
- surname first and surname last;
- joined and separated romanization;
- hyphenated given names;
- documented English names;
- institutional affiliation;
- former employer, university, city, or title.

## 5.5 Chinese legal-entity suffixes

| Chinese suffix | English translation |
|---|---|
| `有限公司` | limited liability company |
| `股份有限公司` | company limited by shares / joint-stock limited company |
| `集团有限公司` | group limited liability company |
| `科技有限公司` | technology limited liability company |
| `信息技术有限公司` | information technology limited liability company |
| `分公司` | branch company |
| `子公司` | subsidiary |
| `合伙企业` | partnership enterprise |
| `有限合伙` | limited partnership |
| `个人独资企业` | sole proprietorship enterprise |

Remove or vary a suffix when a full-name search is too restrictive, but restore the full legal name before making an attribution.

---
# 6. Corporate identity and ownership dorks

## 6.1 Corporate-profile keywords

| Chinese term | English translation | Analytical use |
|---|---|---|
| `法定代表人` | legal representative | Registered individual authorized to represent the entity; not automatically the owner or CEO. |
| `法人` | legal person / legal entity | A legal concept, not a synonym for an individual owner. Some commercial interfaces use it loosely; verify the field label. |
| `股东` | shareholder | Direct registered shareholder information. |
| `持股比例` | shareholding percentage | Percentage held by a shareholder. |
| `控股股东` | controlling shareholder | Shareholder with control under the relevant disclosure context. |
| `实际控制人` | actual controller | Person or entity that ultimately exercises control; common in securities disclosures. |
| `股权结构` | equity structure | Ownership structure. |
| `对外投资` | external investments | Other entities in which the target has invested. |
| `注册资本` | registered capital | Legally registered capital; not necessarily cash already contributed. |
| `实缴资本` | paid-in capital | Capital actually contributed, where disclosed. |
| `成立日期` | establishment date | Registered formation date. |
| `注册地址` | registered address | Legal registration address; may differ from operating location. |
| `经营范围` | business scope | Registered scope of activities. |
| `变更记录` | change history | Historical changes to names, officers, capital, address, or scope. |
| `分支机构` | branches | Registered branch entities. |
| `子公司` | subsidiary | Subsidiary relationship; verify ownership percentage and date. |
| `母公司` | parent company | Parent entity. |
| `关联公司` | affiliated / related company | Broad relationship label; verify the basis. |
| `经营异常名录` | list of abnormal business operations | Administrative registry status; read the reason and removal status. |
| `严重违法失信名单` | list of seriously unlawful and dishonest entities | Serious administrative credit designation; verify current status and issuing authority. |
| `注销` | deregistered / cancelled | Registration has been cancelled. |
| `吊销` | business license revoked | License revoked; the entity may still require deregistration. |
| `存续` | active / existing | Common active-status label; wording varies by jurisdiction. |
| `在业` | operating / active | Another active-status label used by some local systems. |

## 6.2 Corporate dork library

| Goal | Query template | English translation |
|---|---|---|
| Find the legal representative | `"[目标公司全称]" 法定代表人` | company name plus **legal representative** |
| Find shareholders | `"[目标公司全称]" 股东` | company name plus **shareholders** |
| Find share percentages | `"[目标公司全称]" 持股比例` | company name plus **shareholding percentage** |
| Find the controlling shareholder | `"[目标公司全称]" 控股股东` | company name plus **controlling shareholder** |
| Find the actual controller | `"[目标公司全称]" 实际控制人` | company name plus **actual controller** |
| Find the equity structure | `"[目标公司全称]" 股权结构` | company name plus **equity structure** |
| Find external investments | `"[目标公司全称]" 对外投资` | company name plus **external investments** |
| Find registered capital | `"[目标公司全称]" 注册资本` | company name plus **registered capital** |
| Find paid-in capital | `"[目标公司全称]" 实缴资本` | company name plus **paid-in capital** |
| Find business scope | `"[目标公司全称]" 经营范围` | company name plus **business scope** |
| Find historical changes | `"[目标公司全称]" 变更记录` | company name plus **change history** |
| Find former names | `"[目标公司全称]" 曾用名` | company name plus **former name** |
| Find branches | `"[目标公司全称]" 分支机构` | company name plus **branches** |
| Find subsidiaries | `"[目标公司全称]" 子公司` | company name plus **subsidiary** |
| Find parent-company claims | `"[目标公司全称]" 母公司` | company name plus **parent company** |
| Find related entities | `"[目标公司全称]" 关联公司` | company name plus **affiliated/related company** |
| Find abnormal-operation records | `"[目标公司全称]" 经营异常名录` | company name plus **list of abnormal business operations** |
| Find serious-dishonesty records | `"[目标公司全称]" 严重违法失信名单` | company name plus **list of seriously unlawful and dishonest entities** |
| Find deregistration references | `"[目标公司全称]" 注销` | company name plus **deregistered/cancelled** |
| Find license-revocation references | `"[目标公司全称]" 吊销` | company name plus **business license revoked** |

## 6.3 State-ownership and control pivots

| Chinese term | English translation |
|---|---|
| `国有企业` | state-owned enterprise |
| `中央企业` | centrally administered state-owned enterprise |
| `地方国企` | local state-owned enterprise |
| `国资委` | State-owned Assets Supervision and Administration Commission / SASAC |
| `国资背景` | state-owned capital background |
| `混合所有制` | mixed ownership |
| `国有控股` | state-controlled |

Useful queries:

```text
"[目标公司全称]" 国有企业
```

**English translation:** company name plus **state-owned enterprise**.

```text
"[目标公司全称]" 国资委
```

**English translation:** company name plus **SASAC / state-owned assets authority**.

```text
"[目标公司全称]" 国有控股
```

**English translation:** company name plus **state-controlled**.

```text
"[目标公司全称]" 实际控制人
```

**English translation:** company name plus **actual controller**.

## 6.4 Corporate-analysis cautions

- `法定代表人` (**legal representative**) is not automatically the founder, owner, controlling shareholder, CEO, or actual controller.
- `法人` legally means a **legal person/entity**. Do not translate it automatically as “legal representative.”
- `注册资本` (**registered capital**) is not the same as `实缴资本` (**paid-in capital**).
- `注册地址` (**registered address**) may be a registration service address, historical address, or different from the operating site.
- A shareholder list is time-sensitive. Record the effective or disclosure date.
- Commercial business-data platforms are useful lead generators but should be checked against the official National Enterprise Credit Information Publicity System and primary filings.
- A subsidiary relationship can change through transfer, dilution, restructuring, or liquidation. Verify the date and percentage.

---

# 7. Listed-company and securities-disclosure dorks

Listed-company disclosures are often among the richest primary sources for ownership, subsidiaries, related-party transactions, litigation, customers, suppliers, major contracts, risks, and executive biographies.

## 7.1 Securities-disclosure keywords

| Chinese term | English translation |
|---|---|
| `年度报告` | annual report |
| `半年度报告` | half-year / interim report |
| `季度报告` | quarterly report |
| `招股说明书` | prospectus |
| `上市公告书` | listing announcement |
| `临时公告` | ad hoc / interim announcement |
| `问询函` | inquiry letter |
| `回复函` | response letter |
| `风险提示` | risk warning |
| `重大合同` | material contract |
| `关联交易` | related-party transaction |
| `重大诉讼` | material litigation |
| `股权质押` | share / equity pledge |
| `控股股东` | controlling shareholder |
| `实际控制人` | actual controller |
| `重大资产重组` | material asset restructuring |
| `证券代码` | stock code |

## 7.2 Listed-company dorks

| Goal | Query template | English translation |
|---|---|---|
| Annual report | `"[目标公司全称]" 年度报告 filetype:pdf` | company name plus **annual report**, PDF only |
| Prospectus | `"[目标公司全称]" 招股说明书 filetype:pdf` | company name plus **prospectus**, PDF only |
| Inquiry letter | `"[目标公司全称]" 问询函` | company name plus **inquiry letter** |
| Response letter | `"[目标公司全称]" 回复函` | company name plus **response letter** |
| Risk disclosure | `"[目标公司全称]" 风险提示` | company name plus **risk warning** |
| Material contract | `"[目标公司全称]" 重大合同` | company name plus **material contract** |
| Related-party transaction | `"[目标公司全称]" 关联交易` | company name plus **related-party transaction** |
| Material litigation | `"[目标公司全称]" 重大诉讼` | company name plus **material litigation** |
| Equity pledge | `"[目标公司全称]" 股权质押` | company name plus **share/equity pledge** |
| Actual controller | `"[目标公司全称]" 实际控制人` | company name plus **actual controller** |
| Search by stock code | `"[证券代码]" 年度报告` | stock code plus **annual report** |
| CNINFO search | `site:cninfo.com.cn "[目标公司全称]"` | company name limited to CNINFO |
| Shanghai exchange search | `site:sse.com.cn "[证券代码]" 问询函` | stock code plus **inquiry letter**, limited to Shanghai Stock Exchange |
| Shenzhen exchange search | `site:szse.cn "[证券代码]" 回复函` | stock code plus **response letter**, limited to Shenzhen Stock Exchange |
| Hong Kong disclosure search | `site:hkexnews.hk "[official English company name]" annual report` | official English company name plus annual report, limited to HKEXnews |

## 7.3 Where the valuable facts hide

In annual reports and prospectuses, search within the document for:

| Chinese term | English translation |
|---|---|
| `主要客户` | major customers |
| `前五大客户` | top five customers |
| `主要供应商` | major suppliers |
| `前五大供应商` | top five suppliers |
| `子公司` | subsidiaries |
| `参股公司` | companies in which the issuer has a minority stake |
| `关联方` | related parties |
| `研发人员` | R&D personnel |
| `核心技术` | core technology |
| `募投项目` | fundraising investment project |
| `产能` | production capacity |
| `生产基地` | production base |
| `或有事项` | contingencies |
| `诉讼仲裁` | litigation and arbitration |
| `行政处罚` | administrative penalty |

> [!NOTE]
> Customer and supplier names may be anonymized, aggregated, or disclosed only above a materiality threshold. A missing name does not prove the relationship does not exist.

---

# 8. People and professional-biography dorks

This section is for lawful professional, academic, public-service, and corporate biography research. Avoid private family, residential, medical, or personal-contact information.

## 8.1 Professional-biography keywords

| Chinese term | English translation |
|---|---|
| `简历` | résumé / biography |
| `个人简介` | personal profile |
| `履历` | career history |
| `任职` | appointment / holds a position |
| `现任` | currently serves as |
| `曾任` | formerly served as |
| `任免` | appointments and removals |
| `毕业于` | graduated from |
| `校友` | alumnus / alumna |
| `导师` | academic adviser / supervisor |
| `论文` | paper / thesis, depending on context |
| `学位论文` | degree thesis / dissertation |
| `研究员` | researcher; also a formal professional title in some institutions |
| `教授` | professor |
| `专访` | feature interview / exclusive interview |
| `访谈` | interview / discussion |
| `演讲` | speech / talk |
| `会议` | conference / meeting |
| `获奖` | award / received an award |

## 8.2 People dork library

| Goal | Query template | English translation |
|---|---|---|
| Find a biography | `"[目标人物姓名]" 简历` | person's name plus **résumé/biography** |
| Find a profile | `"[目标人物姓名]" 个人简介` | person's name plus **personal profile** |
| Find career history | `"[目标人物姓名]" 履历` | person's name plus **career history** |
| Find current roles | `"[目标人物姓名]" 现任` | person's name plus **currently serves as** |
| Find former roles | `"[目标人物姓名]" 曾任` | person's name plus **formerly served as** |
| Find public appointments | `site:gov.cn "[目标人物姓名]" 任免` | person's name plus **appointments and removals**, limited to government domains |
| Find university affiliation | `site:edu.cn "[目标人物姓名]"` | person's name limited to Chinese education domains |
| Find academic adviser references | `site:edu.cn "[目标人物姓名]" 导师` | person's name plus **academic adviser**, limited to education domains |
| Find theses | `site:edu.cn "[目标人物姓名]" 学位论文 filetype:pdf` | person's name plus **degree thesis/dissertation**, education domains, PDF only |
| Find publications | `"[目标人物姓名]" 论文` | person's name plus **paper/thesis** |
| Find interviews | `"[目标人物姓名]" 专访` | person's name plus **feature interview** |
| Find speeches | `"[目标人物姓名]" 演讲` | person's name plus **speech/talk** |
| Connect person and entity | `"[目标人物姓名]" "[目标公司全称]"` | exact person name plus exact company name |
| Find awards | `"[目标人物姓名]" 获奖` | person's name plus **award** |
| Find conference appearances | `"[目标人物姓名]" 会议` | person's name plus **conference/meeting** |

## 8.3 Disambiguating common names

Add one or more of:

- organization;
- city or province;
- job title;
- university;
- specialty;
- graduation year;
- company identifier;
- coauthor;
- conference or project name.

Example:

```text
"[目标人物姓名]" "[目标机构名称]" 简历
```

**English translation:** exact person name plus exact organization name plus **résumé/biography**.

## 8.4 Biography cautions

- A `简历` (**résumé/biography**) on a government, university, or listed-company page is generally stronger than a scraped biography site.
- Chinese names are highly collision-prone. Match at least two independent attributes before merging records.
- An English name may be chosen, translated, abbreviated, or changed over time.
- “Formerly served as” can refer to a temporary appointment, concurrent role, or subsidiary position. Preserve the original wording and date.
- Do not infer ethnicity, religion, political belief, or family relationships from names alone.

---

# 9. Government, regulatory, and licensing dorks

## 9.1 Government-record keywords

| Chinese term | English translation |
|---|---|
| `公告` | announcement |
| `公示` | public notice / public disclosure |
| `通知` | notice |
| `通报` | bulletin / official circular |
| `批复` | official approval / written reply |
| `备案` | filing / recordal |
| `许可` | license / permit |
| `许可证` | license / permit certificate |
| `行政许可` | administrative license |
| `行政处罚` | administrative penalty |
| `处罚决定书` | penalty decision |
| `监督检查` | supervision and inspection |
| `抽查` | spot check |
| `抽查结果` | spot-check result |
| `整改` | rectification / remediation |
| `责令改正` | ordered to correct |
| `约谈` | regulatory interview / summoned meeting |
| `立案调查` | investigation formally opened |
| `信用信息` | credit information |
| `名单` | list / roster |
| `征求意见稿` | draft for public comment |
| `试行` | trial implementation |
| `暂行` | interim |
| `废止` | repealed / abolished |
| `现行有效` | currently effective |

## 9.2 Government and regulatory dorks

| Goal | Query template | English translation |
|---|---|---|
| Broad government search | `site:gov.cn "[目标公司全称]"` | company name limited to Chinese government domains |
| Public notices | `site:gov.cn "[目标公司全称]" 公示` | company name plus **public notice**, government domains |
| Announcements | `site:gov.cn "[目标公司全称]" 公告` | company name plus **announcement**, government domains |
| Administrative penalties | `site:gov.cn "[目标公司全称]" 行政处罚` | company name plus **administrative penalty**, government domains |
| Penalty decision | `"[目标公司全称]" 处罚决定书 filetype:pdf` | company name plus **penalty decision**, PDF only |
| Licenses | `site:gov.cn "[目标公司全称]" 行政许可` | company name plus **administrative license**, government domains |
| Official approval | `"[目标公司全称]" 批复 filetype:pdf` | company name plus **official approval/reply**, PDF only |
| Filing references | `"[目标公司全称]" 备案` | company name plus **filing/recordal** |
| Inspection result | `"[目标公司全称]" 抽查结果` | company name plus **spot-check result** |
| Ordered correction | `"[目标公司全称]" 责令改正` | company name plus **ordered to correct** |
| Regulatory meeting | `"[目标公司全称]" 约谈` | company name plus **regulatory interview/summoned meeting** |
| Investigation opened | `"[目标公司全称]" 立案调查` | company name plus **investigation formally opened** |
| Rectification | `"[目标公司全称]" 整改` | company name plus **rectification/remediation** |
| Search by official document number | `"[文号]"` | exact official document number |

## 9.3 Environmental, safety, and market-regulation pivots

| Chinese term | English translation |
|---|---|
| `环境影响评价` | environmental impact assessment |
| `环评` | EIA / environmental impact assessment abbreviation |
| `环评批复` | EIA approval |
| `排污许可` | pollutant-discharge permit |
| `环境信息披露` | environmental information disclosure |
| `安全生产` | work safety / production safety |
| `事故调查报告` | accident investigation report |
| `应急预案` | emergency response plan |
| `产品质量` | product quality |
| `监督抽检` | supervisory sampling inspection |
| `不合格` | non-compliant / failed inspection |
| `召回` | recall |

Useful queries:

```text
"[目标公司全称]" 环评 filetype:pdf
```

**English translation:** company name plus **environmental impact assessment**, PDF only.

```text
"[目标公司全称]" 环评批复
```

**English translation:** company name plus **EIA approval**.

```text
"[目标公司全称]" 排污许可
```

**English translation:** company name plus **pollutant-discharge permit**.

```text
"[目标公司全称]" 事故调查报告 filetype:pdf
```

**English translation:** company name plus **accident investigation report**, PDF only.

```text
"[目标产品名称]" 监督抽检 不合格
```

**English translation:** product name plus **supervisory sampling inspection** and **failed/non-compliant**.

## 9.4 Regulatory-status cautions

- `立案调查` (**investigation formally opened**) is not a final finding.
- `涉嫌` (**suspected/alleged**) indicates an allegation, not established liability.
- `征求意见稿` (**draft for public comment**) is not final law or policy.
- `拟` (**proposed/intends to**) signals a planned action, not a completed one.
- A penalty may have been appealed, modified, paid, or later removed from an active list.
- Read the issuing authority, legal basis, date, target entity identifier, operative decision, and current status.

---

# 10. Procurement, tenders, and contract dorks

Procurement records can reveal customers, suppliers, products, pricing, project locations, implementation partners, technical specifications, and institutional relationships.

## 10.1 Procurement vocabulary

| Chinese term | English translation |
|---|---|
| `采购意向` | procurement intention / planned procurement |
| `采购公告` | procurement notice |
| `招标公告` | tender notice |
| `资格预审` | prequalification |
| `招标文件` | tender documents |
| `投标` | bidding / submit a bid |
| `开标` | bid opening |
| `中标候选人` | winning-bid candidate |
| `中标候选人公示` | public notice of winning-bid candidates |
| `中标公告` | award notice / winning-bid announcement |
| `中标人` | successful bidder / awardee |
| `成交公告` | award / transaction notice |
| `更正公告` | correction notice |
| `终止公告` | termination notice |
| `废标公告` | failed-bid / tender-cancellation notice |
| `采购合同` | procurement contract |
| `合同公告` | contract announcement |
| `验收公告` | acceptance / inspection announcement |
| `项目编号` | project number |
| `预算金额` | budget amount |
| `中标金额` | winning-bid amount |
| `成交金额` | transaction / awarded amount |
| `供应商` | supplier / vendor |
| `采购人` | procuring entity |
| `代理机构` | procurement agency |
| `公开招标` | open tender |
| `竞争性磋商` | competitive consultation, a procurement method |
| `竞争性谈判` | competitive negotiation |
| `询价` | request for quotation / price inquiry |
| `单一来源采购` | single-source procurement |
| `入围` | shortlisted / selected for a framework or pool |

## 10.2 Procurement lifecycle

A typical public-procurement trail may include:

`采购意向` (**procurement intention**) → `采购公告` or `招标公告` (**procurement or tender notice**) → `更正公告` (**correction notice**) → `中标候选人公示` (**winning-bid candidate notice**) → `中标公告` or `成交公告` (**award notice**) → `采购合同` or `合同公告` (**procurement contract or contract announcement**) → `验收公告` (**acceptance announcement**).

Not every project uses every stage, and terminology varies by procurement method.

## 10.3 Procurement dork library

| Goal | Query template | English translation |
|---|---|---|
| Find tender notices | `"[目标公司全称]" 招标公告` | company name plus **tender notice** |
| Find procurement notices | `"[目标公司全称]" 采购公告` | company name plus **procurement notice** |
| Find candidate notices | `"[目标公司全称]" 中标候选人公示` | company name plus **winning-bid candidate notice** |
| Find awards | `"[目标公司全称]" 中标公告` | company name plus **award notice** |
| Find transaction awards | `"[目标公司全称]" 成交公告` | company name plus **award/transaction notice** |
| Find contracts | `"[目标公司全称]" 采购合同` | company name plus **procurement contract** |
| Find contract announcements | `"[目标公司全称]" 合同公告` | company name plus **contract announcement** |
| Find acceptance records | `"[目标公司全称]" 验收公告` | company name plus **acceptance announcement** |
| Find winning amounts | `"[目标公司全称]" 中标金额` | company name plus **winning-bid amount** |
| Find single-source procurements | `"[目标公司全称]" 单一来源采购` | company name plus **single-source procurement** |
| Find competitive consultations | `"[目标公司全称]" 竞争性磋商` | company name plus **competitive consultation** |
| Search project number | `"[项目编号]"` | exact project number |
| Government procurement portal | `site:ccgp.gov.cn "[目标公司全称]" 中标公告` | company name plus **award notice**, limited to China Government Procurement Network |
| Public-resources portal | `site:ggzy.gov.cn "[目标公司全称]" 成交公示` | company name plus **award/transaction public notice**, limited to National Public Resources Trading Platform |
| PDF contract search | `"[目标公司全称]" 采购合同 filetype:pdf` | company name plus **procurement contract**, PDF only |
| Spreadsheet award search | `"[目标公司全称]" 中标名单 filetype:xls` | company name plus **awardee list**, Excel only |

## 10.4 Bidirectional relationship searches

Search both sides of a relationship:

```text
"[供应商全称]" "[采购人全称]"
```

**English translation:** exact **supplier name** plus exact **procuring-entity name**.

```text
"[采购人全称]" 供应商 "[供应商全称]"
```

**English translation:** exact procuring entity plus **supplier/vendor** plus exact supplier name.

```text
"[项目编号]" 更正公告
```

**English translation:** exact project number plus **correction notice**.

The project number often connects records that use shortened or inconsistent company names.

## 10.5 Procurement cautions

- `中标候选人` (**winning-bid candidate**) is not necessarily the final awardee.
- `拟中标` (**proposed winner**) is not a completed award.
- `中标公告` (**award notice**) does not prove the contract was signed, performed, accepted, or paid.
- A `更正公告` (**correction notice**) may alter names, amounts, dates, or technical requirements.
- Search the project number across every stage.
- Distinguish the supplier, consortium member, subcontractor, procurement agent, and procuring entity.
- Amounts may include or exclude taxes, options, lots, or framework ceilings.

---

# 11. Litigation, court, and enforcement dorks

Court and enforcement research is legally and ethically sensitive. Use official records where possible, preserve context, and do not equate a named party with wrongdoing.

## 11.1 Legal-record vocabulary

| Chinese term | English translation |
|---|---|
| `诉讼` | litigation |
| `案件` | case |
| `案号` | case number |
| `案由` | cause of action / case classification |
| `原告` | plaintiff |
| `被告` | defendant |
| `上诉人` | appellant |
| `被上诉人` | appellee / respondent on appeal |
| `判决书` | judgment |
| `裁定书` | ruling / order |
| `决定书` | decision |
| `调解书` | mediation statement / mediated settlement document |
| `开庭公告` | hearing notice |
| `庭审` | court hearing / trial proceedings |
| `执行` | enforcement |
| `被执行人` | person or entity subject to enforcement |
| `失信被执行人` | dishonest judgment debtor / judgment defaulter designation |
| `限制高消费` | restriction on high consumption |
| `终本案件` | enforcement case terminated for the current procedure |
| `破产` | bankruptcy / insolvency proceeding |
| `清算` | liquidation |
| `仲裁` | arbitration |

## 11.2 Legal and enforcement dorks

| Goal | Query template | English translation |
|---|---|---|
| Broad litigation search | `"[目标公司全称]" 诉讼` | company name plus **litigation** |
| Find case numbers | `"[目标公司全称]" 案号` | company name plus **case number** |
| Find judgments | `"[目标公司全称]" 判决书` | company name plus **judgment** |
| Find rulings | `"[目标公司全称]" 裁定书` | company name plus **ruling/order** |
| Find hearing notices | `"[目标公司全称]" 开庭公告` | company name plus **hearing notice** |
| Find plaintiff references | `"[目标公司全称]" 原告` | company name plus **plaintiff** |
| Find defendant references | `"[目标公司全称]" 被告` | company name plus **defendant** |
| Find enforcement records | `"[目标公司全称]" 被执行人` | company name plus **subject to enforcement** |
| Find defaulter designations | `"[目标公司全称]" 失信被执行人` | company name plus **dishonest judgment debtor designation** |
| Find consumption restrictions | `"[目标公司全称]" 限制高消费` | company name plus **restriction on high consumption** |
| Find bankruptcy references | `"[目标公司全称]" 破产` | company name plus **bankruptcy** |
| Find liquidation references | `"[目标公司全称]" 清算` | company name plus **liquidation** |
| Find arbitration references | `"[目标公司全称]" 仲裁` | company name plus **arbitration** |
| Search exact case number | `"[案号]"` | exact case number |
| Court-domain search | `site:court.gov.cn "[目标公司全称]"` | company name limited to Chinese court domains |

## 11.3 Case-number variants

Chinese case numbers often contain full-width parentheses and a structured court code. Search the exact form and punctuation variants.

Example placeholder:

```text
"（2024）[法院代码][案件类型][序号]号"
```

**English translation:** exact 2024 Chinese case number with court code, case type, and sequence number.

Retry with ASCII parentheses if necessary:

```text
"(2024)[法院代码][案件类型][序号]号"
```

**English translation:** the same case number using ASCII parentheses.

## 11.4 Legal-analysis cautions

- Being a plaintiff, defendant, or named third party does not itself establish wrongdoing.
- `被执行人` (**subject to enforcement**) is not the same as `失信被执行人` (**dishonest judgment debtor / judgment defaulter designation**).
- A record may have been satisfied, removed, corrected, appealed, or superseded.
- Court-document availability can change, and official portals may require verification or have intermittent access.
- Search the exact legal entity identifier when possible; same-name companies are common.
- Read the disposition, effective status, court level, dates, parties, and amount—not just the headline or snippet.
- Do not republish personal identifiers that are unnecessary to the research purpose.

---
# 12. Reports, PDFs, spreadsheets, and presentation dorks

Public documents often contain names, project numbers, signatures, organizational charts, technical details, budgets, locations, and historical facts that do not appear in ordinary web pages.

## 12.1 Document keywords

| Chinese term | English translation |
|---|---|
| `报告` | report |
| `年度报告` | annual report |
| `社会责任报告` | corporate social responsibility report |
| `可持续发展报告` | sustainability report |
| `环境信息披露报告` | environmental information disclosure report |
| `白皮书` | white paper |
| `蓝皮书` | blue book / analytical report series |
| `手册` | handbook / manual |
| `指南` | guide / guidelines |
| `方案` | plan / proposal / solution |
| `规划` | plan / development plan |
| `通知` | notice |
| `公示` | public notice |
| `名单` | list / roster |
| `附件` | attachment / appendix |
| `会议纪要` | meeting minutes |
| `验收报告` | acceptance report |
| `审计报告` | audit report |
| `评估报告` | assessment report |
| `申请表` | application form |
| `下载` | download |
| `全文` | full text |

## 12.2 File-type dork library

| Goal | Query template | English translation |
|---|---|---|
| General PDF search | `"[目标公司全称]" filetype:pdf` | company name in PDF files |
| Annual reports | `"[目标公司全称]" 年度报告 filetype:pdf` | company name plus **annual report**, PDF only |
| CSR reports | `"[目标公司全称]" 社会责任报告 filetype:pdf` | company name plus **corporate social responsibility report**, PDF only |
| Sustainability reports | `"[目标公司全称]" 可持续发展报告 filetype:pdf` | company name plus **sustainability report**, PDF only |
| White papers | `"[目标产品名称]" 白皮书 filetype:pdf` | product name plus **white paper**, PDF only |
| Audit reports | `"[目标公司全称]" 审计报告 filetype:pdf` | company name plus **audit report**, PDF only |
| Acceptance reports | `"[目标公司全称]" 验收报告 filetype:pdf` | company name plus **acceptance report**, PDF only |
| Public lists in spreadsheets | `"[目标关键词]" 名单 filetype:xls` | target keyword plus **list/roster**, Excel only |
| Modern spreadsheets | `"[目标关键词]" 名单 filetype:xlsx` | target keyword plus **list/roster**, modern Excel only |
| Presentations | `"[目标公司全称]" filetype:ppt` | company name in PowerPoint files |
| Modern presentations | `"[目标公司全称]" filetype:pptx` | company name in modern PowerPoint files |
| Word documents | `"[目标公司全称]" 通知 filetype:doc` | company name plus **notice**, Word only |
| Modern Word documents | `"[目标公司全称]" 公示 filetype:docx` | company name plus **public notice**, modern Word only |
| Attachments | `"[目标公司全称]" 附件 filetype:pdf` | company name plus **attachment/appendix**, PDF only |
| Title-focused public notice | `intitle:公示 "[目标公司全称]"` | title contains **public notice**, plus company name |
| Meeting minutes | `"[目标机构名称]" 会议纪要 filetype:pdf` | organization name plus **meeting minutes**, PDF only |

## 12.3 When `filetype:` does not work

Try these fallback approaches:

1. Search the document title without the operator.
2. Search the extension as text, such as `.pdf`, while recognizing that this is less precise.
3. Use `intitle:` with a document term.
4. Search the issuing organization's site directly.
5. Use the site's own attachment or download filters.
6. Search a unique phrase from a snippet in quotation marks.
7. Try another search engine with stronger documented file-type support.

## 12.4 Document-analysis cautions

- A filename can be misleading. Verify the issuing organization and document body.
- Search-engine dates may reflect crawl or update time rather than publication time.
- A draft may be labeled `征求意见稿` (**draft for public comment**), `草案` (**draft**), `试行` (**trial implementation**), or `暂行` (**interim**).
- Check whether a document was replaced, corrected, repealed, or superseded.
- Spreadsheets may contain hidden sheets, filters, formulas, or multiple tabs. Review the full workbook safely.
- Do not enable macros or active content in untrusted files.
- Respect copyright and redistribution restrictions even when a document is publicly discoverable.

---

# 13. News, incidents, disputes, and reputation dorks

This category is useful for crisis research, due diligence, event reconstruction, and claim verification. It is also highly vulnerable to rumor amplification, duplicated reporting, and mistaken identity.

## 13.1 Incident and response keywords

| Chinese term | English translation |
|---|---|
| `声明` | statement |
| `回应` | response |
| `辟谣` | rumor rebuttal / denial |
| `道歉` | apology |
| `通报` | bulletin / official circular |
| `调查` | investigation |
| `事故` | accident / incident |
| `火灾` | fire |
| `爆炸` | explosion |
| `泄漏` | leak / spill |
| `召回` | recall |
| `停产` | production suspension |
| `整改` | rectification / remediation |
| `投诉` | complaint |
| `维权` | rights-protection action / consumer activism |
| `欠薪` | wage arrears |
| `裁员` | layoffs |
| `停业` | suspension of business / closed for business |
| `破产` | bankruptcy |
| `清算` | liquidation |
| `舆情` | public opinion / media sentiment |
| `涉嫌` | suspected / alleged |
| `处罚` | penalty |
| `失联` | unreachable / reportedly missing from contact |

## 13.2 Incident and reputation dorks

| Goal | Query template | English translation |
|---|---|---|
| Find official or corporate statements | `"[目标公司全称]" 声明` | company name plus **statement** |
| Find responses | `"[目标公司全称]" 回应` | company name plus **response** |
| Find rumor rebuttals | `"[目标公司全称]" 辟谣` | company name plus **rumor rebuttal/denial** |
| Find apologies | `"[目标公司全称]" 道歉` | company name plus **apology** |
| Find official bulletins | `"[目标公司全称]" 通报` | company name plus **official bulletin/circular** |
| Find accident reports | `"[目标公司全称]" 事故` | company name plus **accident/incident** |
| Find fire references | `"[目标公司全称]" 火灾` | company name plus **fire** |
| Find explosion references | `"[目标公司全称]" 爆炸` | company name plus **explosion** |
| Find leak or spill references | `"[目标公司全称]" 泄漏` | company name plus **leak/spill** |
| Find recalls | `"[目标产品名称]" 召回` | product name plus **recall** |
| Find production suspensions | `"[目标公司全称]" 停产` | company name plus **production suspension** |
| Find remediation | `"[目标公司全称]" 整改` | company name plus **rectification/remediation** |
| Find complaints | `"[目标公司全称]" 投诉` | company name plus **complaint** |
| Find labor disputes | `"[目标公司全称]" 欠薪` | company name plus **wage arrears** |
| Find layoff reporting | `"[目标公司全称]" 裁员` | company name plus **layoffs** |
| Find bankruptcy reporting | `"[目标公司全称]" 破产` | company name plus **bankruptcy** |
| Find liquidation reporting | `"[目标公司全称]" 清算` | company name plus **liquidation** |

## 13.3 Build an event chronology

Combine the target with dates and status words:

```text
"[目标公司全称]" 事故 2025年
```

**English translation:** company name plus **accident/incident** plus **the year 2025**.

```text
"[目标公司全称]" 通报 2025年5月
```

**English translation:** company name plus **official bulletin/circular** plus **May 2025**.

```text
"[目标公司全称]" 回应 "[事件关键词]"
```

**English translation:** company name plus **response** plus the exact event keyword.

Search date variants such as `2025年5月` (**May 2025**), `2025-05`, and `2025/05`.

## 13.4 Incident-verification safeguards

- Separate the original allegation, the target's response, regulator statements, police or emergency notices, and later outcomes.
- Syndicated articles can create the illusion of multiple independent sources. Trace them back to the earliest named source.
- `网传` means **circulating online / reportedly shared online** and is not verification.
- `据悉` means **it is reported / it is understood** and may conceal weak sourcing.
- `涉嫌` means **suspected/alleged**, not proven.
- A corporate `声明` (**statement**) is a primary source for what the company says, not independent proof that the statement is true.
- Match the exact company name, location, product, and date before attributing an incident.

---

# 14. Supply-chain, customer, and partnership dorks

## 14.1 Relationship keywords

| Chinese term | English translation |
|---|---|
| `供应商` | supplier / vendor |
| `客户` | customer / client |
| `主要客户` | major customer |
| `合作伙伴` | partner |
| `战略合作` | strategic cooperation |
| `签约` | contract signing / signed an agreement |
| `协议` | agreement |
| `框架协议` | framework agreement |
| `中标` | won a bid / award |
| `入围` | shortlisted / admitted to a supplier pool |
| `经销商` | distributor |
| `代理商` | agent / reseller |
| `渠道商` | channel partner |
| `代工` | contract manufacturing / OEM production |
| `委托生产` | commissioned production / contract manufacturing |
| `生产商` | manufacturer |
| `制造商` | manufacturer |
| `采购` | procurement / purchasing |
| `联合研发` | joint research and development |
| `联合实验室` | joint laboratory |
| `生态伙伴` | ecosystem partner |

## 14.2 Relationship dork library

| Goal | Query template | English translation |
|---|---|---|
| Find suppliers | `"[目标公司全称]" 供应商` | company name plus **supplier/vendor** |
| Find customers | `"[目标公司全称]" 客户` | company name plus **customer/client** |
| Find major customers | `"[目标公司全称]" 主要客户` | company name plus **major customer** |
| Find partners | `"[目标公司全称]" 合作伙伴` | company name plus **partner** |
| Find strategic cooperation | `"[目标公司全称]" 战略合作` | company name plus **strategic cooperation** |
| Find contract-signing news | `"[目标公司全称]" 签约` | company name plus **contract signing** |
| Find framework agreements | `"[目标公司全称]" 框架协议` | company name plus **framework agreement** |
| Find supplier-pool inclusion | `"[目标公司全称]" 入围` | company name plus **shortlisted/admitted to pool** |
| Find distributors | `"[目标产品名称]" 经销商` | product name plus **distributor** |
| Find agents | `"[目标产品名称]" 代理商` | product name plus **agent/reseller** |
| Find contract manufacturers | `"[目标产品名称]" 代工` | product name plus **contract manufacturing/OEM** |
| Find commissioned production | `"[目标公司全称]" 委托生产` | company name plus **commissioned production** |
| Find joint R&D | `"[目标公司全称]" 联合研发` | company name plus **joint R&D** |
| Find joint laboratories | `"[目标公司全称]" 联合实验室` | company name plus **joint laboratory** |
| Test a named relationship | `"[公司A全称]" "[公司B全称]"` | exact company A plus exact company B |

## 14.3 Relationship-verification method

For each suspected relationship, look for at least one of:

- procurement award or contract;
- securities disclosure;
- official announcement by both parties;
- patent co-application;
- joint standard drafting;
- product label or regulatory filing;
- facility or environmental record;
- recurring dated evidence rather than one marketing post.

## 14.4 Relationship cautions

- `合作伙伴` (**partner**) can be a loose marketing label.
- `战略合作` (**strategic cooperation**) may describe a non-binding memorandum.
- `签约` (**contract signing**) does not prove implementation, revenue, exclusivity, or current status.
- `入围` (**shortlisted/admitted to a pool**) may not result in any order.
- A company may appear as a distributor, integrator, agent, reseller, subcontractor, or manufacturer. Do not collapse these roles.
- Search both entities' full legal names and the project or agreement title.

---

# 15. Domains, apps, repositories, and technical-footprint dorks

This section is limited to public attribution, public documentation, public repositories, public filings, and defensive research. It does not include secret hunting or unauthorized access.

## 15.1 Technical-footprint vocabulary

| Chinese term | English translation |
|---|---|
| `ICP备案` | ICP filing |
| `ICP备案号` | ICP filing number |
| `主办单位` | operating / sponsoring entity |
| `网站名称` | website name |
| `域名` | domain name |
| `APP备案` | app filing |
| `隐私政策` | privacy policy |
| `用户协议` | user agreement / terms of service |
| `小程序` | mini program |
| `微信公众号` | WeChat Official Account |
| `软件著作权` | software copyright registration |
| `软著` | software copyright, abbreviated |
| `版本号` | version number |
| `更新日志` | changelog / update log |
| `招聘` | recruiting / jobs |
| `研发` | research and development |
| `运维` | operations and maintenance |
| `技术栈` | technology stack |
| `信息安全` | information security |
| `网络安全` | cybersecurity / network security |
| `数据中心` | data center |
| `云平台` | cloud platform |

## 15.2 Domain and app dork library

| Goal | Query template | English translation |
|---|---|---|
| Find ICP references | `"[目标域名]" ICP备案` | domain plus **ICP filing** |
| Find operating entity | `"[目标域名]" 主办单位` | domain plus **operating/sponsoring entity** |
| Search filing number | `"[备案号]"` | exact filing number |
| Find website name | `"[目标域名]" 网站名称` | domain plus **website name** |
| Find app filings | `"[目标应用名称]" APP备案` | app name plus **app filing** |
| Find privacy policy | `"[目标应用名称]" 隐私政策` | app name plus **privacy policy** |
| Find user agreement | `"[目标应用名称]" 用户协议` | app name plus **user agreement/terms of service** |
| Find mini programs | `"[目标公司全称]" 小程序` | company name plus **mini program** |
| Find WeChat accounts | `"[目标公司全称]" 微信公众号` | company name plus **WeChat Official Account** |
| Find software copyrights | `"[目标公司全称]" 软件著作权` | company name plus **software copyright registration** |
| Search abbreviation | `"[目标公司全称]" 软著` | company name plus abbreviated **software copyright** |
| Find version references | `"[目标应用名称]" 版本号` | app name plus **version number** |
| Find changelogs | `"[目标应用名称]" 更新日志` | app name plus **changelog/update log** |
| Find public Gitee references | `site:gitee.com "[目标公司全称]"` | company name limited to public Gitee pages |
| Find public GitHub references | `site:github.com "[目标域名]"` | domain limited to public GitHub pages |
| Infer public hiring needs | `"[目标公司全称]" 招聘 Java` | company name plus **recruiting/jobs** plus Java |
| Find operations roles | `"[目标公司全称]" 招聘 运维` | company name plus **recruiting/jobs** plus **operations and maintenance** |
| Find security roles | `"[目标公司全称]" 招聘 信息安全` | company name plus **recruiting/jobs** plus **information security** |
| Find data-center references | `"[目标公司全称]" 数据中心` | company name plus **data center** |
| Find cloud-platform references | `"[目标公司全称]" 云平台` | company name plus **cloud platform** |

## 15.3 ICP attribution workflow

1. Search the domain footer for an `ICP备案号` (**ICP filing number**).
2. Query the official Ministry of Industry and Information Technology filing system.
3. Record the `主办单位` (**operating/sponsoring entity**), `网站名称` (**website name**), filing number, and date displayed.
4. Compare the operating entity with the company registry, privacy policy, app store listing, and public disclosures.
5. Check whether the domain redirects, has changed ownership, or hosts a product operated by a subsidiary.

The Ministry of Industry and Information Technology identifies `beian.miit.gov.cn` as the official ICP/IP address/domain filing system domain.[^miit-icp]

## 15.4 Technical-footprint cautions

- An ICP filing identifies a registered operating entity in a particular filing context; it does not by itself prove beneficial ownership, current control, or responsibility for every subdomain.
- Privacy policies and user agreements may identify processors, affiliates, SDK providers, and data-transfer relationships, but they can become stale.
- Job advertisements reveal desired skills, not necessarily the production architecture.
- Public repositories may be unofficial forks, employee hobby projects, mirrors, or abandoned code.
- Do not search for or use exposed credentials, secrets, private keys, tokens, or protected systems.
- Do not bypass repository, app, or website access controls.

---

# 16. Patents, trademarks, software copyright, and standards

Intellectual-property and standards records can reveal inventors, applicants, research themes, product names, ownership transfers, affiliated entities, and technical partnerships.

## 16.1 Intellectual-property vocabulary

| Chinese term | English translation |
|---|---|
| `专利` | patent |
| `专利申请` | patent application |
| `申请人` | applicant |
| `发明人` | inventor |
| `专利权人` | patentee / patent owner |
| `申请号` | application number |
| `公开号` | publication number |
| `授权公告号` | grant publication number |
| `法律状态` | legal status |
| `转让` | assignment / transfer |
| `许可` | license |
| `商标` | trademark |
| `商标注册号` | trademark registration number |
| `商标申请人` | trademark applicant |
| `商标权利人` | trademark owner / rights holder |
| `尼斯分类` | Nice Classification |
| `软件著作权` | software copyright registration |
| `团体标准` | association / group standard |
| `企业标准` | enterprise standard |
| `国家标准` | national standard |
| `行业标准` | industry standard |
| `起草单位` | drafting organization |
| `参编单位` | participating drafting organization |
| `标准号` | standard number |

## 16.2 Patent and trademark dork library

| Goal | Query template | English translation |
|---|---|---|
| Find patents | `"[目标公司全称]" 专利` | company name plus **patent** |
| Find applicant records | `"[目标公司全称]" 申请人 专利` | company name plus **applicant** plus **patent** |
| Find inventors | `"[目标公司全称]" 发明人` | company name plus **inventor** |
| Search an inventor | `"[目标人物姓名]" 发明人` | person's name plus **inventor** |
| Search application number | `"[专利申请号]"` | exact patent application number |
| Search publication number | `"[专利公开号]"` | exact patent publication number |
| Find patent transfers | `"[目标公司全称]" 专利 转让` | company name plus **patent transfer** |
| Find trademarks | `"[目标公司全称]" 商标` | company name plus **trademark** |
| Find brand trademark records | `"[目标产品名称]" 商标` | product name plus **trademark** |
| Search trademark number | `"[商标注册号]"` | exact trademark registration number |
| Find software copyrights | `"[目标公司全称]" 软件著作权` | company name plus **software copyright registration** |
| Find group standards | `"[目标公司全称]" 团体标准` | company name plus **association/group standard** |
| Find enterprise standards | `"[目标公司全称]" 企业标准` | company name plus **enterprise standard** |
| Find drafting organizations | `"[目标公司全称]" 起草单位` | company name plus **drafting organization** |
| Find participating drafters | `"[目标公司全称]" 参编单位` | company name plus **participating drafting organization** |
| Search a standard number | `"[标准号]"` | exact standard number |

## 16.3 Direct official systems

- The **国家知识产权局专利检索及分析系统 (CNIPA Patent Search and Analysis System)** provides public patent search and analysis services.[^cnipa-patent]
- The **中国商标网 (China Trademark Office website)** provides trademark search and related services.[^cnipa-trademark]
- The **全国标准信息公共服务平台 (National Standards Information Public Service Platform)** provides official standards information.[^standards-platform]

## 16.4 IP-analysis cautions

- Patent applicant, current owner, and inventor are different roles.
- A published application is not necessarily granted or currently in force.
- Search the `法律状态` (**legal status**) and relevant dates.
- A trademark application may be rejected, opposed, cancelled, expired, assigned, or limited to specific classes.
- Similar brand names can coexist in different Nice classes.
- A company listed as a `起草单位` (**drafting organization**) helped draft a standard; this does not necessarily mean regulatory authority or exclusive ownership.
- Software copyright registration is evidence of a registration, not a technical security review or proof of originality in every component.

---

# 17. Academic, research, and university dorks

## 17.1 Academic vocabulary

| Chinese term | English translation |
|---|---|
| `论文` | paper / thesis |
| `学位论文` | degree thesis / dissertation |
| `作者` | author |
| `导师` | academic adviser / supervisor |
| `课题` | research topic / project |
| `项目` | project |
| `项目编号` | project number |
| `基金项目` | funded project |
| `实验室` | laboratory |
| `重点实验室` | key laboratory |
| `研究中心` | research center |
| `研究院` | research institute |
| `研究员` | researcher; sometimes a formal professional title |
| `会议论文` | conference paper |
| `专著` | monograph |
| `成果` | research result / achievement |
| `获奖` | award |
| `招生` | admissions / recruiting students |
| `博士生导师` | doctoral supervisor |
| `硕士生导师` | master's supervisor |

## 17.2 Academic dork library

| Goal | Query template | English translation |
|---|---|---|
| University-domain search | `site:edu.cn "[目标人物姓名]"` | person's name limited to Chinese education domains |
| Find papers | `"[目标人物姓名]" 论文` | person's name plus **paper/thesis** |
| Find degree theses | `"[目标人物姓名]" 学位论文` | person's name plus **degree thesis/dissertation** |
| Find thesis PDFs | `site:edu.cn "[目标人物姓名]" 学位论文 filetype:pdf` | person's name plus **degree thesis/dissertation**, education domains, PDF only |
| Find advisers | `"[目标人物姓名]" 导师` | person's name plus **academic adviser** |
| Find doctoral-supervisor pages | `"[目标人物姓名]" 博士生导师` | person's name plus **doctoral supervisor** |
| Find research projects | `"[目标人物姓名]" 课题` | person's name plus **research project/topic** |
| Search project number | `"[项目编号]"` | exact project number |
| Find funded projects | `"[目标机构名称]" 基金项目` | organization name plus **funded project** |
| Find laboratories | `"[目标机构名称]" 实验室` | organization name plus **laboratory** |
| Find key laboratories | `"[目标机构名称]" 重点实验室` | organization name plus **key laboratory** |
| Find research centers | `"[目标机构名称]" 研究中心` | organization name plus **research center** |
| Find conference papers | `"[目标人物姓名]" 会议论文` | person's name plus **conference paper** |
| Search Chinese Academy domains | `site:cas.cn "[目标人物姓名]"` | person's name limited to Chinese Academy of Sciences domains |
| Find awards | `"[目标人物姓名]" 科研 获奖` | person's name plus **scientific research** plus **award** |

## 17.3 Academic-source pivots

Useful sources include:

- `xueshu.baidu.com` — **百度学术 (Baidu Scholar)**;
- `cnki.net` — **中国知网 (China National Knowledge Infrastructure / CNKI)**;
- `wanfangdata.com.cn` — **万方数据 (Wanfang Data)**;
- university repositories under `edu.cn`;
- Chinese Academy of Sciences sites under `cas.cn`;
- Crossref, ORCID, Google Scholar, institutional repositories, and publisher sites for cross-checking international publication records.

Access, indexing, and full-text availability vary. Use bibliographic metadata to locate the authoritative publisher or institutional copy.

## 17.4 Academic-analysis cautions

- A name match is not enough. Confirm affiliation, coauthors, field, dates, and adviser.
- Chinese and English author-name order may differ.
- A paper may be retracted, corrected, duplicated, translated, or published under a former affiliation.
- `导师` (**academic adviser**) can refer to a formal supervisor, mentor, or program listing depending on context.
- A `项目编号` (**project number**) is often a stronger link than a topic title.
- Keep bibliographic metadata separate from claims about employment or political affiliation.

---

# 18. Locations, facilities, factories, and projects

## 18.1 Location and facility vocabulary

| Chinese term | English translation |
|---|---|
| `地址` | address |
| `注册地址` | registered address |
| `办公地址` | office address |
| `总部` | headquarters |
| `分公司` | branch company |
| `办事处` | office / representative office |
| `工厂` | factory |
| `厂区` | plant / factory site |
| `生产基地` | production base |
| `研发中心` | R&D center |
| `数据中心` | data center |
| `仓库` | warehouse |
| `产业园` | industrial park |
| `园区` | park / industrial campus |
| `项目地址` | project address |
| `建设地点` | construction location |
| `占地面积` | site area / land area |
| `建筑面积` | floor area / building area |
| `产能` | production capacity |
| `搬迁` | relocation |
| `扩建` | expansion |
| `新建` | new construction |
| `改建` | reconstruction / modification |
| `竣工` | completion |
| `竣工验收` | completion acceptance |
| `环评` | environmental impact assessment abbreviation |

## 18.2 Location and facility dorks

| Goal | Query template | English translation |
|---|---|---|
| Find registered address | `"[目标公司全称]" 注册地址` | company name plus **registered address** |
| Find office address | `"[目标公司全称]" 办公地址` | company name plus **office address** |
| Find headquarters | `"[目标公司全称]" 总部` | company name plus **headquarters** |
| Find branches | `"[目标公司全称]" 分公司` | company name plus **branch company** |
| Find offices | `"[目标公司全称]" 办事处` | company name plus **office/representative office** |
| Find factories | `"[目标公司全称]" 工厂` | company name plus **factory** |
| Find plant sites | `"[目标公司全称]" 厂区` | company name plus **plant/factory site** |
| Find production bases | `"[目标公司全称]" 生产基地` | company name plus **production base** |
| Find R&D centers | `"[目标公司全称]" 研发中心` | company name plus **R&D center** |
| Find data centers | `"[目标公司全称]" 数据中心` | company name plus **data center** |
| Find project addresses | `"[目标公司全称]" 项目地址` | company name plus **project address** |
| Find construction locations | `"[目标公司全称]" 建设地点` | company name plus **construction location** |
| Find relocation records | `"[目标公司全称]" 搬迁` | company name plus **relocation** |
| Find expansion records | `"[目标公司全称]" 扩建` | company name plus **expansion** |
| Find new construction | `"[目标公司全称]" 新建` | company name plus **new construction** |
| Find EIA documents | `"[目标公司全称]" 环评 filetype:pdf` | company name plus **environmental impact assessment**, PDF only |
| Find completion acceptance | `"[目标公司全称]" 竣工验收` | company name plus **completion acceptance** |
| Find production capacity | `"[目标公司全称]" 产能` | company name plus **production capacity** |

## 18.3 Geospatial workflow

1. Collect registered, office, project, and facility addresses separately.
2. Search the exact address in Baidu Maps, Amap/Gaode Maps, Tencent Maps, and ordinary web search.
3. Compare address variants, old street names, district changes, and transliteration.
4. Search the project or facility name plus `环评` (**environmental impact assessment**), `批复` (**official approval**), and `竣工验收` (**completion acceptance**).
5. Cross-check satellite imagery, street-level imagery where lawfully available, official planning documents, procurement records, and company disclosures.
6. Record the date of each source; facilities open, close, expand, and relocate.

## 18.4 Location cautions

- A registered address is not necessarily an operating site.
- Map points can be user-generated, duplicated, outdated, or placed at a building entrance rather than the actual facility.
- A planned project is not necessarily constructed.
- An EIA approval is not proof of completion or current operation.
- A production-capacity figure may be designed, approved, installed, or actual capacity; preserve the qualifier.

---
# 19. Chinese social and community-platform pivots

Search engines index social platforms unevenly. Use web search for discovery, then use the platform's native search when lawful, available, and necessary.

## 19.1 Platform map and site-restricted dorks

| Chinese platform name | English description | Domain and query template |
|---|---|---|
| `知乎` | Zhihu — Q&A and knowledge-sharing community, often compared with Quora | `site:zhihu.com "[目标关键词]"` — target keyword limited to Zhihu |
| `微博` | Weibo — microblogging and social-media platform | `site:weibo.com "[目标关键词]"` or `site:m.weibo.cn "[目标关键词]"` — target keyword limited to Weibo |
| `百度贴吧` | Baidu Tieba — interest-based forum communities | `site:tieba.baidu.com "[目标关键词]"` — target keyword limited to Baidu Tieba |
| `微信公众号` | WeChat Official Accounts — publisher and organization accounts inside WeChat | `site:mp.weixin.qq.com "[目标关键词]"` — target keyword limited to public WeChat article pages |
| `哔哩哔哩` | Bilibili — video and community platform | `site:bilibili.com "[目标关键词]"` — target keyword limited to Bilibili |
| `小红书` | Xiaohongshu / RED — lifestyle and social-content platform | `site:xiaohongshu.com "[目标关键词]"` — target keyword limited to Xiaohongshu |
| `抖音` | Douyin — short-video platform | `site:douyin.com "[目标关键词]"` — target keyword limited to Douyin |
| `快手` | Kuaishou — short-video and livestream platform | `site:kuaishou.com "[目标关键词]"` — target keyword limited to Kuaishou |
| `百度百科` | Baidu Baike — collaborative online encyclopedia | `site:baike.baidu.com "[目标关键词]"` — target keyword limited to Baidu Baike |
| `百度知道` | Baidu Zhidao — Q&A platform | `site:zhidao.baidu.com "[目标关键词]"` — target keyword limited to Baidu Zhidao |
| `百度文库` | Baidu Wenku — document-sharing platform | `site:wenku.baidu.com "[目标关键词]"` — target keyword limited to Baidu Wenku |
| `百度学术` | Baidu Scholar — academic search | `site:xueshu.baidu.com "[目标关键词]"` — target keyword limited to Baidu Scholar |

## 19.2 Platform-name pivots

Adding a platform name can change the context of a search and surface indexed discussions or reposts.

```text
"[目标公司全称]" 知乎
```

**English translation:** company name plus **Zhihu**.

```text
"[目标人物姓名]" 微博
```

**English translation:** person's name plus **Weibo**.

```text
"[目标产品名称]" 贴吧
```

**English translation:** product name plus **Tieba forum**.

```text
"[目标公司全称]" 微信公众号
```

**English translation:** company name plus **WeChat Official Account**.

```text
"[目标事件关键词]" 小红书
```

**English translation:** event keyword plus **Xiaohongshu/RED**.

```text
"[目标事件关键词]" 抖音
```

**English translation:** event keyword plus **Douyin**.

## 19.3 Useful social-content terms

| Chinese term | English translation |
|---|---|
| `账号` | account |
| `用户名` | username |
| `昵称` | display name / nickname |
| `认证` | verification / certified account status |
| `官方账号` | official account |
| `公众号` | public / official account, commonly WeChat context |
| `博主` | blogger / account creator |
| `作者` | author |
| `原帖` | original post |
| `转发` | repost / reshare |
| `转载` | republished / reposted article |
| `评论` | comment |
| `视频` | video |
| `直播` | livestream |
| `合集` | collection / playlist |
| `删除` | deleted |
| `已注销` | account deregistered / closed, depending on context |

## 19.4 Social-platform cautions

- Search-engine indexing is partial and can lag behind native platform search.
- Native search may require an account, app, region, or CAPTCHA. Do not bypass those controls.
- Display names and avatars are easy to copy. Verify account IDs, certification, linked domains, historical posts, and cross-platform references.
- A certified account can verify platform identity, but not the truth of every post.
- Posts can be edited, deleted, reposted without context, or copied from another source.
- Baidu Baike, Baidu Zhidao, Zhihu, Tieba, and similar community sources are leads, not authoritative records.
- WeChat articles can be difficult to index consistently. Search exact titles, unique sentences, author names, public-account names, and reposts.

---

# 20. Reposts, deleted pages, and archival pivots

A deleted page may survive as a quoted sentence, repost, screenshot, syndicated copy, archived URL, search snippet, attachment, or reference in another document.

## 20.1 Archival and repost vocabulary

| Chinese term | English translation |
|---|---|
| `原文` | original text / original article |
| `全文` | full text |
| `转载` | republished / reposted article |
| `转载自` | republished from |
| `转发` | repost / reshare |
| `来源` | source |
| `作者` | author |
| `截图` | screenshot |
| `存档` | archive |
| `备份` | backup |
| `网页` | webpage |
| `链接` | link |
| `已删除` | deleted |
| `删除文章` | deleted article |
| `失效链接` | dead / invalid link |
| `附件` | attachment |
| `标题` | title |
| `发布时间` | publication time |

## 20.2 Archival dork library

| Goal | Query template | English translation |
|---|---|---|
| Search exact title | `"[完整文章标题]"` | exact full article title |
| Search a unique sentence | `"[独特原文句子]"` | exact unique sentence from the original text |
| Find reposts | `"[完整文章标题]" 转载` | exact title plus **republished/reposted** |
| Find the original | `"[完整文章标题]" 原文` | exact title plus **original article/text** |
| Find full text | `"[完整文章标题]" 全文` | exact title plus **full text** |
| Find screenshots | `"[目标事件关键词]" 截图` | event keyword plus **screenshot** |
| Find backups | `"[完整文章标题]" 备份` | exact title plus **backup** |
| Find archives | `"[完整文章标题]" 存档` | exact title plus **archive** |
| Search a dead URL | `"[完整URL]"` | exact full URL |
| Search URL slug or ID | `"[URL中的独特编号]"` | exact unique identifier from the URL |
| Find source attribution | `"[独特原文句子]" 来源` | unique sentence plus **source** |
| Find WeChat reposts | `site:mp.weixin.qq.com "[完整文章标题]"` | exact title limited to public WeChat pages |
| Find Zhihu discussion | `site:zhihu.com "[完整文章标题]"` | exact title limited to Zhihu |
| Find forum discussion | `site:tieba.baidu.com "[目标事件关键词]"` | event keyword limited to Baidu Tieba |

## 20.3 External archival tools

For a known URL, check lawful public archives such as:

- Internet Archive's Wayback Machine;
- archive.today / archive.ph;
- Common Crawl indexes;
- institutional or national web archives where applicable;
- publisher mirrors and syndication partners.

Archive coverage is incomplete. A missing archived copy is not proof that the page never existed.

## 20.4 Critical correction: platform pivots are not archive commands

A query such as:

```text
"[敏感关键词]" 知乎
```

**English translation:** sensitive keyword plus **Zhihu**.

may find indexed Zhihu discussions, quotations, screenshots, or reposts. It does **not** directly retrieve an archive, bypass filtering, or guarantee recovery of deleted material.

Use precise language when teaching this technique:

> “Add a platform name to look for secondary discussion or reposts,” not “add Zhihu to retrieve archived data.”

## 20.5 Archival cautions

- Search snippets can outlive the underlying page and can be truncated or misattributed.
- Screenshots can be edited. Seek the original URL, surrounding context, timestamp, and independent copies.
- Reposts may omit corrections, disclaimers, images, or publication dates.
- An archived page proves what the archive captured at a point in time, not necessarily authorship, authenticity, or current status.
- Respect copyright and privacy when preserving or redistributing archived material.

---

# 21. Sensitive terms, warning banners, and filtered results

Some political, religious, public-order, health, security, or socially sensitive searches may produce warning banners, curated results, reduced result sets, or different results across engines and locations.

The example in the source slide shows the warning:

```text
提高理性认知，远离邪教陷阱
```

**English translation:** “Improve rational understanding; stay away from cult traps.”

Treat such a banner as an observation about the search environment—not as proof of why a specific page is absent or what every user sees.

## 21.1 Responsible research response

When results appear filtered, incomplete, or unusually curated:

1. Record the exact query, engine, date, location, language setting, and warning text.
2. Search the target's formal name, alternate names, related people, dates, locations, organizations, document numbers, and quoted phrases.
3. Search official terminology and ordinary-language terminology separately.
4. Search multiple public indexes and the relevant platform's native search.
5. Search primary databases directly rather than relying on general web search.
6. Look for lawful reposts, citations, bibliographies, screenshots, or archived URLs.
7. Compare result sets without assuming a single cause for differences.
8. State uncertainty explicitly.

## 21.2 Useful context pivots

| Chinese term | English translation |
|---|---|
| `官方通报` | official bulletin |
| `情况通报` | situation bulletin / official update |
| `历史` | history |
| `研究` | research |
| `论文` | academic paper / thesis |
| `新闻` | news |
| `评论` | commentary |
| `知乎` | Zhihu |
| `微博` | Weibo |
| `贴吧` | Tieba forum |
| `原文` | original text |
| `全文` | full text |
| `截图` | screenshot |

These terms change the context of a query. They are not guaranteed workarounds.

## 21.3 What research says—and what it does not say

Historical studies documented filtering, bias, concentration, and substantial differences among Chinese search-engine result sets.[^zhu-filtering][^jiang-search] Those studies are valuable for understanding that search results are constructed and can vary over time. They do not establish the current treatment of every term, engine, user, or location.

Use current observations, multiple sources, and cautious language.

---

# 22. Official and high-value source map

Search engines are most useful when they lead you to a primary portal. The following map emphasizes official sources and high-value public systems. Availability, CAPTCHA requirements, login requirements, interfaces, and coverage can change.

## 22.1 Company and credit records

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `国家企业信用信息公示系统` | National Enterprise Credit Information Publicity System | [Official company and market-entity information system](https://www.gsxt.gov.cn/). Search by entity name, Unified Social Credit Identifier, or registration number. Official help states that the system provides market-entity credit information and supports name or identifier queries.[^gsxt-help] |
| `信用中国` | Credit China | [National public-credit portal](https://www.creditchina.gov.cn/). Useful for public credit information, administrative records, and linked sectoral sources. |
| `企查查` | Qichacha, commercial business-data aggregator | [Commercial platform](https://www.qcc.com/). Useful for leads and relationship visualization; verify against official records. |
| `天眼查` | Tianyancha, commercial business-data aggregator | [Commercial platform](https://www.tianyancha.com/). Useful for leads; verify important facts. |
| `爱企查` | Aiqicha, Baidu business-data service | [Commercial platform](https://aiqicha.baidu.com/). Useful for discovery; verify important facts. |

> [!NOTE]
> **Access friction is the norm here.** The commercial aggregators above increasingly gate detailed records behind login, Chinese mobile-number or real-name verification, paid subscriptions, and rate limits, and they often restrict or degrade access from outside mainland China. The official `gsxt.gov.cn` system commonly requires a sliding-puzzle CAPTCHA. Plan for this, do not bypass the controls, and record any access limitation in your evidence log (Section 23) so gaps in your findings are not mistaken for confirmed absences.

## 22.2 Procurement and public-resource transactions

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `中国政府采购网` | China Government Procurement Network | [Official national government-procurement site](https://www.ccgp.gov.cn/). The site identifies itself as the Ministry of Finance's designated national government-procurement information publication medium.[^ccgp-official] |
| `全国公共资源交易平台` | National Public Resources Trading Platform | [Official national public-resource transaction platform](https://www.ggzy.gov.cn/). It aggregates public-resource transaction, entity, credit, and regulatory information.[^ggzy-official] |
| `全国公共资源交易平台数据服务` | National Public Resources Trading Platform data service | [Data-service portal](https://data.ggzy.gov.cn/). Useful for entity and award queries. |
| `地方政府采购网` | local government-procurement websites | Search the province or city's official government-procurement domain. Local records may not be fully represented in national search results. |

## 22.3 Courts, cases, and enforcement

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `中国裁判文书网` | China Judgments Online | [Official court-judgment portal](https://wenshu.court.gov.cn/). **Coverage caveat:** after a period of rapid expansion, the number of newly published judgments fell sharply from around 2021 onward, and reporting indicates that courts have shifted much routine publication to a separate internal database that is not open to the public. Treat the *absence* of a judgment here as inconclusive — it may reflect non-publication, redaction, or removal rather than the absence of a case. Use exact entity names and case numbers, and cross-check enforcement, bankruptcy, and listed-company disclosures. |
| `中国执行信息公开网` | China Enforcement Information Disclosure Network | [Official enforcement-information portal](https://zxgk.court.gov.cn/). The Supreme People's Court describes it as a judicial-publicity platform for enforcement information.[^zxgk-official] |
| `中国司法大数据服务网` | China Judicial Big Data Service Network | [Official judicial data and reports portal](https://data.court.gov.cn/). Includes links to major court-publicity systems. |
| `人民法院案例库` | People's Courts Case Database | [Official case database](https://rmfyalk.court.gov.cn/), where available. Focuses on selected reference cases rather than every judgment. |
| `全国企业破产重整案件信息网` | National Enterprise Bankruptcy and Reorganization Case Information Network | [Official bankruptcy and reorganization information portal](https://pccz.court.gov.cn/), where available. |

## 22.4 Laws and regulations

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `国家法律法规数据库` | National Laws and Regulations Database | [Official database maintained by the National People's Congress system](https://flk.npc.gov.cn/). It provides advanced search by title, full text, issuing authority, status, and dates.[^law-database] |
| `中国政府网政策文件库` | State Council / Chinese Government policy document collection | [Central government portal](https://www.gov.cn/zhengce/). Useful for national policy, State Council documents, and official interpretations. |
| `国家规章库` | National rules database | Use the official link from the National Laws and Regulations Database or Ministry of Justice resources; verify current domain and status. |

## 22.5 Domains, apps, and internet filings

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `工业和信息化部ICP/IP地址/域名信息备案管理系统` | MIIT ICP/IP address/domain filing system | [Official filing system](https://beian.miit.gov.cn/). Use for domain and operating-entity attribution.[^miit-icp] |
| `公安机关互联网站安全管理服务平台` | Public-security internet-site security filing service | Search the current official public-security filing portal and verify the domain before use; interfaces may change. |
| `应用商店开发者页面` | app-store developer page | Use official Apple, Huawei, Xiaomi, Tencent, and other store listings to identify developer names, privacy policies, versions, and linked domains. |

## 22.6 Intellectual property and standards

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `国家知识产权局专利检索及分析系统` | CNIPA Patent Search and Analysis System | [Official public patent search and analysis system](https://pss-system.cponline.cnipa.gov.cn/).[^cnipa-patent] |
| `专利业务办理系统` | CNIPA Patent Business Processing System | [Official patent services and examination-information portal](https://cponline.cnipa.gov.cn/). |
| `中国商标网` | China Trademark Office website | [Official trademark services and search portal](https://sbj.cnipa.gov.cn/). |
| `全国标准信息公共服务平台` | National Standards Information Public Service Platform | [Official standards-information portal](https://std.samr.gov.cn/). |

## 22.7 Listed companies and securities

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `巨潮资讯网` | CNINFO listed-company disclosure portal | [Disclosure portal](https://www.cninfo.com.cn/). Search company name, stock code, announcement title, and date. |
| `上海证券交易所` | Shanghai Stock Exchange | [Official exchange site](https://www.sse.com.cn/). |
| `深圳证券交易所` | Shenzhen Stock Exchange | [Official exchange site](https://www.szse.cn/). |
| `北京证券交易所` | Beijing Stock Exchange | [Official exchange site](https://www.bse.cn/). |
| `香港交易所披露易` | HKEXnews disclosure portal | [Official Hong Kong listed-company disclosure portal](https://www.hkexnews.hk/). Search official English and Chinese names and stock code. |
| `全国中小企业股份转让系统` | National Equities Exchange and Quotations / NEEQ | [Official market site](https://www.neeq.com.cn/). |

## 22.8 Education, research, and scholarly sources

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `百度学术` | Baidu Scholar | [Academic search](https://xueshu.baidu.com/). |
| `中国知网` | China National Knowledge Infrastructure / CNKI | [Academic database](https://www.cnki.net/). Access may require subscription. |
| `万方数据` | Wanfang Data | [Academic and standards database](https://www.wanfangdata.com.cn/). Access varies. |
| `中国科学院` | Chinese Academy of Sciences | Search official sites under `cas.cn`. |
| `中国教育和科研计算机网域名` | Chinese education and research domains | Use `site:edu.cn` for universities and educational institutions, while recognizing that coverage is not universal. |

## 22.9 Maps and geospatial sources

| Chinese source name | English purpose | Link and notes |
|---|---|---|
| `百度地图` | Baidu Maps | [Map and POI search](https://map.baidu.com/). |
| `高德地图` | Amap / Gaode Maps | [Map and POI search](https://www.amap.com/). |
| `腾讯地图` | Tencent Maps | [Map and POI search](https://map.qq.com/). |
| `天地图` | Tianditu / National Platform for Common Geospatial Information Services | [Official geospatial platform](https://www.tianditu.gov.cn/). |

> [!IMPORTANT]
> Official portals can still contain errors, delayed updates, incomplete records, redactions, or interface limitations. “Official” means authoritative for the issuing system—not infallible or exhaustive.

---
# 23. Verification and analytical safeguards

A good query finds a page. Good OSINT establishes what the page proves, what it does not prove, and how confidently it can be attributed.

## 23.1 Source hierarchy

Use this hierarchy as a starting point, not an automatic scoring system:

1. **Primary official records:** registries, court documents, procurement notices, exchange disclosures, regulatory decisions, official laws, patents, standards, and signed public contracts.
2. **Direct entity sources:** official websites, verified accounts, privacy policies, annual reports, press releases, job postings, product documentation, and public statements.
3. **Independent professional sources:** reputable newsrooms, academic research, industry publications, and specialist databases with transparent sourcing.
4. **Aggregators:** business-data platforms, scraped biography sites, document mirrors, and republishers.
5. **User-generated content:** forums, Q&A sites, social posts, comments, screenshots, and anonymous claims.

A source's position can change by claim. A company statement is primary evidence of what the company said, but not necessarily independent evidence that the statement is true.

## 23.2 Status words that change the meaning

| Chinese term | English translation | Analytical significance |
|---|---|---|
| `拟` | proposed / intends to | The action is planned, not completed. |
| `征求意见稿` | draft for public comment | Not final law, regulation, or policy. |
| `草案` | draft | Not final. |
| `试行` | trial implementation | In force on a trial basis if formally issued, but check dates and scope. |
| `暂行` | interim | Temporary or interim measure. |
| `修订` | revised / revision | Check which version is effective. |
| `废止` | repealed / abolished | No longer effective from the applicable date. |
| `失效` | expired / invalid | No longer effective. |
| `现行有效` | currently effective | Current status according to the source. |
| `涉嫌` | suspected / alleged | Not a finding of liability. |
| `立案调查` | investigation formally opened | Investigation stage, not final outcome. |
| `中标候选人` | winning-bid candidate | Not necessarily the final awardee. |
| `拟中标` | proposed winner | Not a final award. |
| `中标人` | successful bidder / awardee | Final award status in that notice, subject to later correction or cancellation. |
| `更正` | correction | Earlier information may be wrong or superseded. |
| `终止` | terminated | Process or project stopped. |
| `注销` | deregistered / cancelled | Entity registration cancelled. |
| `吊销` | business license revoked | License revoked; not identical to deregistration. |
| `已履行` | performed / satisfied | Obligation reported as fulfilled. |
| `生效` | effective / entered into force | Legally or operationally effective, depending on context. |

## 23.3 Common analytical traps

Do not automatically equate:

| Finding | Incorrect shortcut |
|---|---|
| `法定代表人` — legal representative | owner, founder, CEO, or actual controller |
| `注册资本` — registered capital | cash paid in or company valuation |
| `注册地址` — registered address | headquarters or active operating facility |
| `中标候选人` — winning-bid candidate | final awardee |
| `中标公告` — award notice | completed contract or successful performance |
| `战略合作` — strategic cooperation | binding, exclusive, or current commercial relationship |
| `被执行人` — subject to enforcement | criminal conviction or dishonest-debtor designation |
| `行政处罚` — administrative penalty | criminal judgment |
| `立案调查` — investigation opened | guilt or liability established |
| Baidu Baike or a scraped profile | verified biography |
| social-media repetition | independent corroboration |
| search warning banner | proof of the reason every result is absent |
| absence from search results | proof that the event or record does not exist |

## 23.4 Three-point identity test

Before merging two records, match at least three strong attributes where possible:

- exact Chinese legal name;
- Unified Social Credit Identifier;
- registered location;
- legal representative or officer;
- stock code;
- domain and ICP operator;
- project number;
- case number;
- patent or trademark identifier;
- dated institutional affiliation.

For people with common names, a company, university, specialty, city, coauthor, or title is essential.

## 23.5 Translation discipline

- Preserve the original Chinese text next to the translation.
- Distinguish official English names from your own translations.
- Machine translation is a research aid, not an authority.
- Legal, regulatory, procurement, and corporate terms often require context-specific translation.
- Do not silently translate `法人` as “legal representative”; use `法定代表人` for that role.
- Preserve qualifiers such as “proposed,” “alleged,” “candidate,” “interim,” and “formerly.”
- Have a qualified human review high-stakes translations.

## 23.6 Evidence log template

| Field | What to record |
|---|---|
| Research question | The claim or relationship being tested |
| Query | Exact query, including Chinese characters and operators |
| English gloss | Translation of the query |
| Engine or portal | Baidu, Google, Bing, official registry, procurement portal, court portal, etc. |
| Date and time | Include time zone |
| Access context | Location, language setting, logged-in or logged-out status if relevant |
| Source URL | Exact page or document URL |
| Issuer / publisher | Organization that issued or published the record |
| Publication date | Date shown on the source |
| Effective date | If different from publication date |
| Target identifiers | Legal name, Unified Social Credit Identifier, stock code, case number, project number, etc. |
| Original passage | Minimum necessary Chinese text |
| English translation | Faithful translation with qualifiers preserved |
| Archive / screenshot | Lawful preserved copy and capture date |
| Confidence | High, medium, low, or another documented scale |
| Contradictions | Conflicting records and how they were resolved |
| Next step | Additional verification required |

## 23.7 Preservation

Where appropriate and lawful:

- save the original document;
- capture a full-page screenshot with URL and timestamp;
- preserve the original filename and metadata;
- record the page title and issuing authority;
- calculate a file hash for integrity;
- save a translation separately rather than overwriting the source;
- note whether the page was dynamic, personalized, or behind an account;
- avoid redistributing unnecessary personal information.

Example SHA-256 integrity commands:

**Linux:**

```bash
sha256sum evidence-file.pdf
```

**macOS:**

```bash
shasum -a 256 evidence-file.pdf
```

**Windows PowerShell:**

```powershell
Get-FileHash -Path .\evidence-file.pdf -Algorithm SHA256
```

Record the command or tool used, the resulting hash, and the time of calculation.

---

# 24. Troubleshooting weak or noisy results

## Problem: Too many irrelevant results

Try:

- quote the full legal name;
- add a location or identifier;
- add one high-specificity Chinese pivot term;
- restrict to an official domain;
- use `intitle:` for the document type;
- exclude a dominant noise term;
- search a project, case, filing, or stock number instead of a name.

Example:

```text
"[目标公司全称]" 行政处罚 site:gov.cn -招聘
```

**English translation:** company name plus **administrative penalty**, limited to government domains, excluding **recruiting/jobs**.

## Problem: Zero results

Relax one constraint at a time:

1. Remove `filetype:`.
2. Remove `site:`.
3. Shorten the quoted phrase.
4. Remove the legal suffix such as `有限公司` (**limited liability company**).
5. Search the abbreviation or former name.
6. Search the identifier.
7. Search Traditional Chinese.
8. Search the English or romanized name.
9. Try another engine.
10. Search the official portal directly.

## Problem: Quotation marks seem ignored

- Use a longer distinctive phrase.
- Add an identifier.
- Verify whether the result actually contains the full phrase.
- Use Baidu Advanced Search's exact-phrase field.
- Search a unique sentence from the page.
- Try another engine with documented exact-match behavior.

## Problem: `site:` results are sparse

- Search the exact host rather than a broad parent domain.
- Remove the protocol and path.
- Search the title or identifier without `site:` and inspect the destination domain.
- Use the website's internal search.
- Search the official portal's downloadable files or data service.
- Remember that `site:` is not exhaustive.

## Problem: `filetype:` returns ordinary pages

- Confirm the actual destination content type.
- Try both legacy and modern extensions: `doc` and `docx`, `xls` and `xlsx`, `ppt` and `pptx`.
- Search the document title and `附件` (**attachment**).
- Use the issuing site's attachment filters.
- Try Google or Bing, which document file-type search behavior.

## Problem: A platform requires login or CAPTCHA

- Do not bypass it.
- Use public search-engine results, public share URLs, official APIs where available, or lawful manual access.
- Record that access limitations affected completeness.
- Search quoted titles, usernames, article IDs, and unique sentences across other public sources.

## Problem: Machine translation looks wrong

- Break the sentence into smaller units.
- Check the field's domain context: corporate, legal, procurement, academic, or technical.
- Compare multiple translations.
- Search the Chinese term plus `英文` (**English**) or a trusted bilingual reference.
- Ask a qualified speaker for high-stakes interpretation.
- Preserve the original wording and flag uncertainty.

## Problem: Many articles repeat the same claim

- Find the earliest timestamp.
- Identify the named original source.
- Search the exact first sentence.
- Compare whether later copies added or removed qualifiers.
- Count independent reporting chains, not URLs.

## Problem: A result disappeared

- Search the exact title, URL, article ID, and unique sentence.
- Add `转载` (**reposted**), `原文` (**original article**), `全文` (**full text**), `截图` (**screenshot**), or `存档` (**archive**).
- Check lawful public archives.
- Record that the current page is unavailable; do not overstate why.

---

# 25. Quick-reference cheat sheet

## 25.1 Core query formula

```text
"[TARGET]" [CHINESE KEYWORD] site:[DOMAIN] filetype:[EXTENSION]
```

Start broad. Add one constraint at a time.

## 25.2 Identity

| Chinese term | English translation |
|---|---|
| `中文名` | Chinese name |
| `英文名` | English name |
| `全称` | full name |
| `简称` | abbreviation / short name |
| `曾用名` | former name |
| `官网` | official website |
| `统一社会信用代码` | Unified Social Credit Identifier |
| `ICP备案` | ICP filing |
| `主办单位` | operating / sponsoring entity |

## 25.3 Company and ownership

| Chinese term | English translation |
|---|---|
| `法定代表人` | legal representative |
| `股东` | shareholder |
| `控股股东` | controlling shareholder |
| `实际控制人` | actual controller |
| `股权结构` | equity structure |
| `注册资本` | registered capital |
| `实缴资本` | paid-in capital |
| `经营范围` | business scope |
| `对外投资` | external investments |
| `子公司` | subsidiary |
| `变更记录` | change history |

## 25.4 People

| Chinese term | English translation |
|---|---|
| `简历` | résumé / biography |
| `个人简介` | personal profile |
| `履历` | career history |
| `现任` | currently serves as |
| `曾任` | formerly served as |
| `任免` | appointments and removals |
| `毕业于` | graduated from |
| `导师` | academic adviser |
| `论文` | paper / thesis |
| `专访` | feature interview |

## 25.5 Government and regulation

| Chinese term | English translation |
|---|---|
| `公示` | public notice |
| `公告` | announcement |
| `批复` | official approval / reply |
| `备案` | filing / recordal |
| `行政许可` | administrative license |
| `行政处罚` | administrative penalty |
| `处罚决定书` | penalty decision |
| `抽查结果` | spot-check result |
| `责令改正` | ordered to correct |
| `立案调查` | investigation formally opened |
| `整改` | rectification / remediation |

## 25.6 Procurement

| Chinese term | English translation |
|---|---|
| `采购意向` | procurement intention |
| `招标公告` | tender notice |
| `中标候选人公示` | winning-bid candidate notice |
| `中标公告` | award notice |
| `成交公告` | award / transaction notice |
| `采购合同` | procurement contract |
| `更正公告` | correction notice |
| `项目编号` | project number |
| `中标金额` | winning-bid amount |
| `单一来源采购` | single-source procurement |

## 25.7 Legal and enforcement

| Chinese term | English translation |
|---|---|
| `案号` | case number |
| `判决书` | judgment |
| `裁定书` | ruling / order |
| `开庭公告` | hearing notice |
| `被执行人` | subject to enforcement |
| `失信被执行人` | dishonest judgment debtor / judgment defaulter designation |
| `限制高消费` | restriction on high consumption |
| `破产` | bankruptcy |
| `清算` | liquidation |
| `仲裁` | arbitration |

## 25.8 Documents

| Chinese term | English translation |
|---|---|
| `年度报告` | annual report |
| `白皮书` | white paper |
| `社会责任报告` | corporate social responsibility report |
| `审计报告` | audit report |
| `名单` | list / roster |
| `附件` | attachment |
| `会议纪要` | meeting minutes |
| `验收报告` | acceptance report |
| `全文` | full text |
| `下载` | download |

## 25.9 Incidents and response

| Chinese term | English translation |
|---|---|
| `声明` | statement |
| `回应` | response |
| `辟谣` | rumor rebuttal / denial |
| `通报` | official bulletin |
| `事故` | accident / incident |
| `召回` | recall |
| `停产` | production suspension |
| `整改` | rectification / remediation |
| `欠薪` | wage arrears |
| `裁员` | layoffs |

## 25.10 Technology and apps

| Chinese term | English translation |
|---|---|
| `ICP备案` | ICP filing |
| `APP备案` | app filing |
| `隐私政策` | privacy policy |
| `用户协议` | user agreement / terms of service |
| `小程序` | mini program |
| `微信公众号` | WeChat Official Account |
| `软件著作权` | software copyright registration |
| `招聘` | recruiting / jobs |
| `运维` | operations and maintenance |
| `技术栈` | technology stack |

## 25.11 Repost and archive

| Chinese term | English translation |
|---|---|
| `原文` | original article / text |
| `全文` | full text |
| `转载` | reposted / republished |
| `转载自` | republished from |
| `截图` | screenshot |
| `存档` | archive |
| `备份` | backup |
| `来源` | source |
| `已删除` | deleted |
| `失效链接` | dead / invalid link |

---

# 26. Classroom exercises

These exercises use fictional or instructor-approved targets. Students should document every query in Chinese and English and cite primary sources.

## Exercise 1: Domain to legal entity

**Task:** Given a public Chinese domain, identify the operating entity and verify its registered company record.

**Expected workflow:**

1. Search the domain plus `ICP备案` (**ICP filing**).
2. Query the official MIIT filing system.
3. Record the `主办单位` (**operating/sponsoring entity**) and `ICP备案号` (**ICP filing number**).
4. Search the operating entity in the National Enterprise Credit Information Publicity System.
5. Compare the domain footer, privacy policy, company identifier, and registered status.
6. State what the filing proves and what it does not prove.

## Exercise 2: Procurement relationship

**Task:** Determine whether a vendor won a public-sector project and whether a contract or acceptance record can be found.

**Expected workflow:**

1. Search the vendor plus `中标公告` (**award notice**).
2. Search `site:ccgp.gov.cn` and `site:ggzy.gov.cn`.
3. Extract the `项目编号` (**project number**).
4. Search the project number plus `更正公告` (**correction notice**), `采购合同` (**procurement contract**), and `验收公告` (**acceptance announcement**).
5. Distinguish candidate, final award, contract, and acceptance stages.

## Exercise 3: Executive timeline

**Task:** Build a verified professional timeline for a public executive or official.

**Expected workflow:**

1. Search the name plus `简历` (**résumé/biography**), `现任` (**currently serves as**), and `曾任` (**formerly served as**).
2. Restrict to `gov.cn`, `edu.cn`, listed-company disclosures, and official organization sites.
3. Disambiguate with institution, city, title, and date.
4. Preserve the original Chinese wording for each appointment.
5. Identify gaps and conflicting dates without guessing.

## Exercise 4: Incident verification

**Task:** Verify a reported industrial incident involving a company.

**Expected workflow:**

1. Search company plus `事故` (**accident/incident**), location, and date.
2. Search `通报` (**official bulletin**), `调查报告` (**investigation report**), `回应` (**response**), and `整改` (**remediation**).
3. Identify the earliest source and independent official confirmation.
4. Separate allegations, confirmed facts, response, penalty, and later status.
5. Check whether the named company is the operator, owner, contractor, or unrelated same-name entity.

## Exercise 5: Deleted article recovery

**Task:** Trace a public article that is no longer available at its original URL.

**Expected workflow:**

1. Search the exact title.
2. Search a unique sentence.
3. Add `转载` (**reposted**), `原文` (**original article**), `全文` (**full text**), and `截图` (**screenshot**).
4. Search the URL and article ID.
5. Check lawful public archives.
6. Compare reposts for omissions or changes.
7. State what can and cannot be authenticated.

## Exercise 6: Company-control analysis

**Task:** Determine the difference between a company's legal representative, shareholders, controlling shareholder, and actual controller.

**Expected workflow:**

1. Search and record `法定代表人` (**legal representative**).
2. Search `股东` (**shareholders**) and `持股比例` (**shareholding percentage**).
3. Search listed-company or official disclosures for `控股股东` (**controlling shareholder**) and `实际控制人` (**actual controller**).
4. Draw a dated ownership chart.
5. Explain why the four concepts should not be treated as interchangeable.

---

# 27. Briefing-slide summary

## Slide: China Web OSINT — The Core Method

- Search the target's **Chinese name**, not only its English name.
- Build an alias matrix: full name, short name, former names, brands, domains, and identifiers.
- Use the formula: **target + Chinese pivot term + source domain + file type**.
- Search multiple engines and platform-native search; no index is complete.
- Move from search results to official registries, procurement portals, court systems, and disclosures.
- Preserve the original Chinese text and provide an English translation.
- Treat search results as leads; verify before making claims.

## Slide: High-Value Chinese Pivots

- `招聘` — **recruiting/jobs**
- `股东` — **shareholder**
- `实际控制人` — **actual controller**
- `中标公告` — **award notice**
- `行政处罚` — **administrative penalty**
- `判决书` — **judgment**
- `简历` — **résumé/biography**
- `环评` — **environmental impact assessment**
- `ICP备案` — **ICP filing**
- `软件著作权` — **software copyright registration**
- `转载` — **reposted/republished**
- `截图` — **screenshot**

## Slide: The Five Biggest Mistakes

1. Searching only in English.
2. Confusing a brand, subsidiary, and registered legal entity.
3. Treating a search-engine result count as complete.
4. Treating a candidate, allegation, or proposed action as final.
5. Citing a secondary post when a primary record exists.

## Slide: Baidu Caveat

- Baidu is a useful window into mainland Chinese web content, but it is not identical to Google.
- Similar operators can behave differently.
- Sensitive searches may produce warnings or curated results.
- Adding `知乎` (**Zhihu**) can find discussion or reposts; it is not an archive command.
- Compare engines, search primary portals directly, and document uncertainty.

---

# 28. Sources and further reading

The operational examples in this guide are designed to be tested against live search behavior. Search engines and portals change, so review the official pages before teaching a fixed operator list.

## Search-engine documentation

- **百度高级搜索 (Baidu Advanced Search):** official interface for exact phrases, excluded words, time, language, file format, title/URL position, and site restriction.[^baidu-advanced]
- **百度网页搜索帮助 (Baidu Web Search Help):** official overview of Baidu web search.[^baidu-help]
- **Google Search Help — Refine searches:** official guidance on quotes and `site:`.[^google-refine]
- **Google Search Central — `site:` operator:** official limitations and behavior.[^google-site]
- **Google Search Central — indexable file types:** official `filetype:` guidance and supported formats.[^google-filetypes]
- **Microsoft Support — Bing advanced search options:** official Boolean and symbol behavior.[^bing-options]
- **Microsoft Support — Bing advanced search keywords:** official `site:`, `filetype:`, `ext:`, `intitle:`, and related keyword behavior.[^bing-keywords]

## Search filtering and result-set research

- Tao Zhu, Christopher Bronk, and Dan S. Wallach, **“An Analysis of Chinese Search Engine Filtering.”** This historical study found that filtering policies varied by term, engine, and time.[^zhu-filtering]
- Min Jiang, **“The Business and Politics of Search Engines: A Comparative Study of Baidu and Google's Search Results of Internet Events in China.”** This historical research found low overlap and ranking differences among result sets.[^jiang-search]

## Official public-source systems

- **国家企业信用信息公示系统 (National Enterprise Credit Information Publicity System):** official company and market-entity records.[^gsxt-help]
- **中国政府采购网 (China Government Procurement Network):** official national government-procurement publication site.[^ccgp-official]
- **全国公共资源交易平台 (National Public Resources Trading Platform):** official public-resource transaction platform.[^ggzy-official]
- **中国执行信息公开网 (China Enforcement Information Disclosure Network):** official enforcement-publicity system.[^zxgk-official]
- **国家法律法规数据库 (National Laws and Regulations Database):** official laws and regulations database.[^law-database]
- **工业和信息化部ICP/IP地址/域名信息备案管理系统 (MIIT ICP/IP Address/Domain Filing System):** official internet filing system.[^miit-icp]
- **国家知识产权局专利检索及分析系统 (CNIPA Patent Search and Analysis System):** official public patent search and analysis service.[^cnipa-patent]
- **中国商标网 (China Trademark Office website):** official trademark services and search.[^cnipa-trademark]
- **全国标准信息公共服务平台 (National Standards Information Public Service Platform):** official standards information.[^standards-platform]

---

## Footnotes

[^baidu-advanced]: Baidu, **百度高级搜索 (Baidu Advanced Search)**, accessed 21 June 2026, https://www.baidu.com/gaoji/advanced.html.

[^baidu-help]: Baidu, **百度搜索帮助中心—网页搜索帮助 (Baidu Search Help Center — Web Search Help)**, accessed 21 June 2026, https://www.baidu.com/search/page_help.htm.

[^google-refine]: Google, **Refine Google searches**, accessed 21 June 2026, https://support.google.com/websearch/answer/2466433.

[^google-site]: Google Search Central, **How to use the `site:` search operator**, accessed 21 June 2026, https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site.

[^google-filetypes]: Google Search Central, **File types indexable by Google**, updated 3 February 2026, https://developers.google.com/search/docs/crawling-indexing/indexable-file-types.

[^bing-options]: Microsoft Support, **Advanced search options**, accessed 21 June 2026, https://support.microsoft.com/en-us/bing/advanced-search-options.

[^bing-keywords]: Microsoft Support, **Advanced search keywords**, accessed 21 June 2026, https://support.microsoft.com/en-us/bing/advanced-search-keywords.

[^zhu-filtering]: Tao Zhu, Christopher Bronk, and Dan S. Wallach, **An Analysis of Chinese Search Engine Filtering**, arXiv:1107.3794, 2011, https://arxiv.org/abs/1107.3794. The study is historical and should not be treated as a current keyword list.

[^jiang-search]: Min Jiang, **The Business and Politics of Search Engines: A Comparative Study of Baidu and Google's Search Results of Internet Events in China**, *New Media & Society* 16, no. 2 (2014): 212–233, https://doi.org/10.1177/1461444813481196. The data were collected historically; the enduring lesson is that indexes and rankings can differ substantially.

[^gsxt-help]: 国家企业信用信息公示系统, **使用帮助 (National Enterprise Credit Information Publicity System — Help)**, accessed 21 June 2026, https://bt.gsxt.gov.cn/affiche-query-info-help-660000.html.

[^ccgp-official]: 中国政府采购网, **China Government Procurement Network**, accessed 21 June 2026, https://www.ccgp.gov.cn/.

[^ggzy-official]: 全国公共资源交易平台, **平台介绍 (National Public Resources Trading Platform — Platform Introduction)**, accessed 21 June 2026, https://www.ggzy.gov.cn/platform/platform.html.

[^zxgk-official]: Supreme People's Court of the People's Republic of China, **中国执行信息公开网改版升级 (China Enforcement Information Disclosure Network Upgraded)**, 8 June 2018, https://www.court.gov.cn/shenpan/xiangqing/101002.html.

[^law-database]: 全国人大常委会办公厅, **国家法律法规数据库 (National Laws and Regulations Database)**, accessed 21 June 2026, https://flk.npc.gov.cn/.

[^miit-icp]: Ministry of Industry and Information Technology, **关于调整“工业和信息化部ICP/IP地址/域名信息备案管理系统”域名的公告 (Notice on Changing the Domain of the MIIT ICP/IP Address/Domain Information Filing System)**, 19 April 2019, https://www.miit.gov.cn/jgsj/xgj/hlwgl/art/2020/art_b9c05f8e533744f18a8c447f26fcf86c.html.

[^cnipa-patent]: China National Intellectual Property Administration, **智能化专利检索及分析系统正式运行 (Intelligent Patent Search and Analysis System Officially Launched)**, 26 July 2022, https://www.cnipa.gov.cn/art/2022/7/26/art_53_176815.html.

[^cnipa-trademark]: 国家知识产权局商标局, **中国商标网 (China Trademark Office Website)**, accessed 21 June 2026, https://sbj.cnipa.gov.cn/.

[^standards-platform]: 全国标准信息公共服务平台, **国家标准 (National Standards)**, accessed 21 June 2026, https://std.samr.gov.cn/gb/.

---

## Maintenance note

This guide should be reviewed periodically. Before publishing a revised version:

1. Test the Baidu examples against the live interface.
2. Confirm that official portal domains still resolve to the issuing authority.
3. Check whether login, CAPTCHA, geographic, or account requirements have changed.
4. Update the “Last reviewed” date.
5. Record material changes in a changelog.

---

## Reuse note

This guide is published by Argelius Labs for educational use under the Creative Commons Attribution 4.0 International (CC BY 4.0) license (see [`LICENSE`](LICENSE)). You are free to share and adapt it, including commercially, as long as you give appropriate credit. Before redistributing a modified version, update the author credit, contact information, contribution policy, and the "Last reviewed" date so readers can tell your edition apart from the original.

If you are reading this as a standalone file, note that it is intended to live in a repository alongside a short [`README.md`](README.md) front door and a [`LICENSE`](LICENSE) file.
