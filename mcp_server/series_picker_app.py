"""The MCP App that builds a report from a search: pick series, then save.

This is the MCP-native form of the browser's two-step create flow
(`html/js/forms.js:197` `showSeriesSelectionTable` -> `showCreateReportForm`). The
table, the client-side filter and the "selection survives filtering" behaviour are
ported from there; what is new is how the page is fed and how it writes back, because
there is no suspended graph on this surface and no session to resume.

The three legs, all read out of the shipped Goose bundle rather than docs
(`/Applications/Goose.app/Contents/Resources/app.asar`, build dated Sep 23):

* **Prefill in** -- ``ui/notifications/tool-input``, whose params the host documents as
  "Complete tool call arguments as key-value pairs". ``plot_app.py`` does not listen for
  this, which is why an earlier reading of *this repo* concluded the route did not
  exist; the host sends it (``sendToolInput``). Repo silence is not host absence.
* **Rows in** -- ``ui/notifications/tool-result``. Its params are *nearly* the standard
  MCP result: the host rebuilds every block through a whitelist that drops unknown block
  types and ``annotations``, strips the server's ``_meta``, and renames
  ``structuredContent`` to ``rawOutput``. So the page reads both names and falls back to
  the JSON text block, which is the leg proven in production. ``plot_app.py`` reads only
  ``content[]`` by choice, not by constraint.
* **Writes out** -- a ``tools/call`` request posted to the host, which forwards it to
  this same server (``e.tools && (this.oncalltool = ... this._client.request({method:
  'tools/call', ...}))``). ``serverTools`` IS advertised: the host's capability literal
  is ``{... serverTools:{}, serverResources:{}, logging:{}, message:{text:{}}}``.

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

The one string not proven from the bundle is the App-side method name. The host's
handler is registered against a minified schema alias imported from the MCP SDK chunk,
and the only ``tools/call`` schema literal in the bundle lives 1.5MB away in that chunk,
so ``tools/call`` is inference rather than observation. It is therefore surfaced as a
visible error rather than a silent no-op: if the first Create reports
"the host refused tools/call", that inference is wrong and nothing was written. The
server log settles it either way -- a proxied call reaches `request_log.py` like any
other.

Why the page writes the report itself instead of handing cache_ids back to the model:
a proxied call is invisible to the model and to the transcript, which is the cost of
this route, but it is also the whole point. The browser picker's ids are retyped by
router-model turns on the way to `create_report` (see the report-flow trace), and a
dropped or reordered id there is not an error -- it silently produces a report short a
series. Here the ids never leave the page. The consequence to live with is that the
chat shows nothing after a successful save, so the page renders its own confirmation
and names the report_id.
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
 input,textarea{font:inherit;color:inherit;background:var(--field);
   border:1px solid var(--line);border-radius:5px;padding:5px 7px;width:100%}
 input:focus,textarea:focus{outline:1px solid var(--accent);border-color:var(--accent)}
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
 /* Only the title may wrap: FRED titles run to 482 characters, so the unbounded
    column has to be the one that is allowed to take the slack. */
 td.title{white-space:normal;min-width:16em}
 tr.row{cursor:pointer}
 tr.row:hover{background:rgba(0,0,0,.03)}
 tr.sel{background:var(--sel)}
 td.num{text-align:right;font-variant-numeric:tabular-nums}
 code{font:11px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace}
 .grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
 .field label{display:block;font-size:11px;color:var(--muted);margin-bottom:2px}
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
 #done{display:flex;flex-direction:column;gap:3px;font-size:12px;color:var(--muted);
   border-top:1px solid var(--line);padding-top:6px;margin-top:2px}
 #done .good{color:var(--good);font-weight:500}
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
    <h1 id="head">Create Time Series Report</h1>
    <div class="sub" id="sub">Waiting for search results&hellip;</div>
  </div>

  <div id="picker">
    <input id="filter" type="text" placeholder="Filter by id, title or units&hellip;"
           autocomplete="off" autocapitalize="off" spellcheck="false">
    <div class="tablewrap">
      <table>
        <thead><tr>
          <th style="width:2rem"><input id="all" type="checkbox" title="Select all shown"></th>
          <th>ID</th><th>Title</th><th>Units</th><th>Freq</th>
          <th class="num">Pop.</th><th>Start</th><th>End</th>
        </tr></thead>
        <tbody id="rows"></tbody>
      </table>
      <div id="empty" class="empty">No series yet.</div>
    </div>

    <div class="grid" style="margin-top:8px">
      <div class="field"><label for="title">Report title</label>
        <input id="title" type="text" placeholder="e.g. Commodity Prices"></div>
      <div class="field"><label for="desc">Description</label>
        <input id="desc" type="text" placeholder="optional"></div>
      <div class="field"><label for="from">From (YYYY-MM-DD)</label>
        <input id="from" type="text" placeholder="earliest of the selection"></div>
      <div class="field"><label for="to">To (YYYY-MM-DD)</label>
        <input id="to" type="text" placeholder="blank = track latest"></div>
      <div class="field"><label for="tags">Tags (comma separated)</label>
        <input id="tags" type="text" placeholder="e.g. energy, inflation"></div>
      <div class="field"><label for="note">Note</label>
        <input id="note" type="text" placeholder="optional remark"></div>
    </div>

    <div class="bar" style="margin-top:8px">
      <div class="status" id="status"></div>
      <button id="create" class="primary" disabled>Create</button>
    </div>
  </div>

  <div id="done" class="hide"></div>
  <div class="meta" id="meta"></div>
</div>
<script>
(function(){
var theme = 'light', lastH = 0, hostCaps = '?';
var mode = 'inline';       // tracked off host-context-changed; see the listener
var all = [];              // every row the search returned
var sel = new Map();       // series_id -> row; survives filtering, as in forms.js
var toolArgs = null;       // ui/notifications/tool-input
var envelope = null;       // the FredHits envelope, for total/detail/status

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
  if (sc && Array.isArray(sc.series)) return sc;
  var blocks = result.content || [];
  for (var i = 0; i < blocks.length; i++){
    var b = blocks[i];
    if (b && b.type === 'text' && b.text){
      try {
        var o = JSON.parse(b.text);
        if (o && Array.isArray(o.series)) return o;
      } catch (_){ /* a human-readable block, not the payload */ }
    }
  }
  return null;
}

function describeSearch(){
  var a = toolArgs || {};
  var bits = [];
  if (a.category) bits.push('category "' + a.category + '"');
  if (a.query) bits.push('"' + a.query + '"');
  if (a.frequency) bits.push(a.frequency);
  return bits.join(' + ');
}

function render(result){
  envelope = rowsFrom(result);
  if (!envelope){
    // A non-ok envelope (ambiguous_filter, unresolvable_filter, no_match) legitimately
    // carries zero rows and the next step in `detail`, so show that rather than "empty".
    var sc = (result && (result.structuredContent || result.rawOutput)) || {};
    $('sub').textContent = sc.detail || 'The search returned nothing this page can read.';
    $('picker').classList.add('hide');
    reportSize();
    return;
  }
  all = envelope.series || [];
  var what = describeSearch();
  var head = all.length
    ? all.length + ' of ' + (envelope.total || all.length).toLocaleString()
      + ' matches, most popular first'
    : (envelope.detail || 'Nothing matched.');
  $('sub').textContent = what ? head + ' · ' + what : head;
  // No prefilled title. Deriving one from the search produced report names like
  // "Prices > House Price Indexes" -- a category path, not a title, and identical for
  // every report built from the same search, which makes resolving a report by title
  // ambiguous. The heading above already says what was searched; the title is the one
  // thing the user has to supply, and Create refuses an empty one.
  applyFilter();
  reportSize();
}

// ---- the table (ported from forms.js:197) --------------------------------------
function td(text, cls){
  var c = document.createElement('td');
  if (cls) c.className = cls;
  c.textContent = text == null ? '' : String(text);
  return c;
}

function draw(rows){
  var tb = $('rows');
  tb.innerHTML = '';
  $('empty').style.display = rows.length ? 'none' : '';
  $('empty').textContent = all.length ? 'No row matches the filter.' : 'No series yet.';
  rows.forEach(function(r){
    var tr = document.createElement('tr');
    tr.className = 'row' + (sel.has(r.series_id) ? ' sel' : '');
    var cc = document.createElement('td');
    var cb = document.createElement('input');
    cb.type = 'checkbox'; cb.checked = sel.has(r.series_id);
    cc.appendChild(cb);
    var idc = document.createElement('td');
    var code = document.createElement('code');
    code.textContent = r.series_id || '';
    idc.appendChild(code);
    tr.append(cc, idc, td(r.title, 'title'), td(r.units), td(r.frequency_class),
              td(r.popularity, 'num'), td(r.observation_start), td(r.observation_end));
    function toggle(on){
      on ? sel.set(r.series_id, r) : sel.delete(r.series_id);
      tr.classList.toggle('sel', on); cb.checked = on; refresh();
    }
    tr.addEventListener('click', function(e){
      if (e.target !== cb) toggle(!sel.has(r.series_id));
    });
    cb.addEventListener('change', function(){ toggle(cb.checked); });
    tb.appendChild(tr);
  });
  reportSize();
}

// Blank the form after a save, so the next report starts clean instead of inheriting
// the last one's title, dates and tags -- the title especially, since Create refuses an
// empty one and two reports sharing a name are ambiguous to every tool that resolves a
// report by title. Keep this list in step with the fields the Create handler reads; the
// search results and the filter are deliberately NOT cleared, because they describe what
// is on screen rather than what is being written.
function clearForm(){
  ['title','desc','from','to','tags','note'].forEach(function(id){ $(id).value = ''; });
  // `from` prefills with the earliest start in the selection until the user types in it.
  // Clearing the value without clearing that flag would leave the prefill switched off
  // for every later report in this session.
  delete $('from').dataset.touched;
}

function shown(){
  var q = $('filter').value.trim().toLowerCase();
  if (!q) return all;
  return all.filter(function(r){
    return (r.series_id || '').toLowerCase().indexOf(q) >= 0
        || (r.title || '').toLowerCase().indexOf(q) >= 0
        || (r.units || '').toLowerCase().indexOf(q) >= 0;
  });
}
function applyFilter(){ draw(shown()); refresh(); }

function refresh(){
  var n = sel.size;
  $('create').disabled = n === 0;
  $('create').textContent = n ? 'Create (' + n + ')' : 'Create';
  var vis = shown();
  $('all').checked = vis.length > 0 && vis.every(function(r){ return sel.has(r.series_id); });
  // Default the range to the earliest start in the selection, as the browser form does.
  // ISO dates sort lexicographically, so a string min is a date min.
  if (!$('from').dataset.touched){
    var starts = [];
    sel.forEach(function(r){ if (r.observation_start) starts.push(r.observation_start); });
    $('from').value = starts.length ? starts.reduce(function(a,b){ return a < b ? a : b; }) : '';
  }
}

$('filter').addEventListener('input', applyFilter);
$('from').addEventListener('input', function(){ $('from').dataset.touched = '1'; });
$('all').addEventListener('change', function(){
  var on = $('all').checked;
  shown().forEach(function(r){ on ? sel.set(r.series_id, r) : sel.delete(r.series_id); });
  draw(shown());
});

// ---- writing back ---------------------------------------------------------------
// The host forwards this to the same MCP server, so `res` is a CallToolResult.
function callTool(name, args){
  return rpc('tools/call', {name: name, arguments: args}, 120000).then(function(res){
    var sc = (res && res.structuredContent) || null;
    if (!sc){
      var blocks = (res && res.content) || [];
      for (var i = 0; i < blocks.length; i++){
        if (blocks[i] && blocks[i].type === 'text'){
          try { sc = JSON.parse(blocks[i].text); break; } catch (_){ }
        }
      }
    }
    if (res && res.isError) {
      throw new Error((sc && sc.detail) || (name + ' failed'));
    }
    // yada's tools report refusals in the body with status:"error", not as isError.
    if (sc && sc.status && sc.status !== 'ok'){
      throw new Error(sc.detail || (name + ': ' + sc.status));
    }
    return sc || {};
  });
}

$('create').addEventListener('click', function(){
  var picks = [];
  sel.forEach(function(r){ picks.push(r); });
  if (!picks.length) return;
  var title = $('title').value.trim();
  if (!title){ say('Give the report a title.', 'bad'); $('title').focus(); return; }

  $('create').disabled = true;
  var ids = [], failed = [];

  // Sequential on purpose: each fetch hits the upstream source, and the browser form
  // fetches one at a time for the same reason. The ids never leave this page.
  function step(i){
    if (i >= picks.length){
      if (failed.length){
        say('Could not fetch ' + failed.join(', ') + '. Deselect those and retry.', 'bad');
        $('create').disabled = false;
        return;
      }
      say('Saving the report…');
      return callTool('create_report', {
        report_title: title,
        report_description: $('desc').value.trim(),
        cache_ids: ids,
        date_from: $('from').value.trim(),
        date_to: $('to').value.trim() || null,
        // Split here rather than sending the raw string: the tool takes a list, and
        // the server lowercases and dedupes, so what comes back is what was stored.
        tags: $('tags').value.split(',').map(function(s){ return s.trim(); })
                               .filter(function(s){ return s.length; }),
        note: $('note').value.trim()
      }).then(function(rep){
        // The picker STAYS. Hiding it on success was wrong twice over: this page's whole
        // premise is that it remains usable while results accumulate, and a form that
        // vanishes when you submit it reads as the host having torn the frame down --
        // which is exactly how it got reported. Each save appends a line instead, so a
        // session that builds three reports leaves three ids on screen.
        var name = rep.report_title || title;
        $('done').classList.remove('hide');
        var line = document.createElement('div');
        line.innerHTML = '<span class="good">Saved “' + esc(name) + '”</span> with '
          + ids.length + ' series · <code>' + esc(rep.report_id || '?') + '</code>'
          // Echo the stored tags, not the typed ones: they are lowercased and deduped on
          // write, so "Energy, energy" comes back as one tag and the user should see which.
          + ((rep.tags && rep.tags.length)
               ? ' · tagged <code>' + esc(rep.tags.join(', ')) + '</code>' : '');
        $('done').appendChild(line);
        // Ready for the next one: the rows and the filter stay, the selection does not.
        // applyFilter redraws the checkboxes and refresh re-disables Create until
        // something is picked again.
        sel.clear();
        clearForm();
        applyFilter();
        say('Saved. Pick more series to build another report, or ask to “plot ' + name
            + '” — a proxied call is invisible to the chat, so it will not draw itself.',
            'good');
        reportSize();
      }).catch(fail);
    }
    var r = picks[i];
    say('Fetching ' + (i+1) + ' of ' + picks.length + ': ' + r.series_id + '…');
    return callTool('fetch_fred_series', {series_id: r.series_id})
      .then(function(e){ if (e.cache_id) ids.push(e.cache_id); else failed.push(r.series_id); })
      .catch(function(){ failed.push(r.series_id); })
      .then(function(){ return step(i+1); });
  }

  function fail(err){
    var m = String(err && err.message || err);
    // The one inferred string in this page. If the host has no tools/call handler the
    // whole write-back route is wrong, and saying so beats a dead button.
    if (/method not found|unknown method|unhandled/i.test(m)){
      say('The host refused tools/call, so nothing was written. This App cannot save '
          + 'on this client.', 'bad');
    } else {
      say(m, 'bad');
    }
    $('create').disabled = false;
    reportSize();
  }
  step(0);
});

// ---- host handshake (ported from plot_app.py, which proves this part) -----------
window.addEventListener('message', function(e){
  var d = e.data;
  if (!d || !d.method) return;
  if (d.method === 'ui/notifications/tool-input' && d.params){
    toolArgs = d.params.arguments || d.params;
    if (!envelope) $('sub').textContent = 'Searching ' + (describeSearch() || '…');
    reportSize();
  }
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
  appInfo: {name:'yada-series-picker', version:'1.0.0'},
  appCapabilities: {availableDisplayModes: ['inline','fullscreen']}
}, 8000).then(function(res){
  var ctx = (res && res.hostContext) || {};
  hostCaps = Object.keys((res && res.hostCapabilities) || {}).join(',') || 'none';
  theme = ctx.theme || 'light';
  document.documentElement.setAttribute('data-theme', theme);
  notify('ui/notifications/initialized', {});
  // Inline, deliberately: no `ui/request-display-mode` here. `availableDisplayModes`
  // still declares fullscreen, so the host may offer its own expand control; what
  // changed is that the PAGE no longer decides. See the module docstring for why.
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
