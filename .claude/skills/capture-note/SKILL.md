---
name: capture-note
description: Route dictated material into the right notebook files — profile, story, recommendation, or question — cleaning up transcription without inventing detail. Use when Daniel dictates experience, a product verdict, a question, or background, rather than asking for a task.
---

# Capture dictated material into the notebook

Daniel dictates. The material arrives half-formed, with transcription errors, often
mixing several different kinds of thing in one pass. This skill routes it.

Read `CLAUDE.md` § *Why the detail keeps arriving* first if it is not already in
context. The short version: the small details are the method, not padding, and
what he volunteers about himself is public by default and does not need clearing
item by item.

## Route by kind, and expect one dictation to contain several

| What arrived | Where it goes |
| --- | --- |
| A thing tried, with a verdict | `recommendations/<slug>.md`, one file per intervention |
| A sensitivity, trigger, or coping strategy | `context/profile.md` |
| How something was discovered, or changed over time | `context/story.md` |
| A question he wants researched | `questions/YYMMDD-<slug>.md` |
| A research lead he does not want chased yet | the open list in `context/scope.md` |

A single dictation about earplugs, on 2026-08-12, produced two recommendations, a
question, a profile trigger, three story beats and a scope entry. **Splitting is
normal; assume the material is multi-destination until you have checked.**

## Fix the transcription, preserve the intent

Dictation errors are usually recoverable from context: "attenuation" arriving as
"authentication", "Accannuation", "an authentication to". Fix them silently.

**Never smooth away a tension.** If he says the trigger is speech rather than
volume, and then says he reaches for earplugs when it is *loud enough*, both go in
with a FLAG saying it is unresolved. That contradiction is data about the thing
being described. Tidying it produces a cleaner file and a worse record.

## Never invent, always flag

The gaps are the norm. A date, a price, a brand, whether something worked — half
of these arrive missing. Do not infer them and do not leave them silently blank.

```markdown
<!--
FLAG — `since:` unknown. Bracketed by the previous apartment and the current move,
but not dated. Ask Daniel rather than inferring a year from the apartment history.
-->
```

Rules that have already been paid for:

- **Convert relative dates to absolute.** "Thirteen months ago" said on 2026-08-12
  becomes July 2025, and say in the file that it was derived.
- **Mark recalled figures as recalled.** "I wanna say three years ago" becomes
  `since: 2023-00` with a note that it is ±1 and not looked up, plus an instruction
  not to build anything on it.
- **Do not let one recollection look like two sources.** When two files inherit the
  same remembered date, say so in both.
- **Answering one question is not answering the neighbouring one.** He named the ANC
  headphones as Sony without saying whether they helped. The verdict flag stayed
  open, with a note that "he wears the customs now" is not evidence about the
  headphones.

## Write recommendations to the five-part shape

Set out in `recommendations/README.md`: the problem, what was tried, what happened,
**what it did not fix**, transferability.

The fourth is mandatory and is the reason the file is worth publishing. If there is
no recorded failure mode, either ask for one or write down that it is unrecorded —
do not ship the entry without the section.

## Cross-link in both directions

A new recommendation is not finished until the thing it came from points at it.
Profile triggers link to the interventions used for them; the story links to the
recommendations it produced; `scope.md` carries anything that became a research
question. A file nothing links to will not be found again.

Also update the index table in `recommendations/README.md`.

## Then commit

Message body should say what was learned, what was resolved, and what is still
flagged — not what the diff contains. Push; this repo is public and deployed by
being pushed.

## The failure mode this skill exists to prevent

**A detail mentioned in conversation and not written to a file is lost**, because
the repository is the memory. Replying "noted" and moving on is the one outcome
that defeats the entire exercise.
