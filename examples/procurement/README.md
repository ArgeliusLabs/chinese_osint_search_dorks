# Worked exercise: candidate, award, and correction

This is an offline, bilingual exercise for [the procurement chapter](../../guide.md#10-procurement-tenders-and-contract-dorks). It teaches how to preserve identity, document status, and chronology when notices disagree.

**Every source in this bundle is synthetic.** The publisher, suppliers, project, identifiers, dates, and amounts were invented for teaching. Any resemblance to real organizations is coincidental. No live search was run, and these records do not describe a real procurement. `CLASSROOM-*` identifiers are not Unified Social Credit Identifiers or official project numbers. The Chinese entity names are preserved exactly; no English legal names are asserted.

## Materials

Read these in order, retaining earlier versions:

1. [Candidate notice](sources/01-candidates.md), dated October 5, 2026.
2. [Award notice](sources/02-award.md), dated October 8, 2026.
3. [Correction notice](sources/03-correction.md), dated October 9, 2026.

Use the [blank evidence-log CSV](../../templates/evidence-log.csv) and its [field guide](../../templates/README.md). A [completed evidence log](evidence-log.csv) is supplied for comparison.

## Questions

1. Who ranks first in the candidate notice, and who receives the final award?
2. How do the names and identifiers distinguish the two suppliers?
3. What award amount can you report after reading all three records?
4. Do these documents establish why the first-ranked candidate did not win, that a contract was signed, or that goods were delivered and paid for?
5. Which observations should remain in the log when a later notice corrects an earlier one?

## Worked method and answer key

**Step 1 — Define a bounded question.** Ask: “According to this three-record bundle, who was awarded CLASSROOM-PROC-001, and for what reported amount?” This scope does not claim complete coverage of a live portal.

**Step 2 — Resolve identity before translating names.** The first-ranked candidate is `示例晨星教学设备有限公司`, teaching ID `CLASSROOM-SUPPLIER-A`. The second is `示例晨新教学设备有限公司`, teaching ID `CLASSROOM-SUPPLIER-B`. The names differ at `星` versus `新`. Similar spelling or romanization does not establish identity. These fixture IDs are sufficient for this closed exercise only; real research needs independently verified legal identifiers.

**Step 3 — Preserve status.** The October 5 notice says `中标候选人` (award candidate), explicitly not a final award. The October 8 notice says `中标人` (awardee) and identifies **CLASSROOM-SUPPLIER-B**, which was ranked second. Neither ranking nor chronology explains why; the bundle contains no reason.

**Step 4 — Follow the document identifier and correction.** The October 9 notice explicitly corrects `CLASSROOM-NOTICE-002` for the same project. Report **RMB 89,000** as the corrected award amount. Retain the earlier RMB 98,000 entry and link the correction; do not silently overwrite the original passage. The supplier is unchanged by the correction.

**Step 5 — State the supported conclusion.** Within this fictional bundle, 示例晨新教学设备有限公司 (`CLASSROOM-SUPPLIER-B`) received the award for `CLASSROOM-PROC-001`, with a corrected reported amount of RMB 89,000. The bundle does not establish contract signature, delivery, payment, or the reason the first-ranked candidate did not receive the award.

**Step 6 — Record limits and the next action.** If this were real research, the next records to seek would be the adjudication/explanation, signed contract, and acceptance or payment records. Their absence from this limited bundle is not proof that those events never happened. See [the completed log](evidence-log.csv) for three separate source entries, original passages, translations, qualifiers, and contradiction handling.

## Illustrative queries — not executed

These strings show possible pivots only. Do not search for the invented entities or treat them as tested queries.

| Intended pivot | Chinese query | English gloss |
|---|---|---|
| Find the award | `"CLASSROOM-PROC-001" 中标公告` | exact fictional project identifier + award notice |
| Find corrections | `"CLASSROOM-PROC-001" 更正公告` | exact fictional project identifier + correction notice |
| Follow the awardee | `"示例晨新教学设备有限公司" 合同公告` | exact fictional supplier name + contract notice |

For real work, replace the teaching identifiers with a verified public project/entity, record the exact query actually run, and inspect the results rather than assuming a successful match.

## Provenance and log conventions

- Authored for this repository on **November 24, 2026** under the repository's [CC BY 4.0 license](../../LICENSE).
- Source dates and the log's `observed_at` values describe an invented October 2026 classroom timeline. They are **not real publication or collection events**. Each row records `source_kind=synthetic` and `timestamp_basis=synthetic_scenario`.
- Query strings in the log are marked `query_status=illustrative_not_run`. The sources were supplied as local files, not discovered by those queries.
- `source_url` and `http_status` are blank because there was no web request. Relative `source_file` and `archive_reference` paths are resolved from the CSV's directory.
- The SHA-256 values describe the actual bundled file bytes, calculated with Python's standard-library `hashlib` when the exercise was prepared. Recalculate after editing or changing line endings; a matching hash establishes file integrity, not authenticity.
- Confidence is **high only for what the supplied fictional text states**. It is not confidence in a real entity, live search coverage, or unobserved contract performance.
