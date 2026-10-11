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
"""

HTML = r"""<!doctype html>
<html><head><meta charset="utf-8"><style>
 *{box-sizing:border-box}
 :root{--fg:#1a1a1a;--muted:#666;--line:rgba(0,0,0,.08)}
 html{background:transparent}
 html,body{height:auto;min-height:100%;margin:0}
 body{font:13px/1.5 -apple-system,system-ui,sans-serif;color:var(--fg);padding:10px}
 .wrap{display:flex;flex-direction:column;gap:10px}
 .note{white-space:pre-wrap}
 .note h2{font-size:15px;margin:0 0 4px}
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
    theme = 'light', lastH = -1;

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
function renderNote(text){
  if(!text){ note.innerHTML = ''; return; }
  var html = escapeHtml(text)
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  note.innerHTML = html;
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
    : theme) + ' · build __BUILD__';
  reportSize();
}

// The host pushes the originating tool's result here, which is what lets one
// static resource serve every call.
window.addEventListener('message', function(e){
  var d = e.data;
  if (!d || !d.method) return;
  if (d.method === 'ui/notifications/tool-result') render(d.params);
  if (d.method === 'ui/notifications/host-context-changed' && d.params) {
    if (d.params.theme) { theme = d.params.theme; meta.textContent = theme; }
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
  theme = ctx.theme || 'light';
  setMode(ctx.displayMode || 'inline');
  notify('ui/notifications/initialized', {});
  meta.textContent = theme + ' · build __BUILD__';
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

#: Every known `_meta` shape at once — nested (current spec), flat (deprecated), and
#: namespaced — so a host picks up whichever it reads. Goose reads the nested form
#: with a flat fallback and checks no server capability, so this is belt and braces.
def meta_for(resource_uri: str, visibility: list[str]) -> dict:
    return {
        "ui/resourceUri": resource_uri,
        "ui/visibility": visibility,
        "io.modelcontextprotocol/ui": {
            "resourceUri": resource_uri,
            "visibility": visibility,
        },
    }
