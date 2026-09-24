#!/usr/bin/env python3
"""prep_inbox.py — sort and clean a messy folder of documents into
material that's actually ready to upload as a Custom GPT's Knowledge.

Point it at a folder (your "inbox" — Downloads, a dumping-ground folder,
whatever) and it will:

  1. Walk the folder recursively, finding every PDF/DOCX/TXT/MD/RTF file.
  2. Extract plain text from each one.
  3. Skip exact duplicates (by content hash) — common when the same file
     got saved twice under different names.
  4. Skip empty or unreadable files, logging why.
  5. Flag files whose text contains likely-sensitive patterns (password,
     api key, SSN-shaped numbers, etc.) instead of silently including
     them — Knowledge files are not private, and this needs a human
     decision, not a script's guess.
  6. Write one clean .md file per surviving source document into the
     output folder, with a small header noting where it came from.
  7. Write an INDEX.md cataloguing everything: what went in cleanly,
     what got skipped and why, and what got flagged for review.

This does NOT try to semantically categorize or summarize your
documents — that step benefits from an actual reader (you, or a Claude/
ChatGPT conversation working through INDEX.md with you) more than a
script guessing. What this script buys you is the mechanical part:
turning a folder of scattered PDFs/Word docs into a flat set of clean
text files plus a map of what's there, so that conversation — or your
own read-through — has something organized to work from instead of a
raw folder.

Usage:
    python3 prep_inbox.py /path/to/inbox --output /path/to/cleaned

Requires: pypdf, python-docx (see requirements.txt — run inside the
tools/.venv this repo's README sets up, not your system Python).

PRIVACY: this script makes no network calls. It only reads files under
the inbox path you give it and writes files under the output path you
give it — nothing is sent anywhere, to OpenAI or otherwise. Don't take
that on faith: this file has zero imports of `requests`, `urllib`,
`http`, `socket`, or any other networking module (check the import
block below, or `grep -nE "^(import|from) " prep_inbox.py`), and you can
run it with your network disconnected entirely to confirm the same
thing empirically. See ../docs/06-privacy-and-data.md for where the
local/not-local line actually falls in the rest of the process — this
script is the local part; uploading its output to Knowledge is not.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

try:
    import docx as python_docx
except ImportError:
    python_docx = None


SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt", ".md", ".rtf"}

# Deliberately conservative and over-inclusive — a false positive here
# just means one extra file to glance at before uploading; a false
# negative means something sensitive quietly ends up in Knowledge,
# which is not private (see the guide's warning in docs/01-walkthrough.md).
SENSITIVE_PATTERNS = {
    "password/credential": re.compile(r"\b(password|passwd|pwd)\s*[:=]\s*\S+", re.IGNORECASE),
    "API key / secret": re.compile(r"\b(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*\S+", re.IGNORECASE),
    "SSN-shaped number": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "credit-card-shaped number": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}

JUNK_FILENAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}


@dataclass
class ProcessResult:
    cleaned: list[Path] = field(default_factory=list)
    duplicates: list[tuple[Path, Path]] = field(default_factory=list)  # (dup, original)
    skipped_empty: list[Path] = field(default_factory=list)
    skipped_unreadable: list[tuple[Path, str]] = field(default_factory=list)
    skipped_unsupported: list[Path] = field(default_factory=list)
    flagged: list[tuple[Path, list[str]]] = field(default_factory=list)  # (path, reasons)


def extract_text(path: Path) -> Optional[str]:
    """Best-effort plain-text extraction. Returns None if the file type
    isn't supported or extraction fails outright."""
    ext = path.suffix.lower()
    try:
        if ext == ".pdf":
            if PdfReader is None:
                raise RuntimeError("pypdf not installed — see tools/requirements.txt")
            reader = PdfReader(str(path))
            return "\n\n".join(page.extract_text() or "" for page in reader.pages)
        if ext == ".docx":
            if python_docx is None:
                raise RuntimeError("python-docx not installed — see tools/requirements.txt")
            doc = python_docx.Document(str(path))
            return "\n\n".join(p.text for p in doc.paragraphs)
        if ext in (".txt", ".md"):
            return path.read_text(encoding="utf-8", errors="replace")
        if ext == ".rtf":
            # No dependency for RTF — strip control words with a light
            # regex rather than pull in a whole RTF parser for one format.
            raw = path.read_text(encoding="utf-8", errors="replace")
            text = re.sub(r"\\[a-z]+\d* ?", " ", raw)
            text = re.sub(r"[{}]", "", text)
            return text
    except Exception as exc:  # noqa: BLE001 — genuinely want to catch anything and report it
        raise RuntimeError(str(exc)) from exc
    return None


def find_sensitive(text: str) -> list[str]:
    return [label for label, pattern in SENSITIVE_PATTERNS.items() if pattern.search(text)]


def safe_slug(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-")
    return slug or "untitled"


def process_inbox(inbox: Path, output: Path) -> ProcessResult:
    result = ProcessResult()
    seen_hashes: dict[str, Path] = {}
    output.mkdir(parents=True, exist_ok=True)

    all_files = sorted(p for p in inbox.rglob("*") if p.is_file())
    for path in all_files:
        if path.name in JUNK_FILENAMES or path.name.startswith("."):
            continue
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            result.skipped_unsupported.append(path)
            continue

        try:
            text = extract_text(path)
        except RuntimeError as exc:
            result.skipped_unreadable.append((path, str(exc)))
            continue

        if text is None:
            result.skipped_unsupported.append(path)
            continue

        normalized = text.strip()
        if not normalized:
            result.skipped_empty.append(path)
            continue

        content_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        if content_hash in seen_hashes:
            result.duplicates.append((path, seen_hashes[content_hash]))
            continue
        seen_hashes[content_hash] = path

        sensitive = find_sensitive(normalized)
        if sensitive:
            result.flagged.append((path, sensitive))
            continue  # flagged files are NOT auto-written to output — see below

        rel = path.relative_to(inbox)
        out_name = safe_slug(str(rel.with_suffix(""))) + ".md"
        out_path = output / out_name
        # Avoid collisions from two different source files slugging to
        # the same name (e.g. two "notes.pdf" in different subfolders).
        counter = 2
        while out_path.exists():
            out_path = output / f"{safe_slug(str(rel.with_suffix('')))}-{counter}.md"
            counter += 1

        header = f"<!-- source: {rel} -->\n\n"
        out_path.write_text(header + normalized, encoding="utf-8")
        result.cleaned.append(out_path)

    return result


def write_index(inbox: Path, output: Path, result: ProcessResult) -> Path:
    lines: list[str] = []
    lines.append(f"# Inbox prep report\n")
    lines.append(f"Source: `{inbox}`  \nOutput: `{output}`\n")
    lines.append(f"**{len(result.cleaned)}** files cleaned and ready to upload.\n")

    if result.cleaned:
        lines.append("## Ready for Knowledge upload\n")
        for p in result.cleaned:
            lines.append(f"- `{p.name}`")
        lines.append("")

    if result.flagged:
        lines.append("## ⚠️ Flagged — review before including (not written to output)\n")
        lines.append("These matched a pattern that often means sensitive content. "
                      "Open the original, decide if it's actually safe to share, and "
                      "if so copy it into the output folder yourself.\n")
        for p, reasons in result.flagged:
            lines.append(f"- `{p}` — possible: {', '.join(reasons)}")
        lines.append("")

    if result.duplicates:
        lines.append("## Skipped as duplicates\n")
        for dup, original in result.duplicates:
            lines.append(f"- `{dup}` — identical content to `{original}`")
        lines.append("")

    if result.skipped_unreadable:
        lines.append("## Skipped — couldn't read\n")
        for p, reason in result.skipped_unreadable:
            lines.append(f"- `{p}` — {reason}")
        lines.append("")

    if result.skipped_empty:
        lines.append("## Skipped — empty after extraction\n")
        for p in result.skipped_empty:
            lines.append(f"- `{p}`")
        lines.append("")

    if result.skipped_unsupported:
        lines.append("## Skipped — unsupported file type\n")
        for p in result.skipped_unsupported:
            lines.append(f"- `{p}`")
        lines.append("")

    lines.append("## Next step\n")
    lines.append(
        "The output folder now has one clean .md file per surviving document — "
        "flat, de-duplicated, and small enough to read through. Two ways to go "
        "from here, per docs/05-prepping-your-inbox.md:\n\n"
        "1. **Upload as-is** if the files are already well-organized by topic.\n"
        "2. **Consolidate first** — paste this INDEX.md into a Claude or ChatGPT "
        "conversation and ask it to help you group related files and merge small, "
        "overlapping ones into fewer, better-structured documents before uploading."
    )

    index_path = output / "INDEX.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    return index_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("inbox", type=Path, help="Folder to sort through")
    parser.add_argument("--output", type=Path, default=None, help="Where to write cleaned files (default: <inbox>/../cleaned)")
    args = parser.parse_args()

    inbox = args.inbox.expanduser().resolve()
    if not inbox.is_dir():
        sys.exit(f"Not a folder: {inbox}")

    output = (args.output or inbox.parent / "cleaned").expanduser().resolve()
    if output == inbox or str(output).startswith(str(inbox) + "/"):
        sys.exit("Output folder can't be inside the inbox folder — pick a separate location with --output.")

    print(f"Scanning {inbox} ...")
    result = process_inbox(inbox, output)
    index_path = write_index(inbox, output, result)

    print(f"\n✓ {len(result.cleaned)} files cleaned → {output}")
    if result.flagged:
        print(f"⚠ {len(result.flagged)} files flagged for manual review (not copied — see INDEX.md)")
    if result.duplicates:
        print(f"  {len(result.duplicates)} duplicates skipped")
    if result.skipped_unreadable:
        print(f"  {len(result.skipped_unreadable)} files couldn't be read")
    print(f"\nFull report: {index_path}")


if __name__ == "__main__":
    main()
