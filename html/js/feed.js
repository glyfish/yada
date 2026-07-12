import { feedCount, sessionId, inputEl, textValue } from "./state.js";
import { renderMarkdownInto, clampMarkdown } from "./markdown.js";

const FEED_MAX_CARDS = 40;
export const FEED_MAX_CHARS = 80000;

let lastCard = null;

// Fill the meta footer of the most recently prepended card.
export function fillLastCardMeta(meta) {
    const footer = lastCard?.querySelector(".result-meta");
    if (!footer || !meta) return;
    const parts = [];
    if (meta.total_tokens > 0) {
        parts.push(
            `${meta.total_tokens.toLocaleString()} tokens ` +
            `(${meta.input_tokens.toLocaleString()} in / ${meta.output_tokens.toLocaleString()} out)`
        );
    }
    if (meta.cost_usd > 0) {
        parts.push(`$${meta.cost_usd.toPrecision(4)}`);
    }
    if (meta.trace_url) {
        parts.push(`<a href="${meta.trace_url}" target="_blank" rel="noopener">LangSmith trace</a>`);
    }
    footer.innerHTML = parts.join('<span style="color:#ccc">|</span>');
}

export async function prependResultCard(userPrompt, markdown) {
    const feed = document.getElementById("results-feed");
    const sc = document.scrollingElement || document.documentElement;
    const before = sc.scrollTop, prevH = sc.scrollHeight;

    const card = document.createElement("section");
    card.className = "result-card";

    const head = document.createElement("div");
    head.className = "result-head";
    head.textContent = new Date().toLocaleString();

    const body = document.createElement("div");
    body.className = "result-body";

    const qDiv = document.createElement("div");
    qDiv.className = "user-question";
    qDiv.innerHTML = `<span class="label">Request</span><div class="text"></div>`;
    qDiv.querySelector(".text").textContent = userPrompt || "";

    const aDiv = document.createElement("div");
    aDiv.className = "markdown-output";

    body.appendChild(qDiv);
    body.appendChild(aDiv);

    const metaFooter = document.createElement("div");
    metaFooter.className = "result-meta";

    card.appendChild(head);
    card.appendChild(body);
    card.appendChild(metaFooter);
    lastCard = card;

    feed.insertBefore(card, feed.firstChild);
    feedCount.val = feed.children.length;
    updateResponsesHeader();

    const clamped = clampMarkdown(markdown, FEED_MAX_CHARS);
    await renderMarkdownInto(aDiv, clamped.text);

    if (clamped.truncated) {
        const moreRow = document.createElement("div");
        moreRow.style = "display:flex;justify-content:flex-end;padding:.5rem .9rem;";
        const btn = document.createElement("button");
        btn.className = "btn";
        btn.textContent = "Show full";
        btn.onclick = async () => {
            btn.disabled = true;
            await renderMarkdownInto(aDiv, clamped.full);
            moreRow.remove();
        };
        moreRow.appendChild(btn);
        card.appendChild(moreRow);
    }

    const delta = sc.scrollHeight - prevH;
    sc.scrollTop = before + delta;

    while (feed.children.length > FEED_MAX_CARDS) {
        feed.removeChild(feed.lastChild);
    }
    feedCount.val = feed.children.length;
    updateResponsesHeader();
}

export function startNewChat() {
    sessionId.val = null;
    const feed = document.getElementById("results-feed");
    while (feed.firstChild) feed.removeChild(feed.firstChild);
    feedCount.val = 0;
    updateResponsesHeader();
    textValue.val = "";
    if (inputEl.ref) {
        inputEl.ref.value = "";
        inputEl.ref.style.height = "auto";
    }
}

export function updateResponsesHeader() {
    const h = document.getElementById("responses-header");
    if (!h) return;
    h.style.display = feedCount.val > 0 ? "block" : "none";
}
