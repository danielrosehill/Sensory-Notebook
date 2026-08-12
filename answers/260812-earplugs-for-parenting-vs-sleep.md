---
question: 260812-earplugs-for-parenting-vs-sleep.md
answered: 2026-08-12
sources:
  - sources/calderon-2016-child-cry-sound-levels.md
  - sources/hpd-warning-signal-audibility.md
  - sources/iso-7731-auditory-danger-signals.md
  - sources/sleep-arousal-thresholds-and-alarms.md
  - sources/hpd-overprotection-and-derating.md
  - sources/custom-earplug-attenuation-and-filters.md
  - sources/israeli-siren-level-not-published.md
confidence: medium
---

# Parenting versus sleep: the advice holds, but not for the reason you were given

> Not medical advice, and not safety certification. This is a literature summary written
> for a personal notebook by someone who is not a clinician or an acoustician. See the
> disclaimer in the [README](../README.md).

## Short answer

1. **The audiologist was right, and the reasoning is better than "reuse what you have".**
   For a normal-hearing listener, a hearing protector attenuates the signal *and* the
   background by roughly the same amount, so the **signal-to-noise ratio at the eardrum is
   preserved**. Earplugs do not selectively delete the baby. This is measured, not
   theoretical: across 80 listeners and seven warning signals, wearing hearing protection
   **improved** audibility for normal-hearing listeners.
2. **The two cases do differ — and sleep is the harder one.** Detecting a sound while awake
   and being woken by it are different thresholds, and the sleeping threshold is higher and
   individually unpredictable. So a plug you have validated against *sleep* is
   **conservative in the right direction** when used awake. The advice you were given errs
   safe.
3. **"Unsafe" cuts both ways, and the direction you weren't worried about is the real
   one.** **Overprotection** is a recognised occupational failure mode: too much
   attenuation degrades communication, causes missed signals, and — the self-defeating
   outcome — makes people take the protection off. The target is a **band, not a maximum**.
4. **The crying is loud enough to be worth protecting against.** Measured levels from
   crying children fall between **99 and 120 dB(A)**, and the authors of that study
   independently recommend earplugs for parents.
5. **The siren limb cannot be answered numerically.** The Israeli siren specification is
   not publicly published, in English or Hebrew. Anyone who gives you a dB figure for it is
   probably quoting a burglar alarm.

## Why preserved signal-to-noise is the whole answer

The intuition behind the original worry — that blocking sound might cut you off from the
baby — imports a model where an earplug is a switch. It is not. It is a subtraction applied
to everything arriving at the ear.

If the cry is 100 dB and the room is 40 dB, a 20 dB plug gives you an 80 dB cry in a 20 dB
room. The **60 dB gap between them is unchanged**. What decides whether you detect the cry
is not the absolute level but whether it clears your **masked threshold** — audibility
against the background — and that relationship survives attenuation nearly intact for a
normal-hearing ear. [`sources/hpd-warning-signal-audibility.md`](../sources/hpd-warning-signal-audibility.md)

This is why the railway study found HPDs *improving* audibility for normal-hearing
listeners rather than degrading it. It also explains where the argument fails: for
**hearing-impaired** listeners it reverses, because the attenuated signal can drop below an
already-elevated absolute threshold. The authors propose a usable criterion — security is
assured where average absolute threshold at 500/1000/2000 Hz in the better ear stays
**below 30 dB HL**. Your hearing tested completely normal
([`context/profile.md`](../context/profile.md)), which places you in the group the finding
applies to, not the exception.

## Why sleep is the harder case, not the easier one

This is the part that actually answers "are these different requirements".

Being woken is governed by the **auditory arousal threshold**, which is not the same
quantity as your waking detection threshold — and there is **no correlation between the
two**. A normal audiogram tells you nothing about how easily you wake. Roughly 55–70 dBA at
the pillow wakes most adults, regulations generally specify **75 dBA at the pillow** for
bedroom alarms, and even so **20% of adults in one study slept through a ten-minute
alarm**. [`sources/sleep-arousal-thresholds-and-alarms.md`](../sources/sleep-arousal-thresholds-and-alarms.md)

So the ordering is: **arousal threshold > waking detection threshold**. A plug specified so
that a baby can still wake you is, by construction, a plug through which you can hear a
baby while conscious. Going the other way — validating for parenting and assuming it covers
sleep — would be the unsafe direction, and is not what you were advised to do.

*(Speculation, flagged: nobody has measured arousal thresholds through earplugs. Subtracting
an attenuation figure from an arousal threshold is a reasonable inference and not a
finding. It is the weakest structural step in this answer.)*

## The direction of "unsafe" you were not asking about

You framed the request as *take the edge off without being unsafe*, meaning: don't block so
much that I miss something. The occupational literature has a name for exactly that
concern — **overprotection** — and treats it as a real failure mode rather than a
theoretical one: missed safety signals, degraded communication, feeling "out of touch",
slower responses, and protectors being removed in order to hear.
[`sources/hpd-overprotection-and-derating.md`](../sources/hpd-overprotection-and-derating.md)

Two consequences:

- **In moderate noise, 10–15 dB of real attenuation is typically all that is needed**, and
  guidance frames the goal as a protected level in the **70–80 dBA** region — a floor as
  well as a ceiling.
- **Labelled attenuation is not obtained attenuation.** OSHA halves the NRR; NIOSH subtracts
  25% for muffs, 50% for foam plugs and **70% for all other earplugs** — the category custom
  moulds fall into. Whatever number is on the box, assume you are getting substantially
  less, which incidentally makes over-blocking less likely than the box suggests.

So the audiologist declining to sell you a heavier pair is consistent with the hygiene
literature, not just commercially decent.

## The siren: what can and cannot be said

**Cannot:** there is no public specification for the sound-pressure level of the Home Front
Command siren network. Searched in English and Hebrew on 2026-08-12 across press, Hebrew
Wikipedia and civil-defence material, and it is not there. The 115 dB and 125 dB figures
that surface are **commercial burglar-alarm sounders** — a different product class
entirely. [`sources/israeli-siren-level-not-published.md`](../sources/israeli-siren-level-not-published.md)

**Can, structurally:** this exact problem is what **ISO 7731** exists for. Its introduction
states that correctly designed danger signals reliably call attention to a hazard **even
when hearing protection is worn**, and its normative Annex B gives the method for
calculating the **effective masked threshold** — a quantity whose definition explicitly
folds in hearing-protector attenuation as a known input. The standard's position is that a
protected listener is a normal design case, not an excluded one.
[`sources/iso-7731-auditory-danger-signals.md`](../sources/iso-7731-auditory-danger-signals.md)

**Can, factually about the system:** the Israeli alert is **multi-channel by design** —
public sirens, the Home Front Command app, the national emergency portal, radio and TV
interruption, and location-based SMS with loud audio notification, staged from 15–30
minutes ahead down to roughly 90 seconds before impact. The siren is one path among
several, and its own documentation concedes coverage is incomplete in some areas. That is a
description of how the system is built, not a recommendation about what to rely on.

**The honest bottom line on this limb:** the general acoustic argument says a
normal-hearing person wearing moderate attenuation is not thereby deaf to a loud
low-frequency external siren. But that is reasoning from principle with **the key input
missing**, and it is about a *sleeping* listener, where the evidence is weakest. This
notebook cannot responsibly turn that into an assurance, and does not.

## What would change this answer

- **~~Knowing which plugs you actually own.~~ Partially resolved 2026-08-12.** Visual
  inspection found **no filter bore**, indicating **solid** plugs — the **25–30 dB** end of
  the range rather than a filtered 9 or 15 dB. Two caveats that keep this from being
  settled: it is an inference from appearance rather than a specification, and NIOSH
  derates non-foam earplugs by **70%**, so delivered attenuation is materially below the
  nominal figure.
  [`sources/custom-earplug-attenuation-and-filters.md`](../sources/custom-earplug-attenuation-and-filters.md)
- **The siren specification**, if it can be obtained from the Standards Institution of
  Israel, the civil-defence regulations, or the 104 hotline.
- **Any study of arousal thresholds through hearing protection.** None was found. If one
  exists it replaces the weakest step in this answer.

## One thing worth knowing about the materials

Silicone versus acrylic is a **comfort, seal and durability** distinction. The **filter, not
the shell material, sets the attenuation curve** — no source found gave a direct acoustic
comparison between the two materials. So "the soft pair" and "the hard pair" are not
inherently different amounts of protection, which makes the advice to reuse the sleep pair
less surprising than it first sounded.

**And the original brief says the same thing.** Recorded 2026-08-12 in
[`recommendations/custom-moulded-earplugs.md`](../recommendations/custom-moulded-earplugs.md):
the request to the audiologist was for something usable at night *and* through a full
working day at **roughly the same attenuation**. The two pairs were therefore commissioned
as **equivalent in attenuation and different in wearing posture**, which is the whole
explanation for the later advice. There was never a stronger pair to be sold — reusing the
silicone one was not a compromise, it was the design.

*(That is Daniel's recollection of a conversation from about 2023, and his own phrasing
rather than a written specification. It corroborates the acoustic argument; it does not
independently confirm it.)*
