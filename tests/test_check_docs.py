"""Regression tests for failures that matter to this Markdown repository."""

from pathlib import Path
import tempfile
import unittest

from scripts.check_docs import check_repository


class MarkdownChecks(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name, body):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")

    def check(self):
        return check_repository(self.root)

    def test_missing_file_and_wrong_case_even_on_windows(self):
        self.write("README.md", "[guide](GUIDE.md)\n[license](LICENSE)\n")
        self.write("guide.md", "# Guide\n")
        errors = self.check()
        self.assertEqual(2, len(errors))
        self.assertIn("filename case mismatch", errors[0])
        self.assertIn("missing local path: LICENSE", errors[1])

    def test_cross_file_anchors_and_duplicate_headings(self):
        self.write("README.md", "[one](guide.md#first) [two](guide.md#first-1) [missing](guide.md#first-2)")
        self.write("guide.md", "# First\n# First\n")
        self.assertEqual(["README.md:1: missing heading anchor: guide.md#first-2"], self.check())

    def test_unicode_formatting_and_encoded_paths(self):
        self.write("README.md", "[guide](<docs/My Guide.md#查询-sitegovcn>)\n[encoded](docs/My%20Guide.md#查询-sitegovcn)")
        self.write("docs/My Guide.md", "# 查询 `site:gov.cn`\n")
        self.assertEqual([], self.check())

    def test_parent_paths_and_parent_escape(self):
        self.write("README.md", "# Home\n")
        self.write("docs/guide.md", "[home](../README.md#home)\n[outside](../../outside.md)")
        self.assertEqual(["docs/guide.md:2: local link leaves the repository"], self.check())

    def test_footnote_and_reference_resolution(self):
        self.write("README.md", "A[^one] B[^missing]\n[Guide][G] [missing][bad]\n[^one]: Some text\n[g]: guide.md#guide\n")
        self.write("guide.md", "# Guide\n")
        errors = self.check()
        self.assertEqual(2, len(errors))
        self.assertIn("undefined footnote: missing", errors[0])
        self.assertIn("undefined link reference: bad", errors[1])

    def test_bad_reference_destination_is_checked(self):
        self.write("README.md", "[guide][g]\n[g]: absent.md\n")
        self.assertEqual(["README.md:2: missing local path: absent.md"], self.check())

    def test_footnote_body_links_are_checked(self):
        self.write("README.md", "A[^one]\n[^one]: [source](missing.md)\n")
        self.assertEqual(["README.md:2: missing local path: missing.md"], self.check())

    def test_adjacent_footnotes_are_not_link_references(self):
        self.write("README.md", "Claim.[^one][^two]\n[^one]: First\n[^two]: Second\n")
        self.assertEqual([], self.check())

    def test_comments_inline_code_and_fences_are_ignored(self):
        self.write("README.md", "<!--\n[x](missing.md)\n-->\n`[x](missing.md)`\n````md\n```\n[x](missing.md)\n[^undefined]\n````\n")
        self.assertEqual([], self.check())

    def test_unclosed_or_mismatched_fence_fails(self):
        self.write("README.md", "# Example\n~~~text\ncontent\n```\n")
        self.assertEqual(["README.md:2: unclosed fenced code block"], self.check())

    def test_setext_and_explicit_html_anchors(self):
        self.write("README.md", "Heading\n=======\n<a id=\"custom\"></a>\n[heading](#heading) [custom](#custom)")
        self.assertEqual([], self.check())

    def test_parentheses_in_filename_and_link_title(self):
        self.write("README.md", '[guide](docs/guide(v1).md "A title")')
        self.write("docs/guide(v1).md", "# Guide")
        self.assertEqual([], self.check())

    def test_external_links_are_not_requested(self):
        self.write("README.md", "[web](https://invalid.example/absent#anchor) [mail](mailto:editor@example.com)")
        self.assertEqual([], self.check())


if __name__ == "__main__":
    unittest.main()
