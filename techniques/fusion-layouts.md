# Fusion layouts — talking-head + graphics grammar

Aditya's main use case: a talking-head video fused with motion graphics.
This doc is the **layout state machine** — when the speaker is full-frame,
when they shrink, when graphics take over completely, and how the
transitions read. Drive it from the cue sheet.

## The four states

| State | Speaker | Graphics | When |
|---|---|---|---|
| `FULL_HEAD` | full frame | lower-third / caption only | personal story, opinion, direct address |
| `HEAD_PIP` | corner PiP | graphic canvas dominates | important word lands while evidence shows |
| `SPLIT_55` | bottom 52–100% | top 0–48% panel | demo / process narration |
| `FULL_GRAPHIC` | gone | full-frame takeover | data, diagrams, network maps, slams |

Geometry @1080×1920 (panel-only 1080×576 uses the same ratios):
- `HEAD_PIP`: speaker cutout x 0.55–1.0, y 0.62–1.0, no border, soft
  drop shadow. Free-floating caption (shadowed, no pill).
- `SPLIT_55`: graphic panel top 0–48% on paper texture with faint
  construction guides; black pill caption ON the seam (y≈920–1050).
- `FULL_HEAD`: speaker center, head y≈350–750; captions y 1390–1470.
- PiP and split use **identical corner radii** (~60px) so swaps don't
  reflow the eye.

## The cue-sheet contract

Annotate every beat with a layout intent. Add one field to each cue:

```
beat 12 | t=34.2-41.0 | layout: HEAD_PIP | trigger: emphasis("capture")
beat 13 | t=41.0-58.3 | layout: FULL_GRAPHIC | trigger: evidence(diagram_act_1)
beat 14 | t=58.3-63.9 | layout: FULL_HEAD | trigger: personal("when I first saw this")
```

Trigger vocabulary (keep it small):
- `emphasis(word)` — an important word lands → `HEAD_PIP`.
- `evidence(kind)` — diagram / network / chart / comparison → `FULL_GRAPHIC`.
- `demo(kind)` — screen-record / process → `SPLIT_55`.
- `personal(phrase)` — story, opinion, direct address → `FULL_HEAD`.
- `slam(word)` — title-card moment → `FULL_GRAPHIC` + slam overlay.

## When to shrink vs when to go full-graphic

**Shrink to PiP when:**
- The narration names an entity AND the graphic shows it (face/logo
  appears while he says the name).
- A keyword needs emphasis but the sentence is still personal
  ("…and that's what regulatory *capture* means").
- The graphic is a *reaction* to the words (pop, chip, small card).

**Go full-graphic when:**
- The beat is evidence: diagrams, networks, timelines, comparisons.
  The speaker adds nothing visually here — their voice carries it.
- A slam word lands (REGULATORY CAPTURE). Full-panel title, no face.
- Screen-record / UI demo fills the frame.

**Return to full head when:**
- Personal pronoun density spikes ("I", "my", "when I…").
- Direct address ("look", "think about it", "you've seen this").
- Punchline / verdict beats — the face sells the take.

Rule of thumb: **graphics explain, the face persuades.** If the beat
is explanation → shrink or leave. If the beat is persuasion → face.

## Transition grammar

| From → To | Transition | Params |
|---|---|---|
| any → any (beat change) | hard cut | default; 0 frames |
| any → FULL_GRAPHIC (topic change) | zoom-through | out 1.0→1.35 in 0.35s, cut, in 0.85→1.0 in 0.5s |
| FULL_HEAD → HEAD_PIP | shrink-move | scale 1.0→0.42 + translate to corner, `ease_out_expo`, 0.5s |
| HEAD_PIP → FULL_HEAD | grow-move | reverse of shrink-move, 0.5s |
| FULL_GRAPHIC → FULL_HEAD | hard cut | the face "returns" — a cut reads as confidence |
| SPLIT_55 → FULL_GRAPHIC | panel-expand | top panel grows to full frame, `ease_in_out_cubic`, 0.4s |

Never cross-dissolve. Never slide the speaker (they scale in place).

## Caption rules per state

- `FULL_HEAD`: style's caption system (chips / pills / karaoke).
- `HEAD_PIP`: free-floating white bold sans + soft shadow, centered,
  y≈0.55–0.62 — **no pill** (the graphic already has enough chrome).
- `SPLIT_55`: black pill on the seam, white bold ~52px, ≤2 lines.
- `FULL_GRAPHIC`: diagram labels + stepper pills; no narration captions
  (the graphic IS the narration).

## The 70/30 vertical assembly (final delivery)

When the deliverable is the fused 1080×1920 reel (not panel-only):
- Speaker occupies bottom 70% (y≈576–1920).
- Animated panel top 30% (y≈100–676, 1080×576 panel).
- Panel content obeys panel-internal safe zones; the panel's own
  top 100px stays clear (IG progress bar).
- Subtitles sit on the speaker's torso area, centered, max ~850px wide,
  clear of the right action rail and the bottom ~350px caption zone.

## State-machine sketch

```python
STATES = ("FULL_HEAD", "HEAD_PIP", "SPLIT_55", "FULL_GRAPHIC")

def plan_layout(cues):
    """cues: list of dicts with 'layout' + 'trigger'. Returns segments."""
    segs, cur = [], None
    for c in cues:
        if c["layout"] != cur:
            segs.append({
                "t0": c["t0"], "from": cur, "to": c["layout"],
                "transition": pick_transition(cur, c["layout"], c["trigger"]),
            })
            cur = c["layout"]
    return segs

def pick_transition(frm, to, trigger):
    if frm is None: return "cut"
    if to == "FULL_GRAPHIC" and trigger.startswith("evidence"):
        return "zoom_through"
    if (frm, to) == ("FULL_HEAD", "HEAD_PIP"): return "shrink_move"
    if (frm, to) == ("HEAD_PIP", "FULL_HEAD"): return "grow_move"
    if (frm, to) == ("SPLIT_55", "FULL_GRAPHIC"): return "panel_expand"
    return "cut"
```

## Checklist

- [ ] Every cue has a `layout` + `trigger`.
- [ ] No `FULL_GRAPHIC` longer than 25s without a face return.
- [ ] PiP caption has no pill; seam caption is always a pill.
- [ ] Shrink/grow moves are 0.5s `ease_out_expo`, speaker scales in place.
- [ ] Safe zones hold in all four states.
