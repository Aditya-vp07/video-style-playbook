# Video Style Playbook

A style-reference + recipe library for **vertical (9:16) motion-graphics
editing** — built by reverse-engineering real viral reels and YouTube
videos frame-by-frame.

This is the *"which style should I use, and how"* companion repo. It
doesn't build videos; it tells you exactly which visual language to
speak and gives you copy-paste specs to build it.

## Who this is for

Aditya's main use case: **end-to-end talking-head → motion-graphics
fusion videos** — he sends a talking-head video, the pipeline returns a
finished reel with animated panels, networks, slams, and captions baked
in. This repo is the style + technique reference that pipeline builds
from: *which visual language to speak* (`STYLES.md`, `INTAKE.md`) and
*how to engineer each motion* (`techniques/`).

## What's inside

- **`STYLES.md`** — the catalog: 6 styles with palette, type system,
  caption rules, motion grammar, layout, safe zones, and *why to use
  each one*.
- **`techniques/`** — the implementation track: code-ready playbooks
  for pro-grade motion on our ffmpeg/Python stack — `camera.md`
  (buttery GSAP-grade virtual camera), `network-graph.md`
  (investigation-style relationship mapping), `fusion-layouts.md`
  (talking-head + graphics grammar), `ai-clip-planning.md`
  (prompt discipline for generated clips), and `ANALYSIS-PROTOCOL.md`
  (the forensic DNA-capture method, repeatable for new videos).
- **`INTAKE.md`** — the "what are you expecting?" questionnaire: answer
  5 questions → get a style recommendation + fallback mixes.
- **`RECIPES.md`** — concrete build recipes with copy-paste params
  (hexes, px values @1080×1920, timing, easing).
- **`examples/<style>/`** — 5 image mockup frames per style, 5
  different scenarios each: (1) hook/title card, (2) talking-head
  caption beat, (3) stat/data panel, (4) product/comparison panel,
  (5) end card/CTA.
- **`docs/`** — interactive style-guide website (open `docs/index.html`):
  style gallery, per-style pages with click-to-copy hexes + CSS
  snippets, and a question-driven style chooser.

## The 6 styles

| # | Style | Vibe | Best for |
|---|---|---|---|
| 1 | **Warm Editorial** | calm, premium, credible | education, AI/tech explainers |
| 2 | **Dark Sticker Collage** | viral, playful, maximal | tutorials, AI-tool demos |
| 3 | **Neon Product Ad** | hype, no-speaker ad | app promos, before→after selling |
| 4 | **Dark Fintech** | money, premium dark | finance explainers, fintech |
| 5 | **Warm Ed-tech** | friendly, teaching | course promos, learning apps |
| 6 | **Mono Kinetic Type** | type-as-content, no speaker | motivational, editor portfolios |

See `STYLES.md` for the full specs.

## Quick start

1. Not sure which style? → answer the 5 questions in `INTAKE.md`
   (or use the chooser in the `docs/` site).
2. Read the style's section in `STYLES.md`.
3. Look at the 5 scenario images in `examples/<style>/`.
4. Copy the chip/card/title recipes from `RECIPES.md`.

## Source notes

Styles were derived from frame-by-frame analysis of 10 Instagram reels
and 5 YouTube videos (downloaded as MP4, inspected via ffmpeg frame
extraction). Colors are eyeball estimates unless noted as sampled;
font names are style matches. The single biggest lesson: **the best
reference video won on restraint, not effects** — one serif, one
grotesque, three chip colors, and motion synced to word timestamps.

## License

MIT — see `LICENSE`.
