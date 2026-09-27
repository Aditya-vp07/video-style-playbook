# Camera — buttery GSAP-grade motion for the virtual camera

This is the motion layer under everything: zooms, pans, and transitions
driven by a virtual camera, with easing curves that feel like GSAP
(`expo.out` / `expo.inOut`). All params assume 1080×1920 @ 30fps unless
noted. The reference implementation targets a numpy per-frame envelope
fed into ffmpeg (`zoompan` or `scale`+`crop` with `eval=frame`).

## The easing math (copy this)

```python
import math

def ease_out_expo(t):      # GSAP expo.out
    return 1.0 if t >= 1 else 1 - 2 ** (-10 * t)

def ease_in_out_expo(t):   # GSAP expo.inOut
    if t <= 0: return 0.0
    if t >= 1: return 1.0
    return (2 ** (20 * t - 10) / 2) if t < 0.5 else (2 - 2 ** (-20 * t + 10)) / 2

def ease_out_cubic(t):     # snappier, cheaper feel for small moves
    return 1 - (1 - t) ** 3

def ease_in_out_cubic(t):  # pans, tracking moves
    return 4*t**3 if t < 0.5 else 1 - (-2*t + 2)**3 / 2
```

Rules of thumb (from the forensic pass):
- **Zooms:** `ease_out_expo`, 0.5–1.2s. Expo feels "expensive"; cubic feels "snappy".
- **Pans / tracking:** `ease_in_out_cubic`, 1.0–2.0s. Never expo a pan — it whips.
- **Pops (chips, labels):** `ease_out_cubic`, 0.15–0.25s, scale 0.9→1.0.
- Never linear. Never the same duration twice in a row — alternate 0.6s / 1.1s.

## Zoom-on-word-timestamp (the best-video move)

The signature device: the camera zoom fires **on the same word
timestamps** as the title/caption. Implementation: the cue sheet already
has word timestamps; attach zoom events to marked words.

```python
def zoom_envelope(n_frames, fps, events, base=1.0):
    """events: list of (t_sec, target_scale, dur_sec). Returns per-frame scale."""
    import numpy as np
    s = np.full(n_frames, base)
    for t, target, dur in events:
        f0 = int(t * fps); f1 = min(n_frames, f0 + int(dur * fps))
        if f1 <= f0: continue
        start = s[f0 - 1] if f0 > 0 else base
        for f in range(f0, f1):
            u = (f - f0) / max(1, (f1 - f0))
            s[f] = start + (target - start) * ease_out_expo(u)
        s[f1:] = s[f1 - 1]  # hold
    return s
```

Feed it into ffmpeg. Two routes:

**Route A — zoompan (simple, slight jitter on text; fine for plates):**
```
-vf "zoompan=z='1+0.35*in/90':d=1:s=1080x1920:fps=30"
```

**Route B — scale+crop with eval=frame (crisp, preferred for type):**
Render frames large (e.g. 1620×2880), then:
```
-vf "scale=1620:2880,crop=1080:1920:'(in_w-out_w)/2+(in_w-out_w)/2*0.06*sin(2*PI*t/8)':'(in_h-out_h)/2',scale=1080:1920"
```
For scripted zooms, generate the envelope in Python and pass per-frame
`x`,`y`,`w`,`h` via a `sendcmd` file or bake frames with PIL (see below).

**Baking with PIL (deterministic, recommended):**
```python
from PIL import Image
def apply_zoom(base: Image.Image, scale: float, cx=0.5, cy=0.5, out=(1080,1920)):
    W, H = base.size
    w, h = int(W / scale), int(H / scale)
    x = int((W - w) * cx); y = int((H - h) * cy)
    return base.crop((x, y, x + w, y + h)).resize(out, Image.LANCZOS)
```
Render the scene at 1.5×, then `apply_zoom` per frame with the envelope.
Zoom range: keep `1.0 → 1.15` for push-ins, `1.15 → 1.0` for pullbacks.
Beyond 1.25× the upscale softens — stay under it.

## Virtual camera rig recipe

```python
class VCam:
    def __init__(self, fps=30):
        self.fps, self.moves = fps, []  # (t0, dur, kind, params)
    def zoom(self, t0, dur, frm, to):
        self.moves.append((t0, dur, 'zoom', (frm, to)))
    def pan(self, t0, dur, frm_xy, to_xy):
        self.moves.append((t0, dur, 'pan', (frm_xy, to_xy)))
    def envelope(self, total):
        import numpy as np
        n = int(total * self.fps)
        zoom = np.ones(n); cx = np.full(n, 0.5); cy = np.full(n, 0.5)
        for t0, dur, kind, p in self.moves:
            f0, f1 = int(t0*self.fps), min(n, int((t0+dur)*self.fps))
            ease = ease_out_expo if kind=='zoom' else ease_in_out_cubic
            for f in range(f0, f1):
                u = ease((f-f0)/max(1,f1-f0))
                if kind=='zoom':
                    z0 = zoom[f0-1] if f0>0 else 1.0
                    zoom[f] = z0 + (p[1]-z0)*u if f==f0 else zoom[f]  # chain
                else:
                    cx[f] = p[0][0]+(p[1][0]-p[0][0])*u
                    cy[f] = p[0][1]+(p[1][1]-p[0][1])*u
            if kind=='zoom': zoom[f1:] = zoom[f1-1]
        return zoom, cx, cy
```

Notes:
- Chain moves: each zoom starts from the *current* zoom, not 1.0.
- One camera, one envelope per scene. A new scene = new VCam.
- Typical scene: pullback 1.12→1.0 over 1.2s on the title beat, then two
  push-ins (1.0→1.08) on keyword beats, 0.7s each.

## Zoom-through transitions (beat changes)

Instead of a hard cut: zoom *through* the cut.
- Outgoing scene: zoom 1.0→1.35 over 0.35s (`ease_in_out_expo`).
- Hard cut at peak.
- Incoming scene: starts at 0.85, settles 0.85→1.0 over 0.5s (`ease_out_expo`).

The 0.35s out + cut + 0.5s in reads as "diving into" the next idea.
Use sparingly — max 2–3 per minute, reserved for topic changes.
Everyday beat changes stay hard cuts (per the forensic pass: dissolves
almost never appear in the source videos).

## Tracking-style moves

Slow lateral drift behind a static graphic (e.g. diagram act panning):
- `pan` 0.5→0.35 in x over 6–10s, `ease_in_out_cubic`.
- Amplitude ≤ 8% of frame width — it's felt, not seen.
- Pair with a 1.0→1.06 slow zoom so edges never show.

## Checklist before render

- [ ] No linear ramps anywhere.
- [ ] Zoom durations alternate (0.6 / 1.1 pattern).
- [ ] Pans use cubic, never expo.
- [ ] Max zoom 1.25× (upscale budget).
- [ ] Zoom events land on cue-sheet word timestamps, not scene starts.
- [ ] Zoom-throughs ≤ 3 per minute.
