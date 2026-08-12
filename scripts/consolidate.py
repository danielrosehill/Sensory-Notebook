#!/usr/bin/env python3
"""Assemble the whole notebook into one Q&A-formatted markdown document.

Output: outputs/consolidated-YYMMDD.md, ready for scripts/build-pdf.sh.

Design notes, because they are not obvious from the code:

- Research answers and personal recommendations are kept in separate top-level
  parts, and every entry carries a provenance banner. CLAUDE.md requires a reader
  to never be unsure whether a claim came from a study or from Daniel's kitchen,
  and a consolidated export is exactly where that distinction is easiest to lose.
- HTML comments are stripped. The repo uses <!-- FLAG: ... --> for internal notes
  to the next agent; those must not reach a printable document.
- Repo-relative .md links become plain emphasised text. A PDF reader cannot follow
  them, and leaving them as links produces dead blue text.

No third-party dependencies: standard library only, so it runs anywhere typst and
pandoc do.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- front matter


def split_front_matter(text: str) -> tuple[dict[str, object], str]:
    """Return (front-matter dict, body). Flat YAML subset only — that is all the
    repo uses. Handles `key: value`, inline `key: [a, b]`, and block sequences."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw, body = text[4:end], text[end + 5 :]

    meta: dict[str, object] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(("  - ", "- ")) and current_key:
            meta.setdefault(current_key, [])
            seq = meta[current_key]
            if isinstance(seq, list):
                seq.append(line.split("- ", 1)[1].strip().strip("\"'"))
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        current_key = key
        if not value:
            meta[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            meta[key] = [p.strip().strip("\"'") for p in inner.split(",") if p.strip()]
        else:
            meta[key] = value.strip("\"'")
    return meta, body


# ------------------------------------------------------------------- cleaning

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SETEXT_H1_RE = re.compile(r"^# ", re.MULTILINE)


def strip_comments(text: str) -> str:
    text = COMMENT_RE.sub("", text)
    # Collapse the blank-line craters left behind by removed comment blocks.
    return re.sub(r"\n{3,}", "\n\n", text)


def delink(text: str) -> str:
    """Keep external links; flatten repo-internal ones to emphasised text."""

    def repl(m: re.Match[str]) -> str:
        label, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        label = label.strip().strip("`")
        return f"*{label}*"

    return MD_LINK_RE.sub(repl, text)


def demote(text: str, levels: int = 2) -> str:
    """Push every heading down so file H1s sit under the export's structure."""
    out = []
    for line in text.splitlines():
        if line.startswith("#"):
            hashes = len(line) - len(line.lstrip("#"))
            if 0 < hashes <= 6:
                line = "#" * min(hashes + levels, 6) + line[hashes:]
        out.append(line)
    return "\n".join(out)


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def prepare(text: str, levels: int = 2) -> str:
    body = strip_comments(text)
    body = delink(body)
    # The file's own H1 becomes the entry title, emitted by the caller.
    body = SETEXT_H1_RE.sub("## ", body, count=1)
    return demote(body, levels - 1).strip()


# --------------------------------------------------------------------- pieces


def read(path: Path) -> tuple[dict[str, object], str]:
    meta, body = split_front_matter(path.read_text(encoding="utf-8"))
    return meta, body


def banner(kind: str) -> str:
    """A one-line provenance blockquote. Rendered as a callout by the template."""
    if kind == "research":
        return (
            "> **Research summary.** Drawn from the literature. Every non-obvious claim\n"
            "> is traceable to a file in the source list at the end of this document.\n"
        )
    return (
        "> **Personal experience.** Something actually tried, in the real world, with a\n"
        "> verdict. Not evidence, not a finding, and not a recommendation to anyone else.\n"
    )


def collect_qa(repo: Path) -> list[tuple[Path, Path]]:
    pairs = []
    for q in sorted((repo / "questions").glob("*.md")):
        a = repo / "answers" / q.name
        if a.exists():
            pairs.append((q, a))
    return pairs


def collect_recommendations(repo: Path) -> list[Path]:
    return sorted(
        p for p in (repo / "recommendations").glob("*.md") if p.name != "README.md"
    )


def collect_sources(repo: Path) -> list[Path]:
    return sorted(
        p for p in (repo / "sources").glob("*.md") if p.name != "README.md"
    )


# ---------------------------------------------------------------------- build


def build(repo: Path, date: dt.date) -> str:
    out: list[str] = []
    stamp = date.strftime("%Y-%m-%d")

    out.append("---")
    out.append('title: "Sensory Notebook"')
    out.append('subtitle: "Living with sensory sensitivity — research, and what has actually worked"')
    out.append(f'date: "{stamp}"')
    out.append("---")
    out.append("")

    out.append("# About this document")
    out.append("")
    out.append(
        "This is a consolidated export of the Sensory Notebook, a public repository "
        "that does two things at once and tries never to blur them: it records "
        "longform, sourced answers to research questions about sensory processing, "
        "and it records one person's own sensory profile and the interventions he has "
        "actually tried."
    )
    out.append("")
    out.append(
        "**Keeping those apart is the point.** Every entry below carries a banner "
        "saying which kind it is. Research summaries cite sources; personal "
        "experience does not need a citation and is never presented as a finding."
    )
    out.append("")
    out.append(
        "**This is not medical advice.** It is written by someone who is not a "
        "clinician. Describing what an intervention does is not the same as telling "
        "you to use it."
    )
    out.append("")
    out.append(
        "Sensory terminology is contested. Where a term belongs to a particular "
        "framework — DSM-5-TR, ICD-11, the occupational-therapy literature — the "
        "entries name the framework rather than using the terms interchangeably."
    )
    out.append("")
    out.append(f"Generated {stamp} from the repository as it stood on that date.")
    out.append("")

    # ---- Part I: the person
    profile = repo / "context" / "profile.md"
    story = repo / "context" / "story.md"
    if profile.exists() or story.exists():
        out.append(r"\newpage")
        out.append("")
        out.append("# Part I — The profile")
        out.append("")
        out.append(banner("experience"))
        out.append("")
        for path in (profile, story):
            if path.exists():
                _, body = read(path)
                out.append(prepare(body, levels=2))
                out.append("")

    # ---- Part II: research
    pairs = collect_qa(repo)
    if pairs:
        out.append(r"\newpage")
        out.append("")
        out.append("# Part II — Questions and answers")
        out.append("")
        out.append(banner("research"))
        out.append("")
        for q_path, a_path in pairs:
            q_meta, q_body = read(q_path)
            a_meta, a_body = read(a_path)
            title = first_heading(q_body) or q_path.stem
            out.append(f"## {title}")
            out.append("")
            bits = []
            if q_meta.get("asked"):
                bits.append(f"Asked {q_meta['asked']}")
            if a_meta.get("answered"):
                bits.append(f"answered {a_meta['answered']}")
            if a_meta.get("confidence"):
                bits.append(f"confidence: {a_meta['confidence']}")
            tags = q_meta.get("tags")
            if isinstance(tags, list) and tags:
                bits.append("tags: " + ", ".join(tags))
            if bits:
                out.append(f"*{' · '.join(bits)}*")
                out.append("")
            out.append("### The question")
            out.append("")
            out.append(prepare(q_body, levels=4))
            out.append("")
            out.append("### The answer")
            out.append("")
            out.append(prepare(a_body, levels=4))
            out.append("")

    # ---- Part III: experience
    recs = collect_recommendations(repo)
    if recs:
        out.append(r"\newpage")
        out.append("")
        out.append("# Part III — What has actually worked")
        out.append("")
        out.append(banner("experience"))
        out.append("")
        for path in recs:
            meta, body = read(path)
            title = first_heading(body) or path.stem
            out.append(f"## {title}")
            out.append("")
            bits = []
            for key in ("kind", "verdict", "since", "cost"):
                if meta.get(key):
                    bits.append(f"{key}: {meta[key]}")
            mods = meta.get("modality")
            if isinstance(mods, list) and mods:
                bits.append("modality: " + ", ".join(mods))
            if bits:
                out.append(f"*{' · '.join(bits)}*")
                out.append("")
            out.append(prepare(body, levels=3))
            out.append("")

    # ---- Part IV: sources
    sources = collect_sources(repo)
    if sources:
        out.append(r"\newpage")
        out.append("")
        out.append("# Part IV — Sources")
        out.append("")
        out.append(
            "One entry per load-bearing source. The **read** field records how much of "
            "each was actually seen, so a verified claim can be told from a relayed one "
            "without redoing the work."
        )
        out.append("")
        for path in sources:
            meta, body = read(path)
            title = first_heading(body) or path.stem
            out.append(f"## {title}")
            out.append("")
            if meta.get("citation"):
                out.append(f"{meta['citation']}")
                out.append("")
            bits = []
            for key in ("type", "doi", "pmid", "url", "accessed", "read"):
                if meta.get(key):
                    bits.append(f"{key}: {meta[key]}")
            if bits:
                out.append(f"*{' · '.join(bits)}*")
                out.append("")

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="YYYY-MM-DD, defaults to today")
    ap.add_argument("--out", help="output path, defaults to outputs/consolidated-YYMMDD.md")
    args = ap.parse_args()

    date = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    out_path = Path(args.out) if args.out else REPO / "outputs" / f"consolidated-{date:%y%m%d}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build(REPO, date), encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
