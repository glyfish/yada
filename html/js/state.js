import van from "../vendor/van-1.5.5.min.js";

const { state } = van;

export const isLoading  = state(false);
export const statusText = state("");
export const feedCount  = state(0);
export const sessionId  = state(null);
export const textValue  = state("");

// Mutable ref to the textarea DOM element, assigned once in app.js.
export const inputEl = { ref: null };

// Clear the request textarea after a request has been consumed (result rendered,
// or a form-driven flow completed). Resets both the reactive value and the DOM.
export function clearInput() {
    textValue.val = "";
    if (inputEl.ref) {
        inputEl.ref.value = "";
        inputEl.ref.style.height = "auto";
    }
}
