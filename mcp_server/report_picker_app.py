"""The MCP App that picks a saved report and plots it.

The MCP-native form of the browser's report picker (`html/js/forms.js`), and the
counterpart to `series_picker_app.py`: that one *writes* a report, this one *chooses*
one. The difference in what they do with the choice is the whole design, because the
Goose host constrains it in two ways that were read out of the shipped bundle
(`/Applications/Goose.app/Contents/Resources/app.asar`, build dated Sep 23) rather
than from docs:

* **A page cannot dismiss itself.** `ui/notifications/request-teardown` exists only as
  an orphaned schema literal in the SDK chunk, with zero occurrences in Goose's own
  chunk, and `ui/resource-teardown` is reachable only through the SDK renderer's
  `useImperativeHandle` -- Goose renders a component that takes no ref. Unmounting is
  React cleanup keyed on the transcript row. So "select, then the view closes" is not
  available at all, and this page no longer approximates it by leaving an overlay: it
  renders inline and stays put while the chart arrives underneath it.

* **A page cannot mount another page.** Mounting is decided from
  `_meta.goose.mcpApp`, which goosed synthesizes Rust-side; the server's own result
  `_meta` never reaches the decider, and a proxied `tools/call` runs no mount logic at
  all -- its result comes straight back to the calling frame. So this page cannot
  proxy `plot_report` and have the chart appear: it would get base64 PNG bytes back
  and have to draw them itself, which is a second renderer, and this repo has already
  paid for a second renderer once (see `TimeSeriesReportPlotAgent.report_plot`'s
  docstring on the five tools that drifted).

So the hand-off goes through `ui/message`, whose handler passes the first text block
to `append` -- which is `handleSubmit`, the composer's own submit path. The model then
calls `plot_report` and the chart mounts the ordinary way. That is not an imitation of
the existing plot path, it IS the existing plot path, which is the point: no second
renderer, no divergence to keep in sync.

The cost is one model turn carrying one `report_id`. That is acceptable here and was
not acceptable for `series_picker_app.py`, and the asymmetry is worth stating: N
cache_ids retyped by a model can be silently dropped or reordered, and a report short
a series still looks like a valid report. One report_id either resolves or fails
loudly in `plot_report`. So the picker writes its own report but delegates its own
plot.

Frames stack rather than replace -- each App-bound result is a new transcript row with
a new React key, and the earlier page keeps its DOM, its JS state and a working proxy.
So this page deliberately stays usable after plotting: pick another report and another
chart appears below it. The table is not torn down and the selection is not cleared.

**Display mode: inline, and the page never asks for anything else.** Both pickers
first self-promoted to `fullscreen`, on the reasoning that a form wants a modal and
`modal` is not one of the three modes. Three findings out of the bundle say inline is
the right default instead:

* `fullscreen` in this host is literally an overlay: the same container div gains
  `fixed inset-0 z-[1000]` while an invisible spacer holds its place in the transcript.
  So it covers the transcript these pages are trying to add to, which contradicts the
  premise that results stack underneath the picker.
* The mode is `useState` local to ONE transcript row, and the transcript render site
  passes neither `displayMode` nor `onDisplayModeChange`. Nothing outside the component
  stores it, so any remount of that row silently returns to `inline`. Inline is the only
  mode that is stable by construction.
* On the first real use the view was reported as dismissed on Create. Most of that was
  this page hiding its own form on success -- a behaviour since removed -- which reads
  exactly like the host tearing the frame down. The page's proxied `tools/call` is
  provably not a host-side cause of anything: that leg is a pass-through that writes
  nothing to the message store and touches no display-mode state, and the session
  database holds no row at all for the write. Inline, the frame demonstrably survives
  the write; whether the overlay additionally closed on its own was never settled, and
  not entering it makes the question moot.

What is NOT a reason, and was wrongly given as one before: losing page state. A mode
change does not remount the iframe -- the effect that creates it is keyed
`[t.permissions, t.url.href]` and the URL carries no nonce -- so switching modes is safe.
It is the ROW unmounting, not the mode change, that reloads a page from scratch.
`availableDisplayModes` still declares `fullscreen`, which is what makes the host draw
its own expand control; what changed is that the page no longer decides.
"""

HTML = r"""<!doctype html>
<html><head><meta charset="utf-8"><style>
 *{box-sizing:border-box}
 :root{--fg:#1a1a1a;--muted:#666;--line:rgba(0,0,0,.08);--rule:rgba(0,0,0,.22);
        --sel:rgba(0,110,220,.10);--bg:transparent;--field:rgba(0,0,0,.03);
        --accent:#0a66c2;--bad:#b3261e;--good:#17683a}
 html{background:var(--bg)}
 /* No min-height. The frame's height is whatever this page last reported, so
    `min-height:100%` pins the body to that height and scrollHeight can never fall
    below it: the card would stay tall after the picker hides itself, and the table
    rule below would ratchet upward instead of settling. */
 html,body{height:auto;margin:0}
 body{font:13px/1.5 -apple-system,system-ui,sans-serif;color:var(--fg);padding:10px}
 .wrap{display:flex;flex-direction:column;gap:8px}
 h1{font-size:14px;margin:0;font-weight:600}
 .sub{color:var(--muted);font-size:12px}
 input{font:inherit;color:inherit;background:var(--field);
   border:1px solid var(--line);border-radius:5px;padding:5px 7px;width:100%}
 input:focus{outline:1px solid var(--accent);border-color:var(--accent)}
 /* A pixel cap, not `vh`. Inline, the frame's height comes from what this page
    reports, measured from content that includes this table -- so a `vh` cap makes the
    table a fraction of a height the table itself determines. That loop converges, but
    only after a dozen resize round-trips, and it settles wherever the host happened
    to open. */
 .tablewrap{max-height:300px;overflow:auto;border:1px solid var(--line);border-radius:6px}
 table{border-collapse:collapse;width:100%;font-size:12px}
 thead th{position:sticky;top:0;background:#fafafa;text-align:left;font-weight:600;
   padding:5px 7px;border-bottom:1px solid var(--rule);white-space:nowrap}
 td{padding:4px 7px;border-bottom:1px solid var(--line);white-space:nowrap}
 /* Title and the member list are the two unbounded columns, so they take the slack. */
 td.title{white-space:normal;min-width:12em}
 td.members{white-space:normal;min-width:14em}
 tr.row{cursor:pointer}
 tr.row:hover{background:rgba(0,0,0,.03)}
 tr.sel{background:var(--sel)}
 tr.plotted td.title::after{content:' (plotted)';color:var(--muted);font-weight:400}
 td.num{text-align:right;font-variant-numeric:tabular-nums}
 code{font:11px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace}
 .bar{display:flex;gap:8px;align-items:center;justify-content:space-between}
 button{font:inherit;padding:6px 12px;border-radius:6px;border:1px solid var(--line);
   background:var(--field);color:inherit;cursor:pointer}
 button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
 button[disabled]{opacity:.45;cursor:default}
 .status{font-size:12px;color:var(--muted);min-height:1.4em}
 .status.bad{color:var(--bad)}
 .status.good{color:var(--good)}
 .meta{color:var(--muted);font-size:11px;border-top:1px solid var(--line);padding-top:6px}
 .empty{color:var(--muted);text-align:center;padding:14px}
 .hide{display:none}
 @media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){--fg:#e8e8e8;--muted:#9a9a9a;
    --line:rgba(255,255,255,.12);--rule:rgba(255,255,255,.26);
    --field:rgba(255,255,255,.06);--sel:rgba(80,160,255,.16);--accent:#4c9aff;
    --bad:#ff8a80;--good:#6ee7a0}
  :root:not([data-theme="light"]) thead th{background:#1e1e1e}
  :root:not([data-theme="light"]) tr.row:hover{background:rgba(255,255,255,.05)}
 }
 :root[data-theme="dark"]{--fg:#e8e8e8;--muted:#9a9a9a;--line:rgba(255,255,255,.12);
   --rule:rgba(255,255,255,.26);--field:rgba(255,255,255,.06);
   --sel:rgba(80,160,255,.16);--accent:#4c9aff;--bad:#ff8a80;--good:#6ee7a0}
 :root[data-theme="dark"] thead th{background:#1e1e1e}
</style></head>
<body><div class="wrap">
  <div>
    <h1 id="head">Plot Time Series Report</h1>
    <div class="sub" id="sub">Waiting for your reports&hellip;</div>
  </div>

  <div id="picker">
    <input id="filter" type="text"
           placeholder="Filter by title, description or series id&hellip;"
           autocomplete="off" autocapitalize="off" spellcheck="false">
    <div class="tablewrap">
      <table>
        <thead><tr>
          <th>Title</th><th>Series</th><th class="num">#</th><th>From</th><th>To</th>
        </tr></thead>
        <tbody id="rows"></tbody>
      </table>
      <div id="empty" class="empty">No reports yet.</div>
    </div>

    <div class="bar" style="margin-top:8px">
      <div class="status" id="status"></div>
      <button id="plot" class="primary" disabled>Plot</button>
    </div>
  </div>

  <div class="meta" id="meta"></div>
</div>
<script>
(function(){
var theme = 'light', lastH = 0, hostCaps = '?';
var mode = 'inline';       // tracked off host-context-changed; see the listener
var all = [];              // every report the tool returned
var sel = null;            // the one chosen report; survives filtering and plotting
var plotted = {};          // report_id -> true, so the table shows what was already drawn
var envelope = null;

var $ = function(id){ return document.getElementById(id); };

function notify(method, params){
  parent.postMessage({jsonrpc:'2.0', method:method, params:params || {}}, '*');
}
function rpc(method, params, ms){
  return new Promise(function(res, rej){
    var id = 'yada-' + Math.floor(performance.now()*1000) + '-' + Math.floor(Math.random()*1e6);
    function onMsg(e){
      var d = e.data; if(!d || d.id !== id) return;
      window.removeEventListener('message', onMsg);
      d.error ? rej(new Error(d.error.message || JSON.stringify(d.error))) : res(d.result);
    }
    window.addEventListener('message', onMsg);
    parent.postMessage({jsonrpc:'2.0', id:id, method:method, params:params}, '*');
    setTimeout(function(){ window.removeEventListener('message', onMsg);
                           rej(new Error('no reply from host')); }, ms || 20000);
  });
}

// Inline height is the one dimension an app controls; without this the card is clipped
// at the host's 200px default. Guarded, or resizing the frame re-fires forever.
function reportSize(){
  // Measure the BODY's border box, not `documentElement.scrollHeight`. The latter is
  // floored by the VIEWPORT -- which is the height this page itself last asked for --
  // so it can only ever grow. That is why the card kept its full height and showed a
  // screenful of blank space once the table was hidden: the shrink was never reported.
  // The body is `height:auto` with `box-sizing:border-box`, so its own box is the
  // content height and is free to fall.
  var b = document.body;
  var h = Math.ceil(b.getBoundingClientRect().height || b.scrollHeight);
  if (Math.abs(h - lastH) < 2) return;
  lastH = h; notify('ui/notifications/size-changed', {height: h});
}

function esc(s){
  return String(s == null ? '' : s).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];
  });
}
function say(msg, kind){
  var el = $('status');
  el.className = 'status' + (kind ? ' ' + kind : '');
  el.textContent = msg || '';
  reportSize();
}

// ---- reading the payload -------------------------------------------------------
// Goose RENAMES this field on the notification leg: `ui/notifications/tool-result`
// rebuilds the result through a whitelist that replaces `structuredContent` with
// `rawOutput` (the proxy leg leaves it alone, so `callTool` below keeps the standard
// name). Both are read here, then the JSON-in-a-text block as a last resort -- that
// one is the leg proven in production. Anything else leaves `all` empty, not a throw.
function rowsFrom(result){
  if (!result) return null;
  var sc = result.structuredContent || result.rawOutput;
  if (sc && Array.isArray(sc.reports)) return sc;
  var blocks = result.content || [];
  for (var i = 0; i < blocks.length; i++){
    var b = blocks[i];
    if (b && b.type === 'text' && b.text){
      try { var o = JSON.parse(b.text); if (o && Array.isArray(o.reports)) return o; }
      catch (_){ }
    }
  }
  return null;
}

function render(result){
  var env = rowsFrom(result);
  if (!env){
    say('The host sent a result this page could not read.', 'bad');
    return;
  }
  envelope = env;
  all = env.reports || [];
  if (env.status && env.status !== 'ok'){
    say(env.detail || ('the tool reported ' + env.status), 'bad');
  }
  $('sub').textContent = all.length === 1 ? '1 saved report'
                                          : all.length + ' saved reports';
  applyFilter();
}

function members(r){
  var s = r.series || [];
  return s.join(', ');
}

// Filtering reads the member ids too, so "DCOILWTICO" finds a report whose TITLE does
// not say it. That is client-side only: no tool can filter reports by content today.
function matches(r, q){
  if (!q) return true;
  var hay = [r.report_title, r.report_description, members(r)].join(' ').toLowerCase();
  return hay.indexOf(q) !== -1;
}

function applyFilter(){
  var q = $('filter').value.trim().toLowerCase();
  var shown = all.filter(function(r){ return matches(r, q); });
  var tb = $('rows');
  tb.textContent = '';
  shown.forEach(function(r){
    var tr = document.createElement('tr');
    tr.className = 'row'
      + (sel && sel.report_id === r.report_id ? ' sel' : '')
      + (plotted[r.report_id] ? ' plotted' : '');
    tr.innerHTML =
        '<td class="title">' + esc(r.report_title || '(untitled)')
      + (r.report_description
           ? '<div class="sub">' + esc(r.report_description) + '</div>' : '')
      + '</td>'
      + '<td class="members"><code>' + esc(members(r)) + '</code></td>'
      + '<td class="num">' + esc(r.series_count) + '</td>'
      + '<td>' + esc(r.time_range_from) + '</td>'
      + '<td>' + esc(r.time_range_to || 'latest') + '</td>';
    tr.addEventListener('click', function(){ choose(r); });
    tb.appendChild(tr);
  });
  $('empty').className = shown.length ? 'empty hide' : 'empty';
  if (!shown.length && all.length){
    $('empty').textContent = 'No report matches "' + q + '".';
  } else if (!all.length){
    $('empty').textContent = 'No saved reports. Create one first.';
  }
  reportSize();
}

function choose(r){
  sel = r;
  $('plot').disabled = false;
  say('');
  applyFilter();
}

function fail(err){
  var m = (err && err.message) || String(err);
  // The one inferred leg: if ui/message is not how a page asks the host to send a
  // turn, say so rather than leaving a dead button. Also catches the standalone
  // window, whose render site passes no `append` handler at all.
  if (/not found|unsupported|unknown method|not available/i.test(m)){
    m = 'The host refused ui/message (' + m + '), so nothing was plotted.';
  }
  say(m, 'bad');
  $('plot').disabled = false;
}

$('filter').addEventListener('input', applyFilter);

$('plot').addEventListener('click', function(){
  if (!sel) return;
  var r = sel, id = r.report_id, title = r.report_title || id;
  $('plot').disabled = true;
  say('Plotting ' + title + '…');

  // Drop out of the overlay first, if the user put us there with the host's own expand
  // control -- otherwise they would be left staring at the picker with the chart behind
  // it. `mode` is tracked off `host-context-changed`, which is the only honest source;
  // the reply to this very request reports the mode from before the change. Not
  // awaited: postMessage delivers in order, so the host applies this before the message
  // below, and waiting would only buy a timeout.
  if (mode !== 'inline') rpc('ui/request-display-mode', {mode:'inline'}, 6000).catch(function(){});

  // Name the parameter, so the model passes the id and not the whole sentence.
  // plot_report resolves a UUID before a title, and an id that does not resolve
  // fails loudly -- which is why one id through a model turn is acceptable here.
  rpc('ui/message', {
    role: 'user',
    content: [{type: 'text', text: 'Plot the report with report_id ' + id}]
  }, 20000).then(function(){
    plotted[id] = true;
    $('plot').disabled = false;
    say('Plotting ' + title + ' — the chart appears below. '
        + 'Pick another report to plot it too.', 'good');
    applyFilter();
  }).catch(fail);
});

// ---- host handshake (ported from plot_app.py, which proves this part) -----------
window.addEventListener('message', function(e){
  var d = e.data;
  if (!d || !d.method) return;
  if (d.method === 'ui/notifications/tool-result') render(d.params);
  if (d.method === 'ui/notifications/host-context-changed' && d.params){
    if (d.params.theme){
      theme = d.params.theme;
      document.documentElement.setAttribute('data-theme', theme);
    }
    // This notification is the ONLY way to learn the display mode. The reply to
    // `ui/request-display-mode` reports the mode from BEFORE the change, because the
    // bridge answers that request out of its stored host context while a separate raw
    // postMessage listener applies the change -- so the reply is useless and the host
    // tells you here instead. Matters because the host draws its own expand control:
    // the page can be in fullscreen without ever having asked.
    if (d.params.displayMode) mode = d.params.displayMode;
    reportSize();
  }
});

// protocolVersion sits at params level, not inside appCapabilities: getting that wrong
// fails with a zod error naming the path. Declaring availableDisplayModes is what makes
// the host draw its own chrome.
rpc('ui/initialize', {
  protocolVersion: '2026-01-26',
  appInfo: {name:'yada-report-picker', version:'1.0.0'},
  appCapabilities: {availableDisplayModes: ['inline','fullscreen']}
}, 8000).then(function(res){
  var ctx = (res && res.hostContext) || {};
  hostCaps = Object.keys((res && res.hostCapabilities) || {}).join(',') || 'none';
  theme = ctx.theme || 'light';
  document.documentElement.setAttribute('data-theme', theme);
  notify('ui/notifications/initialized', {});
  // Inline, deliberately -- and here it also removes a contradiction: this page's whole
  // premise is that the chart appears UNDERNEATH it and the picker stays usable, which
  // an overlay makes impossible. `availableDisplayModes` still declares fullscreen so
  // the host may offer its own expand control.
  $('meta').textContent = 'build __BUILD__ · ' + theme + ' · host: ' + hostCaps;
  reportSize();
}).catch(function(err){
  $('meta').textContent = 'handshake failed: ' + err.message;
  reportSize();
});

window.addEventListener('resize', reportSize);
if (window.ResizeObserver) new ResizeObserver(reportSize).observe(document.body);
reportSize();
})();
</script>
</body></html>
"""
