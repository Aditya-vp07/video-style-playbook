# Network graph — investigation-style relationship mapping

How to build a live network map where **links draw without messing up
node routes**: nodes travel, links follow, labels stay readable. This is
the core of the "follow the money / who funds whom" visual language.
All geometry @1080×1920 panel space (use the panel's own coordinate
system; the panel here is 1080×576 in fusion layouts — same math).

## The sequencing contract (this is the whole trick)

Links and nodes are **never animated at the same time**. Strict order
per beat:

1. **Links draw** — bezier path trims 0→1, `ease_in_out_cubic`, 0.4s each,
   staggered 60ms.
2. **Nodes travel** — only after their link is fully drawn. Node moves
   along a straight line to its slot, `ease_out_expo`, 0.6s, staggered
   80ms per node.
3. **Labels/chips fade-pop** — after the node lands, 0.15s pop (scale
   0.9→1).

Why it works: a traveling node dragging a half-drawn link looks like
spaghetti. Drawing the route first, then traveling the node along the
*already-visible* route, reads as "the entity follows the money".

## Node placement — readable by construction

- **Ring layout:** hub node at panel center; satellites on an ellipse.
  Ring 1: ≤6 nodes. Ring 2 (if needed): ≤10 nodes, radius ×1.8.
- **Deterministic slots:** precompute slot angles with a seeded shuffle
  so re-renders are identical. Slot angle jitter ≤ ±8° to break symmetry.
- **Keepout radius:** `r = max(node_r, label_halfwidth) + 24px`.
  No two keepout circles may overlap — if they do, push the satellite
  outward along its radial (never tangentially; radial moves preserve
  the mental model).
- **Cap:** satellite node ≤ 1.15× hub scale at entrance; relationship
  chips ≤ half the node label width (chips overlapping node labels at
  rest was a real defect in our PRO build — enforce the cap).

## Bezier link routing (no spaghetti)

Each link is a quadratic bezier: `P0` (hub edge) → `C` (control) →
`P1` (satellite edge).

```python
import math
def link_bezier(p0, p1, bend=0.22, side=1):
    """Control point pushed perpendicular so links arc around the hub."""
    mx, my = (p0[0]+p1[0])/2, (p0[1]+p1[1])/2
    dx, dy = p1[0]-p0[0], p1[1]-p0[1]
    L = math.hypot(dx, dy) or 1
    # perpendicular unit vector, bent away from center
    px, py = -dy/L * side, dx/L * side
    C = (mx + px*L*bend, my + py*L*bend)
    return p0, C, p1

def bez_point(p0, C, p1, t):
    u = 1-t
    return (u*u*p0[0] + 2*u*t*C[0] + t*t*p1[0],
            u*u*p0[1] + 2*u*t*C[1] + t*t*p1[1])
```

Rules:
- `bend=0.22` default; alternate `side` (+1/−1) per link so arcs don't
  stack on one side.
- Link starts/ends at **node edges**, not centers: shrink P0/P1 toward
  the segment by the node radius.
- Link width 2–3px; color = dim version of the style accent (e.g.
  `#4c8fa2` on the dark collage style). Hub links brighter than
  satellite-to-satellite links.
- **Trim animation:** draw the bezier progressively — sample N points,
  reveal `k = int(N * ease_in_out_cubic(u))` points per frame.

## Staggered node entrances

```python
def entrance_schedule(nodes, link_draw_dur=0.4, link_stagger=0.06,
                      node_dur=0.6, node_stagger=0.08):
    """Returns {node_id: (link_t0, node_t0)} in seconds."""
    sched = {}
    t = 0.0
    for i, n in enumerate(nodes):
        link_t0 = t + i * link_stagger
        node_t0 = link_t0 + link_draw_dur   # node waits for its link
        sched[n] = (link_t0, node_t0)
        t = link_t0
    return sched
```

- Node travel path: straight line from spawn point (panel edge nearest
  its slot, or hub center for the first node) to slot, `ease_out_expo`.
- Entrance scale: 0.6→1.0 (never above 1.15×).

## Label placement rules

1. Label sits **below** the node center, `node_r + 14px`.
2. Max 2 lines, 28–34px sans, centered. Long names get a
   **relationship chip** instead: small rounded chip (`radius=½h`)
   offset along the link's perpendicular, 18px from the link midpoint.
3. Chips never overlap node keepout circles — check at rest, nudge the
   chip along the link tangent if needed.
4. Real faces/logos: circular crop, white 2px ring, drop shadow.
   Logos get a white rounded-square badge (never a text pill).
5. Active-node label brightens to full white; inactive labels dim to
   55% opacity when another node is highlighted.

## Highlight / pulse grammar

- **Pulse:** expanding ring stroke on the active node — radius
  `node_r → node_r+26px` over 0.8s, alpha 0.8→0, loop 2×, then rest.
- **Highlight:** active node scale 1.0→1.15 (`ease_out_expo`, 0.4s);
  its links brighten to full accent; everything else dims to 55%.
- **Slam (the REGULATORY CAPTURE moment):** full-panel title card,
  150–180px grotesque, 0.3s scale 1.6→1.0 `ease_out_expo` + 0.1s hold
  before the network resumes. One per video max.

## Draw order (PIL, per frame)

```
1. panel background
2. links (dim) 
3. highlighted links (bright)
4. node badges (face/logo)
5. nodes (circles)
6. pulse rings
7. relationship chips
8. labels
9. slam card (if active)
```

## Readability checklist

- [ ] ≤6 satellites on ring 1; ring 2 only if the script demands it.
- [ ] No keepout-circle overlaps at rest (check programmatically).
- [ ] Chips ≤ half node-label width.
- [ ] Links drawn before nodes travel — never simultaneous.
- [ ] Inactive elements dim to 55% during highlight.
- [ ] Max one slam card per video.
