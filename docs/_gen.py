#!/usr/bin/env python3
"""Generate docs/styles/<slug>.html for the Video Style Playbook."""
import html, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def esc(s): return html.escape(s)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — Video Style Playbook</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<nav class="nav"><div class="nav-inner">
  <a class="brand" href="../index.html">Video Style <span>Playbook</span></a>
  <div class="nav-links">
    <a href="../index.html">Styles</a>
    <a href="../chooser.html">Style chooser</a>
    <a href="../../STYLES.md">Specs</a>
    <a href="../../RECIPES.md">Recipes</a>
  </div>
</div></nav>
<div class="wrap">
  <header class="hero">
    <h1>{name}</h1>
    <div class="tags">{tags}</div>
    <p>{lede}</p>
    <p class="lead" style="font-size:14px">Source: {source}</p>
  </header>

  <section class="block">
    <h2 class="sec">Palette</h2>
    <p class="lead">Click any swatch to copy its hex.</p>
    <div class="swatches">
{swatches}    </div>
  </section>

  <section class="block">
    <h2 class="sec">Type system</h2>
    <div class="specimen">
{specimen}    </div>
  </section>

  <section class="block">
    <h2 class="sec">Caption / subtitle system</h2>
    <p class="lead">{caption_desc}</p>
    <div class="code-wrap">
      <button class="copy-btn" data-copy="{css_copy}">Copy CSS</button>
      <pre class="code">{css}</pre>
    </div>
  </section>

  <section class="block">
    <h2 class="sec">Motion grammar</h2>
    <ul class="tight">
{motion}    </ul>
  </section>

  <section class="block">
    <h2 class="sec">Layout rules</h2>
    <ul class="tight">
{layout}    </ul>
  </section>

  <section class="block why">
    <h2 class="sec">Why use it</h2>
    <p class="lead">{why}</p>
    <p><b>Best for:</b> {best_for}</p>
  </section>

  <section class="block">
    <h2 class="sec">Scenario examples</h2>
    <p class="lead">Mockup frames in this style's exact palette and type language. Video versions come later.</p>
    <div class="scen-grid">
{scenarios}    </div>
  </section>
</div>
<footer><div class="wrap">
  <span>Video Style Playbook — reverse-engineered from real viral reels, frame by frame.</span>
  <span><a href="../../README.md">README</a> · <a href="../../RECIPES.md">Recipes</a></span>
</div></footer>
<script src="../assets/site.js"></script>
</body>
</html>
"""

SWATCH = """      <div class="swatch" data-copy="{hex}">
        <div class="color" style="background:{hex}"></div>
        <div class="meta"><b>{label}</b><code>{hex}</code></div>
      </div>
"""

SPEC = """      <div class="row">
        <div class="lbl">{label}</div>
        <div style="{css}">{sample}</div>
      </div>
"""

SCEN = """      <div class="scen">
        <img src="../../examples/{slug}/{file}" alt="{label}">
        <div class="cap"><b>{label}</b>{desc}</div>
      </div>
"""

SCEN_PENDING = """      <div class="scen pending">
        <div class="ph">Pending —<br>regenerating</div>
        <div class="cap"><b>{label}</b>{desc}</div>
      </div>
"""

styles = [
dict(
slug="warm-editorial", name="Warm Editorial",
tags=["calm","premium","credible","speaker"],
lede="Cream + ink, butter-yellow chips, blur-resolve serif titles. The calm-authority premium explainer — restraint is the whole aesthetic.",
source="“How does AI work? episode 01” (118.7s timestamped beat map)",
palette=[("Cream","#F8F7F2"),("Ink","#1E1E1E"),("Butter-yellow chip","#F2C14E"),
("Navy chip text","#1E2A44"),("Charcoal chip","#22262B"),("Terracotta","#D06D58"),
("Credential blue","#2E5BFF")],
specimen=[
("Hero title — Didone italic serif","font-family: Georgia, 'Times New Roman', serif; font-style: italic; font-size: 64px; color: #1E1E1E; line-height: 1.05","AI work?"),
("Kicker — italic serif small","font-family: Georgia, serif; font-style: italic; font-size: 22px; color: #6b6b66","episode 01"),
("Brand beat — bold grotesque","font-family: Arial, sans-serif; font-weight: 900; font-size: 34px; letter-spacing: -0.02em; color: #1E1E1E","ANTHROPIC"),
("Chip — geometric sans","font-family: Verdana, sans-serif; font-weight: 600; font-size: 18px; background: #F2C14E; color: #1E2A44; display: inline-block; padding: 8px 20px; border-radius: 999px","neural network"),
],
caption_desc="Three flavors on an emphasis rhythm — pill = emphasis, no-pill = filler. Phrase-level swaps with a 150ms pop. No karaoke.",
css=""".chip-yellow {
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
/* title entrance */
@keyframes blur-resolve {
  from { filter: blur(26px); opacity: 0; transform: scale(.96); }
  to   { filter: blur(0);    opacity: 1; transform: scale(1); }
}
.title-word { animation: blur-resolve 1.8s cubic-bezier(.16,1,.3,1) both; }""",
motion=["<b>Blur→sharp staggered word resolve</b> — ~1.5–2s hero lockups, &lt;0.5s single-word beats.",
"<b>Camera zoom fires on the same word timestamps</b> as the title (pullback on open, push-ins on key beats).",
"<b>Letter-spacing animates wide</b> on extent words (“Sa mp le”) — text performs meaning.",
"Diagram acts: bars grow, dotted trajectories draw, scene pans horizontally; stepper pills on top.",
"Hard cuts; warm grade — soft daylight, 15% black scrim over top 300px, mild grain."],
layout=["Titles: y 170–450 (below IG progress bar), centered; list variant top-left x≈225.",
"Chips: centered x≈540; y≈1390–1470 (talking head), y≈1158 (diagram boundary). Nothing below y≈1570.",
"Key content within x 90–990 (clear of right action rail).",
"Floating graphic cards: cream #FBFAF7, radius ~28px, soft shadow, slide in from left (scale 0.9→1); speaker ducks to bottom ~45%."],
why="The calm-authority premium explainer. One serif, one grotesque, three chip colors — and motion synced to word timestamps, not decoration. Lowest risk of looking cheap.",
best_for="Education, AI/tech explainers, product walkthroughs with credibility",
scenarios=[("01-hook.webp","Hook / title card","Serif hero lockup with kicker"),
("02-caption-beat.webp","Talking-head caption beat","Butter-yellow chip over speaker"),
("03-data-panel.webp","Stat / data panel","Diagram act with stepper pills + slider"),
("04-comparison-panel.webp","Product / comparison panel","Floating UI card, terracotta badge"),
("05-end-card.webp","End card / CTA","Serif close + subscribe pill")],
),

dict(
slug="dark-sticker-collage", name="Dark Sticker Collage",
tags=["viral","playful","maximal","speaker"],
lede="Cyan-glow floating cards, B&W paper cutouts, magenta emphasis pops. The 2026 viral talking-head look — maximum energy per second.",
source="“How to Edit a Viral Talking-Head Using ONLY AI (2026 Style)” — Joseph | Video Editing",
palette=[("Olive black","#10120f"),("Ice-cyan glow","#a5f2ff"),("Cyan falloff","#4c8fa2"),
("Magenta pop","#c026d3"),("Light card","#e7e6e1"),("Paper white","#f2f2f2")],
specimen=[
("Capability label — cyan uppercase","font-family: Arial, sans-serif; font-weight: 700; font-size: 15px; letter-spacing: .22em; color: #a5f2ff; background: rgba(165,242,255,.08); display: inline-block; padding: 8px 18px; border-radius: 999px","CAPTIONS"),
("Emphasis pop — magenta display","font-family: Arial, sans-serif; font-weight: 900; font-size: 52px; color: #c026d3; transform: rotate(-3deg); display: inline-block","naah!!"),
("Card title — grotesque","font-family: Arial, sans-serif; font-weight: 800; font-size: 26px; color: #1a1a1a","the average american adult"),
],
caption_desc="No fixed chip system — captions live on demo cards and as pop labels. Bullet lists build line-by-line on light cards.",
css=""".glow-card {
  background: #10120f; border: 1.5px solid rgba(165,242,255,.8);
  border-radius: 24px; box-shadow: 0 0 48px rgba(165,242,255,.25);
}
.cap-label { color: #a5f2ff; font: 700 22px/1 "Inter", sans-serif;
  letter-spacing: .22em; background: rgba(165,242,255,.08);
  border-radius: 999px; padding: 10px 18px; }
.pop { color: #c026d3; font: 900 64px/1 "Inter", sans-serif;
  transform: rotate(-3deg); }""",
motion=["<b>Rapid panel pop-ins over a continuous talking head</b> — one panel = one idea.",
"Panels enter with glow, sit ~3–5s, cut hard. No dissolves.",
"Emphasis words pop beside the speaker (2–4 words max), in on beat, out hard.",
"Talking head stays center-left; graphics live in the freed space."],
layout=["Floating 9:16 demo cards centered over the 16:9 frame.",
"Cyan uppercase capability labels pinned around cards (CLIP / CAPTIONS / ANIMATIONS).",
"<b>Contrast rule:</b> B&W cutouts sit on light cards (#e7e6e1), never on the dark bg.",
"Paper-cutout hands / torn portraits / thought bubbles for “doubt” beats."],
why="The 2026 viral talking-head editing look. One panel = one idea keeps the energy high without chaos — the collage is the content.",
best_for="Tutorials, AI-tool demos, “editing style” content, hype explainers",
scenarios=[("01-hook.webp","Hook / title card","Huge title + glowing demo card"),
("02-caption-beat.webp","Talking-head caption beat","Magenta pop beside speaker"),
("03-data-panel.webp","Stat / data panel","Line-by-line bullets on light card"),
("04-comparison-panel.webp","Product / comparison panel","RAW vs AI with VS divider"),
("05-end-card.webp","End card / CTA","SUBSCRIBE pop + thought bubble")],
),

dict(
slug="neon-product-ad", name="Neon Product Ad",
tags=["hype","no-speaker","sells"],
lede="Magenta-glow keywords, static chrome frame, “4 HOURS vs 10 MINUTES” contrast chips. The product-ad formula — selling through contrast.",
source="“COMMENT AI” neon product ad (11.15s, pure motion graphics)",
palette=[("Content panel","#120C26"),("Magenta glow","#FF3FD4"),("Highlight bar","#E8439B"),
("Icon square","#1B1433"),("Lavender glyph","#9D8DF1"),("Blue star","#4796E3"),
("Chip black","#140F22"),("Vignette light","#F2F2F2")],
specimen=[
("Keyword — neon glow","font-family: Arial, sans-serif; font-weight: 800; font-style: italic; font-size: 44px; color: #fff; text-shadow: 0 0 20px #FF3FD4, 0 0 44px #FF3FD4","perfect"),
("Wordmark — grotesque + stroke","font-family: Arial, sans-serif; font-weight: 900; font-size: 30px; color: #fff; -webkit-text-stroke: 2px #111; letter-spacing: .04em","COMMENT AI"),
("Contrast chip","font-family: Arial, sans-serif; font-weight: 900; font-size: 30px; color: #fff; background: #140F22; display: inline-block; padding: 12px 26px; border-radius: 28px","10 MINUTES"),
],
caption_desc="No subtitle system at all — the panel copy IS the narration. The selling mechanic is visual time-contrast.",
css=""".neon-kw { color: #fff; font: italic 800 64px/1 "Inter", sans-serif;
  text-shadow: 0 0 20px #FF3FD4, 0 0 44px #FF3FD4; }
.neon-panel { background: #120C26; }
.contrast-chip { background: #140F22; color: #fff;
  border-radius: 28px; padding: 24px 40px;
  font: 900 90px/1 "Inter", sans-serif; }
/* hard wipe between beats */
.beat { animation: wipe .4s ease-in both; }
@keyframes wipe { from { transform: translateX(100%);} to { transform: none; } }""",
motion=["<b>Hard 0.3–0.5s leftward wipes</b> between beats. No fades, ever.",
"Static chrome frame persists: header wordmark + logo row + bottom contrast chips.",
"Keyword glow pulses on the selling word. 5-beat structure: quote → object → before/after → calendar → payoff."],
layout=["Content panel: full-bleed dark #120C26, y≈290–1130.",
"Header: title center (y≈115), app icons top-left, brand lockup right — asymmetric.",
"Bottom contrast chips: two black rounded chips, slight vertical stagger — “4 HOURS” vs “10 MINUTES”."],
why="Built for selling through contrast. The fixed chrome frame means the brand is always visible while content rotates underneath — steal the contrast-chip device even outside this style.",
best_for="App promos, tool launches, SaaS ads, before→after selling",
scenarios=[("01-hook.webp","Hook / title card","Chrome header + glowing keyword"),
("02-app-beat.webp","App screen beat","Before/after phone mockups"),
("03-data-panel.webp","Stat / data panel","Calendar grid, red-circled days"),
("04-comparison-panel.webp","Product / comparison panel","4 HOURS vs 10 MINUTES chips"),
("05-end-card.webp","End card / CTA","“you start now” neon payoff")],
),

dict(
slug="dark-fintech", name="Dark Fintech",
tags=["money","premium","dark","speaker"],
lede="Green glow, glassmorphic cards, rounded-arch portals. Money reads serious here — the dark-mode fintech explainer.",
source="“How do credit cards profit?” dark fintech explainer",
palette=[("Canvas","#0A0E0A"),("Green glow","#1DB954"),("Glass card","#101410"),
("Money green","#2ECC71"),("White text","#FFFFFF")],
specimen=[
("Card headline — grotesque","font-family: Arial, sans-serif; font-weight: 800; font-size: 28px; color: #fff","Late payments = <span style='color:#2ECC71'>+$</span>"),
("Payoff script — glowing","font-family: Georgia, serif; font-style: italic; font-size: 52px; color: #2ECC71; text-shadow: 0 0 24px #1DB954","Result"),
("CTA","font-family: Arial, sans-serif; font-weight: 700; font-size: 20px; color: #fff","Comment “Link” and I’ll send it"),
],
caption_desc="Cards carry full sentences — no word captions needed. The screen-record beat doubles as a credibility device.",
css=""".fin-card { background: rgba(16,20,16,.9);
  border: 1px solid rgba(255,255,255,.25); border-radius: 28px;
  padding: 28px; }
.fin-card h4 { color: #fff; font: 800 44px/1.2 "Inter", sans-serif; margin: 0; }
.fin-card .dollar { color: #2ECC71; }
.fin-canvas { background: #0A0E0A;
  background-image: radial-gradient(ellipse at 50% 100%, rgba(29,185,84,.25), transparent 60%); }""",
motion=["Beat structure: hook cards (0–10s) → screen-record of the prompt doc (12–20s) → payoff cards + glowing “Result” (24–32s) → comment-screenshot CTA.",
"Screen-record plays mid-reel — browser tabs visible is fine; it’s content, not a watermark.",
"Smooth panel entrances; glowing script payoff is the climax."],
layout=["Speaker in <b>rounded-arch portal</b> (radius ~120px, top y≈1024, x 90–990).",
"Card zone y≈540–945 (top third).",
"Green radial glow at bottom of canvas; faint spotlight beams."],
why="The money-topic dark mode. Glass + green glow reads premium-financial instantly — and showing the actual prompt/doc as a beat is a credibility device most fintech content skips.",
best_for="Finance explainers, fintech products, “how X makes money” content",
scenarios=[("01-hook.webp","Hook / title card","“$? How do credit cards profit?”"),
(None,"Talking-head caption beat","Arch portal + floating cards — regenerating"),
("03-data-panel.webp","Stat / data panel","Stacked glass cards with icons"),
("04-comparison-panel.webp","Product / comparison panel","Glowing “Result” payoff"),
("05-end-card.webp","End card / CTA","Comment-“Link” CTA card")],
),

dict(
slug="warm-edtech", name="Warm Ed-tech",
tags=["friendly","teaching","speaker"],
lede="Cream + orange, dark-pill keyword captions, scrolling app cards, giant keyword slams. The friendly teacher.",
source="“Learn Your Way” warm teacher-desk explainer",
palette=[("Cream","#FAF5EC"),("Orange accent","#E8734A"),("Dark pill","#2A2A2A"),
("Gray label","#8A8A8A"),("Card white","#FFFFFF"),("Waveform green","#3FA66A")],
specimen=[
("Keyword slam — black grotesque","font-family: Arial, sans-serif; font-weight: 900; font-size: 56px; color: #1a1a1a","Paper"),
("Dark-pill caption","font-family: Arial, sans-serif; font-weight: 600; font-size: 17px; color: #fff; background: rgba(42,42,42,.8); display: inline-block; padding: 8px 20px; border-radius: 999px","adapts to you"),
("Ghost serif","font-family: Georgia, serif; font-size: 64px; color: rgba(255,255,255,.55)","Scale"),
],
caption_desc="Dark-pill keyword captions (≤2 lines), never plain text. Gray pill labels under cards for meta-labels.",
css=""".ed-pill { background: rgba(42,42,42,.8); color: #fff;
  border-radius: 999px; padding: 14px 28px;
  font: 600 30px/1 "Inter", sans-serif; }
.ed-label { background: #8A8A8A; color: #fff; border-radius: 999px;
  padding: 8px 18px; font: 600 22px/1 "Inter", sans-serif; }
.ed-card { background: #fff; border: 2px solid #E8734A; border-radius: 36px; }
.ed-slam { color: #1a1a1a; font: 900 90px/1 "Inter", sans-serif; }""",
motion=["App cards scroll vertically full-bleed.",
"Giant keyword slams (~90px black) with 3D renders — “File / Book / Paper”.",
"Ghost serif (~120px white, semi-transparent) behind the speaker for depth.",
"B-roll in rounded-rect split screens."],
layout=["Cream paper bg everywhere.",
"Keyword captions centered y≈1390–1470; gray pill labels y≈1360–1440.",
"White app cards radius 36px, thin orange borders, green waveform bars.",
"End: phone mockups + chips (“every industry” / “disrupted”)."],
why="Cream + orange reads warm, approachable, trustworthy — the opposite energy of Dark Fintech. Pairs naturally with a guide persona at a desk.",
best_for="Course promos, learning apps, ed-tech launches, study content",
scenarios=[("01-hook.webp","Hook / title card","“Learn Your Way” title"),
("02-caption-beat.webp","Talking-head caption beat","Desk speaker + dark pill"),
("03-data-panel.webp","Stat / data panel","Scrolling app cards"),
("04-comparison-panel.webp","Product / comparison panel","File / Book / Paper slams"),
("05-end-card.webp","End card / CTA","Phone mockups + industry chips")],
),

dict(
slug="mono-kinetic", name="Mono Kinetic Type",
tags=["type-as-content","no-speaker","monochrome"],
lede="Dashed selection boxes with anchor handles, swoosh wipes, strict monochrome. The workshop aesthetic — process as content.",
source="“Skill over Scroll” kinetic-typography reel (pure type, no speaker)",
palette=[("Paper","#F5F5F3"),("Ink","#141414"),("Gray","#6E6E6E"),
("Dot grid","#D8D8D8"),("Teal accent","#2FA8A0"),("Brass accent","#8A6D3B")],
specimen=[
("Keyword — heavy grotesque","font-family: 'Arial Black', Arial, sans-serif; font-weight: 900; font-size: 46px; color: #141414; letter-spacing: -.01em","NO MAGIC PILLS"),
("Quote — italic serif","font-family: Georgia, serif; font-style: italic; font-size: 20px; color: #6E6E6E","“Here is the truth.”"),
("Selection box","font-family: 'Arial Black', Arial, sans-serif; font-weight: 900; font-size: 30px; color: #141414; border: 2px dashed #141414; display: inline-block; padding: 10px 22px; position: relative","HARDWORK ▢"),
],
caption_desc="No subtitles — the type IS the content. Marquees and letter-by-letter typing carry the narration.",
css=""".select-box { border: 1.5px dashed #141414; position: relative;
  display: inline-block; padding: 14px 28px;
  font: 900 64px/1 "Arial Black", sans-serif; color: #141414; }
/* anchor handles via ::before/::after + box-shadow copies */
.marquee { overflow: hidden; white-space: nowrap; }
.marquee span { display: inline-block;
  animation: scroll 12s linear infinite; }
@keyframes scroll { to { transform: translateX(-50%); } }""",
motion=["<b>Dashed selection boxes</b> with anchor handles; arrow cursor drags them; text types in letter-by-letter.",
"Diagonal swoosh wipes, kinetic marquee R→L with motion blur, scale-pop on boxes.",
"Slow blurred-blob drift at edges. Hard cuts, ~2–2.5s per beat.",
"Closer: black side bars squeeze in (letterbox close) → end card."],
layout=["Paper #F5F5F3 + faint dot grid (1.5px dots, 28px spacing).",
"Strictly monochrome — ONE colored 3D object per video as the accent (teal phone / brass watch).",
"~7 beats per 16s; type always the hero, never decoration."],
why="Type-driven storytelling with zero speaker needed. The monochrome restraint + one moving device (selection boxes) makes it cheap to produce and instantly recognizable.",
best_for="Motivational content, “hard truths” posts, editor portfolio pieces, quote explainers",
scenarios=[("01-hook.webp","Hook / title card","Dashed box + cursor drag"),
(None,"Kinetic beat","NO MAGIC PILLS — regenerating"),
("03-data-panel.webp","Stat / data panel","Marquee + dashed boxes"),
("04-comparison-panel.webp","Product / comparison panel","Swoosh wipe before/after"),
("05-end-card.webp","End card / CTA","Letterbox close")],
),
]

outdir = os.path.join(BASE, "docs", "styles")
os.makedirs(outdir, exist_ok=True)

for st in styles:
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in st["tags"])
    swatches = "".join(SWATCH.format(label=esc(l), hex=esc(h)) for l, h in st["palette"])
    specimen = "".join(SPEC.format(label=esc(l), css=c, sample=s) for l, c, s in st["specimen"])
    motion = "".join(f"      <li>{m}</li>\n" for m in st["motion"])
    layout = "".join(f"      <li>{l}</li>\n" for l in st["layout"])
    scens = ""
    for item in st["scenarios"]:
        f, label, desc = item
        if f:
            scens += SCEN.format(slug=st["slug"], file=f, label=esc(label), desc=esc(" — " + desc) if desc else "")
        else:
            scens += SCEN_PENDING.format(label=esc(label), desc=esc(" — " + desc) if desc else "")
    css_copy = st["css"].replace('"', "&quot;")
    page = PAGE.format(
        name=esc(st["name"]), tags=tags, lede=esc(st["lede"]), source=esc(st["source"]),
        swatches=swatches, specimen=specimen,
        caption_desc=esc(st["caption_desc"]),
        css=esc(st["css"]), css_copy=css_copy,
        motion=motion, layout=layout,
        why=esc(st["why"]), best_for=esc(st["best_for"]),
        scenarios=scens,
    )
    path = os.path.join(outdir, st["slug"] + ".html")
    with open(path, "w") as fh:
        fh.write(page)
    print("wrote", path)
