"""Every registered App page's JavaScript must parse.

A page is a Python string. Nothing in the toolchain reads it: pytest does not, pyright
does not, and the MCP server happily serves a file whose script cannot be parsed. The
client is the first thing that tries, and when it fails there is no error anywhere --
the host mounts the iframe, the static HTML renders, and the page simply sits at
whatever its markup says before any script runs.

That is exactly how it failed: one stray quote in `series_picker_app.py` opened a
string literal that swallowed the rest of the file, so the whole IIFE was never
evaluated. No `ui/initialize`, no message listener, no `reportSize` -- the picker
mounted, showed "Waiting for search results..." and "No series yet." forever, clipped
at the host's default height. The tool had returned ten rows.

So the parse is checked here, against whichever JS engine the machine has. These tests
skip rather than fail when there is none, because a skip is honest about what was not
checked; a machine with no engine should not be able to report a green page.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

import mcp_server.server as S

SCRIPT = re.compile(r"<script\b[^>]*>(.*?)</script>", re.S)


def _engine():
    """(kind, path) for a JS engine that can parse without executing, or None.

    `node --check` parses a classic script and runs nothing. JavaScriptCore, reached
    through `osascript -l JavaScript`, is on every mac; `new Function(src)` there
    compiles the body and never calls it. Both report the syntax error's message.
    """
    node = shutil.which("node")
    if node:
        return ("node", node)
    if sys.platform == "darwin":
        osa = shutil.which("osascript")
        if osa:
            return ("osascript", osa)
    return None


ENGINE = _engine()
needs_engine = pytest.mark.skipif(
    ENGINE is None, reason="no JavaScript engine (node or macOS osascript) on this machine")


def _syntax_error(source: str) -> str | None:
    """The engine's message if `source` does not parse, else None."""
    kind, exe = ENGINE
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
        fh.write(source)
        path = fh.name
    try:
        if kind == "node":
            done = subprocess.run([exe, "--check", path], capture_output=True, text=True)
            return None if done.returncode == 0 else (done.stderr.strip() or "parse failed")
        jxa = (
            "ObjC.import('Foundation');\n"
            "var p = '%s';\n"
            "var s = ObjC.unwrap($.NSString."
            "stringWithContentsOfFileEncodingError(p, $.NSUTF8StringEncoding, null));\n"
            "try { new Function(s); 'OK' } catch (e) { 'ERR ' + e.name + ': ' + e.message }\n"
        ) % path
        done = subprocess.run([exe, "-l", "JavaScript", "-e", jxa],
                              capture_output=True, text=True)
        out = done.stdout.strip()
        if done.returncode != 0:
            return done.stderr.strip() or "osascript failed"
        return None if out == "OK" else out
    finally:
        Path(path).unlink(missing_ok=True)


def _pages():
    """(uri, html) for every page the server registers, stamped as it is served."""
    return [(uri, S._stamp(html)) for uri, html, *_ in S._APP_PAGES]


def test_there_are_pages_to_check():
    """Guards the two ways this suite could pass by checking nothing: an empty registry,
    and a `_stamp` signature that no longer takes the HTML."""
    pages = _pages()
    assert pages, "_APP_PAGES is empty -- these tests would pass vacuously"
    for uri, html in pages:
        assert "<script" in html, f"{uri} has no script tag; the regex below finds nothing"


@needs_engine
@pytest.mark.parametrize("uri", [uri for uri, *_ in S._APP_PAGES])
def test_the_page_script_parses(uri):
    html = dict(_pages())[uri]
    blocks = SCRIPT.findall(html)
    assert blocks, f"{uri}: no <script> body extracted"
    for i, body in enumerate(blocks):
        err = _syntax_error(body)
        assert err is None, f"{uri} script #{i} does not parse -- {err}"


@needs_engine
def test_the_check_really_catches_a_broken_page():
    """Pins the harness, not a page. A parse check that cannot fail is decoration, and
    this one has three moving parts (temp file, engine choice, return-code reading)."""
    assert _syntax_error("var a = 1;") is None
    # The exact shape of the real defect: a stray quote that opens a string and runs off
    # the end of the file.
    assert _syntax_error("var a = 'x' + ('y')'\nvar b = 2;") is not None
