// Pandoc Typst template for Sensory Notebook consolidated exports.
//
// Used by scripts/build-pdf.sh via:
//   pandoc --pdf-engine=typst --template=templates/notebook.typ
//
// Pandoc's typst writer fills the dollar-delimited placeholders below.
// Keep the body, title, subtitle and date variables — everything else is
// ordinary Typst and safe to restyle. NOTE: a literal dollar sign anywhere
// in this file, including inside a comment, is parsed by pandoc as the start
// of a template variable and will fail the build. Write "dollar" in prose.
//
// The one design rule that carries meaning rather than taste: blockquotes
// are styled as provenance callouts, because consolidate.py uses a
// blockquote to mark whether an entry is research or personal experience.
// If you restyle quotes into something inconspicuous, that distinction
// stops being visible and the export breaks its own premise.

// --- helpers pandoc's typst writer expects the template to provide.
// Taken from `pandoc -D typst`. Without these, output containing a thematic
// break or a definition list fails with "unknown variable: horizontalrule".
#let horizontalrule = line(start: (25%, 0%), end: (75%, 0%))

#show terms: it => {
  it.children
    .map(child => [
      #strong[#child.term]
      #block(inset: (left: 1.5em, top: -0.4em))[#child.description]
    ])
    .join()
}

#set table(inset: 6pt, stroke: none)

#let notebook(
  title: none,
  subtitle: none,
  date: none,
  body,
) = {
  set document(title: if title != none { title } else { "Sensory Notebook" })

  set page(
    paper: "a4",
    margin: (top: 2.6cm, bottom: 2.4cm, x: 2.4cm),
    numbering: "1",
    number-align: center,
    footer: context {
      set text(size: 8pt, fill: luma(120))
      grid(
        columns: (1fr, auto, 1fr),
        align: (left, center, right),
        [Sensory Notebook],
        counter(page).display("1"),
        [Not medical advice],
      )
    },
  )

  set text(font: ("Libertinus Serif", "Linux Libertine", "DejaVu Serif"), size: 10.5pt, lang: "en")
  set par(justify: true, leading: 0.62em, spacing: 1.1em)

  show heading: set block(above: 1.5em, below: 0.85em)
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(
      width: 100%,
      inset: (bottom: 6pt),
      stroke: (bottom: 1pt + luma(30)),
      text(size: 19pt, weight: "bold", it.body),
    )
  }
  show heading.where(level: 2): set text(size: 14pt)
  show heading.where(level: 3): set text(size: 11.5pt)
  show heading.where(level: 4): set text(size: 10.5pt, style: "italic", weight: "regular")

  show link: set text(fill: rgb("#1a4f7a"))
  show raw: set text(font: ("DejaVu Sans Mono", "Liberation Mono"), size: 9pt)

  // Provenance callouts. See the note at the top of this file.
  show quote.where(block: true): it => block(
    width: 100%,
    fill: luma(244),
    stroke: (left: 2.5pt + luma(120)),
    inset: (x: 11pt, y: 9pt),
    radius: 2pt,
    text(size: 9.5pt, it.body),
  )

  show table: set text(size: 9.5pt)
  set table(stroke: 0.5pt + luma(180))

  // ---- title page
  v(6cm)
  align(center)[
    #text(size: 30pt, weight: "bold")[#title]
    #if subtitle != none {
      v(0.8em)
      text(size: 12.5pt, fill: luma(70), style: "italic")[#subtitle]
    }
    #v(2.2em)
    #if date != none { text(size: 10pt, fill: luma(110))[#date] }
  ]
  v(1fr)
  align(center)[
    #block(width: 78%)[
      #set text(size: 9pt, fill: luma(90))
      #set par(justify: false)
      A public research notebook and personal record. Research summaries cite their
      sources; personal experience is labelled as experience and is never presented
      as a finding. Nothing here is medical advice.
    ]
  ]
  pagebreak()

  // ---- contents
  outline(depth: 2, indent: auto)

  body
}

#show: doc => notebook(
  title: [$title$],
  subtitle: [$subtitle$],
  date: [$date$],
  doc,
)

$body$
