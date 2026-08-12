---
citation: "ISO 3382-3, Acoustics — Measurement of room acoustic parameters — Part 3: Open plan offices; with supporting irrelevant-speech experimental literature incl. Haapakangas et al. and Ebissou/Jeon-type STI-graded studies."
type: standard
year: 2022
url: https://www.iso.org/standard/70317.html
accessed: 2026-08-12
read: secondary-summary
---

# STI 0.20 and STI 0.50: what the two standard thresholds actually mean

The measurement scaffolding behind any claim about how much speech reduction is enough.
Companion to [`hongisto-haapakangas-sti-performance.md`](hongisto-haapakangas-sti-performance.md),
which has the dose–response curve; this file has the standardised distances.

## The two distances

ISO 3382-3 defines two descriptors of an open-plan office, both expressed as a distance
from a speaker:

- **Distraction distance (r_D)** — the distance at which **STI falls below 0.50**. Derived
  from Hongisto's assumption that 0.50 is the critical threshold for performance effects.
- **Privacy distance (r_P)** — the distance at which **STI falls below 0.20**. Below this,
  speech is essentially unintelligible; **STI 0.20 corresponds to under 30% word
  intelligibility**, and conversations cannot meaningfully be overheard.

So 0.50 is *"stops damaging your work"* and 0.20 is *"cannot be understood at all"*. They
are different targets and choosing between them is a real decision, not a rounding.

The older Articulation Index literature has the same figure: office workers are generally
satisfied with speech privacy at **AI ≤ 0.20** ("normal privacy"), and reaching it usually
requires **raising** background sound with electronic masking.

## What the experiments say about where the real threshold is

The graded-STI experiments broadly support a low threshold but do not agree on one number:

- A cut-off around **STI 0.23**, after which writing performance drops sharply — the
  disruption attributed to the speech's **semanticity** rather than its acoustic properties.
- Proof-reading performance **unaffected between STI 0.00 and 0.30**, worst at the highest
  STI.
- Serial recall accuracy falling from **98.4% to 85.6%** as STI rose from **0.12 to 0.51**.
- Across seven conditions (STI 0.17 to 0.57), employees had to **exert more effort to
  resist distraction between 0.26 and 0.45**, with efficiency dropping further above 0.50
  when task-switching was involved.
- A dissenting result: one study across STI 0.2–0.7 found no strong variation between the
  two lower values and **could not confirm the ISO 3382-3 target values**. Others put the
  steepest decline lower than Hongisto predicted, varying by cognitive task.

The convergent reading — 0.21 in Haapakangas 2020, 0.23 here, "unaffected below 0.30"
there — is that the useful target is **around 0.2, not 0.5**. The effort finding matters
independently: between roughly 0.26 and 0.45 performance can be maintained, but only by
spending effort to maintain it. A measure that only looks at output will score that band as
fine.

## Why this is hard to achieve in practice

In typical open-plan offices with an absorbing ceiling and no screens, **STI stays above
0.50 over distances up to 18 m**, and **STI < 0.20 is not achieved when background noise is
low**.

The counter-intuitive corollary, which matches the masking logic already in this notebook:
**a background level that is too low makes distraction worse**, because there is nothing
for distant conversation to disappear into.

## What this source does not support

- STI is a property of a **room and a listening position**. It is not a property of an
  earplug, and there is no defined way to read an attenuation figure as an STI change. Any
  move from "aim for STI 0.2" to "therefore buy an N dB plug" is an inference this
  literature does not license.
- The privacy distance was designed for **confidentiality**, not for concentration. Using
  0.20 as a personal comfort target borrows it from its intended purpose.
- The disagreement between studies is genuine and unresolved; the ISO target values are
  **contested in the literature**, not settled.

## Provenance

**Relayed from search-result summaries.** The ISO 3382-3 record itself was not opened, and
the year in the front-matter refers to the current edition as listed rather than to a
verified publication date — **check it before citing.**

The definitions of distraction and privacy distance, and their 0.50 and 0.20 anchors, are
reported consistently across multiple independent acoustics sources and are treated as
reliable. The individual experimental figures (0.23 cut-off, 98.4%→85.6%, the seven-
condition study, the 18 m and non-confirmation results) are each from a single summary,
were **not** traced to their papers, and are recorded here as leads rather than as
established values. Several of them may well be the same studies already catalogued in
`hongisto-haapakangas-sti-performance.md` under different descriptions.
