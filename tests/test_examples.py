"""Integrity checks for the offline teaching bundle, without live searches."""

import csv
from datetime import date, datetime
import hashlib
from pathlib import Path, PureWindowsPath
import unittest


ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "examples" / "procurement"


def read_log(path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames, list(reader)


class ProcurementExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fields, cls.rows = read_log(BUNDLE / "evidence-log.csv")
        cls.template_fields, cls.template_rows = read_log(
            ROOT / "templates" / "evidence-log.csv"
        )

    def local_source(self, value):
        """Reject external or escaping references on Windows and POSIX alike."""
        self.assertTrue(value, "A fixture reference must not be empty")
        self.assertNotIn("://", value, "Fixtures must use local paths")
        self.assertFalse(Path(value).is_absolute())
        self.assertFalse(PureWindowsPath(value).is_absolute())
        path = (BUNDLE / value).resolve(strict=True)
        self.assertTrue(path.is_relative_to(BUNDLE.resolve()), value)
        self.assertTrue(path.is_file(), value)
        return path

    def test_csv_matches_blank_template(self):
        self.assertTrue(self.fields)
        self.assertEqual(self.fields, self.template_fields)
        self.assertEqual(len(self.fields), len(set(self.fields)))
        self.assertNotIn("", self.fields)
        self.assertEqual(self.template_rows, [], "Template must contain only headers")
        self.assertTrue(self.rows, "The worked example must contain observations")
        record_ids = []
        for row in self.rows:
            with self.subTest(record_id=row.get("record_id")):
                self.assertNotIn(None, row, "CSV row has extra cells")
                self.assertTrue(all(value is not None for value in row.values()))
                self.assertTrue(row["record_id"])
                record_ids.append(row["record_id"])
        self.assertEqual(len(record_ids), len(set(record_ids)))

    def test_source_and_archive_paths_stay_inside_bundle(self):
        for row in self.rows:
            for field in ("source_file", "archive_reference"):
                with self.subTest(record_id=row["record_id"], field=field):
                    self.local_source(row[field])

    def test_source_hashes_match_bundled_bytes(self):
        for row in self.rows:
            with self.subTest(record_id=row["record_id"]):
                self.assertRegex(row["source_sha256"], r"^[0-9a-f]{64}$")
                path = self.local_source(row["source_file"])
                self.assertEqual(
                    hashlib.sha256(path.read_bytes()).hexdigest(),
                    row["source_sha256"],
                    "Update the evidence log after an intentional fixture edit",
                )

    def test_observations_do_not_claim_real_collection(self):
        for row in self.rows:
            with self.subTest(record_id=row["record_id"]):
                self.assertEqual(row["source_kind"], "synthetic")
                self.assertEqual(row["timestamp_basis"], "synthetic_scenario")
                self.assertEqual(row["query_status"], "illustrative_not_run")
                self.assertEqual(row["access_method"], "local_file")
                self.assertEqual(row["source_url"], "")
                self.assertEqual(row["http_status"], "")

    def test_log_preserves_original_passages_and_translations(self):
        for row in self.rows:
            source = self.local_source(row["source_file"]).read_text(encoding="utf-8")
            for field in ("original_passage", "english_translation"):
                with self.subTest(record_id=row["record_id"], field=field):
                    self.assertTrue(row[field].strip())
                    self.assertIn(row[field], source)

    def test_dates_have_timezones_and_consistent_chronology(self):
        observations = []
        for row in self.rows:
            with self.subTest(record_id=row["record_id"]):
                observed = datetime.fromisoformat(row["observed_at"])
                self.assertIsNotNone(observed.utcoffset(), "Observation needs a time zone")
                published = date.fromisoformat(row["publication_date"])
                self.assertLessEqual(published, observed.date())
                source = self.local_source(row["source_file"]).read_text(encoding="utf-8")
                self.assertIn(row["publication_date"], source)
                if row["effective_date"]:
                    effective = date.fromisoformat(row["effective_date"])
                    self.assertLessEqual(effective, observed.date())
                    self.assertIn(row["effective_date"], source)
                observations.append(observed)
        self.assertEqual(observations, sorted(observations))

    def test_each_source_discloses_its_synthetic_origin(self):
        for row in self.rows:
            with self.subTest(record_id=row["record_id"]):
                source = self.local_source(row["source_file"]).read_text(encoding="utf-8")
                self.assertIn("SYNTHETIC CLASSROOM RECORD", source)


if __name__ == "__main__":
    unittest.main()
