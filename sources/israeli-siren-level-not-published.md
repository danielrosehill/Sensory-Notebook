---
citation: "Negative result. Searches for the Israeli Home Front Command (פיקוד העורף) public siren sound-pressure-level specification, English and Hebrew, 2026-08-12."
type: terminology-note
year: 2026
url: https://www.oref.org.il/
accessed: 2026-08-12
read: secondary-summary
---

# The Israeli siren level specification is not publicly documented

A deliberate record of something **not** found, so the next person does not repeat the
search. Recorded because an empty result looks identical to "there is no such thing", and
here the difference matters.

## What was searched

2026-08-12, English and Hebrew:

- English: Home Front Command red alert siren decibel level, civil defence siren
  specification, Israeli Standard siren installation.
- Hebrew: `תקן צופר אזעקה פיקוד העורף עוצמת דציבל התגוננות אזרחית` and variants.
- Sources reached: OSAC's Israel air-raid siren report, Home Front Command coverage in
  Israeli press, Hebrew Wikipedia `אזעקת מלחמה בישראל`, Kol-Zchut on siren noise limits,
  tzevaadom.co.il.

## What was found

**No dB figure for the national siren network, in either language.** The technical
specification of the siren array does not appear to be publicly published.

What *is* documented:

- The Red Alert siren is a **continuous ascending and descending tone**; the all-clear is a
  continuous single pitch.
- The country is divided into **polygons**; all sirens in a polygon sound when a projectile
  is tracked toward it. Polygons have been made smaller over time to reduce unnecessary
  alerting.
- Alerts are **multi-channel**: public sirens, the Home Front Command app, the national
  emergency portal, radio and TV interruption, and location-based SMS. A staged protocol
  includes a pre-alert 15–30 minutes ahead, an SMS around 10 minutes ahead with **loud
  audio notification**, and the siren itself about **90 seconds** before impact.
- Modern sirens are **electronic PA systems** — synthesised tone, amplified through
  loudspeakers — rather than the older mechanical/compressor units.
- Official guidance says only that you **should always be able to hear a siren**. No
  numeric threshold accompanies it.
- Coverage is explicitly incomplete: sirens are sited in populated areas, and on roads and
  away from settlements **they cannot be heard**, which is why radio interruption exists.

## A trap to avoid

Searches return **115 dB and 125 dB** figures that look authoritative and are not. Those
are specifications for **commercial and domestic burglar-alarm sounders** sold in Israel —
an entirely different class of product. Do not let those numbers migrate into an answer
about civil-defence sirens.

## Where the number would actually be

Not yet tried, and the obvious next steps:

- Israeli Civil Defence Law regulations — **תקנות ההתגוננות האזרחית**.
- **Standards Institution of Israel (מכון התקנים)** SI standards for protective
  installations.
- Home Front Command directly, via the **104** hotline or oref.org.il.

Note for whoever picks this up: `oref.org.il` and other `.gov.il` targets frequently refuse
non-Israeli traffic, so a plain web fetch is the wrong first move — route the request
through an Israeli egress.

## What follows for the notebook

The siren limb of
[`questions/260812-earplugs-for-parenting-vs-sleep.md`](../questions/260812-earplugs-for-parenting-vs-sleep.md)
**cannot be answered numerically** with public information. It can only be answered
structurally, through the ISO 7731 masked-threshold framework in
[`iso-7731-auditory-danger-signals.md`](iso-7731-auditory-danger-signals.md) — and any
answer must say plainly that the input figure is missing rather than substituting a
plausible one.

## Provenance

This file records the *absence* of a source. The positive facts about the alert system
(tone pattern, polygons, multi-channel alerting, timing, electronic sirens, incomplete
coverage) are **relayed from search-result summaries** of press coverage and Hebrew
Wikipedia and are **not** verified against Home Front Command's own publications. They are
included as context, not as specification.
