"""Validate the small evidence register and render its Markdown page offline.

No search query or external request is executed by this command. Documentation
review and observed live behavior are deliberately separate evidence states.
"""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    "id", "kind", "service", "label", "status", "query_template", "test_query",
    "documentation_checked_on", "live_tested_on", "access_context",
    "expected_behavior", "observed_behavior", "source_urls", "notes",
}


class ValidationError(ValueError):
    """The register cannot support the evidence state it claims."""


def check_date(value: object, label: str, *, nullable: bool = False) -> date | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValidationError(f"{label}: expected an ISO YYYY-MM-DD date")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{label}: invalid calendar date") from exc


def check_text(value: object, label: str, *, nullable: bool = False) -> None:
    if value is None and nullable:
        return
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label}: expected nonempty text")
    if any(ord(char) < 32 for char in value):
        raise ValidationError(f"{label}: text must be on one line without control characters")


def validate(data: object) -> dict:
    if not isinstance(data, dict) or set(data) != {"schema_version", "review_date", "records"}:
        raise ValidationError("register: expected schema_version, review_date, and records")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValidationError("schema_version: only integer version 1 is supported")
    reviewed = check_date(data["review_date"], "review_date")
    if not isinstance(data["records"], list) or not data["records"]:
        raise ValidationError("records: expected a nonempty list")
    ids: set[str] = set()
    for number, record in enumerate(data["records"], 1):
        label = f"record {number}"
        if not isinstance(record, dict) or set(record) != FIELDS:
            raise ValidationError(f"{label}: fields must match schema version 1")
        for field in ("id", "kind", "service", "label", "status", "expected_behavior", "notes"):
            check_text(record[field], f"{label}.{field}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record["id"]):
            raise ValidationError(f"{label}.id: use lowercase words separated by hyphens")
        if record["id"] in ids:
            raise ValidationError(f"{label}: duplicate id {record['id']}")
        ids.add(record["id"])
        if record["kind"] not in {"operator", "portal"}:
            raise ValidationError(f"{label}.kind: expected operator or portal")
        if record["status"] not in {"documented", "observed", "untested"}:
            raise ValidationError(f"{label}.status: expected documented, observed, or untested")
        for field in ("query_template", "test_query", "access_context", "observed_behavior"):
            check_text(record[field], f"{label}.{field}", nullable=True)
        for field in ("documentation_checked_on", "live_tested_on"):
            checked = check_date(record[field], f"{label}.{field}", nullable=True)
            if checked is not None and checked > reviewed:
                raise ValidationError(f"{label}.{field}: cannot be after review_date")
        if record["kind"] == "operator" and record["query_template"] is None:
            raise ValidationError(f"{label}: an operator needs a query_template")
        if not isinstance(record["source_urls"], list):
            raise ValidationError(f"{label}.source_urls: expected a list")
        for url in record["source_urls"]:
            check_text(url, f"{label}.source_urls entry")
            try:
                parsed = urlsplit(url)
                valid = (parsed.scheme in {"https", "http"} and parsed.hostname
                         and parsed.username is None and parsed.password is None)
            except ValueError:
                valid = False
            if not valid or re.search(r"[\s<>]", url):
                raise ValidationError(f"{label}.source_urls: expected public HTTP(S) URLs")
        if record["status"] == "documented":
            if record["documentation_checked_on"] is None or not record["source_urls"]:
                raise ValidationError(f"{label}: documented requires a review date and source URL")
        if record["status"] == "observed":
            for field in ("live_tested_on", "access_context", "observed_behavior"):
                if record[field] is None:
                    raise ValidationError(f"{label}: observed requires {field}")
            if record["kind"] == "operator" and record["test_query"] is None:
                raise ValidationError(f"{label}: an observed operator requires the executed test_query")
        elif any(record[field] is not None for field in
                 ("test_query", "live_tested_on", "access_context", "observed_behavior")):
            raise ValidationError(f"{label}: live observation fields require observed status")
    return data


def prose(value: str) -> str:
    """Keep register strings literal in Markdown, including query placeholders."""
    return re.sub(r"([\\`*_{}\[\]<>|])", r"\\\1", value)


def render(data: dict) -> str:
    data = validate(data)
    observed_count = sum(record["status"] == "observed" for record in data["records"])
    lines = [
        "<!-- Generated by scripts/render_validation.py; edit data/validation.json instead. -->",
        "# Documentation and validation register", "",
        f"Register reviewed: **{data['review_date']}**. This date is an editorial review, not a claim that live searches succeeded.", "",
        "This is a small, selective register. It does not certify the full guide: examples outside this register remain unverified unless separate evidence is recorded.", "",
        f"Records with a live observation: **{observed_count} of {len(data['records'])}**. See each record for its evidence state and scope.", "",
        "## Evidence states", "",
        "- **Documented:** the cited official documentation was reviewed on the recorded date. This is not a live behavior test; legacy documentation may differ from today's interface.",
        "- **Observed:** a specific live test records its date, client/network context, actual query where applicable, and observed result. One observation does not establish universal support or complete coverage.",
        "- **Untested:** no supported live observation or documented support is claimed. A historical third-party report is not a test by this repository.", "",
        "Query templates are instructions for substitution, not executed test queries. Chinese company-name placeholders mean the full legal company name; 年度报告 means annual report, and 中标公告 means award notice.", "",
        "## Coverage", "",
        "| ID | Service | Check | Status | Documentation reviewed | Live tested |",
        "|---|---|---|---|---|---|",
    ]
    for record in data["records"]:
        lines.append("| " + " | ".join(prose(value) for value in (
            record["id"], record["service"], record["label"], record["status"],
            record["documentation_checked_on"] or "Not recorded",
            record["live_tested_on"] or "Not performed",
        )) + " |")
    lines.extend(["", "## Record details", ""])
    for record in data["records"]:
        lines.extend([f"### {record['id']}", "",
                      f"**{prose(record['service'])}: {prose(record['label'])}** — {record['status']}", ""])
        if record["query_template"] is not None:
            lines.extend([f"Template: {prose(record['query_template'])}", ""])
        lines.extend([f"Expected behavior: {prose(record['expected_behavior'])}", ""])
        if record["status"] == "observed":
            lines.extend([f"Live test date: {record['live_tested_on']}", "",
                          f"Access context: {prose(record['access_context'])}", ""])
            if record["test_query"] is not None:
                lines.extend([f"Executed test query: {prose(record['test_query'])}", ""])
            lines.extend([f"Observed behavior: {prose(record['observed_behavior'])}", ""])
        else:
            lines.extend(["Observed behavior: **Not tested live.**", ""])
        lines.extend([f"Notes: {prose(record['notes'])}", ""])
        if record["source_urls"]:
            lines.append("Sources:")
            lines.append("")
            for index, url in enumerate(record["source_urls"], 1):
                lines.append(f"- [Source {index}](<{url}>)")
            lines.append("")
    lines.extend([
        "## Updating the register", "",
        "1. Review the relevant official documentation. Record its URL and the date actually checked; distinguish legacy documentation from current observed behavior.",
        "2. If a manual live check is appropriate, use a harmless public example. Record the exact query, date, client/network context, expected behavior, and actual result. Record failures and uncertainty without inventing their cause.",
        "3. For external links, use a manual, report-only review: record reachable content, redirects, login/CAPTCHA/challenge pages, HTTP errors, and transport failures separately. An error is not proof of a dead link, an outage, geographic blocking, or a missing record. Do not solve or bypass access controls for this review.",
        "4. Edit the source register, then regenerate this page with `python scripts/render_validation.py`. Run `python scripts/render_validation.py --check` before submitting.", "",
        "These commands use only the local JSON file. They do not query search engines, request external links, schedule checks, or change an observation date automatically. Automated CI checks schema consistency and generated-document freshness only.", "",
        "[Source register](../data/validation.json) · [Guide](../guide.md)", "",
    ])
    return "\n".join(lines)


def no_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"JSON contains duplicate key: {key}")
        result[key] = value
    return result


def generate(root: Path, *, check: bool = False) -> None:
    source = root / "data" / "validation.json"
    target = root / "docs" / "validation.md"
    data = json.loads(source.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys)
    expected = render(data).encode("utf-8")
    if check:
        if not target.is_file() or target.read_bytes() != expected:
            raise ValidationError("docs/validation.md is missing or stale; run python scripts/render_validation.py")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(expected)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing; fail if generated Markdown differs")
    args = parser.parse_args(argv)
    try:
        generate(ROOT, check=args.check)
    except (OSError, ValueError) as exc:
        print(f"Validation register: {exc}", file=sys.stderr)
        return 1
    print("Validation register and generated page are current." if args.check else "Generated docs/validation.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
