import { handleResumeRequest } from "./api.js";
import { prependResultCard, fillLastCardMeta } from "./feed.js";
import { sessionId as sessionIdState, clearInput } from "./state.js";

// Render the create-time-series-report form into `dialog`. Works both as a fresh
// dialog (from the form dispatcher) and as an in-place transition from the series
// selection table (dialog already open) — it only appends/opens when needed.
function showCreateReportForm(dialog, prefill, sessionId, promptLabel) {
    prefill = prefill || {};
    dialog.classList.remove("report-picker", "series-select");
    dialog.innerHTML = `
        <form method="dialog" novalidate autocomplete="off">
            <label for="tsr-title">Title:</label>
            <input id="tsr-title" name="report_title" type="text" placeholder="Report title" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

            <label for="tsr-description">Description:</label>
            <textarea id="tsr-description" name="report_description" rows="3" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Brief description of this report" required></textarea>

            <label for="tsr-ids">Time Series IDs:</label>
            <input id="tsr-ids" name="time_series_ids" type="text" placeholder="id-001, id-002, id-003" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

            <label for="tsr-from">Start Time:</label>
            <input id="tsr-from" name="time_range_from" type="date" autocomplete="off" required>

            <label for="tsr-to">End Time (omit for latest):</label>
            <input id="tsr-to" name="time_range_to" type="date" autocomplete="off">

            <menu>
                <button type="button" class="btn" id="cancelFormBtn">Cancel</button>
                <button type="button" class="btn primary" id="submitFormBtn">Create Report</button>
            </menu>
        </form>
    `;
    if (!dialog.isConnected) document.body.appendChild(dialog);
    if (!dialog.open) dialog.showModal();

    const titleInput       = dialog.querySelector("input[name='report_title']");
    const descriptionInput = dialog.querySelector("textarea[name='report_description']");
    const idsInput         = dialog.querySelector("input[name='time_series_ids']");
    const fromInput        = dialog.querySelector("input[name='time_range_from']");
    const toInput          = dialog.querySelector("input[name='time_range_to']");

    if (prefill.report_title)       titleInput.value       = prefill.report_title;
    if (prefill.report_description) descriptionInput.value = prefill.report_description;
    if (prefill.time_series_ids)    idsInput.value         = prefill.time_series_ids;
    if (prefill.time_range_from)    fromInput.value        = prefill.time_range_from;
    if (prefill.time_range_to)      toInput.value          = prefill.time_range_to;

    requestAnimationFrame(() => titleInput.focus());

    const close = () => { sessionIdState.val = null; dialog.close(); dialog.remove(); };
    dialog.querySelector("#cancelFormBtn").addEventListener("click", close);
    dialog.addEventListener("cancel", e => { e.preventDefault(); close(); });

    const submit = async () => {
        if (!dialog.querySelector("form").reportValidity()) return;
        close();
        const payload = {
            report_title:       titleInput.value.trim(),
            report_description: descriptionInput.value.trim(),
            time_series_ids:    idsInput.value.trim(),
            time_range_from:    fromInput.value.trim(),
        };
        if (toInput.value.trim()) payload.time_range_to = toInput.value.trim();
        await handleResumeRequest(sessionId, payload, promptLabel);
    };
    dialog.querySelector("#submitFormBtn").addEventListener("click", submit);
    [titleInput, idsInput].forEach(
        el => el.addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); submit(); } })
    );
}

// "Create Time Series Report" step 1: run the ETF/FRED search from the prefilled
// query, present the hits as a multi-select table, then on Create fetch the picks
// into the time series cache and hand off to the create-report form.
function showSeriesSelectionTable(dialog, formSchema, sessionId, promptLabel) {
    const prefill = formSchema.prefill || {};
    // A compound report searches several stores at once — prefill carries a list of
    // {source, query} searches. Fall back to a single search_source/search_query pair.
    const searches = (Array.isArray(prefill.searches) && prefill.searches.length)
        ? prefill.searches
        : [{ source: prefill.search_source, query: prefill.search_query }];

    dialog.classList.add("report-picker", "series-select");
    dialog.innerHTML = `
        <form method="dialog" novalidate autocomplete="off">
            <h3 style="margin-top:0">Create Time Series Report</h3>
            <p style="margin:.25rem 0 .75rem;color:#888;">Select the series to include, then click Create.</p>
            <input id="ss-search" type="text" placeholder="Filter by ID, title, or source…"
                autocomplete="off" autocapitalize="off" spellcheck="false"
                style="width:100%;box-sizing:border-box;margin-bottom:.5rem;">
            <div class="report-picker-wrap">
                <table class="report-picker-table">
                    <thead>
                        <tr>
                            <th style="width:2.25rem"></th>
                            <th>ID</th><th>Title</th><th>Source</th><th>Obs Start</th><th>Obs End</th>
                        </tr>
                    </thead>
                    <tbody id="ss-tbody"></tbody>
                </table>
                <p id="ss-status" style="color:#888;text-align:center;">Searching…</p>
            </div>
            <menu>
                <button type="button" class="btn" id="cancelFormBtn">Cancel</button>
                <button type="button" class="btn primary" id="createFormBtn" disabled>Create</button>
            </menu>
        </form>
    `;
    document.body.appendChild(dialog);
    dialog.showModal();

    const tbody     = dialog.querySelector("#ss-tbody");
    const status    = dialog.querySelector("#ss-status");
    const createBtn = dialog.querySelector("#createFormBtn");
    const searchInput = dialog.querySelector("#ss-search");
    const selected  = new Map();  // source:native_id -> row (survives filtering)
    let allRows     = [];         // every search hit; the filter narrows what's rendered

    const updateCreateBtn = () => {
        createBtn.disabled = selected.size === 0;
        createBtn.textContent = selected.size ? `Create (${selected.size})` : "Create";
    };

    const renderRows = (rows) => {
        tbody.innerHTML = "";
        if (!rows.length) { status.style.display = ""; status.textContent = "No matching series found."; return; }
        status.style.display = "none";
        for (const r of rows) {
            const tr = document.createElement("tr");
            tr.className = "report-picker-row";
            tr.innerHTML = `
                <td><input type="checkbox"></td>
                <td><code>${r.native_id}</code></td>
                <td>${r.title || ""}</td>
                <td>${r.source || ""}</td>
                <td>${r.observation_start || ""}</td>
                <td>${r.observation_end || ""}</td>
            `;
            const key = `${r.source}:${r.native_id}`;  // native_id alone can collide across sources
            const cb = tr.querySelector("input[type=checkbox]");
            // Restore prior selection so checks survive filtering / re-render.
            cb.checked = selected.has(key);
            if (selected.has(key)) tr.classList.add("selected");
            const toggle = (on) => {
                if (on) { selected.set(key, r); tr.classList.add("selected"); }
                else    { selected.delete(key); tr.classList.remove("selected"); }
                cb.checked = on;
                updateCreateBtn();
            };
            tr.addEventListener("click", (e) => { if (e.target !== cb) toggle(!selected.has(key)); });
            cb.addEventListener("change", () => toggle(cb.checked));
            tbody.appendChild(tr);
        }
    };

    // Narrow the loaded rows client-side by ID / title / source. Selections persist
    // in `selected`, so hidden picks are still included when Create is clicked.
    const applyFilter = () => {
        const ql = searchInput.value.trim().toLowerCase();
        const rows = !ql ? allRows : allRows.filter(r =>
            (r.native_id || "").toLowerCase().includes(ql) ||
            (r.title || "").toLowerCase().includes(ql) ||
            (r.source || "").toLowerCase().includes(ql));
        renderRows(rows);
    };
    searchInput.addEventListener("input", applyFilter);

    (async () => {
        try {
            const perSearch = await Promise.all(searches.map(async (s) => {
                const src = String(s.source || "").toLowerCase();
                const q = s.query || "";
                if (!src || !q) return [];
                const url = `/api/series/search?source=${encodeURIComponent(src)}&q=${encodeURIComponent(q)}`;
                const resp = await fetch(url);
                if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
                return (await resp.json()).rows || [];
            }));
            // Merge all stores' rows into one table, deduped by source:native_id, order preserved.
            const merged = [];
            const seen = new Set();
            for (const rows of perSearch) {
                for (const r of rows) {
                    const key = `${r.source}:${r.native_id}`;
                    if (seen.has(key)) continue;
                    seen.add(key);
                    merged.push(r);
                }
            }
            allRows = merged;
            applyFilter();
        } catch (e) {
            status.style.display = "";
            status.textContent = `Search failed: ${e.message}`;
        }
    })();

    const close = () => { sessionIdState.val = null; dialog.close(); dialog.remove(); };
    dialog.querySelector("#cancelFormBtn").addEventListener("click", close);
    dialog.addEventListener("cancel", e => { e.preventDefault(); close(); });

    createBtn.addEventListener("click", async () => {
        if (selected.size === 0) return;
        const picks = [...selected.values()];
        createBtn.disabled = true;
        status.style.display = "";
        status.textContent = `Fetching ${picks.length} series into cache…`;

        const cacheIds = [];
        const starts = [];
        const ends = [];
        const failed = [];
        for (const p of picks) {
            try {
                const resp = await fetch("/api/series/fetch", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ source: p.source, native_id: p.native_id }),
                });
                if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
                const entry = await resp.json();
                cacheIds.push(entry.cache_id);
                if (entry.observation_start) starts.push(entry.observation_start);
                if (entry.observation_end) ends.push(entry.observation_end);
            } catch (e) {
                failed.push(p.native_id);
            }
        }

        if (failed.length) {
            status.textContent = `Failed to fetch: ${failed.join(", ")}. Deselect those and retry.`;
            updateCreateBtn();
            return;
        }

        // Default the report start to the earliest of the selected series.
        // ISO dates (YYYY-MM-DD) sort lexicographically, so string min = date min.
        // Leave the end empty so the report tracks the latest data by default.
        const carried = { ...prefill, time_series_ids: cacheIds.join(", ") };
        if (starts.length) carried.time_range_from = starts.reduce((a, b) => (a < b ? a : b));

        // Hand off to the create-report form, prefilled with the resolved cache_ids
        // and the derived time range.
        showCreateReportForm(dialog, carried, sessionId, promptLabel);
    });
}

export function showFormDialog(formSchema, sessionId, promptLabel) {
    const formType = formSchema.type;
    const dialog = document.createElement("dialog");
    dialog.className = "modal";

    if (formType === "load_research_document") {
        dialog.innerHTML = `
            <form method="dialog" novalidate autocomplete="off">
                <label for="rn-filename">Filename:</label>
                <input id="rn-filename" name="filename" type="text" placeholder="document.md" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="rn-path">Path:</label>
                <input id="rn-path" name="path" type="text" placeholder="Relative path from project root" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="rn-title">Title:</label>
                <input id="rn-title" name="title" type="text" placeholder="Document title" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="rn-authors">Authors:</label>
                <input id="rn-authors" name="authors" type="text" placeholder="Troy Stribling" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="rn-document-date">Date:</label>
                <input id="rn-document-date" name="document_date" type="date" autocomplete="off" required>

                <label for="rn-topic">Topic:</label>
                <textarea id="rn-topic" name="topic" rows="3" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="e.g., Signal Processing" required></textarea>

                <label for="rn-shelf">Shelf:</label>
                <input id="rn-shelf" name="shelf" type="text" placeholder="e.g., reading_list" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <menu>
                    <button type="button" class="btn" id="cancelFormBtn">Cancel</button>
                    <button type="button" class="btn primary" id="submitFormBtn">Load Research Document</button>
                </menu>
            </form>
        `;
        document.body.appendChild(dialog);
        dialog.showModal();

        const filenameInput = dialog.querySelector("input[name='filename']");
        const pathInput     = dialog.querySelector("input[name='path']");
        const titleInput    = dialog.querySelector("input[name='title']");
        const authorsInput  = dialog.querySelector("input[name='authors']");
        const dateInput     = dialog.querySelector("input[name='document_date']");
        const topicInput    = dialog.querySelector("textarea[name='topic']");
        const shelfInput    = dialog.querySelector("input[name='shelf']");

        requestAnimationFrame(() => filenameInput.focus());

        const close = () => { sessionIdState.val = null; dialog.close(); dialog.remove(); };
        dialog.querySelector("#cancelFormBtn").addEventListener("click", close);
        dialog.addEventListener("cancel", e => { e.preventDefault(); close(); });

        const submit = async () => {
            if (!dialog.querySelector("form").reportValidity()) return;
            close();
            await handleResumeRequest(sessionId, {
                filename:      filenameInput.value.trim(),
                path:          pathInput.value.trim(),
                title:         titleInput.value.trim(),
                authors:       authorsInput.value.trim(),
                document_date: dateInput.value,
                topic:         topicInput.value.trim(),
                shelf:         shelfInput.value.trim(),
            }, promptLabel);
        };
        dialog.querySelector("#submitFormBtn").addEventListener("click", submit);
        [filenameInput, pathInput, titleInput, authorsInput, dateInput, shelfInput].forEach(
            el => el.addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); submit(); } })
        );

    } else if (formType === "load_github_repo") {
        dialog.innerHTML = `
            <form method="dialog" novalidate autocomplete="off">
                <label for="gh-account">GitHub Account:</label>
                <input id="gh-account" name="account" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="gh-repo">Repository Name:</label>
                <input id="gh-repo" name="repo" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <menu>
                    <button type="button" class="btn" id="cancelFormBtn">Cancel</button>
                    <button type="button" class="btn primary" id="submitFormBtn">Load Repo</button>
                </menu>
            </form>
        `;
        document.body.appendChild(dialog);
        dialog.showModal();

        const accInput  = dialog.querySelector("input[name='account']");
        const repoInput = dialog.querySelector("input[name='repo']");

        // Prefer values extracted from the request; fall back to the last-used
        // account from localStorage when the request didn't name one.
        const prefill = formSchema.prefill || {};
        accInput.value  = prefill.account || localStorage.getItem("gh_account") || "";
        repoInput.value = prefill.repo || "";
        // Focus the first empty field so a fully-prefilled form is ready to submit.
        requestAnimationFrame(() => (repoInput.value ? repoInput : accInput).focus());

        const close = () => { sessionIdState.val = null; dialog.close(); dialog.remove(); };
        dialog.querySelector("#cancelFormBtn").addEventListener("click", close);
        dialog.addEventListener("cancel", e => { e.preventDefault(); close(); });

        const submit = async () => {
            if (!dialog.querySelector("form").reportValidity()) return;
            const account = accInput.value.trim();
            localStorage.setItem("gh_account", account);
            close();
            await handleResumeRequest(sessionId, {
                account,
                repo: repoInput.value.trim(),
            }, promptLabel);
        };
        dialog.querySelector("#submitFormBtn").addEventListener("click", submit);
        [accInput, repoInput].forEach(
            el => el.addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); submit(); } })
        );

    } else if (formType === "create_time_series_report") {
        // Two modes:
        //  (a) search-driven — prefill carries searches (a list of {source, query}) or a
        //      single search_query: show the "Create Time Series Report" selection table
        //      first (search -> pick -> fetch into cache), then the create form prefilled
        //      with the resulting cache_ids.
        //  (b) direct — neither present: show the create form immediately (the LLM already
        //      supplied explicit time_series_ids, or the user fills them in).
        const prefill = formSchema.prefill || {};
        const hasSearch = prefill.search_query
            || (Array.isArray(prefill.searches) && prefill.searches.length > 0);
        if (hasSearch) {
            showSeriesSelectionTable(dialog, formSchema, sessionId, promptLabel);
        } else {
            showCreateReportForm(dialog, prefill, sessionId, promptLabel);
        }

    } else if (formType === "select_time_series_report") {
        const prefill = formSchema.prefill || {};
        const filterQuery = prefill.filter_query || "";
        const filterSource = prefill.filter_source || "";
        dialog.classList.add("report-picker");
        dialog.innerHTML = `
            <form method="dialog" novalidate autocomplete="off">
                <h3 style="margin-top:0">Select Report to Plot</h3>
                <input id="rp-search" type="text" placeholder="Search by title or description…"
                    autocomplete="off" autocapitalize="off" spellcheck="false" style="width:100%;box-sizing:border-box;">
                <div id="rp-table-wrap" class="report-picker-wrap">
                    <table class="report-picker-table">
                        <thead>
                            <tr><th>Title</th><th>Description</th><th>From</th><th>To</th></tr>
                        </thead>
                        <tbody id="rp-tbody"></tbody>
                    </table>
                    <p id="rp-empty" style="display:none;color:#888;text-align:center;">No reports found.</p>
                </div>
                <menu>
                    <button type="button" class="btn" id="cancelFormBtn">Cancel</button>
                    <div style="display:flex;gap:.5rem;">
                        <button type="button" class="btn danger" id="deleteFormBtn" disabled>Delete</button>
                        <button type="button" class="btn secondary" id="editFormBtn" disabled>Edit</button>
                        <button type="button" class="btn primary" id="submitFormBtn" disabled>Plot Report</button>
                    </div>
                </menu>
            </form>
        `;
        document.body.appendChild(dialog);
        dialog.showModal();

        const searchInput  = dialog.querySelector("#rp-search");
        const tbody        = dialog.querySelector("#rp-tbody");
        const emptyMsg     = dialog.querySelector("#rp-empty");
        const submitBtn    = dialog.querySelector("#submitFormBtn");
        const editBtn      = dialog.querySelector("#editFormBtn");
        const deleteBtn    = dialog.querySelector("#deleteFormBtn");
        let selectedId     = null;

        const renderRows = (reports) => {
            tbody.innerHTML = "";
            emptyMsg.style.display = reports.length === 0 ? "" : "none";
            for (const r of reports) {
                const tr = document.createElement("tr");
                tr.className = "report-picker-row";
                tr.dataset.reportId = r.report_id;
                const to   = r.time_range_to || "latest";
                tr.innerHTML = `<td>${r.report_title}</td><td class="rp-desc">${r.report_description || ""}</td><td>${r.time_range_from}</td><td>${to}</td>`;
                tr.addEventListener("click", () => {
                    tbody.querySelectorAll("tr").forEach(row => row.classList.remove("selected"));
                    tr.classList.add("selected");
                    selectedId = r.report_id;
                    submitBtn.disabled = false;
                    editBtn.disabled = false;
                    deleteBtn.disabled = false;
                });
                tbody.appendChild(tr);
            }
        };

        // Load reports once, pre-filtered by the request's content constraint
        // (filter_query -> server-side metadata filter). The search box then narrows
        // that set client-side by title/description — no extra requests, no LLM cost.
        let allReports = [];

        const applyTextFilter = () => {
            const ql = searchInput.value.trim().toLowerCase();
            renderRows(!ql ? allReports : allReports.filter(r =>
                r.report_title.toLowerCase().includes(ql) ||
                (r.report_description || "").toLowerCase().includes(ql)));
        };

        const loadReports = async () => {
            const params = new URLSearchParams();
            if (filterQuery) params.set("filter", filterQuery);
            if (filterSource) params.set("source", filterSource);
            const url = params.toString() ? `/api/reports?${params}` : "/api/reports";
            try {
                const resp = await fetch(url);
                if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
                allReports = await resp.json();
                applyTextFilter();
            } catch (e) {
                tbody.innerHTML = `<tr><td colspan="4" style="color:red">Failed to load reports: ${e.message}</td></tr>`;
            }
        };

        loadReports();

        searchInput.addEventListener("input", () => {
            selectedId = null;
            submitBtn.disabled = true;
            editBtn.disabled = true;
            deleteBtn.disabled = true;
            applyTextFilter();
        });

        const close = () => { sessionIdState.val = null; dialog.close(); dialog.remove(); };
        dialog.querySelector("#cancelFormBtn").addEventListener("click", close);
        dialog.addEventListener("cancel", e => { e.preventDefault(); close(); });

        const submit = async () => {
            if (!selectedId) return;
            const id = selectedId;
            close();  // abandons the suspended graph; plotting is deterministic below
            // Deterministic plot — no agent, no LLM tokens.
            try {
                const resp = await fetch(`/api/reports/${id}/plot`, { method: "POST" });
                if (!resp.ok) {
                    const err = await resp.json().catch(() => ({}));
                    throw new Error(err.detail || `HTTP ${resp.status}`);
                }
                const data = await resp.json();
                await prependResultCard(`Plot report: ${data.report_title}`, data.html);
                fillLastCardMeta({ total_tokens: 0, input_tokens: 0, output_tokens: 0, cost_usd: 0 });
                clearInput();  // request fulfilled — clear the textarea like the stream/resume paths
            } catch (e) {
                await prependResultCard("Plot report", `Failed to plot report: ${e.message}`);
            }
        };
        dialog.querySelector("#submitFormBtn").addEventListener("click", submit);

        const openEditDialog = async (reportId) => {
            let report;
            try {
                const resp = await fetch(`/api/reports/${reportId}`);
                if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
                report = await resp.json();
            } catch (e) {
                alert(`Failed to load report: ${e.message}`);
                return;
            }

            const editDialog = document.createElement("dialog");
            editDialog.className = "modal";
            editDialog.innerHTML = `
                <form method="dialog" novalidate autocomplete="off">
                    <label for="ed-title">Title:</label>
                    <input id="ed-title" name="report_title" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" required>

                    <label for="ed-description">Description:</label>
                    <textarea id="ed-description" name="report_description" rows="3" autocomplete="off" autocapitalize="off" spellcheck="false" required></textarea>

                    <label for="ed-ids">Time Series IDs:</label>
                    <input id="ed-ids" name="time_series_ids" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" required>

                    <label for="ed-from">Start Time:</label>
                    <input id="ed-from" name="time_range_from" type="date" autocomplete="off" required>

                    <label for="ed-to">End Time:</label>
                    <input id="ed-to" name="time_range_to" type="date" autocomplete="off">

                    <menu>
                        <button type="button" class="btn" id="cancelEditBtn">Cancel</button>
                        <button type="button" class="btn primary" id="saveEditBtn">Save</button>
                    </menu>
                </form>
            `;
            document.body.appendChild(editDialog);

            const titleInput = editDialog.querySelector("input[name='report_title']");
            const descInput  = editDialog.querySelector("textarea[name='report_description']");
            const idsInput   = editDialog.querySelector("input[name='time_series_ids']");
            const fromInput  = editDialog.querySelector("input[name='time_range_from']");
            const toInput    = editDialog.querySelector("input[name='time_range_to']");

            titleInput.value = report.report_title || "";
            descInput.value  = report.report_description || "";
            idsInput.value   = (report.time_series_info || []).map(s => s.cache_id).join(", ");
            fromInput.value  = report.time_range_from || "";
            toInput.value    = report.time_range_to || "";

            editDialog.showModal();
            requestAnimationFrame(() => titleInput.focus());

            const closeEdit = () => { editDialog.close(); editDialog.remove(); };
            editDialog.querySelector("#cancelEditBtn").addEventListener("click", closeEdit);
            editDialog.addEventListener("cancel", e => { e.preventDefault(); closeEdit(); });

            editDialog.querySelector("#saveEditBtn").addEventListener("click", async () => {
                if (!editDialog.querySelector("form").reportValidity()) return;
                const payload = {
                    report_title:       titleInput.value.trim(),
                    report_description: descInput.value.trim(),
                    time_series_ids:    idsInput.value.trim(),
                    time_range_from:    fromInput.value,
                    time_range_to:      toInput.value || null,
                };
                try {
                    const resp = await fetch(`/api/reports/${reportId}`, {
                        method: "PUT",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify(payload),
                    });
                    if (!resp.ok) {
                        const err = await resp.json().catch(() => ({}));
                        throw new Error(err.detail || `HTTP ${resp.status}`);
                    }
                } catch (e) {
                    alert(`Save failed: ${e.message}`);
                    return;
                }
                closeEdit();
                selectedId = null;
                submitBtn.disabled = true;
                editBtn.disabled = true;
                loadReports();
            });
        };

        editBtn.addEventListener("click", () => { if (selectedId) openEditDialog(selectedId); });

        deleteBtn.addEventListener("click", async () => {
            if (!selectedId) return;
            if (!confirm("Delete this report? This cannot be undone.")) return;
            try {
                const resp = await fetch(`/api/reports/${selectedId}`, { method: "DELETE" });
                if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
            } catch (e) {
                alert(`Failed to delete report: ${e.message}`);
                return;
            }
            selectedId = null;
            submitBtn.disabled = true;
            editBtn.disabled = true;
            deleteBtn.disabled = true;
            loadReports();
        });

        requestAnimationFrame(() => searchInput.focus());

    } else {
        alert(`Unknown form type: ${formType}`);
    }
}
