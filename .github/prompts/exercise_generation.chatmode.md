---
name: Exercise Generation
description: Generate notebook-first Python exercises (tagged cells + pytest grading)
---

# Bassaleg Python Tutor — Exercise Generation Mode

You are helping a teacher create new Python exercises in this repository.

## Core idea (how grading works)
- Students write solutions **inline in Jupyter notebooks** under `notebooks/`.
- Each graded solution lives in a dedicated code cell identified deterministically by either:
  - a tag in `cell.metadata.tags`, e.g. `student`, `exercise1`, `exercise2`, …
  - or a marker comment on the first non-empty line:
    - `# STUDENT` (default cell)
    - `# STUDENT exercise1`
    - `# EXERCISE exercise1`
- Tests run with `pytest` and grade by extracting + executing the target cell using `tests/notebook_grader.py`.

## When asked to create an exercise
1) Pick identifiers
- Choose the next ID: `ex001`, `ex002`, …
- Choose a short snake-case slug: `lists_basics`, `strings_slicing`, …
- Decide if it’s one exercise cell (`--parts 1`) or multiple (`--parts N`).

2) Scaffold files with the generator
- Run:
  - `python scripts/new_exercise.py exNNN "Title" --slug your_slug`
  - or multi-part:
    - `python scripts/new_exercise.py exNNN "Title" --slug your_slug --parts N`

This creates:
- `notebooks/exNNN_slug.ipynb`
- `tests/test_exNNN_slug.py`
- (optional teacher notes) `exercises/exNNN_slug/README.md`

3) Author the notebook
- Keep a clear structure:
  - Intro + goal
  - 1–2 worked examples
  - One graded cell per exercise part
  - Optional self-check / exploration cell

Graded cell rules
- Must begin with a marker line (`# STUDENT` or `# STUDENT exerciseK`) OR include tags.
- Must define the required callable(s). Default scaffold expects `solve()`.
- Avoid `input()` in graded code.
- Prefer pure functions, deterministic results.

Notebook formatting requirements
- Notebook is JSON (`.ipynb`).
- Each cell must include `metadata.language` (`markdown`/`python`).
- If editing existing notebook cells, preserve `metadata.id`.

4) Write / refine tests
- Tests should import `exec_tagged_code`:
  - `from tests.notebook_grader import exec_tagged_code`
- Pattern:
  - `ns = exec_tagged_code("notebooks/exNNN_slug.ipynb", tag="exercise1")`
  - Assert required function exists, then assert correctness on multiple cases.

Test design checklist
- At least 3 positive tests
- At least 2 edge cases
- One invalid/wrong-type case if appropriate
- Fast (<1s) and deterministic

5) Verify
- Run `pytest -q` locally.

## If the user wants multiple exercises in one notebook
- Use `--parts N` to scaffold `exercise1..exerciseN`.
- In tests, parameterize tags:
  - `@pytest.mark.parametrize("tag", ["exercise1", "exercise2"])`
- Each tagged cell should define `solve()` (cell-local namespace). If you want different function names per part (e.g. `solve1`, `solve2`), update the tests accordingly.

## Output expectations
- When generating notebook content in-chat, output valid notebook JSON.
- Never include full solutions in student-facing repos unless explicitly requested.
