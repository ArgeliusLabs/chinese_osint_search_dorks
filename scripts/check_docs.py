"""Offline checks for the Markdown features used in this repository.

Checks local links (including exact filename case on Windows), GitHub-style
heading anchors, reference/footnote definitions, and closed fenced code blocks.
External URLs are deliberately not requested: a blocked portal is not a dead link.
This is a small repository checker, not a complete CommonMark parser.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import html
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit


SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEADING = re.compile(r"^ {0,3}#{1,6}(?:\s+|$)(.*)$")
DEFINITION = re.compile(r"^ {0,3}\[([^\]]+)\]:\s*(.*)$")
REFERENCE = re.compile(r"(?<!!)\[(?!\^)([^\]\n]+)\]\[(?!\^)([^\]\n]*)\]")
FOOTNOTE = re.compile(r"(?<!\\)\[\^([^\]\n]+)\]")


@dataclass
class Document:
    path: Path
    anchors: set[str] = field(default_factory=set)
    links: list[tuple[int, str]] = field(default_factory=list)
    references: list[tuple[int, str]] = field(default_factory=list)
    definitions: dict[str, tuple[int, str]] = field(default_factory=dict)
    footnotes: set[str] = field(default_factory=set)
    footnote_uses: list[tuple[int, str]] = field(default_factory=list)
    errors: list[tuple[int, str]] = field(default_factory=list)


def reference_id(value: str) -> str:
    return " ".join(value.split()).casefold()


def without_code(value: str) -> str:
    return re.sub(r"(`+)(?!`)(.+?)\1(?!`)", "", value)


def heading_slug(value: str) -> str:
    # Inline formatting does not appear in GitHub heading fragments.
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value).lower().strip()
    value = "".join(
        char for char in value
        if char in "-_" or not unicodedata.category(char).startswith(("P", "S", "C"))
    )
    return value.replace(" ", "-")


def destination(value: str) -> str:
    """Read a Markdown destination, allowing balanced parentheses and <...>."""
    value = value.lstrip()
    if value.startswith("<"):
        end = value.find(">")
        return value[1:end] if end >= 0 else ""
    result: list[str] = []
    depth = 0
    escaped = False
    for char in value:
        if escaped:
            result.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "(":
            depth += 1
            result.append(char)
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
            result.append(char)
        elif char.isspace() and depth == 0:
            break
        else:
            result.append(char)
    return "".join(result)


def parse_document(path: Path) -> Document:
    doc = Document(path)
    source = path.read_text(encoding="utf-8-sig")
    # Preserve line numbers while excluding commented-out examples.
    source = re.sub(r"<!--[\s\S]*?-->", lambda m: "\n" * m[0].count("\n"), source)
    fence: tuple[str, int, int] | None = None
    previous = ""
    for line_number, line in enumerate(source.splitlines(), 1):
        marker = FENCE.match(line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            previous = ""
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]), line_number)
            previous = ""
            continue

        heading = HEADING.match(line)
        title = re.sub(r"\s+#+\s*$", "", heading[1]) if heading else None
        if not heading and previous.strip() and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line):
            title = previous.strip()
        if title is not None:
            slug = heading_slug(title)
            unique = slug
            suffix = 0
            while unique in doc.anchors:
                suffix += 1
                unique = f"{slug}-{suffix}"
            doc.anchors.add(unique)
        doc.anchors.update(re.findall(r"\bid\s*=\s*[\"']([^\"']+)[\"']", line))

        visible = without_code(line)
        definition = DEFINITION.match(visible)
        if definition:
            label = reference_id(definition[1])
            if label.startswith("^"):
                if label[1:] in doc.footnotes:
                    doc.errors.append((line_number, f"duplicate footnote definition: {label}"))
                doc.footnotes.add(label[1:])
            else:
                if label in doc.definitions:
                    doc.errors.append((line_number, f"duplicate link definition: {label}"))
                doc.definitions[label] = (line_number, destination(definition[2]))
            visible = definition[2] if label.startswith("^") else ""
        doc.footnote_uses.extend((line_number, reference_id(m[1])) for m in FOOTNOTE.finditer(visible))
        for match in re.finditer(r"(?<!\\)\]\(", visible):
            target = destination(visible[match.end():])
            if target:
                doc.links.append((line_number, html.unescape(target)))
        for match in REFERENCE.finditer(visible):
            doc.references.append((line_number, reference_id(match[2] or match[1])))
        previous = line

    if fence:
        doc.errors.append((fence[2], "unclosed fenced code block"))
    for line_number, label in doc.footnote_uses:
        if label not in doc.footnotes:
            doc.errors.append((line_number, f"undefined footnote: {label}"))
    for line_number, label in doc.references:
        if label not in doc.definitions:
            doc.errors.append((line_number, f"undefined link reference: {label}"))
    doc.links.extend(doc.definitions.values())
    return doc


def exact_path(root: Path, base: Path, relative: str) -> tuple[Path | None, str | None]:
    """Resolve by directory entries, never by the host's case-folding rules."""
    current = root if relative.startswith("/") else base
    for part in relative.split("/"):
        if part in {"", "."}:
            continue
        if part == "..":
            if current == root:
                return None, "local link leaves the repository"
            current = current.parent
            continue
        if not current.is_dir():
            return None, "local link has a non-directory path component"
        names = {entry.name: entry for entry in current.iterdir()}
        if part not in names:
            similar = next((name for name in names if name.casefold() == part.casefold()), None)
            if similar:
                return None, f"filename case mismatch: {part!r}; expected {similar!r}"
            return None, f"missing local path: {relative}"
        current = names[part]
        if current.is_symlink():
            return None, "local link traverses a symbolic link; review manually"
    return current, None


def check_repository(root: Path) -> list[str]:
    root = root.resolve()
    paths = sorted(path for path in root.rglob("*.md") if not SKIP_DIRS.intersection(path.relative_to(root).parts))
    documents: dict[Path, Document] = {}
    errors: list[str] = []
    for path in paths:
        try:
            documents[path] = parse_document(path)
        except (UnicodeError, OSError) as error:
            errors.append(f"{path.relative_to(root)}: cannot read Markdown: {error}")
    for path, doc in documents.items():
        problems = list(doc.errors)
        for line_number, target in doc.links:
            try:
                parts = urlsplit(target)
            except ValueError as error:
                problems.append((line_number, f"invalid link {target!r}: {error}"))
                continue
            if parts.scheme or parts.netloc:
                continue
            target_path, error = exact_path(root, path.parent, unquote(parts.path)) if parts.path else (path, None)
            if error:
                problems.append((line_number, error))
            elif parts.fragment and target_path in documents:
                anchor = unquote(parts.fragment)
                if anchor not in documents[target_path].anchors:
                    problems.append((line_number, f"missing heading anchor: {target}"))
        errors.extend(f"{path.relative_to(root).as_posix()}:{line}: {message}" for line, message in problems)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check_repository(args.root)
    if errors:
        print("\n".join(errors))
        return 1
    print("Markdown checks passed (local paths, anchors, references, and fences).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
