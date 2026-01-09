# Bassaleg Python Tutor Exercises

Notebook-based Python exercises with automated grading via `pytest` (GitHub Classroom friendly).

## Repo layout

- `notebooks/`
	- One notebook per exercise: `notebooks/exNNN_slug.ipynb`
	- Students write code **inline** in a dedicated student cell (tagged `student` or starting with `# STUDENT`)
- `tests/`
	- `tests/test_exNNN_slug.py` contains automated tests
	- Tests extract + execute the student cell (see `tests/notebook_grader.py`)
- `scripts/new_exercise.py`
	- Scaffolds a new exercise skeleton

Optional (teacher notes / materials):
- `exercises/`
	- One folder per exercise: `exercises/exNNN_slug/README.md`

## Quickstart

Create a virtualenv and install dev dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

Run all tests:

```bash
pytest -q
```

## Create a new exercise

```bash
python scripts/new_exercise.py ex001 "Variables and Types" --slug variables_and_types
```

This creates:
- `notebooks/ex001_variables_and_types.ipynb`
- `tests/test_ex001_variables_and_types.py`

And (optional):
- `exercises/ex001_variables_and_types/README.md`

## Notes

- The notebook is for explanation and scratch work.
- Grading is driven by `pytest` (see `.github/workflows/tests.yml`).

