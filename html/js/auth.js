// One place every request goes through, so there is one place a 401 is handled.
//
// Before this there were eight independent fetch() call sites across three modules and
// no common path, which meant "prompt for a token when the server asks for one" had
// nowhere to live. `request()` is that path; everything else here exists to serve it.
//
// The token is NOT held in JavaScript. POST /api/session hands it to the server, which
// returns it as an HttpOnly cookie, and from then on the browser attaches it to every
// same-origin fetch by itself -- fetch defaults to credentials: "same-origin". So no
// call site passes a credential, and nothing in this file can read one back. That
// matters here specifically: the feed renders model-authored markdown into innerHTML by
// design, and anything reachable from JavaScript is reachable from that.

let promptOpen = null;   // the in-flight prompt, so parallel 401s share one dialog

/** Current identity, or {authenticated:false}. Never throws, never 401s. */
export async function whoami() {
    try {
        const r = await fetch("/api/session");
        return r.ok ? await r.json() : { authenticated: false, required: true };
    } catch {
        return { authenticated: false, required: false };
    }
}

/** Exchange a token for the cookie. Returns the session body, or throws on a bad token. */
export async function signIn(token) {
    const r = await fetch("/api/session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token }),
    });
    if (!r.ok) {
        const body = await r.json().catch(() => ({}));
        throw new Error(body.detail || `Sign-in failed (${r.status})`);
    }
    return r.json();
}

export async function signOut() {
    await fetch("/api/session", { method: "DELETE" });
}

function askForToken(message) {
    // Deduped: a page that fires four requests at once must not stack four dialogs.
    if (promptOpen) return promptOpen;
    promptOpen = (async () => {
        try {
            for (;;) {
                const token = window.prompt(
                    `${message}\n\nPaste your yada token:`);
                if (!token) return false;                  // cancelled -- give up, do not loop
                try {
                    await signIn(token.trim());
                    return true;
                } catch (e) {
                    message = e.message;                   // show why, ask again
                }
            }
        } finally {
            promptOpen = null;
        }
    })();
    return promptOpen;
}

/**
 * fetch(), with one retry after a successful sign-in.
 *
 * Only ONE retry: if the server answers 401 again with a token it just accepted, the
 * problem is not the credential and looping would hide that behind an endless prompt.
 */
export async function request(url, options = {}) {
    let response = await fetch(url, options);
    if (response.status !== 401) return response;

    const body = await response.clone().json().catch(() => ({}));
    const signedIn = await askForToken(body.detail || "This server requires a token.");
    if (!signedIn) return response;                        // caller sees the original 401

    response = await fetch(url, options);
    return response;
}
