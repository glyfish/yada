# yada — analysis pipeline, stores, plotting, agentic frontend

@../sefer/overview.md
@../sefer/conventions.md

Applies the models to *real* data; owns the data stores (Postgres, vector),
plotting, reporting, and the agentic apps. Reference docs live in `sefer/yada/`.

## Environment & commands

- pyenv env `yada-3.11.11`; deps are pip-compiled (`requirements.in` → `.txt`,
  includes `-e ../navi`).
- Tests: `pytest`.
- Layout: `apps/` (agentic + plots), `clients/`, `notebooks/`.
