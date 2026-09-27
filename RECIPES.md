# Recipes — copy-paste build specs

Every recipe below is given with concrete params @1080×1920. Copy the
hexes, px values, and timing straight into your build.

---

## 1. Caption chip system (Warm Editorial)

Three flavors, used on an emphasis rhythm (pill = emphasis, no-pill =
filler):

| Flavor | Fill | Text | Use |
|---|---|---|---|
| Butter-yellow pill | `#F2C14E` | dark navy `#1E2A44` | keyword emphasis |
| Charcoal pill | `#22262B` @85% | white | secondary emphasis |
| Plain | none (soft drop shadow) | white sans | filler lines |

- Size: ~214×72px, full pill (radius = ½ height), 34px geometric sans,
  1–3 words.
- Position: centered x≈540; y≈1390–1470 (talking head),
  y≈1158 (diagram boundary). Nothing below y≈1570.
- Swap: phrase-level, 150ms pop (scale 0.9→1). **No karaoke.**

CSS:

```css
.chip-yellow {
  background: #F2C14E; color: #1E2A44;
  border-radius: 999px; padding: 18px 36px;
  font: 600 34px/1 "Inter", sans-serif;
}
.chip-dark {
  background: rgba(34,38,43,.85); color: #fff;
  border-radius: 999px; padding: 18px 36px;
  font: 600 34px/1 "Inter", sans-serif;
}
.chip-plain { color: #fff; font: 600 34px/1.3 "Inter", sans-serif;
  text-shadow: 0 2px 12px rgba(0,0,0,.45); }
```

## 2. Dark-pill keyword captions (Warm Ed-tech)

- Fill `#2A2A2A` @80%, white sans, centered y≈1390–1470, ≤2 lines.
- Gray pill labels `#8A8A8A` + white text under cards (y≈1360–1440)
  for meta-labels ("made / easier / adapts / tests / podcasts").

## 3. Karaoke captions (maximal energy)

- White bold rounded sans ~40px + soft dark drop shadow (no chip).
- Active word: orange `#F2994A`.
- Band y≈1500–1640, ≤2 lines, true word-level sync.

## 4. Title entrance — blur-resolve (Warm Editorial)

- Hero lockup: blur→sharp staggered word resolve, ~1.5–2s total,
  stagger ~0.15s/word.
- Single-word beats: <0.5s sharp pop.
- **Camera zoom fires on the same timestamps** as the title
  (pullback on open, push-ins on key beats).
- Hero sizes: italic serif ~150–170px, secondary ~80px, kicker ~55px.

CSS keyframe sketch:

```css
@keyframes blur-resolve {
  from { filter: blur(26px); opacity: 0; transform: scale(.96); }
  to   { filter: blur(0);    opacity: 1; transform: scale(1); }
}
.title-word { animation: blur-resolve 1.8s cubic-bezier(.16,1,.3,1) both; }
```

## 5. Track-spread — letter-spacing performs meaning

- On extent words from the cue sheet ("sample", "a spectrum",
  "everything"), animate letter-spacing from 0 → ~40px over the
  word's duration.
- Cheap, high-signal: the type *acts out* the meaning.

## 6. Headline couplet (minimal Swiss)

- Line 1: black grotesque ~110–140px ("Aren't quiet.")
- Line 2: green italic serif counterpoint ("Aren't louder.")
  — always the second line. Lime `#30E040` on white `#FFFFFF`.
- Ruthless whitespace: 60–80% empty frame.

## 7. Dashed selection-box motif (Mono Kinetic Type)

- 1.5px dashed black bounding box around keywords.
- ~10px square anchor handles at corners + midpoints.
- Arrow cursor visibly drags the box; text types in letter-by-letter.
- Base: paper `#F5F5F3` + faint dot grid (`#D8D8D8`, 1.5px dots,
  28px spacing); blurred black blobs drifting at edges.

## 8. Glow-card panel system (Dark Sticker Collage)

- Panel: `#10120f`, 1.5px ice-cyan stroke (`#a5f2ff` @80%) +
  outer blur glow, faint grid background.
- Pin uppercase cyan labels around the card: "CLIP / CAPTIONS /
  ANIMATIONS" (letterspaced, small, on dark rounded chips).
- Floating 9:16 demo card centered.

CSS:

```css
.glow-card {
  background: #10120f; border: 1.5px solid rgba(165,242,255,.8);
  border-radius: 24px; box-shadow: 0 0 48px rgba(165,242,255,.25);
}
.cap-label { color: #a5f2ff; font: 700 22px/1 "Inter", sans-serif;
  letter-spacing: .22em; background: rgba(165,242,255,.08);
  border-radius: 999px; padding: 10px 18px; }
```

## 9. Emphasis pops (Dark Sticker Collage)

- Magenta/purple `#c026d3`-ish, rounded bold display text, 2–4 words
  max, placed beside the speaker.
- Pop in on beat, out hard (no linger).

## 10. Paper-cutout sticker layer

- B&W cutouts: pointing hands, torn-edge portraits, thought bubbles.
- **Contrast rule:** cutouts sit on light cards (`#e7e6e1` /
  `#f2f2f2`), never directly on the dark background.

## 11. Neon keyword glow (Neon Product Ad)

- White text + magenta outer glow (~20px blur `#FF3FD4`).
- Content panel `#120C26`, full-bleed y≈290–1130.
- Beats switch with hard 0.3–0.5s leftward wipes, no fades.
- Static chrome: header wordmark (white fill, 10–14px black stroke),
  bottom contrast chips `#140F22` radius ~28px ("4 HOURS" vs
  "10 MINUTES", white condensed ~90px, slight vertical stagger).

## 12. Fintech glass cards (Dark Fintech)

- `#101410` @90%, 1px `rgba(255,255,255,.25)` border, radius 28px.
- Bold white grotesque ~44px; green `$` `#2ECC71` inline.
- Canvas `#0A0E0A` + green radial glow `#1DB954` @25% at bottom.
- Speaker in rounded-arch portal (radius ~120px, top y≈1024,
  x 90–990); card zone y≈540–945.

## 13. Ed-tech app cards (Warm Ed-tech)

- White cards, radius 36px, thin orange `#E8734A` borders, green
  waveform bars, small illustrations; scroll vertically full-bleed.
- Cream bg `#FAF5EC`.
- Keyword slams: bold black ~90px on cream ("File", "Book",
  "Paper") with 3D renders.
- Ghost serif: huge white semi-transparent serif (~120px) behind
  the speaker for depth.

## 14. Diagram act (Warm Editorial)

- Full-bleed cream scene `#F8F7F2` + subtle paper noise.
- Rounded cards with bar charts (bars grow on beat).
- Stepper pills on top ("recompute → sample → append & repeat",
  active = dark pill).
- Slider devices: "ROLL THE DICE — SEGMENT WIDTH = PROBABILITY"
  with black knob; dotted trajectories draw; scene pans horizontally.

## 15. Split modes for talking head

- **45/55 split:** graphic panel top 0–48% (paper texture `#F4EFE4`
  + construction guide circles), speaker bottom 52–100%, black pill
  caption ON the seam (y≈920–1050, white bold ~52px, 2-line max).
- **PiP mode:** graphic full-frame, speaker cutout bottom-right
  (x 0.55–1.0, y 0.62–1.0, no border), free-floating shadowed caption,
  no pill. *Different caption style per mode — bake it in.*

## 16. Black breath frames (pacing engine)

- Full-black interstitials, 2–4s, carrying only a glowing
  micro-caption. Separates scenes, resets attention.

## 17. Halftone grain unification

- ~3px dot grain @0.05 opacity over ALL white areas + 2px ink
  wire/string lines crossing compositions. One texture = one world.

## 18. Show-your-work beats

- Literally display the AI prompt, tool UI, or screen-record as
  content (dark cards `#0B0B0C`, small gray monospace text).
- Credibility device, not watermark.

## 19. Before/after split frame

- Orange-badged "styled" panel vs dark-badged "original" panel,
  "VS" divider. Two vertical 9:16 panels inside frame.
- Golden-yellow hooks `#f5c518`-ish on dark navy `#04101c`.
- Reuse as a *deliverable device*: raw clip vs treated pass.

## 20. Chapter cards (long-form segmentation)

- Pure black, white grotesque, left-aligned, numbered
  ("1. Motion Graphics Promo"), generous left margin.

## 21. Line-by-line bullet builds

- Small grotesque list on light card, one line per beat.
  Cheap, readable, high-retention.

## 22. Sponsor interstitial

- Solid color field (terracotta `#D06D58`), italic serif sponsor
  line, two tilted screenshot cards, navy pill punchline. ~5s.

## 23. Kanglish hook — 3D gold native-script word

- 3D gold/chrome Kannada (or Devanagari) keyword + drop shadow,
  floating in the forehead band of the 9:16 frame.
- Works with ANY of the 6 styles as a hook device.
- Narration in Kanglish; the Kannada keyword lands as a visual
  punch while the explanation continues in voice.

## 24. Warm-grade preset (Warm Editorial)

```
cream diagrams   #F8F7F2
butter accents   #F2C14E
ink text         #1E1E1E
scrim            black 15% over top 300px (title legibility)
grain            mild film grain
white balance    warm
```

## Safe zones @1080×1920 (all styles)

- Titles: y 170–450 (below IG progress bar)
- Captions/chips: y 1100–1480 (talking head), ~1158 diagram
  boundary; nothing below y≈1570 (IG caption zone)
- Key content within x 90–990 (clear of right action rail)
