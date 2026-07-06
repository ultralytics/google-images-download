# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

## Core Principles (CRITICAL)

**Delete > Replace > Add.** Before writing any change, answer in order: what can I delete? what can I replace? only then, what must I add?

The most common agent failure in this repo is reaching for the locally-safest edit — a new guard, flag, or helper — instead of fixing ownership. These tripwires override that instinct:

1. **Never guard a symptom — relocate the trigger.** A fix that adds a condition to suppress bad behavior (a staleness check, an is-initialized flag, a skip-first-call guard, a try/except around broken logic) is wrong by default. Find the code path that should own the behavior, move the logic there, and delete the code that got it wrong. Example: a warning fired from stale state; the right fix was not a recency guard — it deleted the stale detection and moved the trigger into the code path that observes the event live.
2. **Bugfixes are net-negative by default.** A bugfix that adds more lines than it removes needs a one-sentence justification in the PR body naming why deletion and relocation were impossible.
3. **Search the repo before creating anything.** This repo has no shared-utility package — the three top-level scripts are standalone — so before adding logic check whether `bing_scraper.py` already implements it (it has helpers for URL cleaning, format detection, and safe filenames). Avoid premature abstraction — three similar lines beat a helper nobody else calls.
4. **Deletion beats caution.** Zero regression means understanding the code you remove, not leaving it in place as insurance. Keeping broken or duplicated code "to be safe" is itself the regression: it is how repos rot. All changes must still ship debugged, validated, and production ready.

**Output gate:** every PR body must contain a `Deleted:` line naming the code removed (functions, branches, files, config). Features must name what they reused or consolidated. `Deleted: nothing` demands the rule-2 justification.

**Review gate:** adversarial reviewers must answer two questions before LGTM: (a) what could have been deleted instead of added? (b) does any added condition suppress a symptom rather than relocate a trigger? A finding on either blocks LGTM.

**This file is code — additions require deletions.** To add a rule here, remove or merge one. When everything is emphasized, nothing is.

**NEVER push to `main`. NEVER force push.** Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Launch an independent adversarial review agent with cold context (just the PR diff and this file) to hunt for bugs, regressions, and Core Principles violations — use the Codex CLI, one fresh `codex exec` run per round. Fix, push, and repeat until a fresh run reports LGTM.
3. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never force-push, reset, or revert commits you did not author.
4. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

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
- `requirements.txt` covers `bing_scraper.py` only (numpy, tqdm, pillow, selenium). The auxiliary scripts need extra deps not listed there: `beautiful_scraper.py` uses `requests`+`beautifulsoup4`, `clean_images.py` uses `scikit-image`.

## Architecture

Three independent top-level scripts, none installable as a package; each is run directly with `python <script>.py`.

- `bing_scraper.py` — the primary scraper, a Bing-adapted fork of hardikvasa/google-images-download (the `googleimagesdownload` class keeps the original name). `user_input()` parses argparse flags (or a `--config_file` JSON of `Records`), `main()` loops records, and `download()` → `download_executor()` → `download_image()` does the work. Searches of `--limit` ≤ 100 scrape the results HTML via `download_page()`; above 100 they call `download_extended_page()`, which lazily imports Selenium and drives Chrome (optional `--chromedriver` path). Note `download()` special-cases `__name__ == "__main__"` to also print encoded paths.
- `beautiful_scraper.py` — standalone Baidu/Bing scraping and folder-organizing helpers (`requests` + BeautifulSoup).
- `clean_images.py` — standalone pass over `images/**` that removes gif/svg and corrupt files and downsizes large ones with scikit-image.

## Conventions

- Every file starts with `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license` — Ultralytics Actions adds headers automatically; don't add or revert them manually.
- Google-style docstrings; `format.yml` runs Ruff, docformatter, prettier (YAML/JSON/Markdown), and codespell, and its prettier output can differ from local — expect bot commits on PR branches.
- Tests (`tests/`) run fully offline: `conftest.py` puts the repo root on `sys.path`, and `test_bing_scraper.py` uses `monkeypatch`/stubs so no network or Chrome is needed — keep new tests network-free to stay CI-safe.
- No versioning or release process: the repo is not published to PyPI, has no `__version__`, and needs no version bump.
