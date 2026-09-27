# Style Catalog — 6 vertical motion-graphics styles

Every style below was reverse-engineered frame-by-frame from real viral
reels and YouTube videos (see the `examples/` folders for flat-design
mockup frames of each style in 5 scenarios). All measurements assume a
**1080×1920** vertical canvas unless noted otherwise.

Quick reference:

| Style | Slug | Vibe | Canvas | Accent | Speaker? |
|---|---|---|---|---|---|
| Warm Editorial | `warm-editorial` | calm, credible, premium | cream `#F8F7F2` | butter-yellow `#F2C14E` | yes |
| Dark Sticker Collage | `dark-sticker-collage` | viral, playful, maximal | olive-black `#10120f` | ice-cyan `#a5f2ff` | yes |
| Neon Product Ad | `neon-product-ad` | hype, no-speaker ad | dark `#120C26` | magenta `#FF3FD4` | no |
| Dark Fintech | `dark-fintech` | money, premium dark | near-black `#0A0E0A` | green `#1DB954` | yes |
| Warm Ed-tech | `warm-edtech` | friendly, teaching | cream `#FAF5EC` | orange `#E8734A` | yes |
| Mono Kinetic Type | `mono-kinetic` | type-as-content | paper `#F5F5F3` | ink only | no |

---

## 1. Warm Editorial — `warm-editorial`

**Source:** "How does AI work? episode 01" (best reference — full 118.7s
timestamped beat map exists in the analysis notes).

### Palette
- Cream background `#F8F7F2` (diagram scenes: flat cream + subtle paper noise)
- Ink text `#1E1E1E`
- Butter-yellow chip `#F2C14E` + dark navy text `#1E2A44`
- Charcoal chip `#22262B` @85% opacity + white text
- Terracotta `#D06D58` (interstitials/sponsor beats)
- Electric blue `#2E5BFF` (credential callouts only)

### Type system
- **Display:** high-contrast Didone italic serif (Cormorant-like), white
  with soft shadow. Hero ~150–170px, secondary ~80px, kicker ~55px.
  Pattern: italic serif line / BIG grotesque line (e.g. "How does" italic
  80px / "AI work?" 160px / "episode 01" italic 55px).
- **Brand beats:** bold grotesque ~110px, tight tracking
  (e.g. "ANTHROPIC", "✳ Claude" with coral `#E0653A` asterisk).
- **Chips:** medium-weight geometric sans ~34px, 1–3 words.

### Caption system
Three flavors, used on an **emphasis rhythm** — pill = emphasis,
no-pill = filler:
1. Butter-yellow pill `#F2C14E` + navy text — keyword emphasis,
   especially in diagram acts.
2. Charcoal pill `#22262B`@85% + white text.
3. Plain white sans + soft drop shadow, no pill.

Shape: full pill, radius = ½ chip height (~214×72px @1080×1920).
Chips swap phrase-by-phrase with a fast 150ms pop (scale 0.9→1).
**No karaoke** — phrase swaps, not word highlighting.

### Motion grammar
- Title entrances: **blur→sharp staggered word resolve**
  (~1.5–2s hero lockups, <0.5s single-word beats).
- Camera zoom fires **on the same word timestamps** as the title
  (pullback ~4.2s with title; push-ins at ~28.5s / 60.5s / 114.5s).
- Letter-spacing animates wide on extent words ("Sa mp le" when
  explaining tokens) — *text performs meaning*.
- Diagram acts: bars grow, dotted trajectories draw, scene pans
  horizontally; stepper pills on top (active = dark pill).
- Hard cuts; gentle warm grade (soft daylight, shallow DOF,
  ~15% black scrim over top 300px for title legibility, mild grain).

### Layout rules
- Titles: y 170–450 (below IG progress bar), centered; list variant
  top-left x≈225.
- Chips: centered x≈540, y≈1390–1470 (talking head), y≈1158
  (diagram/speaker boundary). Nothing below y≈1570.
- Key content within x 90–990 (clear of right action rail).
- Floating graphic cards: cream `#FBFAF7`, radius ~28px, soft shadow,
  slide in from left (scale 0.9→1); speaker ducks to bottom ~45%.

### Why use it
The calm-authority premium explainer. Best for **education, AI/tech
explainers, product walkthroughs with credibility**. Feels like a
well-designed book, not an ad. Works brilliantly with a speaker who has a
warm room/bookshelf background. Lowest risk of looking cheap — restraint
is the whole aesthetic.

---

## 2. Dark Sticker Collage — `dark-sticker-collage`

**Source:** "How to Edit a Viral Talking-Head Using ONLY AI (2026 Style)"
by Joseph | Video Editing — the 2026 viral talking-head look.

### Palette
- Near-black olive background `#10120f` + faint grid
- Ice-cyan glow `#a5f2ff` (core), `#83e0ef`, falloff `#4c8fa2`
- Magenta/purple emphasis `#c026d3`-ish
- Light cards `#e7e6e1` / `#f2f2f2` (cutouts sit on THESE, never on
  the dark bg — contrast rule)

### Type system
- Small **uppercase cyan labels** on dark rounded chips: "CLIP",
  "CAPTIONS", "ANIMATIONS" — capability labels pinned around demo cards.
- **Emphasis pops:** magenta/purple rounded bold display words beside the
  talking head (e.g. "naah!!"), 2–4 words max, pop in on beat, out hard.
- Demo cards: serif/grotesque mix titles.

### Caption system
No fixed chip system — captions live on the demo cards and as pop
labels. Bullet lists build **line-by-line** on light cards
("timing / speed / camera movement") — cheap, readable, high-retention.

### Motion grammar
- Rapid **panel pop-ins over a continuous talking head** — one panel =
  one idea (tool icon row → demo card → comparison grid).
- Panels enter with glow, sit ~3–5s, cut hard.
- Talking head: center-left medium close-up; graphics live in the freed
  space (speaker navy tee, RØDE mic, dark studio, teal backlight).

### Sticker grammar
Black-and-white **paper-cutout elements**: pointing hands, torn-edge
portrait cutouts, thought bubbles ("they want to see you fail" — man at
desk surrounded by pointing hands). Cutouts only on light-gray/white
cards.

### Why use it
The 2026 viral talking-head editing look. Best for **tutorials,
AI-tool demos, "editing style" content, hype explainers**. Maximum
energy per second. Works when the topic is fun/process-y ("how I edit",
"watch what AI does here"). Can overwhelm calm topics — match the mood.

---

## 3. Neon Product Ad — `neon-product-ad`

**Source:** "COMMENT AI" neon product ad (11.15s, no speaker — pure
motion graphics).

### Palette
- Content panel dark `#120C26`
- Magenta glow keywords `#FF3FD4`, highlight bars `#E8439B`
- Icon squares `#1B1433` with lavender glyphs `#9D8DF1`
- Blue `#4796E3` (Gemini-style star), red circled days `#E5484D`
- Chrome background: light gray radial vignette (`#F2F2F2` → `#CFCFCF`)

### Type system
- Heavy rounded grotesque (Poppins/ExtraBold class).
- **Keyword glow:** white text + magenta outer glow (~20px blur).
- Header wordmark: heavy grotesque, white fill, thick black stroke
  (~10–14px @1080).

### Layout rules
- **Static chrome frame** persists: top header (title + "Pr"/"Ae" icons +
  brand lockup), bottom **contrast chips** — two black rounded chips
  (`#140F22`, radius ~28px): "4 HOURS" vs "10 MINUTES", white heavy
  condensed ~90px, slight vertical stagger.
- Content panel: full-bleed dark y≈290–1130.
- **Hard 0.3–0.5s leftward wipes** between beats (5 beats: brain quote →
  pocket watch → before/after phones → calendar → payoff). No fades.
- No subtitle system at all — the panel copy IS the narration.
  The selling mechanic is **visual time-contrast**.

### Why use it
The product-ad formula. Best for **app promos, tool launches,
"before → after" selling, SaaS ads**. The fixed chrome frame means the
brand is always visible while content rotates. Selling through contrast
("4 HOURS" vs "10 MINUTES") is the signature move — steal it even
outside this style.

---

## 4. Dark Fintech — `dark-fintech`

**Source:** "How do credit cards profit?" dark fintech explainer.

### Palette
- Canvas `#0A0E0A` + green radial glow at bottom `#1DB954` @~25%
- Faint spotlight beams
- Glass cards `#101410` @90%, 1px rgba(255,255,255,.25) border,
  radius ~28px
- Money-green `$` `#2ECC71`, sparkle accents
- Glowing green script "Result" (Dancing/Allura-style with outer glow)

### Type system
- Bold white grotesque ~44px for card headlines; green `$` inline.
- Cards carry **full sentences** — no word captions needed.

### Layout rules
- Speaker in **rounded-arch portal** (corner radius ~120px,
  top y≈1024, x 90–990).
- Card zone y≈540–945 (top third).
- Beat structure: hook cards (0–10s) → screen-record of the prompt
  doc (12–20s, browser tabs visible — *content, not watermark*) →
  payoff cards + glowing "Result" (24–32s) → comment-screenshot CTA.

### Why use it
The money-topic dark mode. Best for **finance explainers, fintech
products, "how X makes money" content, productivity apps with a premium
feel**. The screen-record beat doubles as a credibility device (show the
actual prompt/doc). Don't use for warm/friendly topics — the dark green
glow reads serious.

---

## 5. Warm Ed-tech — `warm-edtech`

**Source:** "Learn Your Way" warm teacher-desk explainer.

### Palette
- Cream paper background `#FAF5EC`
- Peach/orange accent `#E8734A`
- Dark-pill captions `#2A2A2A` @80% + white sans, centered y≈1390–1470
- Gray pill labels `#8A8A8A` + white text ("made / easier / adapts /
  tests / podcasts"), y≈1360–1440
- White app cards, radius ~36px, thin orange borders, green waveform bars

### Type system
- **Keyword slams:** bold black ~90px on cream ("File", "Book",
  "Paper") with 3D book renders.
- Ghost-serif variant: huge white semi-transparent serif ("Scale"
  ~120px) behind the speaker — depth device.
- Dark-pill keyword captions (≤2 lines), never plain text.

### Layout rules
- App cards scroll **vertically full-bleed**.
- B-roll in rounded-rect split screens.
- End: phone mockups + chips ("every industry" / "disrupted").

### Why use it
The friendly teacher. Best for **course promos, learning apps,
ed-tech launches, study content**. Cream + orange reads warm,
approachable, trustworthy — the opposite energy of Dark Fintech.
Pairs naturally with a woman-at-desk speaker or any "guide" persona.

---

## 6. Mono Kinetic Type — `mono-kinetic`

**Source:** "Skill over Scroll" kinetic-typography reel (16.35s —
pure type, no speaker, no subtitles; the type IS the content).

### Palette
- Paper `#F5F5F3` + faint dot grid (dots ~1.5px, spacing ~28px,
  `#D8D8D8`)
- Ink `#141414`, gray `#6E6E6E`
- Large blurred black organic blobs (~400–600px, blur ~40–60px)
  drifting top-left/bottom-right; slight paper grain
- Accents ONLY inside 3D objects: teal `#2FA8A0` phone screen,
  brass `#8A6D3B` pocket watch

### Type system
- Heavy grotesque (Archivo Black / Anton class) keywords ~64–110px.
- Regular ~40px supporting lines.
- Italic serif (Georgia class) ~34px centered for quotes.

### Signature device — the edit-UI made visible
**Dashed text-selection boxes** with anchor handles: 1.5px dashed
black bounding box around keywords, ~10px square handles at
corners+midpoints; arrow cursor visibly drags boxes; text types/slides
in letter-by-letter inside the box. *The "workshop aesthetic":
process as content.*

### Motion grammar
- Diagonal swoosh wipes, kinetic marquee scrolling R→L with motion
  blur, scale-pop on boxes, slow blob drift.
- Hard cuts, no dissolves. ~7 beats, ~2–2.5s each.
- Closer: black side bars squeeze in (letterbox close) → "DM For
  Paid Work" end card.

### Why use it
Type-driven storytelling with zero speaker needed. Best for
**motivational content, "hard truths" posts, portfolio pieces for
editors, quote explainers**. The monochrome restraint + one moving
device (selection boxes) makes it cheap to produce and instantly
recognizable. Add ONE colored 3D object per video as the accent.

---

## Cross-style constants (observed across ≥3 sources)

- **Keyword BIG / explanation SMALL** — never invert.
- **Hard cuts dominate**; dissolves almost never appear.
- **One motion idea per beat** (slam, draw, morph, pop) with
  hard-edged easing.
- **Real imagery = credibility** — real photos, logos, UI screenshots
  in rounded cards, never text-only pills pretending to be product.
- **Rounded-corner media cards** ~60px radius, inset ~40px — identical
  geometry for speaker footage AND graphic cards so layouts swap
  without reflow.
- **Safe zones @1080×1920:** titles y 170–450; key content within
  x 90–990 (right rail clear); nothing important below y≈1570
  (IG caption zone).

## Kanglish / Kannada note

For Aditya's Kanglish content, steal the **3D metallic native-script
word overlay** from the StorySync course: gold/chrome 3D Kannada
keyword + drop shadow, floating in the forehead band of the 9:16
frame. It works with ANY of the 6 styles as a hook device — put the
Kannada keyword big on screen while narration runs in Kanglish.
Also: the Warm Editorial caption-chip system and the Mono Kinetic
selection-box motif both transfer cleanly to Kannada script.
