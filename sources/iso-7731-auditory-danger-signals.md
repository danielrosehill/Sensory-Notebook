---
citation: "ISO 7731:2003. Ergonomics — Danger signals for public and work areas — Auditory danger signals. 2nd edition, 2003-11-01. ISO/TC 159 Ergonomics, SC 5 Ergonomics of the physical environment."
type: standard
year: 2003
url: https://www.iso.org/standard/33590.html
accessed: 2026-08-12
read: abstract-and-summary
supersedes: "ISO 7731:1986, Danger signals for work places — Auditory danger signals."
---

# The standard that already answers "can I hear an alarm through hearing protection"

The framework the siren question belongs to. It exists, it is normative, and it explicitly
contemplates hearing protection.

## What it is

Second edition, dated **2003-11-01**, cancelling and technically revising ISO 7731:1986.
Prepared by ISO/TC 159 (Ergonomics), SC 5. It specifies design principles, ergonomic
requirements and test methods for auditory danger signals **in the signal reception area**,
and applies particularly where ambient noise is high.

It distinguishes three signal types by the response required: emergency evacuation signal
(leave immediately), emergency signal (urgent rescue or protection), warning signal
(preventative or preparatory action). ISO 8201 covers evacuation signals and ISO 11429
covers auditory and visual danger signals in more detail. It does **not** cover spoken
warnings — that is ISO 9921.

## The premise, in the standard's own introduction

Correctly designed signals reliably call attention to a hazard or dangerous situation
**even when hearing protection is worn**, without causing fright.

That sentence is the whole answer to the general form of the question. The standard's
position is not "hearing protection defeats alarms"; it is that an alarm which fails
through hearing protection is a badly designed alarm, and designing around protected
listeners is a normal requirement rather than an edge case.

## The audibility criteria

A signal is deemed clearly audible if:

- its A-weighted SPL exceeds the ambient noise by **15 dB or more** (clause 4.2.2.2), and
- its A-weighted SPL is **not lower than 65 dB** (clause 4.2.2.1);
- **or** its SPL in one or more octave bands exceeds the **effective masked threshold**.

These two together are described as *sufficient but not always necessary*: where the
signal's frequency or temporal structure clearly differs from the ambient noise, a lower
level may do. **Annex B is normative and is titled "Calculation of effective masked
threshold"** — so the standard provides the machinery, not just the rule of thumb.

## The hearing-protection clause

The signal shall be clearly audible, the effective masked threshold shall be distinctly
exceeded, and **where hearing protectors are worn, their attenuation shall be known and
introduced into the assessment**. The standard's definition of effective masked threshold
explicitly folds in "listening deficiencies", naming hearing protection alongside hearing
loss and other masking.

The practical reading: hearing protection does not disqualify you from hearing an alarm.
It shifts a number in a calculation that the standard already knows how to do.

## What this source does not support

- **It is a workplace and public-area standard.** It is not Israeli civil-defence
  regulation and has no authority over a national siren network. It is the right
  *framework* for the question, not the governing document — see
  [`israeli-siren-level-not-published.md`](israeli-siren-level-not-published.md).
- **It says nothing about sleeping listeners.** Every criterion here assumes an awake
  person in a reception area.
- One cited critique holds that the 15 dB figure does not match real listener behaviour:
  in a free-adjustment study, the level listeners chose as clearly audible without being
  frightening differed from the standard's prescription.

## Provenance

The standard's number, full title, second-edition date (2003-11-01), the superseded 1986
first edition, the TC 159/SC 5 committee attribution, the three-way signal-type table, the
ISO 8201 / 11429 / 9921 relationships, the normative Annex B on calculating the effective
masked threshold, and the introduction's statement about hearing protection were all
**confirmed 2026-08-12 by extracting text from the publicly downloadable ISO/iTeh preview
PDF** with `pdftotext -layout`. (Fetching that PDF through an ordinary web-fetch returns
raw binary; extracting locally is the route that works.)

The preview contains only front matter, contents and introduction. **The numeric criteria
in clauses 4.2.2.1 and 4.2.2.2 — the 65 dB floor and the 15 dB margin — were NOT in the
preview and are relayed from secondary summaries.** They are consistently reported across
several independent sources, including a signalling manufacturer's technical note, but the
clause text itself has not been read. Verify against the purchased standard before relying
on the exact figures.

The free-adjustment critique is a secondary summary and the study was not identified.
