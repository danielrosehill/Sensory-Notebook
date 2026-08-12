---
question: 260812-ideal-attenuation-for-focused-work.md
answered: 2026-08-12
sources:
  - sources/hpd-cognitive-performance.md
  - sources/iso-3382-3-distraction-and-privacy-distance.md
  - sources/hongisto-haapakangas-sti-performance.md
  - sources/hpd-overprotection-and-derating.md
  - sources/custom-earplug-attenuation-and-filters.md
  - sources/hpd-warning-signal-audibility.md
confidence: low
---

# Ideal attenuation for focused work: the number does not exist, and the question is aimed slightly wrong

> Not medical advice. A literature summary for a personal notebook, written by someone who
> is not a clinician or an acoustician. See the disclaimer in the [README](../README.md).

## Short answer

1. **There is no published ideal attenuation figure for concentration.** Not "it is
   disputed" — it has not been established. No study found measured attenuation against
   cognitive performance. The confident numbers online come from earplug manufacturers.
2. **More is not better, and that part is well supported.** **Overprotection** is a
   recognised failure mode with a stated target *band* rather than a maximum. Hearing
   protection has an optimum.
3. **The variable that predicts performance loss is intelligibility, not level** — which
   means an earplug is a slightly indirect instrument for the problem in your profile.
4. **Whether it scales with severity is unstudied.** Every study found used unselected
   adults. The question is not contested; it is unasked.
5. **Yes, there is a cost to over-blocking** — increased listening effort, and one small
   study found worse mood and higher anxiety while occluded. But there is also an
   **acclimatisation effect**, so first impressions understate a plug.
6. **The flatness of the curve probably matters more than the number on the box.**

## Why the number does not exist

The honest state of the evidence, and the reason this answer carries `confidence: low`
despite being fairly definite:

- Research on hearing-protection devices found **all tested HPDs degraded performance on
  most tasks** versus the open ear, specifically by **increasing listening effort** —
  cognitive resources spent on hearing are not available for the task. That is measured in
  conditions where you still need to monitor sound; in silent solo work it should largely
  not arise, but that boundary is reasoned, not tested.
- One pilot study — **thirty adults, two hours** — found visual attention **improved**
  during occlusion and stayed elevated afterwards, while **state anxiety rose and mood
  fell**. The same review notes prior studies were **inconsistent**, some finding nothing.
- Almost everything else asserting that earplugs aid concentration is **manufacturer
  content** — Loop, CURVD, Snugs, Hearprotek. It leans on the solid *noise impairs
  cognition* literature and then makes an untested leap to *therefore earplugs improve
  productivity*.

[`sources/hpd-cognitive-performance.md`](../sources/hpd-cognitive-performance.md)

This notebook carries a Loop recommendation. That recommendation stands on its own terms —
it records what happened when you used them. It is not evidence, and the company's
marketing is not evidence either, and keeping those apart is the point of the repository.

## The question is aimed slightly wrong, and that is the useful finding

The whole quantitative apparatus for background speech and work performance is built on
**STI — the Speech Transmission Index**, not on decibels. What predicts performance loss is
**how intelligible** the speech is, not how loud. Performance decline begins around
**STI ≈ 0.21**, and where speech is audible at all its effect relates more to
intelligibility than to level.
[`sources/hongisto-haapakangas-sti-performance.md`](../sources/hongisto-haapakangas-sti-performance.md)

ISO 3382-3 fixes two thresholds: **distraction distance** at STI 0.50 and **privacy
distance** at STI 0.20, where speech falls under 30% word intelligibility. The graded
experiments cluster low — a cut-off near 0.23, performance unaffected between 0.00 and
0.30, effort required to resist distraction from about 0.26 upward. So the target is
**around 0.2, not 0.5**.
[`sources/iso-3382-3-distraction-and-privacy-distance.md`](../sources/iso-3382-3-distraction-and-privacy-distance.md)

**The catch: STI is a property of a room and a listening position, not of an earplug.**
There is no defined way to convert an attenuation figure into an STI change, so
"aim for STI 0.2, therefore buy an N dB plug" is a step the literature does not license.

This is why your own profile note reads the way it does. If intelligibility rather than
volume is the operative variable, then a plug — which lowers level roughly uniformly and
leaves the speech/background ratio intact — is attacking the problem side-on. The levers
that actually move STI are **absorption, screens, distance, and masking sound**, and
masking *raises* total level while *lowering* intelligibility. Your instinct to close a door
([`recommendations/closing-doors.md`](../recommendations/closing-doors.md)) is, in these
terms, a better-targeted intervention than the earplugs are.

*(Speculation, flagged: this reasoning also predicts that an earplug should help less with
the speech-while-concentrating trigger than with the honking-at-night one — which is
exactly the distinction your profile draws for independent reasons. Suggestive, not
demonstrated, and the notebook does not currently record whether the plugs help with the
speech case at all.)*

## Is more blocking better? No, and here is the shape of the ceiling

**Overprotection** is a documented occupational failure mode: degraded communication,
missed signals, feeling "out of touch", slower response, and protectors removed so people
can hear. In moderate noise **10–15 dB of real attenuation is typically sufficient**, with
target protected levels quoted in the **70–80 dBA** region — a floor as well as a ceiling.
[`sources/hpd-overprotection-and-derating.md`](../sources/hpd-overprotection-and-derating.md)

Against that, **labelled attenuation is not obtained attenuation**. NIOSH derates
non-foam earplugs by **70%**. So the practical risk of accidentally over-blocking with an
off-the-shelf number is lower than the box implies — and the practical value of a *fitted*
plug is that its delivered attenuation is more predictable, not that it is higher.

## Does the answer differ if you are more affected?

**Unstudied.** Every study located used unselected adults; none stratified by sensory
over-responsivity, and none looked at ADHD populations.

What is documented is that **individual susceptibility to the irrelevant speech effect
varies**, and that variation is measured, not anecdotal — already catalogued in the
existing STI source. That is the empirical hook for saying a population-average acoustic
target under-protects some people. It supports *"the right target is not the same for
everyone"*. It does not tell you which way, or by how much, and it is about room acoustics
rather than hearing protection.

So the second limb of the question is a genuine open research question, and worth stating
as one rather than answering thinly.

## Is there a point where blocking too much is its own problem?

Three real effects, none quantified against a threshold:

- **Listening effort**, above — a cost paid whenever you still need to hear something.
- **Mood and anxiety**, from the thirty-person pilot. One small study; recorded because it
  is the only signal found in either direction, not because it is solid.
- **Flatness of the curve.** The steeper the attenuation slope across frequency, the more
  the protected ear differs from the open ear. Germany's IFA codes protectors for this:
  **code W** requires a mean slope no greater than **3.6 dB/octave**, **code X** an
  extremely flat **≤ 2 dB/octave**. Foam is the bad case — it kills highs far harder than
  lows, which is why everything sounds muffled through it.
  [`sources/hpd-warning-signal-audibility.md`](../sources/hpd-warning-signal-audibility.md)

**Practical reading: choose flat over strong.** A 15 dB flat filter and a 25 dB steep plug
are not two points on one scale; the first leaves the world sounding like itself, quieter.
Filters around **15 dB are reported to be the flattest**, and a solid unfiltered custom plug
is **25–30 dB** — the blunt end of the range.
[`sources/custom-earplug-attenuation-and-filters.md`](../sources/custom-earplug-attenuation-and-filters.md)

## The finding that vindicates how this notebook already chose

Every recommendation in this repository was decided on **comfort**, with no attenuation
figure compared — noted in
[`recommendations/README.md`](../recommendations/README.md) before any of this research was
done. Two results say that was not a lazy proxy:

- **Overprotection's characteristic outcome is people removing the protection.** Wearability
  is not a soft criterion; it is the one the safety literature keeps arriving at.
- **Acclimatisation is documented**: pianists' reported degradation dropped between a first
  and second performance. So judging a plug on first wear systematically underrates it —
  which is worth knowing before rejecting one, and is the closest thing to actionable advice
  this answer contains.

## What would close the gap

- **Which filter, if any, is in the custom plugs.** Still unrecorded, still the single most
  useful missing fact.
- **Any study measuring attenuation against cognitive performance.** None found; if it
  exists, it answers the question as posed.
- **Anything stratifying acoustic targets by sensory over-responsivity.** Would answer limb
  two, which is currently unanswerable rather than merely unanswered.
