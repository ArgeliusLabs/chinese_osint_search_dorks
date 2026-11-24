# Reusable evidence log

Download [evidence-log.csv](evidence-log.csv) and add one row per source observation. The file contains column headers only. Import it as UTF-8 and set identifiers, dates, query text, and original passages to text columns so spreadsheet software does not alter them. Inspect untrusted text before opening it in a spreadsheet, since leading formula characters can be interpreted as formulas.

See [the completed synthetic example](../examples/procurement/evidence-log.csv) and its [walkthrough](../examples/procurement/README.md). Its scenario timestamps and unexecuted query examples must not be copied into a real investigation as actual observations.

## Field definitions

| Columns | What to record |
|---|---|
| `record_id` | Stable identifier for this observation; do not reuse it for a different source. |
| `source_kind` | `public_record`, `other_public_source`, or `synthetic`; describe other kinds explicitly. |
| `research_question` | The precise claim or relationship this source could support. |
| `query`, `query_english` | Exact query, including characters and operators, and its English gloss. Leave blank if no query was used. |
| `query_status` | `executed`, `planned`, `illustrative_not_run`, or `not_applicable`. A proposed query is not evidence that a search occurred. |
| `engine_or_portal` | Search engine, official portal, or local bundle name. |
| `access_method` | Such as `browser`, `http_client`, `api`, or `local_file`. |
| `access_result` | One of the observation categories below. |
| `http_status` | Actual HTTP response code if observed; otherwise blank. Do not infer a code from a page's appearance. |
| `access_context` | Network location at a non-sensitive level, language, account state, and relevant interface/client version. Do not include credentials, cookie values, or session tokens. |
| `access_notes` | Visible message or technical evidence and any uncertainty. Separate observed facts from hypotheses about the cause. |
| `observed_at` | Actual observation timestamp with time zone, preferably ISO 8601, e.g. `2026-11-24T10:15:00-07:00`. |
| `timestamp_basis` | `actual_observation` for real collection; `synthetic_scenario` for invented teaching timelines. |
| `source_url` | Exact source URL, without credentials or access tokens; blank for a local-only source. |
| `source_file`, `source_sha256` | Optional saved filename/path and SHA-256 of those exact bytes. State how relative paths resolve. Recalculate after any file modification. |
| `publisher` | Issuing authority or publisher, as shown on the source. |
| `publication_date`, `effective_date` | Source publication date and separate effective date, if given. Leave unknown dates blank; do not assume they equal the access date. |
| `target_name`, `target_identifiers` | Original legal/entity name and verified identifiers, with identifier type and scope. Preserve leading zeros. |
| `document_status` | Status in the source: candidate, award, correction, draft, effective, repealed, etc.; preserve the original Chinese term. |
| `original_passage`, `english_translation` | Minimum necessary original text and a faithful translation with qualifiers preserved. |
| `archive_reference` | Optional archive URL or local preserved-copy path; use `observed_at` for this observation's capture time or explain a different capture time in `access_notes`. |
| `confidence`, `confidence_basis` | Documented confidence category and its basis. Distinguish confidence in the statement from entity identity or source completeness. |
| `contradictions` | Conflicting observations and links/record IDs for corrections; retain the earlier entry. |
| `next_step` | The specific missing evidence or follow-up needed. |

## Access-result categories

| Value | Meaning |
|---|---|
| `accessible_record` | The record was accessible and reviewed. |
| `accessible_no_match` | The interface worked but the recorded query returned no matching record within the inspected scope. This is not proof of absence. |
| `login_required` | Authentication was explicitly required. |
| `captcha` | A CAPTCHA was observed. |
| `javascript_challenge` | A JavaScript/browser challenge was observed; record the supporting message/header/body evidence. |
| `rate_limited` | Rate limiting was indicated; record the response/message. |
| `unavailable` | The source could not be accessed; record the observed failure. Do not infer a global outage or geographic block. |
| `unknown` | The access result could not be classified from available evidence. |

An HTTP status alone does not prove a JavaScript challenge, geographic restriction, or outage. Stop at access controls; this template is for documenting limitations, not bypassing them. Leave unknown values blank or explain them rather than fabricating a successful search, inferred cause, date, or identifier.
