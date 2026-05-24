import { isLoading, statusText, sessionId, inputEl, textValue } from "./state.js";
import { prependResultCard } from "./feed.js";

export const YADA_REQUEST_STREAM = "/api/request/stream";
export const YADA_REQUEST_RESUME = "/api/request/resume";

export async function handleResumeRequest(resumeSessionId, formData, promptLabel) {
    isLoading.val = true;
    statusText.val = "Processing...";
    try {
        const response = await fetch(YADA_REQUEST_RESUME, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ session_id: resumeSessionId, form_data: formData }),
        });
        if (!response.ok) {
            let msg = `Resume failed (${response.status})`;
            try { const e = await response.json(); msg = e?.detail || e?.message || msg; } catch (_) {}
            throw new Error(msg);
        }
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = "";
        let currentEvent = "message";
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
                    } else if (currentEvent === "result") {
                        statusText.val = "";
                        isLoading.val = false;
                        if (parsed.session_id) sessionId.val = parsed.session_id;
                        await prependResultCard(promptLabel, parsed.result ?? "");
                        textValue.val = "";
                        if (inputEl.ref) {
                            inputEl.ref.value = "";
                            inputEl.ref.style.height = "auto";
                        }
                    } else if (currentEvent === "error") {
                        throw new Error(parsed.message || "Unknown resume error");
                    }
                    currentEvent = "message";
                }
            }
        }
    } catch (err) {
        alert(`Error: ${err.message}`);
    } finally {
        isLoading.val = false;
        statusText.val = "";
    }
}
