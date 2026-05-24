import van from "../vendor/van-1.5.5.min.js";
import { isLoading, statusText, feedCount, sessionId, textValue, inputEl } from "./state.js";
import { prependResultCard, startNewChat, updateResponsesHeader, fillLastCardMeta } from "./feed.js";
import { handleResumeRequest, YADA_REQUEST_STREAM } from "./api.js";
import { showFormDialog } from "./forms.js";

const { div, span, textarea, button, h3 } = van.tags;
const { add } = van;

const handleYadaRequestSubmit = async () => {
    isLoading.val = true;
    statusText.val = "Thinking...";

    const promptBeforeSend = textValue.val;

    try {
        const payload = { input: promptBeforeSend };
        if (sessionId.val) payload.session_id = sessionId.val;

        const response = await fetch(YADA_REQUEST_STREAM, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            let msg = `Request failed (${response.status})`;
            try {
                const errBody = await response.json();
                if (errBody?.detail) msg = errBody.detail;
                else if (errBody?.message) msg = errBody.message;
            } catch (_) {}
            throw new Error(msg);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = "";
        let currentEvent = "message";
        let resultHandled = false;
        let interruptData = null;

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split("\n");
            buffer = lines.pop();

            for (const line of lines) {
                if (line.startsWith("event:")) {
                    currentEvent = line.slice(6).trim();
                } else if (line.startsWith("data:")) {
                    const raw = line.slice(5).trim();
                    let parsed;
                    try { parsed = JSON.parse(raw); } catch (_) { continue; }

                    if (currentEvent === "status" && parsed.text) {
                        statusText.val = parsed.text;
                    } else if (currentEvent === "result" && !resultHandled) {
                        resultHandled = true;
                        if (parsed.session_id) sessionId.val = parsed.session_id;
                        statusText.val = "";
                        isLoading.val = false;
                        await prependResultCard(promptBeforeSend, parsed.result ?? "");
                        textValue.val = "";
                        if (inputEl.ref) {
                            inputEl.ref.value = "";
                            inputEl.ref.style.height = "auto";
                        }
                    } else if (currentEvent === "interrupt" && !resultHandled) {
                        resultHandled = true;
                        interruptData = parsed;
                    } else if (currentEvent === "meta") {
                        fillLastCardMeta(parsed);
                    } else if (currentEvent === "error") {
                        throw new Error(parsed.message || "Unknown stream error");
                    }
                    currentEvent = "message";
                }
            }
        }

        if (interruptData) {
            isLoading.val = false;
            statusText.val = "";
            showFormDialog(interruptData.form_schema, interruptData.session_id, promptBeforeSend);
            return;
        }
    } catch (err) {
        alert(`Error: ${err.message}`);
    } finally {
        isLoading.val = false;
        statusText.val = "";
    }
};

inputEl.ref = textarea({
    rows: 4,
    placeholder: "Ask something...",
    disabled: () => isLoading.val,
    oninput: e => {
        e.target.style.height = "auto";
        e.target.style.height = e.target.scrollHeight + "px";
        textValue.val = e.target.value;
    },
});

add(document.getElementById("app"),
    div(
        div({ class: "input-container" },
            inputEl.ref,
            div({ class: "button-wrapper", style: "margin-top: .5rem; display:flex; gap:.5rem;" },
                button({ class: "btn primary", onclick: handleYadaRequestSubmit, disabled: () => isLoading.val }, "Submit"),
                button({ class: "btn secondary", onclick: startNewChat, disabled: () => isLoading.val }, "New Chat"),
            ),
            div({
                class: "status-bar",
                style: () => statusText.val ? "visibility:visible" : "visibility:hidden",
            },
                div({ class: "status-spinner" }),
                span(() => statusText.val),
            ),
            h3({
                id: "responses-header",
                style: "display:none; margin-top:4rem;",
            }, "YADA Responses"),
            div({ id: "results-feed", class: "markdown-feed" }),
        )
    )
);
