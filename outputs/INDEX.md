# Outputs index

Consolidated exports live here as `consolidated-YYMMDD.md`, with the PDF alongside.
Both are committed — the PDF is the artifact people actually want, and keeping it in
the repo means it can be read without a Typst toolchain.

Build with `scripts/build-pdf.sh`, or via the `consolidate-pdf` skill in
`.claude/skills/`, which carries the toolchain gotchas.

| Date | Files | Pages | Contents |
| --- | --- | --- | --- |
| 2026-08-12 | [`consolidated-260812.md`](consolidated-260812.md) · [`consolidated-260812.pdf`](consolidated-260812.pdf) | 28 | First export. Profile and story; 3 Q&A pairs (background speech and focus; earplugs for parenting vs sleep; ideal attenuation for focused work); 4 recommendations (closing doors, custom moulded earplugs, Loop, earmuffs); 20 sources. |

## What an export contains

Four parts, in this order:

1. **The profile** — `context/profile.md` and `context/story.md`. Experience.
2. **Questions and answers** — every `questions/<slug>.md` that has a matching
   `answers/<slug>.md`. Research.
3. **What has actually worked** — everything in `recommendations/`. Experience.
4. **Sources** — the citation and `read:` field of every file in `sources/`.

Parts II and III are deliberately separated and each carries a banner stating its
provenance, because a consolidated document is the easiest place to lose the
distinction between a study and a kitchen.

An unanswered question does not appear. Only pairs are exported, so a question filed
as `deferred` stays out until it has an answer file.
