/* shared: copy-to-clipboard + toast */
function toast(msg) {
  let t = document.querySelector('.toast');
  if (!t) { t = document.createElement('div'); t.className = 'toast'; document.body.appendChild(t); }
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._h);
  t._h = setTimeout(() => t.classList.remove('show'), 1400);
}
function copyText(txt) {
  navigator.clipboard.writeText(txt).then(
    () => toast('Copied: ' + txt),
    () => toast('Copy failed'));
}
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-copy]').forEach(el => {
    el.addEventListener('click', e => {
      e.preventDefault();
      copyText(el.getAttribute('data-copy'));
    });
  });
});

/* chooser logic */
const STYLES = {
  'warm-editorial':       { name: 'Warm Editorial',       page: 'styles/warm-editorial.html' },
  'dark-sticker-collage': { name: 'Dark Sticker Collage', page: 'styles/dark-sticker-collage.html' },
  'neon-product-ad':      { name: 'Neon Product Ad',      page: 'styles/neon-product-ad.html' },
  'dark-fintech':         { name: 'Dark Fintech',         page: 'styles/dark-fintech.html' },
  'warm-edtech':          { name: 'Warm Ed-tech',          page: 'styles/warm-edtech.html' },
  'mono-kinetic':         { name: 'Mono Kinetic Type',    page: 'styles/mono-kinetic.html' }
};
/* option value -> style score deltas */
const SCORES = {
  q1: {
    education:  { 'warm-editorial': 3, 'warm-edtech': 2 },
    product:    { 'neon-product-ad': 3, 'warm-editorial': 1, 'dark-fintech': 1 },
    tutorial:   { 'dark-sticker-collage': 3, 'mono-kinetic': 1 },
    money:      { 'dark-fintech': 3 },
    motivate:   { 'mono-kinetic': 3, 'dark-sticker-collage': 1 }
  },
  q2: {
    learners:   { 'warm-editorial': 1, 'warm-edtech': 2 },
    customers:  { 'neon-product-ad': 2 },
    creators:   { 'dark-sticker-collage': 2, 'mono-kinetic': 1 },
    casual:     { 'dark-sticker-collage': 1, 'warm-edtech': 1 }
  },
  q3: {
    calm:    { 'warm-editorial': 2, 'warm-edtech': 1 },
    hype:    { 'neon-product-ad': 2, 'dark-sticker-collage': 2 },
    playful: { 'dark-sticker-collage': 2, 'warm-edtech': 1 },
    serious: { 'dark-fintech': 2, 'warm-editorial': 1 }
  },
  q4: {
    speaker:   { 'warm-editorial': 1, 'dark-sticker-collage': 1, 'dark-fintech': 1, 'warm-edtech': 1 },
    nospeaker: { 'mono-kinetic': 2, 'neon-product-ad': 1 }
  },
  q5: {
    full:     { 'warm-editorial': 2, 'warm-edtech': 1 },
    keywords: { 'dark-sticker-collage': 2, 'warm-editorial': 1 },
    none:     { 'neon-product-ad': 2, 'mono-kinetic': 1 }
  }
};
const MIXES = [
  ['warm-editorial', 'neon-product-ad', 'Warm Editorial base + Neon contrast chips — a premium explainer that still sells ("old way vs new way" beat).'],
  ['dark-sticker-collage', 'warm-edtech', 'Dark Sticker Collage + Warm Ed-tech cards — hype tutorial with friendly app-card explainers inside.'],
  ['mono-kinetic', 'warm-editorial', 'Mono Kinetic Type opener + Warm Editorial body — type-driven hook, then calm teaching.']
];
function initChooser() {
  const state = {};
  document.querySelectorAll('.q').forEach(q => {
    const key = q.dataset.q;
    q.querySelectorAll('.opt').forEach(btn => {
      btn.addEventListener('click', () => {
        q.querySelectorAll('.opt').forEach(b => b.classList.remove('sel'));
        btn.classList.add('sel');
        state[key] = btn.dataset.v;
        maybeScore(state);
      });
    });
  });
}
function maybeScore(state) {
  if (!['q1','q2','q3','q4','q5'].every(k => state[k])) return;
  const totals = {};
  Object.keys(STYLES).forEach(s => totals[s] = 0);
  Object.keys(state).forEach(q => {
    const d = (SCORES[q] || {})[state[q]] || {};
    Object.keys(d).forEach(s => totals[s] += d[s]);
  });
  const ranked = Object.keys(totals).sort((a,b) => totals[b] - totals[a]);
  const top = ranked[0], runner = ranked[1];
  const box = document.getElementById('result');
  box.style.display = 'block';
  let mix = MIXES.find(m =>
    (m[0] === top && m[1] === runner) || (m[0] === runner && m[1] === top));
  box.innerHTML =
    '<div class="result-card">' +
    '<h2>Your style: <a href="' + STYLES[top].page + '">' + STYLES[top].name + '</a></h2>' +
    '<p class="lead">Runner-up: <a href="' + STYLES[runner].page + '">' + STYLES[runner].name + '</a></p>' +
    (mix ? '<div class="runner"><b>Mix idea:</b> ' + mix[2] + '</div>' : '') +
    '<p style="margin-top:16px"><a class="btn" href="' + STYLES[top].page + '">Open the ' + STYLES[top].name + ' playbook &rarr;</a></p>' +
    '</div>';
  box.scrollIntoView({ behavior: 'smooth', block: 'center' });
}
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('chooser')) initChooser();
});
