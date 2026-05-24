import { handleResumeRequest } from "./api.js";

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

        const close = () => { dialog.close(); dialog.remove(); };
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

        const close = () => { dialog.close(); dialog.remove(); };
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

    } else if (formType === "load_pdf_document") {
        dialog.innerHTML = `
            <form method="dialog" novalidate autocomplete="off">
                <label for="pdf-filename">Filename:</label>
                <input id="pdf-filename" name="filename" type="text" placeholder="document.pdf" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="pdf-title">Title:</label>
                <input id="pdf-title" name="title" type="text" placeholder="Document title" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="pdf-authors">Authors:</label>
                <input id="pdf-authors" name="authors" type="text" placeholder="Author Name" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <label for="pdf-published-date">Published Date:</label>
                <input id="pdf-published-date" name="published_date" type="date" autocomplete="off" required>

                <label for="pdf-topic">Topic:</label>
                <textarea id="pdf-topic" name="topic" rows="3" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="e.g., Machine Learning" required></textarea>

                <label for="pdf-shelf">Shelf:</label>
                <input id="pdf-shelf" name="shelf" type="text" placeholder="e.g., reading_list" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="text" required>

                <menu>
                    <button type="button" class="btn" id="cancelFormBtn">Cancel</button>
                    <button type="button" class="btn primary" id="submitFormBtn">Load PDF Document</button>
                </menu>
            </form>
        `;
        document.body.appendChild(dialog);
        dialog.showModal();

        const filenameInput = dialog.querySelector("input[name='filename']");
        const titleInput    = dialog.querySelector("input[name='title']");
        const authorsInput  = dialog.querySelector("input[name='authors']");
        const dateInput     = dialog.querySelector("input[name='published_date']");
        const topicInput    = dialog.querySelector("textarea[name='topic']");
        const shelfInput    = dialog.querySelector("input[name='shelf']");

        requestAnimationFrame(() => filenameInput.focus());

        const close = () => { dialog.close(); dialog.remove(); };
        dialog.querySelector("#cancelFormBtn").addEventListener("click", close);
        dialog.addEventListener("cancel", e => { e.preventDefault(); close(); });

        const submit = async () => {
            if (!dialog.querySelector("form").reportValidity()) return;
            close();
            await handleResumeRequest(sessionId, {
                filename:       filenameInput.value.trim(),
                title:          titleInput.value.trim(),
                authors:        authorsInput.value.trim(),
                published_date: dateInput.value,
                topic:          topicInput.value.trim(),
                shelf:          shelfInput.value.trim(),
            }, promptLabel);
        };
        dialog.querySelector("#submitFormBtn").addEventListener("click", submit);
        [filenameInput, titleInput, authorsInput, dateInput, shelfInput].forEach(
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

        const close = () => { dialog.close(); dialog.remove(); };
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

    } else {
        alert(`Unknown form type: ${formType}`);
    }
}
