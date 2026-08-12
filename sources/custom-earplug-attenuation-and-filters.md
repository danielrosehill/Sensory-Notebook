---
citation: "Synthesis of manufacturer and clinical technical material on custom-moulded hearing protection, incl. Minuendo, 'Custom Molded Earplugs — The Myths and Truths'; Honeywell Safety, 'So, What's the Story with Custom-Molded Earplugs?'; MEE Audio custom earplug filter specifications."
type: terminology-note
year: 2026
url: https://www.minuendo.com/post/custom-molded-earplugs-the-myths-and-truths
accessed: 2026-08-12
read: secondary-summary
---

# What custom moulded plugs actually attenuate, and what sets the curve

Background for [`recommendations/custom-moulded-earplugs.md`](../recommendations/custom-moulded-earplugs.md),
which was written entirely on comfort and contains no acoustic data.

## The numbers

- A **solid** custom plug — no filter, no bore — gives roughly **25–30 dB**.
- **Filtered** custom plugs have a bore drilled through the plug holding a filter that
  brings attenuation down to a chosen value. Common filter values are **9, 15 and 25 dB**.
- Filters around **15 dB are generally the flattest** across frequency.
- A published curve for one 25 dB filter shows it is not perfectly flat: **−25 dB from
  125 Hz to 2 kHz, −20 dB from 3–6 kHz, −25 dB at 8 kHz.**

## The filter sets the curve, not the shell material

The important structural point, and the one that answers the silicone-versus-acrylic
question directly: the distinction between soft silicone and hard acrylic is normally about
**comfort and seal versus durability and hygiene**, not about frequency response. **The
filter, not the shell material, determines the attenuation curve.** No source found gave a
direct acoustic comparison between the two materials.

Which means: two custom plugs in different materials with the same filter should attenuate
about the same, and a solid plug of either material is a solid plug.

## Why flat response is the selling point

Conventional plugs — foam especially — block high frequencies far more aggressively than
low ones, which is why speech and music sound muffled and bass-heavy through them. Flat
filters reduce levels evenly so the spectrum arriving at the ear resembles the one that
left the source, just quieter. This is the same property that IFA codes W and X describe
for warning-signal audibility, in
[`hpd-warning-signal-audibility.md`](hpd-warning-signal-audibility.md).

## The counterpoint worth keeping

Custom is not automatically better attenuating. The literature reports custom and
non-custom as **largely comparable**, with custom having **less variability** rather than
more attenuation, and non-custom plugs having an advantage in sealing at bass frequencies:

- Custom moulded plugs showed a standard deviation of **6.4 dB at 250 Hz** for untrained
  users.
- **Deeply inserted foam attenuated more at all frequencies** than an optimally fitted
  custom silicone plug, for trained users.

This is described as well established in the literature and under-communicated to
consumers. It is consistent with what this notebook already concluded from the other
direction: the case for custom moulds is **wearability**, not performance.

## What this source does not support

- **These are manufacturer and vendor figures.** The 25–30 dB solid-plug range and the
  9/15/25 dB filter values are product specifications, not independent measurements, and
  are subject to the same lab-versus-field gap as any NRR — see
  [`hpd-overprotection-and-derating.md`](hpd-overprotection-and-derating.md).
- **These are not measurements of the specific plugs in the recommendation.** Visual
  inspection on 2026-08-12 found **no filter bore**, which points to solid plugs and
  therefore the **25–30 dB** end of the range — but that is an inference from appearance,
  not a specification, and no manufacturer documentation has been seen. See
  [`../recommendations/custom-moulded-earplugs.md`](../recommendations/custom-moulded-earplugs.md).
  Remember also that NIOSH derates non-foam earplugs by 70%, so whatever the nominal
  figure, delivered attenuation is materially lower.

## Provenance

Entirely **relayed from search-result summaries** of vendor and manufacturer pages. **No
primary measurement report was opened** — not ACS, not Etymotic, not Elacin, not Westone,
whose test reports are where the real curves live.

The 6.4 dB standard deviation at 250 Hz and the deeply-inserted-foam comparison are
attributed to studies the summaries did not name; those attributions are **unverified** and
are the least reliable claims in the file. The material-versus-filter point is stated
consistently across independent vendors, including ones selling both materials, which is
weak but real evidence that it is not a sales line.
