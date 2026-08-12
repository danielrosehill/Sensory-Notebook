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

## Startup

Read `context/profile.md` and `context/scope.md` before answering anything. The profile
is the grounding context — an answer about, say, noise tolerance that ignores what is
already recorded there is a worse answer.

If the `research-space` plugin is installed, `/research-space:research-init` loads prior
state. It is not installed by default here (skills live in the OpenViking substrate), so
falling back to reading `questions/`, `answers/` and `outputs/INDEX.md` directly is fine.

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

Selected Q&A pairs get concatenated into `outputs/consolidated-YYMMDD.md`, then handed to
the Typst toolchain for a PDF. Keep `outputs/INDEX.md` current. Consolidated exports may
mix research answers and recommendations, but must keep them visually distinct sections.

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
  records pasted in verbatim — summarise instead.
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
