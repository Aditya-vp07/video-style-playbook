#!/usr/bin/env python3
"""Convert techniques/*.md to docs/techniques/*.html (minimal converter)."""
import html, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TECH = os.path.join(BASE, "techniques")
OUT = os.path.join(BASE, "docs", "techniques")
os.makedirs(OUT, exist_ok=True)

def inline(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+?)`', r'<code>\1</code>', s)
    return s

def md_to_html(md):
    out, in_code, in_list, para = [], False, False, []
    raw = md.split('\n')
    # join indented continuation lines to their list item (code-fence aware)
    lines, fenced = [], False
    for l in raw:
        if l.strip().startswith('```'):
            fenced = not fenced
            lines.append(l); continue
        if (not fenced and l[:1].isspace() and l.strip() and lines
                and lines[-1].strip()
                and re.match(r'^([-*]|\d+\.)\s+', lines[-1].strip())):
            lines[-1] = lines[-1].rstrip() + ' ' + l.strip()
        else:
            lines.append(l)
    i = 0
    def flush_para():
        if para:
            out.append('<p>' + ' '.join(inline(l) for l in para) + '</p>')
            para.clear()
    def close_list():
        nonlocal in_list
        if in_list:
            out.append('</ul>'); in_list = False
    while i < len(lines):
        l = lines[i]
        if l.strip().startswith('```'):
            flush_para(); close_list()
            if not in_code:
                lang = l.strip()[3:].strip()
                out.append(f'<div class="code-wrap"><pre class="code">')
                in_code = True
            else:
                out.append('</pre></div>'); in_code = False
            i += 1; continue
        if in_code:
            out.append(html.escape(l)); i += 1; continue
        s = l.strip()
        if not s:
            flush_para(); close_list(); i += 1; continue
        if s.startswith('|') and i+1 < len(lines) and re.match(r'^\|[\s\-|:]+\|$', lines[i+1].strip()):
            flush_para(); close_list()
            headers = [c.strip() for c in s.strip('|').split('|')]
            out.append('<table class="cmp"><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in headers) + '</tr>')
            i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('</table>')
            continue
        m = re.match(r'^(#{1,4})\s+(.*)', s)
        if m:
            flush_para(); close_list()
            lvl = len(m.group(1))
            tag = {1:'h1',2:'h2',3:'h3',4:'h4'}[lvl]
            cls = ' class="sec"' if lvl == 2 else ''
            out.append(f'<{tag}{cls}>{inline(m.group(2))}</{tag}>')
            i += 1; continue
        if re.match(r'^[-*]\s+', s) or re.match(r'^\d+\.\s+', s):
            flush_para()
            if not in_list:
                out.append('<ul class="tight">'); in_list = True
            item = re.sub(r'^([-*]|\d+\.)\s+', '', s)
            # checkbox
            item = re.sub(r'^\[ \]\s*', '☐ ', item)
            out.append(f'<li>{inline(item)}</li>')
            i += 1; continue
        if s.startswith('>'):
            flush_para(); close_list()
            out.append(f'<p class="lead">{inline(s[1:].strip())}</p>')
            i += 1; continue
        para.append(s); i += 1
    flush_para(); close_list()
    if in_code: out.append('</pre></div>')
    return '\n'.join(out)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Video Style Playbook</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<nav class="nav"><div class="nav-inner">
  <a class="brand" href="../index.html">Video Style <span>Playbook</span></a>
  <div class="nav-links">
    <a href="../index.html">Styles</a>
    <a href="../chooser.html">Style chooser</a>
    <a href="index.html" class="active">Techniques</a>
    <a href="../../RECIPES.md">Recipes</a>
  </div>
</div></nav>
<div class="wrap">
{body}
</div>
<footer><div class="wrap">
  <span>Video Style Playbook — reverse-engineered from real viral reels, frame by frame.</span>
  <span><a href="../../README.md">README</a> · <a href="../../RECIPES.md">Recipes</a></span>
</div></footer>
<script src="../assets/site.js"></script>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Techniques — Video Style Playbook</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<nav class="nav"><div class="nav-inner">
  <a class="brand" href="../index.html">Video Style <span>Playbook</span></a>
  <div class="nav-links">
    <a href="../index.html">Styles</a>
    <a href="../chooser.html">Style chooser</a>
    <a href="index.html" class="active">Techniques</a>
    <a href="../../RECIPES.md">Recipes</a>
  </div>
</div></nav>
<div class="wrap">
  <header class="hero">
    <h1>Implementation <em>techniques.</em></h1>
    <p>Code-ready playbooks for pro-grade motion on the ffmpeg/Python stack — the engineering track behind the styles.</p>
  </header>
  <div class="grid">
    <div class="card"><div class="card-body">
      <h3><a href="camera.html">Camera</a></h3>
      <div class="tags"><span class="tag">easing</span><span class="tag">virtual camera</span></div>
      <p>Buttery GSAP-grade motion: expo zoom curves, smooth pans, zoom-on-word-timestamp rig, zoom-through transitions.</p>
    </div></div>
    <div class="card"><div class="card-body">
      <h3><a href="network-graph.html">Network Graph</a></h3>
      <div class="tags"><span class="tag">bezier</span><span class="tag">sequencing</span></div>
      <p>Investigation-style relationship mapping: links draw before nodes travel, staggered entrances, highlight grammar.</p>
    </div></div>
    <div class="card"><div class="card-body">
      <h3><a href="fusion-layouts.html">Fusion Layouts</a></h3>
      <div class="tags"><span class="tag">talking head</span><span class="tag">state machine</span></div>
      <p>Talking-head + graphics grammar: four states, cue-sheet triggers, transition rules, when to shrink vs go full-graphic.</p>
    </div></div>
    <div class="card"><div class="card-body">
      <h3><a href="ai-clip-planning.html">AI Clip Planning</a></h3>
      <div class="tags"><span class="tag">prompt discipline</span><span class="tag">style lock</span></div>
      <p>What to generate vs build, where prompts live, style-lock protocol, when NOT to generate.</p>
    </div></div>
  </div>
  <section class="block">
    <h2 class="sec">Method</h2>
    <p class="lead"><a href="analysis-protocol.html">ANALYSIS-PROTOCOL</a> — the forensic DNA-capture method, written as a repeatable protocol for the next wave of 10–20 videos.</p>
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

for fn in sorted(os.listdir(TECH)):
    if not fn.endswith('.md'): continue
    md = open(os.path.join(TECH, fn)).read()
    body = md_to_html(md)
    title = fn[:-3].replace('-', ' ').title()
    if fn == 'ANALYSIS-PROTOCOL.md': title = 'Analysis Protocol'
    html_out = PAGE.replace('{title}', title).replace('{body}', body)
    outp = os.path.join(OUT, fn[:-3] + '.html')
    open(outp, 'w').write(html_out)
    print('wrote', outp)
open(os.path.join(OUT, 'index.html'), 'w').write(INDEX)
print('wrote', os.path.join(OUT, 'index.html'))
