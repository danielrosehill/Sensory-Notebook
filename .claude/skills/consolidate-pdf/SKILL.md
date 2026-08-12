---
name: consolidate-pdf
description: Build the whole notebook into one printable Q&A-formatted PDF via Typst. Use when asked to consolidate, export, produce a release, "make the PDF", or distil the repository into a single document.
---

# Consolidate the notebook into a PDF

Produces one self-contained printable document containing the profile, every
answered question with its answer, every recommendation, and the source list.

## Run it

```bash
scripts/build-pdf.sh              # today's date
scripts/build-pdf.sh 2026-08-12   # a specific date
```

Outputs `outputs/consolidated-YYMMDD.md` and `outputs/consolidated-YYMMDD.pdf`.

Requires `python3`, `pandoc` (≥3.0, for the Typst writer) and `typst`. All three
were present and working on this machine as of 2026-08-12 — pandoc 3.7.0.2,
typst 0.14.2. The script checks for them and fails loudly rather than half-building.

## What to do after building

1. **Read at least two pages of the PDF.** Not the markdown — the PDF. The build
   succeeding proves the toolchain ran, not that the document is right.
2. **Add a row to `outputs/INDEX.md`.** Date, page count, what changed since the
   previous export.
3. **Commit both the `.md` and the `.pdf`.** The PDF is the artifact people
   actually want, and having it in the repo means it can be downloaded without a
   toolchain. It is deliberately not gitignored.

## The pipeline

```
repository markdown
  → scripts/consolidate.py   assembles outputs/consolidated-YYMMDD.md
  → pandoc --pdf-engine=typst --template=templates/notebook.typ
  → outputs/consolidated-YYMMDD.pdf
```

`scripts/consolidate.py` is standard-library-only Python. It walks the repo, pairs
`questions/<slug>.md` with `answers/<slug>.md`, and emits four parts:

| Part | Content | Provenance |
| --- | --- | --- |
| I | `context/profile.md`, `context/story.md` | experience |
| II | Question/answer pairs, in slug order | research |
| III | Everything in `recommendations/` except `README.md` | experience |
| IV | Source list with the `read:` field of each | — |

## The three things that will bite you

**1. A literal dollar sign anywhere in `templates/notebook.typ` breaks the build,
including inside a Typst comment.** Pandoc parses the template first and reads a
dollar as the start of a variable name, failing with `unexpected "$"` and a line
number that points at your comment. Write the word "dollar" in prose instead.
Learned the hard way 2026-08-12.

**2. Pandoc's Typst writer expects the template to define helpers that its own
default template provides.** Omit them and a document containing a thematic break
dies with `unknown variable: horizontalrule`. `horizontalrule`, the `terms` show
rule for definition lists, and a base `table` set rule are defined at the top of
`notebook.typ` for exactly this reason — do not remove them. Recover the current
set with `pandoc -D typst` if a new one appears.

**3. Blockquotes are load-bearing, not decorative.** `consolidate.py` marks each
part with a blockquote banner saying whether it is research or personal
experience, and `notebook.typ` styles block quotes as grey callouts. If you
restyle quotes into something inconspicuous, the export silently loses the
distinction that `CLAUDE.md` says is the entire point of the repository.

## Verify before shipping

`consolidate.py` strips `<!-- ... -->` comments, because the repo uses them for
internal FLAG notes addressed to the next agent. Those must never reach a
published document. Check it actually happened:

```bash
pdftotext outputs/consolidated-YYMMDD.pdf - | grep -c 'FLAG'   # expect 0
pdfinfo outputs/consolidated-YYMMDD.pdf | grep Pages
```

The 2026-08-12 build was 28 pages with zero FLAG leakage. A sudden large drop in
page count means a directory stopped being picked up — check before assuming the
notebook simply got shorter.

## Restyling

`templates/notebook.typ` is ordinary Typst apart from the pandoc variables. Fonts
degrade gracefully: it asks for Libertinus Serif and falls back with a warning,
which is noise rather than failure. Everything else — margins, heading scale,
callout colour, the footer — is safe to change.
