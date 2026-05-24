import van from "../vendor/van-1.5.5.min.js";

const { state } = van;

export const isLoading  = state(false);
export const statusText = state("");
export const feedCount  = state(0);
export const sessionId  = state(null);
export const textValue  = state("");

// Mutable ref to the textarea DOM element, assigned once in app.js.
export const inputEl = { ref: null };
