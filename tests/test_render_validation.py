"""Regression coverage for unsupported evidence claims and stale generated docs."""

from copy import deepcopy
from datetime import date, timedelta
import json
from pathlib import Path
import tempfile
import unittest

from scripts.render_validation import ROOT, ValidationError, generate, render, validate


class ValidationRegisterTests(unittest.TestCase):
    def setUp(self):
        self.data = {
            "schema_version": 1,
            "review_date": "2026-11-24",
            "records": [{
                "id": "example-site",
                "kind": "operator",
                "service": "Example engine",
                "label": "Site restriction",
                "status": "documented",
                "query_template": 'site:example.org "[organization]"',
                "test_query": None,
                "documentation_checked_on": "2026-11-24",
                "live_tested_on": None,
                "access_context": None,
                "expected_behavior": "Request results from the specified site.",
                "observed_behavior": None,
                "source_urls": ["https://example.org/documentation"],
                "notes": "Synthetic fixture; this is not a claim about a real engine.",
            }],
        }

    def test_observed_requires_date_context_result_and_executed_query(self):
        complete = deepcopy(self.data)
        record = complete["records"][0]
        record.update(status="observed", live_tested_on="2026-11-24",
                      access_context="Manual browser; example test context",
                      observed_behavior="Example result recorded for this test fixture only",
                      test_query='"example public organization"')
        validate(complete)
        for field in ("live_tested_on", "access_context", "observed_behavior", "test_query"):
            with self.subTest(field=field):
                changed = deepcopy(complete)
                changed["records"][0][field] = None
                with self.assertRaisesRegex(ValidationError, "observed.*requires"):
                    validate(changed)

    def test_unexecuted_status_cannot_have_live_fields(self):
        for field, value in (("live_tested_on", "2026-11-24"), ("test_query", "example"),
                             ("access_context", "browser"), ("observed_behavior", "result")):
            with self.subTest(field=field):
                changed = deepcopy(self.data)
                changed["records"][0][field] = value
                with self.assertRaisesRegex(ValidationError, "live observation fields"):
                    validate(changed)

    def test_invalid_dates_and_dates_after_review_are_rejected(self):
        after_review = (date.fromisoformat(self.data["review_date"]) + timedelta(days=1)).isoformat()
        for value in ("2026-2-01", "2026-02-30", after_review, 20261124):
            with self.subTest(value=value):
                changed = deepcopy(self.data)
                changed["records"][0]["documentation_checked_on"] = value
                with self.assertRaises(ValidationError):
                    validate(changed)

    def test_duplicate_ids_and_missing_fields_are_rejected(self):
        self.data["records"].append(deepcopy(self.data["records"][0]))
        with self.assertRaisesRegex(ValidationError, "duplicate id"):
            validate(self.data)
        self.data["records"].pop()
        del self.data["records"][0]["observed_behavior"]
        with self.assertRaisesRegex(ValidationError, "fields must match"):
            validate(self.data)

    def test_documented_claim_requires_a_source_and_date(self):
        for field, value in (("source_urls", []), ("documentation_checked_on", None)):
            with self.subTest(field=field):
                changed = deepcopy(self.data)
                changed["records"][0][field] = value
                with self.assertRaisesRegex(ValidationError, "documented requires"):
                    validate(changed)

    def test_source_urls_reject_credentials_including_empty_username(self):
        for url in ("https://user:secret@example.org/", "https://user@example.org/",
                    "https://:secret@example.org/", "https://@example.org/"):
            with self.subTest(url=url):
                changed = deepcopy(self.data)
                changed["records"][0]["source_urls"] = [url]
                with self.assertRaisesRegex(ValidationError, "public HTTP"):
                    validate(changed)

    def test_render_updates_live_observation_count(self):
        self.assertIn("Records with a live observation: **0 of 1**", render(self.data))
        self.data["records"][0].update(
            status="observed", live_tested_on="2026-11-24",
            access_context="Synthetic browser observation",
            observed_behavior="Synthetic result for unit testing only",
            test_query="site:example.org public organization",
        )
        self.assertIn("Records with a live observation: **1 of 1**", render(self.data))

    def test_generated_output_is_exact_and_check_never_repairs_it(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "data" / "validation.json").write_text(json.dumps(self.data), encoding="utf-8")
            with self.assertRaisesRegex(ValidationError, "missing or stale"):
                generate(root, check=True)
            self.assertFalse((root / "docs").exists())
            generate(root)
            generate(root, check=True)
            target = root / "docs" / "validation.md"
            expected = render(self.data).encode("utf-8")
            self.assertEqual(expected, target.read_bytes())
            stale = expected + b"\nmanual change\n"
            target.write_bytes(stale)
            with self.assertRaisesRegex(ValidationError, "missing or stale"):
                generate(root, check=True)
            self.assertEqual(stale, target.read_bytes())

    def test_changed_source_requires_regeneration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            source = root / "data" / "validation.json"
            source.write_text(json.dumps(self.data), encoding="utf-8")
            generate(root)
            self.data["records"][0]["notes"] += " New evidence qualification."
            source.write_text(json.dumps(self.data), encoding="utf-8")
            with self.assertRaisesRegex(ValidationError, "missing or stale"):
                generate(root, check=True)

    def test_duplicate_json_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "data" / "validation.json").write_text('{"schema_version": 1, "schema_version": 1}', encoding="utf-8")
            with self.assertRaisesRegex(ValidationError, "duplicate key"):
                generate(root)


class RepositoryRegisterIntegrationTest(unittest.TestCase):
    def test_actual_register_is_valid_and_generated_document_is_current(self):
        data = json.loads((ROOT / "data" / "validation.json").read_text(encoding="utf-8"))
        validate(data)
        self.assertEqual(render(data).encode("utf-8"), (ROOT / "docs" / "validation.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
