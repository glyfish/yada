import { marked } from "../vendor/marked.esm.js";

marked.setOptions({
    highlight(code, lang) {
        if (window.hljs && lang && window.hljs.getLanguage(lang)) {
            return window.hljs.highlight(code, { language: lang }).value;
        }
        return window.hljs ? window.hljs.highlightAuto(code).value : code;
    },
    gfm: true,
    breaks: false,
});


// Protect LaTeX so Marked won't touch underscores/dollars.
// Order matters: $$...$$ first, then $...$, then \( \), then \[ \].
// Dollar-delimited math is normalized to \(...\) / \[...\] so that bare $
// characters in data values (prices, units) never trigger MathJax.
export function protectMathBlocks(md) {
    const blocks = [];
    const token = i => `@@MATH${i}@@`;
    const re = /(\$\$[\s\S]*?\$\$)|(\$[^\n$]+\$)|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]/g;
    const text = String(md || "").replace(re, m => {
        let normalized = m;
        if (m.startsWith('$$') && m.endsWith('$$')) {
            normalized = '\\[' + m.slice(2, -2) + '\\]';
        } else if (m.startsWith('$') && m.endsWith('$') && m.length > 1) {
            normalized = '\\(' + m.slice(1, -1) + '\\)';
        }
        const t = token(blocks.length);
        blocks.push(normalized);
        return t;
    });
    return { text, blocks };
}

// Restore tokens with minimal HTML escaping so < and > inside math
// don't get parsed as tags before MathJax typesets them.
export function restoreMathTokens(html, blocks) {
    let out = String(html || "");
    const esc = s => s
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    blocks.forEach((m, i) => {
        const t = `@@MATH${i}@@`;
        out = out.split(t).join(esc(m));
    });
    return out;
}

// Clamp very large markdown bodies (keep head + tail).
export function clampMarkdown(md, max) {
    const text = String(md ?? "");
    if (!max || text.length <= max) {
        return { text, truncated: false, full: text };
    }
    const head = text.slice(0, Math.floor(max * 0.65));
    const tail = text.slice(-Math.floor(max * 0.25));
    const fenceOpen = (head.match(/```/g) || []).length % 2 === 1;
    const middle = "\n\n…\n\n<!-- clipped -->\n\n";
    const safeHead = fenceOpen ? (head + "\n```") : head;
    return { text: safeHead + middle + tail, truncated: true, full: text };
}

// Render markdown + syntax highlight + MathJax into a container element.
export async function renderMarkdownInto(container, mdText) {
    const { text, blocks } = protectMathBlocks(mdText || "");
    let html = marked.parse(text);
    html = html.replace(/<del>([\s\S]*?)<\/del>/g, '$1');
    html = restoreMathTokens(html, blocks);
    container.innerHTML = html;
    if (window.hljs) {
        container.querySelectorAll("pre code").forEach(b => window.hljs.highlightElement(b));
    }
    if (window.MathJax?.typesetPromise) {
        if (window.MathJax.typesetClear) MathJax.typesetClear([container]);
        await window.MathJax.typesetPromise([container]).catch(() => {});
    }
}
