# Sensory Notebook

**Variant:** `general-research-workspace` (research-space plugin)
**Started:** 2026-08-12
**Umbrella theme:** Living with sensory sensitivity — what the research actually says, and what has actually worked.

## Purpose

This workspace is **two things at once**, and answers should respect the difference:

1. **A research notebook.** Daniel poses a question about sensory processing — mechanisms,
   evidence, terminology, products, accommodations — and Claude writes a longform,
   sourced response. Question and answer are logged as a paired record.
2. **A personal record.** Daniel's own sensory profile, his story, and the
   recommendations he has worked out over the years. This is lived experience, not
   literature, and it is not required to have a citation.

Keeping the two separate is the whole point. A reader should never be unsure whether a
claim comes from a study or from Daniel's kitchen. Never launder personal experience into
something that reads like evidence, and never flatten evidence into anecdote.

## Why the detail keeps arriving, and what to do with it

Standing instruction from Daniel, 2026-08-12. Treat everything below as already decided;
do not re-ask it per item.

Daniel will volunteer a lot of small, individually unremarkable detail — which brand, what
the room was like, what he tried first, what it felt like at the time. **That is deliberate
and it is the method, not padding.** The objective is a bank of personal experience held in
the repository, dense enough and cohesive enough that later answers can be drawn from it
rather than from a cold start. He is confident he is very far from unique in this, and the
point of accumulating it is that his own experience can inform the research, and the two
together can produce something validated and genuinely useful for people in the same boat
who have not found solutions yet.

What this means in practice:

- **Record the small things.** If a detail seems too minor to file, that is not a reason to
  drop it. Individually insignificant detail is the raw material here. Put it in the
  relevant `recommendations/`, `context/` or `questions/` file rather than only mentioning
  it in a reply.
- **Assume it is intended for the repository, and assume it is public.** He would not be
  sharing something he did not want recorded. Do not ask "is this okay to publish?" for
  each item — the answer is yes by default. Override that only where there is a compelling
  and specific reason, in which case say what it is rather than asking a general question.
- **The existing rules still apply and are not loosened by this.** Third parties still are
  not named without their own say-so, clinical material is still summarised rather than
  pasted, and personal experience is still labelled as experience rather than dressed up as
  evidence.
- **The gap between "he told me" and "it is written down" is where this fails.** A detail
  mentioned in conversation and not filed is lost, because the repository is the memory.

## Startup

Read `context/profile.md` and `context/scope.md` before answering anything. The profile
is the grounding context — an answer about, say, noise tolerance that ignores what is
already recorded there is a worse answer.

If the `research-space` plugin is installed, `/research-space:research-init` loads prior
state. It is not installed by default here (skills live in the OpenViking substrate), so
falling back to reading `questions/`, `answers/` and `outputs/INDEX.md` directly is fine.

## Skills in this repo

Two, in `.claude/skills/`. They are checked in and specific to this notebook.

| Skill | Use it when |
| --- | --- |
| `capture-note` | Daniel dictates experience, a verdict, a question or background rather than asking for a task. Routes it to the right files without inventing the gaps. |
| `consolidate-pdf` | Asked to consolidate, export, cut a release, or "make the PDF". |

## Workflow

### Capturing a question and answer

- **Question**: `questions/YYMMDD-<slug>.md` — the question as posed. Questions arrive
  dictated and half-formed; fix transcription slips, preserve intent and phrasing.
- **Answer**: `answers/YYMMDD-<slug>.md` — the longform response, same slug as the question.
- **Sources**: anything load-bearing gets a file in `sources/` and a reference from the
  answer's front-matter.

### Capturing a recommendation

`recommendations/<slug>.md` — a thing that was tried, in the real world, with a verdict.
One file per intervention (a product, a technique, an accommodation, a routine). Front-matter:

```yaml
---
kind: product | technique | accommodation | environment | routine
verdict: works | partial | abandoned | untested
since: YYYY-MM       # when it entered use
cost: <approx, currency noted>   # omit if not applicable
---
```

Body: what the problem was, what was tried, what happened, what it did **not** fix, and
what would have to be true for someone else to get the same result. A recommendation with
no failure mode written down is not finished.

### Personal story and profile

`context/profile.md` is the sensory profile — the specific sensitivities, their triggers,
their severity, how they interact. `context/story.md` is the narrative: how this was
noticed, what was misattributed to what, what changed over time.

Both are Daniel's to dictate. Claude may structure, tidy and follow up with clarifying
questions, but must not invent biographical detail, infer a diagnosis, or fill a gap with
a plausible-sounding generality.

### Periodic consolidation

Built, not hand-assembled. `scripts/build-pdf.sh` runs
`scripts/consolidate.py` → pandoc → Typst and produces both
`outputs/consolidated-YYMMDD.md` and the PDF alongside it. The `consolidate-pdf` skill
carries the toolchain gotchas; read it before touching `templates/notebook.typ`.

Keep `outputs/INDEX.md` current. Exports mix research answers and recommendations but
keep them as visually distinct parts, each under a banner stating its provenance — that
banner is a blockquote, and the Typst template styles blockquotes to make it visible, so
the two files have to stay in agreement.

## Conventions

- **Slugs**: short, kebab-case, descriptive (`260812-earplug-attenuation-curves.md`).
- **Pair symmetry**: a `questions/<slug>.md` implies an `answers/<slug>.md`.
- **Front-matter** on question files:

```yaml
---
asked: YYYY-MM-DD
status: answered | in-progress | deferred
tags: [auditory, tactile, visual, interoception, ...]
---
```

- **Front-matter** on answer files:

```yaml
---
question: <slug>.md
answered: YYYY-MM-DD
sources: [sources/<slug>.md, ...]
confidence: high | medium | low
---
```

- **Notes**: `notes/` is scratch and is excluded from exports.

## Rules

- **Cite the research, label the experience.** Every non-obvious empirical claim cites at
  least one file in `sources/`. Personal-experience claims are marked as such and need no
  citation — but must not be dressed up as findings.
- **This is a public repo.** Write for a stranger who arrives via search. Assume no shared
  context. That also means: no third parties named without their say-so, and no clinical
  records pasted in verbatim — summarise instead. What Daniel volunteers about himself is
  public by default and does not need clearing item by item — see
  [Why the detail keeps arriving](#why-the-detail-keeps-arriving-and-what-to-do-with-it).
- **Not medical advice, and say so.** The README carries the disclaimer; answers should
  not quietly drift into prescribing. Describing what a treatment does is fine; telling a
  reader to take it is not.
- **Sensory terminology is contested.** "Sensory processing disorder", "sensory
  over-responsivity", "hypersensitivity" and "misophonia" have different standing in DSM-5-TR,
  ICD-11 and the occupational-therapy literature. Name which framework a term belongs to
  rather than using them interchangeably, and say plainly where a construct is disputed.
- **Mark speculation** — `(speculation)` inline, or `confidence: low` in front-matter.
- **Repeat questions link back.** If a question has been asked before, link the prior
  answer and note only what has changed.
