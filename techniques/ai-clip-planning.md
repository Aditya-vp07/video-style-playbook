# AI clip planning — prompt discipline for generated video/images/plates

AI generation is a **spice, not the meal**. This doc decides what gets
generated, where prompts live, how scenes are cut, how style stays
locked — and when to not generate at all.

## What to generate vs what to build

| Generate (AI) | Build (deterministic) |
|---|---|
| Hook plates (0–3s atmospheric openers) | All text, chips, captions, labels |
| Twist/finale plates | Charts, bar grows, sliders, steppers |
| Entity intro cards (BIG face/logo reveal) | Network graphs, node travel, links |
| Texture/backgrounds (paper grain, gradients) | Transitions, zooms, pans |
| B-roll atmosphere (office, crowd, lab) | UI mockups, phone frames |
| Paper-cutout / doodle illustrations | Anything with numbers or logos |

Rule: **if it carries information, build it. If it carries mood,
generate it.** Text inside generated clips is forbidden — the model
will misspell it and you'll re-render for an hour.

## Where prompts live in the pipeline

```
cue_sheet.md            # beats with t0/t1, layout, trigger
prompt_pack/
  beat_03_hook.md       # one file per generated beat
  beat_11_twist.md
  beat_17_finale.md
style_bible.md          # THE style lock (see below)
```

Each prompt file:
```markdown
# beat 11 — twist plate (t=41.0-44.5, 3.5s)
NEED: dark atmospheric wide shot, paper-cutout texture, teal rim light
AVOID: text, faces, logos, watermark-like elements
STYLE: per style_bible.md §2 (dark collage)
MOTION: slow push-in, no camera shake
DURATION: 3.5s, loopable tail (last 0.5s must match first 0.5s framing)
```

Prompts reference the style bible — never restate the style inline
(prompts drift; the bible doesn't).

## Style-lock protocol

`style_bible.md` (one per project, ~30 lines):
- Palette hexes (3–5 max), texture words ("paper grain", "halftone"),
  light words ("teal rim light", "soft daylight"), lens words
  ("shallow DOF", "35mm").
- 2–3 reference frames (paths to approved stills).
- **Refusal protocol:** a denied/failed prompt is NEVER retried
  mechanically. Options in order: (1) simplify the prompt (fewer
  elements), (2) Ken Burns on a style-locked still, (3) reuse an
  earlier approved clip. Log the refusal with the reason.

## When to cut / when to split scenes

Cut on **clause boundaries** from the cue sheet — never mid-clause.
Scene = one idea = one cue-sheet beat group.

- Max generated clip: **5s**. Longer → split into two beats with a
  deterministic bridge (title card, diagram) between them.
- Generated clips sit at: hook (0–3s), twist (mid-video energy reset),
  finale (last 5s). Max 3–4 generated clips per 3-minute video.
- Everything between generated clips is built motion graphics —
  that's what keeps the video coherent.

## Beat structure (from cue sheets)

```
HOOK (generated plate, 0-3s) → TITLE (built) → BODY (built, alternating
fusion states) → TWIST (generated plate, energy reset) → BODY → FINALE
(generated plate + built slam + CTA)
```

The generated plates are **bookends and pivots**. The built middle is
where the information lives.

## When NOT to generate

1. **Text, numbers, logos** — always built. No exceptions.
2. **Anything under 2s** — a built card + zoom is faster and sharper.
3. **Repeat beats** — reuse an approved clip with a different crop/zoom
   (Ken Burns: slow 1.0→1.08 zoom over the still, 3–5s).
4. **Style drift risk** — if the bible can't describe it in one line,
   build it instead.
5. **Tight deadline** — generation is the slowest, least predictable
   step. Default to built.

## Ken Burns fallback recipe

```python
# still -> 4s clip, slow push-in, 30fps
# ffmpeg: zoompan on the still
ffmpeg -loop 1 -i still.png -vf \
  "zoompan=z='min(1+0.08*in/120,1.08)':d=120:s=1080x1920:fps=30" \
  -t 4 -c:v libx264 -pix_fmt yuv420p kb_still.mp4
```

120 frames, 1.0→1.08, `zoompan` is fine here (no text in the still).

## Checklist

- [ ] Every generated beat has a prompt file referencing the style bible.
- [ ] No text/logos/numbers inside generated clips.
- [ ] ≤4 generated clips per 3-min video; each ≤5s.
- [ ] Cuts land on clause boundaries.
- [ ] Refusals logged; never mechanically retried.
- [ ] Ken Burns fallback ready for every planned generated beat.
