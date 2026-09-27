# ANALYSIS-PROTOCOL — forensic DNA capture for new reference videos

The repeatable method used to reverse-engineer the first 15 videos
(10 IG reels + 5 YouTube). Run this on every new video Aditya sends
(10–20 more expected via Google Drive) so the second wave folds into
the playbook the same way.

## Phase 1 — Acquire

1. Collect the URL or file into `references/incoming/` (see that
   folder's README). Name files `<source>_<id>.<ext>`.
2. If it's a link, download with yt-dlp:
   ```bash
   python3 -m yt_dlp --no-playlist -f 'bv*[height<=1080]+ba/b[height<=1080]/b' \
     --extractor-args "youtube:player_client=android" \
     -o 'references/incoming/<id>.mp4' '<url>'
   ```
   Notes: plain web client 429s from this IP — `android`
   player_client works. Instagram reels download fine without login.
   Be polite: `--sleep-requests 5 --retries 3`.
3. Log it in `references/incoming/INDEX.md`: source, date fetched,
   duration, status (`pending` → `analyzed`).

## Phase 2 — Frame extraction

```bash
id=<id>; mkdir -p /tmp/frames_$id
# 1-fps contact sheet (first 60s)
ffmpeg -i references/incoming/$id.mp4 -t 60 -vf 'fps=1,scale=480:-1' /tmp/frames_$id/c_%04d.jpg
# scene-change frames (whole video, cap ~40)
ffmpeg -i references/incoming/$id.mp4 -vf "select='gt(scene,0.4)',scale=480:-1" -vsync vfr /tmp/frames_$id/s_%04d.jpg
# dense strip for title windows (first 8s at 4fps)
ffmpeg -i references/incoming/$id.mp4 -t 8 -vf 'fps=4,scale=480:-1' /tmp/frames_$id/t_%04d.jpg
```

## Phase 3 — Visual inspection (the actual work)

Inspect frames — **never captions/descriptions alone**. Fill the spec
sheet below. Colors are eyeball estimates unless sampled with a
color picker; font names are style matches, never claims.

### Spec sheet template

```markdown
## <id> — <working title> (<dur>s, <WxH>@<fps>)
**One-line visual summary:**

**Palette:** bg `#______`, ink `#______`, accent `#______`, …
**Type:** display (…px, style), supporting (…px), captions (…px)
**Caption system:** chips/pills/karaoke/plain — position, size, rhythm
**Motion grammar:** entrances, transitions, easing feel, pacing (beats/sec)
**Layout:** zones, speaker treatment, safe zones observed
**Signature device:** the one stealable trick, in one sentence
**Timestamped beats:** t=… — what changes (for the best ones only)
**Recipes:** numbered, each with hexes/px/timing
```

## Phase 4 — Fold into the playbook

For each spec sheet, decide:

| Finding | Action |
|---|---|
| Matches an existing style | Add its recipes to that style's page + `RECIPES.md`; add example notes |
| New visual language | New entry in `STYLES.md` + new `examples/<slug>/` (5 scenario images) + new `docs/styles/<slug>.html` (regen via `docs/_gen.py`) |
| New engineering technique | New file in `techniques/` + Techniques section on the site |
| One-off trick | Add to `RECIPES.md` only |

Then:
1. Update `references/incoming/INDEX.md` → `analyzed`.
2. Regenerate the docs site (`python3 docs/_gen.py` + technique pages).
3. Commit: `git commit -m "analysis wave 2: <ids> → <styles/recipes added>"`.

## Quality bar

- Every hex in a recipe was seen on a frame, not guessed from a
  description.
- Every timing claim has a timestamp.
- "Best video" candidates get the full timestamped beat map treatment.
- If a download fails (throttle/login-wall), say so in the spec sheet
  and analyze what's available (storyboard sprites, thumbnails) —
  never present partial analysis as complete.
