# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

## Core Principles (CRITICAL)

**Less is more. The simplest solution is the best solution.** The action hierarchy for every change: **Delete > Replace > Add**.

1. **Solve at the owner**: Put behavior in the code path that owns or observes it. For fixes, never guard a symptom with a staleness check, initialization flag, skip-first-call branch, or `try/except` around broken logic; relocate the trigger and delete the wrong path. For features, extend the existing owner rather than creating a parallel abstraction.
2. **Search and reuse first**: Search the whole repository before creating a feature, component, helper, workflow, or utility. Reuse or adapt what exists, consolidate in-scope duplication in the shared owner, and delete duplicate paths. Three similar lines beat a helper nobody else calls.
3. **Delete and modify existing code before creating new code**: Bugfixes are net-negative by default unless deletion and relocation are demonstrably impossible. A new file must first prove it cannot fit cleanly in an existing owner.
4. **Keep scope minimal**: Implement only the simplest complete solution. Avoid impossible-state handling, speculative flags, compatibility shims, policy scaffolding, and unrelated cleanup. Tests are out of scope by default — rely on existing coverage and focused validation; only an uncovered, high-risk regression path justifies minimal new test code.
5. **Ship zero-regression, production-ready changes**: Understand what you remove instead of retaining broken code as insurance. Remove unused imports, functions, types, files, and comments; run relevant cleanup checks; and thoroughly debug and validate the changed owner. Do not break existing features or workflows unless the PR intentionally removes them with evidence.

**Review gate:** for every addition, the reviewer decides whether deleting or changing existing code would have fixed the problem instead — if it would, that is a blocking finding. A missing or thin PR description is never itself a finding.

NEVER push to `main`. NEVER force push. Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Review the full diff in-session against the Core Principles, performance, and the review gate above, then batch the fixes into one commit and push. After each round of bot or human commits, pull and resume the same reviewer on `<last-reviewed-sha>..HEAD` plus anything that delta could have invalidated. Repeat until the local head matches the live head.
3. Hand off or merge only on a clean final pass: one cold full-diff review returning LGTM with no findings, on a head that is still live at merge time.
4. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never reset or revert commits you did not author.
5. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
# Install runtime + test deps (mirrors ci.yml; CI adds --system and an unused `ultralytics` install)
uv pip install -r requirements.txt pytest

# Compile-check every file, exactly as CI does
python -m compileall -q .

# Run all tests (CI runs `pytest -q`)
pytest -q

# Single test
pytest tests/test_bing_scraper.py::test_python_search_argument_uses_bing -v

# Format/lint locally (no repo config, so Ruff/docformatter use their defaults; the Actions bot is the source of truth)
ruff format . && ruff check --fix .
```

- CI (`ci.yml`) runs on Python 3.11, ubuntu-latest only, on pull_request/push to main and a daily cron; there is no version matrix and no packaging (no `pyproject.toml`/`setup.py`).
- `requirements.txt` lists only numpy, tqdm, pillow, and selenium. The auxiliary scripts import extra deps not listed there: `beautiful_scraper.py` needs `requests`+`beautifulsoup4`, `clean_images.py` needs `scikit-image`.

## Architecture

Three independent top-level scripts, none installable as a package; each is run directly with `python <script>.py`.

- `bing_scraper.py` — the primary scraper, a Bing-adapted fork of hardikvasa/google-images-download (the `googleimagesdownload` class keeps the original name). `user_input()` parses argparse flags (or a `--config_file` JSON of `Records`), `main()` loops records, and `download()` → `download_executor()` → `download_image()` does the work. Searches of `--limit` ≤ 100 scrape the results HTML via `download_page()`; above 100 they call `download_extended_page()`, which lazily imports Selenium and drives Chrome (optional `--chromedriver` path). Note `download()` special-cases `__name__ == "__main__"` to also print encoded paths.
- `beautiful_scraper.py` — standalone Baidu/Bing scraping and folder-organizing helpers (`requests` + BeautifulSoup).
- `clean_images.py` — standalone pass over `images/**` that removes gif/svg and corrupt files and downsizes large ones with scikit-image.

## Conventions

- Every Python file starts with `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license` — Ultralytics Actions adds headers automatically; don't add or revert them manually.
- Google-style docstrings; `format.yml` runs Ruff, docformatter, prettier (YAML/JSON/Markdown), and codespell, and its prettier output can differ from local — expect bot commits on PR branches.
- Tests (`tests/`) run fully offline: `conftest.py` puts the repo root on `sys.path`, and `test_bing_scraper.py` uses `monkeypatch`/stubs so no network or Chrome is needed — keep new tests network-free to stay CI-safe.
- No versioning or release process: the repo is not published to PyPI, has no `__version__`, and needs no version bump.
