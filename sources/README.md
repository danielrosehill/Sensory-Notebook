# Sources

One file per load-bearing source, referenced by path from an answer's `sources:`
front-matter. Slug is `<firstauthor>-<year>-<short-topic>.md` for papers, or a plain
descriptive slug for terminology notes that synthesise several.

Convention established 2026-08-12 with the first answer; `CLAUDE.md` requires the folder
but does not specify the format, so this is it.

## Front-matter

```yaml
---
citation: "Full citation, one string, author-year-title-journal-volume-pages."
type: journal-article | review | terminology-note | preprint | standard
year: 2020
doi: 10.xxxx/xxxxx          # omit if none
pmid: 12345678              # omit if none
url: https://…              # what was actually opened
accessed: YYYY-MM-DD
read: full-text | full-record | abstract-only | abstract-and-summary | secondary-summary
---
```

## The `read:` field is the important one

It records **how much of the source was actually seen**, so a later reader can tell a
verified claim from a relayed one without re-doing the work.

| Value | Means |
|---|---|
| `full-text` | The paper itself was read. |
| `full-record` | A complete open-access record (e.g. PMC) — abstract, methods, results, caveats. |
| `abstract-and-summary` | Publisher abstract plus a listing summary. |
| `abstract-only` | Only the published abstract, e.g. from the PubMed record. |
| `secondary-summary` | Neither abstract nor full text opened directly; content came from search-result summaries or citing papers. Citation may still be confirmed. |

## Every file ends with a Provenance section

Prose, at the bottom, stating explicitly:

- which bibliographic fields were **confirmed against a primary record**, and against which;
- which fields or claims are **reconstructed or relayed** and should be checked before
  being republished;
- anything **deliberately excluded** — a figure widely repeated on consumer-health pages
  that the peer-reviewed literature does not support, for instance.

This exists because the notebook's whole premise is that a reader can tell where a claim
came from. A citation that looks authoritative and was never opened is precisely the kind
of false signal that premise is meant to prevent.

## Body

Free-form, but in practice: design → findings → authors' conclusion → caveats → what the
source does and does not support. The last of those matters more than it looks: several
files here exist mainly to stop a source being over-read.
