# Recommendations

Things actually tried, in the real world, with a verdict. One file per intervention:
`recommendations/<slug>.md`.

These are **experience, not evidence**. Nothing here needs a citation, and nothing here
should be written so that it reads like a finding. If a recommendation happens to be
backed by research, cite the research and say that's what you're doing.

## Format

```yaml
---
kind: product | technique | accommodation | environment | routine
verdict: works | partial | abandoned | untested
since: YYYY-MM
cost: <approx, currency noted>   # omit if not applicable
modality: [auditory, tactile, ...]
---
```

Then, in the body:

1. **The problem** — the specific situation it was bought or adopted for.
2. **What was tried** — including the models, settings or variants that were rejected first.
3. **What happened** — over what period, and how consistently.
4. **What it did not fix** — mandatory. A recommendation with no stated failure mode isn't finished.
5. **Transferability** — what would have to be true for someone else to get the same result.

The fourth point is the one that makes this worth publishing. Every product review online
already covers the first three.

## Index

| Recommendation | Kind | Verdict | Modality |
| --- | --- | --- | --- |
| [Closing doors](closing-doors.md) | technique | works | auditory |
| [Custom moulded earplugs, made by an audiologist](custom-moulded-earplugs.md) | product | works | auditory |
| [Loop earplugs](loop-earplugs.md) | product | partial | auditory |
| [Earmuffs, worn over earplugs](earmuffs.md) | product | partial | auditory |

Listed in the order they get reached for, which is also cheapest first.

## What the entries have in common so far

Drawn from the verdicts above rather than from any literature, and worth stating because it
was not the expected answer:

**Every one of these was decided on comfort, not on how much sound it blocked.** Generic
earplugs lost because they were unwearable. Loop lost to the custom moulds on comfort.
Earmuffs lost on comfort. The custom moulds won by being inert enough to forget about. Not
one of these verdicts involved comparing attenuation figures, and none of the entries makes
a performance claim.

The practical form of that: an intervention you will actually use beats a better one you
will not, and hearing protection can become its own sensory problem — which makes "does it
stop bothering me after five minutes" the specification that matters. What the *right*
level of attenuation would even be is an open question, not a settled one:
[`questions/260812-ideal-attenuation-for-focused-work.md`](../questions/260812-ideal-attenuation-for-focused-work.md).
