"""The MCP App that displays a chart.

Why an App rather than returning an image block (see
``sefer/planning/yada-mcp-migration-plan.md`` §5.4): a tool result means the *client*
decides how output appears, and Goose collapses images behind an "Output" expander.
An App means yada decides — and it is the only component that can read
``hostContext.theme``, which a plain tool never sees.

The contract this page implements, all verified against Goose 1.52.0:

* ``ui/initialize`` — ``protocolVersion`` sits at **params** level, not inside
  ``appCapabilities``; getting that wrong fails with a zod error naming the path.
  Declaring ``availableDisplayModes`` is also what makes Goose draw its own
  fullscreen chrome.
* ``ui/notifications/tool-result`` — how the chart arrives. The host pushes the
  originating tool's result to the app, so one static resource serves every call.
* ``ui/notifications/size-changed`` — **mandatory**. Inline height is app-driven and
  defaults to 200px, so without this every chart is clipped.
* ``ui/request-display-mode`` — self-promotion to fullscreen. Its reply is useless
  (it returns the *previous* mode), so never branch on it.

How Goose decides to render an App at all
-----------------------------------------
Read out of the shipped 1.52.0 binary, because getting this wrong is silent — the
chart still arrives, just folded into an accordion:

* ``get_tool_resource_uri`` reads **``_meta["ui"]["resourceUri"]`` and nothing else**.
  The flat ``ui/resourceUri`` string does not occur anywhere in the agent binary; it is
  honoured only by a bundled mcp-apps SDK helper the desktop path never reaches. So the
  flat and namespaced keys below are for *other* hosts, and are worth exactly nothing
  here. ``is_tool_visible_to_app`` likewise reads only ``_meta["ui"]["visibility"]``.
* It reads that off the **tool definition** from its cached ``tools/list``, matched by
  name — never off the call result. ``remove_untrusted_mcp_app_meta`` deletes any
  server-sent binding from the result's ``_meta`` before Goose inserts its own, so
  stamping the result is not merely unnecessary, it is defeated on purpose.
* Nothing is required of the server's ``initialize`` result. The capability check is
  host-side: Goose looks up ``io.modelcontextprotocol/ui`` in its *own* declared
  capabilities.
* The "Output" accordion is **not** a fallback — it renders for every result block
  regardless. With a binding the App mounts in addition, below it. "Chart appears only
  inside Output" therefore means no binding was found, not that rendering failed.

A caveat left unresolved: Goose caches ``tools/list`` in process, and this server
advertises ``tools.listChanged: false``, so a changed ``_meta`` may not reach a running
client until the extension is toggled or Goose restarts. When the nested key was added
nobody called the tool in the eight minutes between the server restart and the client
restart, so which one carried the fix was never established. If a ``_meta`` edit ever
looks ignored, restart Goose before doubting the server.
"""

HTML = r"""<!doctype html>
<html><head><meta charset="utf-8"><style>
 *{box-sizing:border-box}
 :root{--fg:#1a1a1a;--muted:#666;--line:rgba(0,0,0,.08);--rule:rgba(0,0,0,.22)}
 html{background:transparent}
 html,body{height:auto;min-height:100%;margin:0}
 body{font:13px/1.5 -apple-system,system-ui,sans-serif;color:var(--fg);padding:10px}
 .wrap{display:flex;flex-direction:column;gap:10px}
 /* pre-wrap lives on the prose runs, not the whole note: inside a table it would
    turn the markup's own indentation into visible text nodes between cells. */
 .note{white-space:normal}
 .note .para{white-space:pre-wrap}
 /* The line above the series key titles the whole block, so it is centred over it.
    Only that one: ordinary agent commentary stays left, where prose belongs. */
 .note .caption{text-align:center;margin-bottom:6px}
 .note h2{font-size:15px;margin:0 0 4px}
 /* The series key. The chart's legend can only carry ids -- the median FRED title is
    81 characters, about as wide as the whole plot -- so this table is what names them,
    and it has to be readable at a glance: ruled columns, headers centred over them. */
 /* margin-inline auto centres the key under its centred caption and over the chart,
    which is centred too -- the three line up as one column. */
 .note table{border-collapse:collapse;margin:2px auto 8px;font-size:12px;
             border:1px solid var(--rule)}
 .note th,.note td{padding:4px 10px;border-right:1px solid var(--rule);
                   text-align:left;vertical-align:top}
 .note th:last-child,.note td:last-child{border-right:0}
 .note th{text-align:center;font-weight:600;white-space:nowrap;
          border-bottom:1px solid var(--rule)}
 /* The fixed-width columns stay on one line; only the title is allowed to wrap, or a
    229-character series name drags the table past the panel. */
 .note td{white-space:nowrap}
 .note td:last-child{white-space:normal}
 .note tbody tr + tr td{border-top:1px solid var(--line)}
 /* Cap the chart rather than filling the feed column. The PNGs are far larger
    than they need to be -- bar charts render at dpi=300, ~2529x1967 -- so left
    at width:100% they dominate the conversation. Controlling this is the point
    of using an App: the client would otherwise decide. --plot-max is raised
    when the app goes fullscreen. */
 :root{--plot-max:720px}
 /* margin-inline:auto centres the chart in the feed column, which is much wider
    than the cap. */
 img{display:block;width:100%;max-width:var(--plot-max);height:auto;
     margin-inline:auto;border-radius:6px;border:1px solid var(--line)}
 .bar{display:flex;gap:8px;align-items:center;justify-content:center;
      color:var(--muted);font-size:11px}
 button{font:inherit;font-size:11px;padding:3px 9px;border:1px solid #c7c7c7;
        border-radius:5px;background:#fafafa;cursor:pointer}
 .empty{color:var(--muted);font-style:italic}
</style></head><body>
<div class="wrap">
  <div class="note" id="note"></div>
  <div id="figs"></div>
  <div class="bar">
    <button id="full">fullscreen</button>
    <span id="meta"></span>
  </div>
</div>
<script>
var note = document.getElementById('note'),
    figs = document.getElementById('figs'),
    meta = document.getElementById('meta'),
    theme = 'light', lastH = -1, hostCaps = '?';

// Fullscreen is worth nothing if the chart stays capped, so the cap tracks the
// display mode. 'none' lets the image fill whatever the host gives us.
function setMode(mode){
  document.documentElement.style.setProperty(
    '--plot-max', (mode === 'fullscreen' || mode === 'standalone') ? 'none' : '720px');
  setTimeout(reportSize, 0);
}

function notify(method, params){
  parent.postMessage({jsonrpc:'2.0', method:method, params:params || {}}, '*');
}
function rpc(method, params, ms){
  return new Promise(function(res, rej){
    var id = 'yada-' + Math.floor(performance.now()*1000);
    function onMsg(e){
      var d = e.data; if(!d || d.id !== id) return;
      window.removeEventListener('message', onMsg);
      d.error ? rej(new Error(JSON.stringify(d.error))) : res(d.result);
    }
    window.addEventListener('message', onMsg);
    parent.postMessage({jsonrpc:'2.0', id:id, method:method, params:params}, '*');
    setTimeout(function(){ window.removeEventListener('message', onMsg);
                           rej(new Error('no reply')); }, ms || 8000);
  });
}

// Inline height is the one dimension an app controls. Without this the card is
// clipped at the host's 200px default. Guarded: resizing the frame resizes the
// body, which would otherwise re-fire this forever.
function reportSize(){
  var h = Math.ceil(document.documentElement.scrollHeight);
  if (Math.abs(h - lastH) < 2) return;
  lastH = h;
  notify('ui/notifications/size-changed', {height: h});
}

function escapeHtml(s){
  return String(s).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];
  });
}

// The agent's commentary is light markdown: "## Title" and "- **bold** item".
// Render just enough of it; anything unrecognised stays literal text.
function inlineMd(s){
  return escapeHtml(s)
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
}

// A pipe table row, and the |---|---| rule that marks the line above it as a header.
function isRow(l){ return !!l && /^\s*\|.*\|\s*$/.test(l); }
function isRule(l){ return !!l && /^\s*\|[\s:|-]*-[\s:|-]*\|\s*$/.test(l); }
// Split on unescaped pipes only. Thousands of FRED titles contain a '|', which the
// server escapes as '\|'; splitting on every pipe would give those rows an extra cell.
function cellsOf(l){
  return l.trim().replace(/^\|/, '').replace(/\|$/, '').split(/(?<!\\)\|/)
          .map(function(c){ return c.trim().replace(/\\\|/g, '|'); });
}

function tableHtml(head, body){
  var th = head.map(function(c){ return '<th>' + inlineMd(c) + '</th>'; }).join('');
  var tr = body.map(function(r){
    return '<tr>' + r.map(function(c){
      return '<td>' + inlineMd(c) + '</td>';
    }).join('') + '</tr>';
  }).join('');
  return '<table><thead><tr>' + th + '</tr></thead><tbody>' + tr + '</tbody></table>';
}

// The series key arrives as a markdown pipe table. Space-padded columns cannot align
// in this page's proportional font, so the pipes are what carry the structure and the
// table is rebuilt as real HTML here. Everything else stays prose.
function renderNote(text){
  if(!text){ note.innerHTML = ''; return; }
  var lines = String(text).split('\n'), out = [], prose = [], i = 0;
  // `caption` marks a prose run that immediately precedes a table -- the summary line
  // a plot tool puts above its series key. That one is centred; ordinary commentary,
  // which can run to paragraphs, is not. Tagged here rather than matched in CSS with
  // :has(+ table) so the rule does not depend on a selector the host may not support.
  function flush(caption){
    // Blank lines around a table are the separator, not content: left in, pre-wrap
    // renders them as an empty row above or below it.
    while (prose.length && !prose[0].trim()) prose.shift();
    while (prose.length && !prose[prose.length - 1].trim()) prose.pop();
    if (prose.length) {
      out.push('<div class="para' + (caption ? ' caption' : '') + '">'
               + inlineMd(prose.join('\n')) + '</div>');
    }
    prose = [];
  }
  while (i < lines.length) {
    if (isRow(lines[i]) && isRule(lines[i + 1])) {
      flush(true);
      var head = cellsOf(lines[i]);
      i += 2;
      var body = [];
      while (i < lines.length && isRow(lines[i])) { body.push(cellsOf(lines[i])); i++; }
      out.push(tableHtml(head, body));
    } else {
      prose.push(lines[i]);
      i++;
    }
  }
  flush(false);
  note.innerHTML = out.join('');
}

function render(result){
  var content = (result && result.content) || [];
  var texts = [], images = [];
  content.forEach(function(b){
    if (b.type === 'text' && b.text) texts.push(b.text);
    // Wire format is camelCase even though mcp 2.x names the field mime_type.
    else if (b.type === 'image' && b.data) images.push(b);
  });

  renderNote(texts.join('\n\n'));
  figs.innerHTML = '';
  images.forEach(function(b){
    var img = document.createElement('img');
    img.src = 'data:' + (b.mimeType || 'image/png') + ';base64,' + b.data;
    img.alt = 'chart';
    img.addEventListener('load', reportSize);
    figs.appendChild(img);
  });
  if (!images.length && !texts.length) {
    figs.innerHTML = '<div class="empty">No chart was returned.</div>';
  }
  meta.textContent = (images.length
    ? images.length + (images.length > 1 ? ' charts' : ' chart') + ' · ' + theme
    : theme) + ' · build __BUILD__ · host: ' + hostCaps;
  reportSize();
}

// The host pushes the originating tool's result here, which is what lets one
// static resource serve every call.
window.addEventListener('message', function(e){
  var d = e.data;
  if (!d || !d.method) return;
  if (d.method === 'ui/notifications/tool-result') render(d.params);
  if (d.method === 'ui/notifications/host-context-changed' && d.params) {
    if (d.params.theme) { theme = d.params.theme; }
    // The reply to our own display-mode request reports the PREVIOUS mode, so
    // this notification is the only trustworthy signal that it changed.
    if (d.params.displayMode) setMode(d.params.displayMode);
    reportSize();
  }
});

document.getElementById('full').addEventListener('click', function(){
  // Reply is the *previous* mode, so it tells us nothing — fire and forget.
  rpc('ui/request-display-mode', {mode:'fullscreen'}, 6000).catch(function(){});
});

// protocolVersion at params level; availableDisplayModes gates the host's own chrome.
rpc('ui/initialize', {
  protocolVersion: '2026-01-26',
  appInfo: {name:'yada-plot', version:'1.0.0'},
  appCapabilities: {availableDisplayModes: ['inline','fullscreen']}
}, 8000).then(function(res){
  var ctx = (res && res.hostContext) || {};
  // Diagnostic, and the answer to whether a picker App is possible at all. Goose
  // bundles the MCP Apps schema for `serverTools` ("Host can proxy tool calls to the
  // MCP server"), `message` (the view posts a user turn) and `updateModelContext` --
  // but whether it ADVERTISES them is a different question, and the only place the
  // answer appears is the ui/initialize reply. Remove once it has been read once.
  hostCaps = Object.keys((res && res.hostCapabilities) || {}).join(',') || 'none';
  theme = ctx.theme || 'light';
  setMode(ctx.displayMode || 'inline');
  notify('ui/notifications/initialized', {});
  meta.textContent = theme + ' · build __BUILD__ · host: ' + hostCaps;
  reportSize();
}).catch(function(err){
  meta.textContent = 'handshake failed: ' + err.message;
  reportSize();
});

window.addEventListener('resize', reportSize);
if (window.ResizeObserver) new ResizeObserver(reportSize).observe(document.body);
reportSize();
</script>
</body></html>
"""

#: The `_meta` shapes `Apps.tool` does NOT supply: flat (deprecated) and namespaced,
#: so a host picks up whichever it reads. Neither is read by Goose (see above) — they
#: are here for hosts that are not Goose, and must never be mistaken for the binding.
#:
#: The *nested* form — ``_meta["ui"]`` — is the current spec, and it is the one Goose
#: actually reads. `Apps.tool` stamps that itself and raises on a `meta` carrying a
#: "ui" key, so this helper must leave it out. That makes this the decorator's
#: companion and **incomplete on its own**; `app_meta` is the whole binding.
def meta_for(resource_uri: str, visibility: list[str]) -> dict:
    return {
        "ui/resourceUri": resource_uri,
        "ui/visibility": visibility,
        "io.modelcontextprotocol/ui": {
            "resourceUri": resource_uri,
            "visibility": visibility,
        },
    }


def app_meta(resource_uri: str, visibility: list[str]) -> dict:
    """The full App binding, for a tool registered with `server.add_tool`.

    Needed by any tool defined *after* `MCPServer` is constructed, which cannot use
    the decorator. Passing `meta_for` alone there looks right and does nothing: the
    tool advertises `ui/resourceUri`, so every server-side check finds the App, while
    Goose — reading only the nested entry — finds none, falls back to rendering the
    tool result, and collapses the chart behind an "Output" expander. Which is the
    exact failure the App exists to avoid.
    """
    return {
        **meta_for(resource_uri, visibility),
        "ui": {"resourceUri": resource_uri, "visibility": list(visibility)},
    }
