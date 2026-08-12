---
citation: "Institut National de Recherche et de Sécurité (INRS) and CNRS UMR5292. Experimental assessment of the effect of wearing hearing protectors on the audibility of railway warning signals for normal hearing and hearing impaired listeners. International Journal of Occupational Safety and Ergonomics. 2022;28(4):2385–2395."
type: journal-article
year: 2022
doi: 10.1080/10803548.2021.1991681
pmid: 34633273
url: https://pubmed.ncbi.nlm.nih.gov/34633273/
accessed: 2026-08-12
read: abstract-only
---

# Hearing protection and whether you can still hear the alarm

The counter-intuitive result that decides most of the "will earplugs stop me hearing X"
question.

## The principle

For a listener with **normal hearing**, a hearing protector attenuates the warning signal
and the background noise by roughly the same amount. The **signal-to-noise ratio at the
eardrum is therefore largely preserved**, and detection is governed by the *masked*
threshold — audibility against the background — rather than by the absolute threshold of
hearing.

The intuition that earplugs make you deaf to an alarm imports the wrong model. Attenuation
is subtractive across the board; it does not selectively remove the thing you wanted to
hear. Detection only fails when the attenuated signal drops below your absolute threshold,
which for a normal-hearing listener in a real room is a long way down.

## The measurement

Masked thresholds for **seven railway warning signals** were measured with and without
hearing protectors across **80 listeners**.

- **Wearing HPDs improved audibility for normal-hearing listeners.**
- It **tended to impede audibility for hearing-impaired listeners.**
- The size of the impediment depended greatly on the acoustical characteristics of the
  particular signal.
- Proposed criterion: setting aside one high-pitched signal the authors judged unsuitable
  as a warning signal, **security is assured where the listener's average absolute hearing
  threshold (mean of 500, 1000 and 2000 Hz, better ear) is below 30 dB HL.**

That last figure is the practically useful one: it converts "am I safe to wear these" into
a question an audiogram already answers.

## Where the preserved-SNR argument breaks down

Three documented limits, all from secondary sources rather than this paper:

1. **Non-flat attenuation.** The steeper the attenuation slope across frequency, the more
   the protected ear differs from the open ear, which degrades recognition even where
   detection survives. Germany's IFA codes protectors for this: **code W** — criteria for
   audibility of warning signals, informational sounds and speech intelligibility met,
   mean octave-band attenuation slope not exceeding **3.6 dB/octave**; **code X** — an
   extremely flat curve, slope **≤ 2 dB/octave**, suitable for people with impaired
   hearing and for musicians.
2. **Falling below absolute threshold.** Practical guidance cited in the occupational
   literature is that an alarm or speech message should sit **15–25 dB above the
   individual's masked threshold**, with higher values risking people removing the
   protector because it is too loud.
3. **Localisation, not detection.** Situational awareness degrades more than detection
   does. Knowing a sound happened and knowing where it came from are different, and HPDs
   damage the second more than the first.

## What this source does not support

- It is about **railway signals in industrial noise**, not domestic sirens, not infant
  crying, and not a sleeping listener. The mechanism generalises; the numbers do not.
- "HPDs improve audibility" is a statement about **masked thresholds in noise**. It does
  not mean earplugs help you hear things in a quiet room — in quiet, there is no masker to
  attenuate, and the argument does not apply.
- Nothing here addresses **arousal from sleep**, which is a different threshold entirely.
  See [`sleep-arousal-thresholds-and-alarms.md`](sleep-arousal-thresholds-and-alarms.md).

## Provenance

Journal, volume, issue, pages, year, DOI, PMID, the 80-listener sample, the seven signals,
the normal-vs-impaired direction of effect and the 30 dB HL criterion were confirmed
2026-08-12 from the PubMed abstract retrieved via NCBI E-utilities `efetch`.

**Author names are not confirmed.** The E-utilities plain-text record returned initials
only in a mangled form; the affiliations (INRS; CNRS UMR5292, Centre Hospitalier Le
Vinatier) came through intact and are used in the citation instead. **Resolve the author
list before republishing this citation anywhere.**

The three "where it breaks down" items, the IFA W/X codes and their dB/octave figures, and
the 15–25 dB-above-masked-threshold guidance are all **relayed from search-result
summaries** and were not verified against IFA or the primary sources. Treat them as
directionally right and numerically unchecked.
