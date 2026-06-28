import { handleResumeRequest } from "./api.js";
import { sessionId as sessionIdState } from "./state.js";

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

        const saved = localStorage.getItem("gh_account");
        if (saved) accInput.value = saved;
        requestAnimationFrame(() => accInput.focus());

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
        dialog.innerHTML = `
            <form method="dialog" novalidate autocomplete="off">
                <label for="tsr-title">Title:</label>
                <input id="tsr-title" name="report_title" type="text" placeholder="Report title" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="tsr-description">Description:</label>
                <textarea id="tsr-description" name="report_description" rows="3" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Brief description of this report" required></textarea>

                <label for="tsr-tags">Tags:</label>
                <input id="tsr-tags" name="tags" type="text" placeholder="gdp, labor, quarterly" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text">

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
        document.body.appendChild(dialog);
        dialog.showModal();

        const titleInput       = dialog.querySelector("input[name='report_title']");
        const descriptionInput = dialog.querySelector("textarea[name='report_description']");
        const tagsInput        = dialog.querySelector("input[name='tags']");
        const idsInput         = dialog.querySelector("input[name='time_series_ids']");
        const fromInput        = dialog.querySelector("input[name='time_range_from']");
        const toInput          = dialog.querySelector("input[name='time_range_to']");

        const prefill = formSchema.prefill || {};
        if (prefill.report_title)       titleInput.value       = prefill.report_title;
        if (prefill.report_description) descriptionInput.value = prefill.report_description;
        if (prefill.tags)               tagsInput.value        = prefill.tags;
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
                tags:               tagsInput.value.trim(),
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

    } else if (formType === "select_time_series_report") {
        dialog.classList.add("report-picker");
        dialog.innerHTML = `
            <form method="dialog" novalidate autocomplete="off">
                <h3 style="margin-top:0">Select Report to Plot</h3>
                <input id="rp-search" type="text" placeholder="Search by title, tag, or description…"
                    autocomplete="off" autocapitalize="off" spellcheck="false" style="width:100%;box-sizing:border-box;">
                <div id="rp-table-wrap" class="report-picker-wrap">
                    <table class="report-picker-table">
                        <thead>
                            <tr><th>Title</th><th>Tags</th><th>From</th><th>To</th></tr>
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
        let debounceTimer  = null;

        const renderRows = (reports) => {
            tbody.innerHTML = "";
            emptyMsg.style.display = reports.length === 0 ? "" : "none";
            for (const r of reports) {
                const tr = document.createElement("tr");
                tr.className = "report-picker-row";
                tr.dataset.reportId = r.report_id;
                const tags = (r.tags || []).join(", ");
                const to   = r.time_range_to || "latest";
                tr.innerHTML = `<td>${r.report_title}</td><td>${tags}</td><td>${r.time_range_from}</td><td>${to}</td>`;
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

        const fetchReports = async (q = "") => {
            const url = q ? `/api/reports?q=${encodeURIComponent(q)}` : "/api/reports";
            try {
                const resp = await fetch(url);
                if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
                renderRows(await resp.json());
            } catch (e) {
                tbody.innerHTML = `<tr><td colspan="4" style="color:red">Failed to load reports: ${e.message}</td></tr>`;
            }
        };

        fetchReports();

        searchInput.addEventListener("input", () => {
            clearTimeout(debounceTimer);
            selectedId = null;
            submitBtn.disabled = true;
            editBtn.disabled = true;
            deleteBtn.disabled = true;
            debounceTimer = setTimeout(() => fetchReports(searchInput.value.trim()), 250);
        });

        const close = () => { sessionIdState.val = null; dialog.close(); dialog.remove(); };
        dialog.querySelector("#cancelFormBtn").addEventListener("click", close);
        dialog.addEventListener("cancel", e => { e.preventDefault(); close(); });

        const submit = async () => {
            if (!selectedId) return;
            close();
            await handleResumeRequest(sessionId, { report_id: selectedId }, promptLabel);
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

                    <label for="ed-tags">Tags:</label>
                    <input id="ed-tags" name="tags" type="text" autocomplete="off" autocapitalize="off" spellcheck="false">

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
            const tagsInput  = editDialog.querySelector("input[name='tags']");
            const idsInput   = editDialog.querySelector("input[name='time_series_ids']");
            const fromInput  = editDialog.querySelector("input[name='time_range_from']");
            const toInput    = editDialog.querySelector("input[name='time_range_to']");

            titleInput.value = report.report_title || "";
            descInput.value  = report.report_description || "";
            tagsInput.value  = (report.tags || []).join(", ");
            idsInput.value   = (report.time_series_info || []).map(s => s.native_id).join(", ");
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
                    tags:               tagsInput.value.trim(),
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
                fetchReports(searchInput.value.trim());
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
            fetchReports(searchInput.value.trim());
        });

        requestAnimationFrame(() => searchInput.focus());

    } else {
        alert(`Unknown form type: ${formType}`);
    }
}
