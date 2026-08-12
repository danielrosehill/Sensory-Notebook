# Scope

## Umbrella theme

Living with sensory sensitivity — what the research actually says about sensory
processing, and what has actually worked in practice.

## In scope

- Mechanisms: how sensory over- and under-responsivity are understood physiologically and
  psychologically; habituation, gating, arousal.
- Terminology and its standing: sensory processing disorder, sensory over-responsivity,
  misophonia, hyperacusis, and where each sits across DSM-5-TR, ICD-11 and the OT literature.
- Overlap with ADHD and with autism — what's established, what's correlational, what's contested.
- Interventions and their evidence base: environmental modification, occupational-therapy
  approaches, sound therapy, medication effects on sensory tolerance.
- Products and equipment: hearing protection, lighting, textiles, workspace design — including
  the measurable specs (attenuation curves, flicker, CRI) rather than marketing claims.
- Accommodation in practice: work, travel, home, family life.
- Cumulative load: whether sensory demand pools across modalities into one budget, what
  overflow looks like, and its downstream effects on mood, irritability, flow and
  well-being. Added 2026-08-12 — see the load model in [`profile.md`](profile.md).

## Out of scope

- Diagnosis, mine or anyone else's.
- Anything that reads as treatment advice for a reader. This now includes the mood and
  well-being material: describing how sensory load appears to affect mood is in scope,
  telling a reader what to do about their own mood is not.
- Other people's sensory experiences unless they have said they're happy to be written about.

## Modalities to track

Auditory, visual, tactile, olfactory, gustatory, vestibular, proprioceptive, interoceptive.
Use these as tags on questions so the notebook can be sliced by modality later.

## Open at the start

<!-- The first questions worth asking. Replace as they get asked and answered. -->

- [x] Which sensory constructs are actually recognised diagnostically, and which are
      clinical-community usage without formal standing?
      → Partly answered for the auditory ones, 2026-08-12. See
      [`sources/spd-diagnostic-status.md`](../sources/spd-diagnostic-status.md) and
      [`sources/decreased-sound-tolerance-terminology.md`](../sources/decreased-sound-tolerance-terminology.md).
      Short version: SPD is in neither DSM-5-TR nor ICD; misophonia is in neither;
      hyperacusis is in ICD-11 (AB7Y); sensory hyper/hyporeactivity has standing only
      inside autism (DSM-5-TR B4), never inside ADHD. Still open for the non-auditory
      modalities.
- [x] What does the evidence say about the ADHD–sensory-sensitivity relationship
      specifically, as distinct from the autism literature that dominates the field?
      → First pass 2026-08-12, auditory only:
      [`answers/260812-background-speech-and-focus.md`](../answers/260812-background-speech-and-focus.md).
- [ ] Does sensory tolerance change with stimulant medication, and in which direction?
      → Still open. Lead: secondary sources claim methylphenidate normalises some sensory
      hypersensitivities (noted in
      [`sources/bijlenga-2017-sensory-profiles-adult-adhd.md`](../sources/bijlenga-2017-sensory-profiles-adult-adhd.md)),
      unverified.

Added 2026-08-12, from the first answer:

- [ ] Does neural speech-tracking research show reduced attended-vs-ignored separation in
      ADHD? Would test the "can't tune out" account directly.
- [ ] Is there evidence separating interference-by-process from attentional capture in
      ADHD specifically? Decides whether effort is a usable lever at all.
- [ ] Early-sensory vs late-control: the sensory-gating findings and the load-theory
      findings conflict. Has anything since 2014 adjudicated?
- [ ] What is the measured STI at a typical open-plan desk, and what would it take to get
      below the 0.21 threshold where performance decline begins?

Added 2026-08-12, from the earplug recommendations:

- [ ] Is intermittent, unpredictable noise (honking, drilling) a different stressor from
      continuous noise at the same level, and is that difference measured? Would speak
      directly to the second auditory trigger in
      [`profile.md`](profile.md), which is described in terms of intrusion and loss of
      environmental control rather than volume.
- [ ] Does hearing protection that reduces the sound also reduce the loss-of-control
      feeling, or only the first of those? The recommendation records that the plugs made
      the honking survivable without restoring what had actually been taken.
- [x] Is the right earplug attenuation for a screaming baby the same as for sleep, or do
      the two want different curves? Includes the Israel-specific constraint: what
      attenuation still leaves a red-alert siren reliably audible, including asleep.
      → Answered 2026-08-12:
      [`answers/260812-earplugs-for-parenting-vs-sleep.md`](../answers/260812-earplugs-for-parenting-vs-sleep.md).
      Hearing protection preserves signal-to-noise, so it does not selectively remove the
      thing you wanted to hear; sleep is the harder threshold of the two, so validating for
      sleep errs safe. **The siren limb is unanswerable numerically** — the specification is
      not public.
- [x] What is the ideal attenuation for studying or working, does it scale with severity,
      and is there a point where blocking too much becomes its own problem? The companion
      to the above: that one is about safety ceilings, this one about the target.
      → Answered 2026-08-12, `confidence: low`:
      [`answers/260812-ideal-attenuation-for-focused-work.md`](../answers/260812-ideal-attenuation-for-focused-work.md).
      No published figure exists. The predictive variable is intelligibility, not level —
      which makes an earplug an indirect instrument for the speech trigger.

Added 2026-08-12, from those two answers:

- [x] Are the custom moulds solid or filtered, and if filtered, at what value?
      → Partially resolved 2026-08-12 by visual inspection: **no filter bore visible**, so
      **solid**, putting them at the 25–30 dB end rather than a filtered 9/15 dB. An
      inference from appearance, not a specification — the manufacturer figure would still
      settle it, and NIOSH derating means delivered attenuation is well below nominal.
      Also recorded: the original brief asked for one attenuation level usable both at
      night and through a full working day, so the two pairs were commissioned as
      equivalent in attenuation and different only in wearing posture.
- [ ] Has anyone measured **auditory arousal thresholds through hearing protection**? None
      found. It is the weakest structural step in the parenting/sleep answer.
- [ ] Has anyone measured attenuation against **cognitive performance**? None found. Would
      answer the focused-work question as originally posed.
- [ ] Does the right acoustic target differ by **severity of sensory over-responsivity**?
      Unstudied rather than contested — every study located used unselected adults.
- [ ] The Israeli siren specification, via the Standards Institution of Israel, the civil
      defence regulations, or Home Front Command's 104 line. Note `.gov.il` targets need an
      Israeli egress. See
      [`sources/israeli-siren-level-not-published.md`](../sources/israeli-siren-level-not-published.md).

Added 2026-08-12, from the sensory-load dictation. None of these has been asked yet — they
are leads, not open questions with work started on them. All of them bear on the load model
in [`profile.md`](profile.md), which is currently pure personal description with nothing
checked against it either way:

- [ ] **Is "sensory load" a measured construct anywhere, or a lay metaphor?** A finite
      cross-modal capacity that fills and spills over. Adjacent framings to check before
      concluding either way: allostatic load, cognitive load theory, ego depletion and its
      replication problems, spoon theory (patient-community origin, no formal standing), and
      the sensory-overload literature in autism. Expect the honest answer to be that the
      metaphor is widespread and the construct is not measured as stated — but check, rather
      than assuming, because an empty search result looks the same as a real absence.
- [ ] **Does load actually pool across modalities?** The testable version: does noise
      exposure measurably lower the same person's tolerance for thermal or tactile
      discomfort later the same day? This is the load model's central claim and the one most
      likely to be wrong.
- [ ] **Is irritability or anger an established endpoint of sensory overload in adults?**
      And how does it relate to the ADHD emotional-dysregulation literature, which is a
      large and separate body of work. Distinct from the question of whether the sensitivity
      itself is ADHD — that one is
      [`answers/260812-background-speech-and-focus.md`](../answers/260812-background-speech-and-focus.md).
- [ ] **Carryover: do environmental-stress effects outlast the exposure — in both
      directions?** The profile records persistence for bad stretches *and* for good ones,
      confirmed 2026-08-12. So the interesting question is not whether stress carries, which
      is well studied, but whether **recovery** carries the same way: is a restorative period
      a durable credit against future load, or does it only hold while it lasts? Leads:
      noise-annoyance research, which already measures effects persisting between exposures,
      and the recovery/restoration literature, which is the less obvious half and the one
      that would actually speak to the stabilising direction. Note the profile is explicit
      that symmetric in direction is not a claim of symmetric in magnitude.
- [ ] **Thermal discomfort and cognitive performance.** There is a substantial
      office-environment literature on temperature and productivity that this notebook has
      not touched at all, and it is the closest existing analogue to the acoustic work
      already logged in `sources/`.
- [ ] **Olfactory distraction and concentration — does odour valence predict disruption?**
      The profile records cooking as neutral and burning as disruptive. That would be the
      olfactory parallel to intelligibility-rather-than-level on the auditory side, which is
      a strong enough parallel to be suspicious of. Also worth separating: unpleasant smell
      versus smell that signals something is wrong.
