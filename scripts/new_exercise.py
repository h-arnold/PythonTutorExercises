#!/usr/bin/env python3
"""Scaffold a new exercise (notebook + tests).

Usage:
  python scripts/new_exercise.py ex001 "Variables and Types" --slug variables_and_types

This creates:
  exercises/ex001_variables_and_types/README.md
  notebooks/ex001_variables_and_types.ipynb
    tests/test_ex001_variables_and_types.py
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    if not text:
        raise SystemExit("Slug is empty; provide --slug or a better title.")
    return text


def _make_notebook(title: str) -> dict:
    """Return a minimal .ipynb JSON object."""

    def _meta(language: str, *, tags: list[str] | None = None) -> dict:
        meta: dict[str, object] = {"id": uuid.uuid4().hex[:8], "language": language}
        if tags:
            meta["tags"] = tags
        return meta

    # NOTE: This intentionally includes per-cell metadata.language to match repo conventions.
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": _meta("markdown"),
                "source": [
                    f"# {title}\n",
                    "\n",
                    "## Goal\n",
                    "Write your solution in the **student** cell, then run the tests.\n",
                    "\n",
                    "## How to work\n",
                    "- Run `pytest -q`\n",
                ],
            },
            {
                "cell_type": "code",
                "metadata": _meta("python", tags=["student"]),
                "execution_count": None,
                "outputs": [],
                "source": [
                    "# STUDENT CELL (graded)\n",
                    "# The tests will execute the code in this cell.\n",
                    "\n",
                    "def example() -> str:\n",
                    "    \"\"\"Return a non-empty string.\"\"\"\n",
                    "    return \"TODO\"\n",
                ],
            },
            {
                "cell_type": "code",
                "metadata": _meta("python"),
                "execution_count": None,
                "outputs": [],
                "source": [
                    "# Optional self-check (not graded)\n",
                    "print(example())\n",
                ],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new exercise skeleton")
    parser.add_argument("id", help='Exercise id like "ex001"')
    parser.add_argument("title", help="Human title for the exercise")
    parser.add_argument(
        "--slug",
        help="Optional slug (snake_case). Defaults to slugified title.",
        default=None,
    )
    args = parser.parse_args()

    ex_id = args.id.strip().lower()
    if not re.fullmatch(r"ex\d{3}", ex_id):
        raise SystemExit('Exercise id must look like "ex001".')

    slug = args.slug.strip().lower() if args.slug else _slugify(args.title)
    if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", slug):
        raise SystemExit("Slug must be snake_case containing only a-z, 0-9, and underscores.")

    exercise_key = f"{ex_id}_{slug}"

    ex_dir = ROOT / "exercises" / exercise_key
    nb_path = ROOT / "notebooks" / f"{exercise_key}.ipynb"
    test_path = ROOT / "tests" / f"test_{exercise_key}.py"

    if ex_dir.exists() or nb_path.exists() or test_path.exists():
        raise SystemExit(f"Exercise already exists: {exercise_key}")

    ex_dir.mkdir(parents=True)

    (ex_dir / "__init__.py").write_text("\n", encoding="utf-8")

    today = _dt.date.today().isoformat()

    (ex_dir / "README.md").write_text(
        "\n".join(
            [
                f"# {args.title}",
                "",
                "## Student prompt",
                "- Open the matching notebook in `notebooks/`.",
                "- Write your solution in the notebook cell tagged `student`.",
                "- Run `pytest -q` until all tests pass.",
                "",
                "## Teacher notes",
                f"- Created: {today}",
                "- Target concepts: (fill in)",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    test_path.write_text(
        "\n".join(
            [
                "from __future__ import annotations",
                "",
                "from tests.notebook_grader import exec_tagged_code",
                "",
                "",
                "def test_example_returns_string() -> None:",
                f"    ns = exec_tagged_code('notebooks/{exercise_key}.ipynb', tag='student')",
                "    assert 'example' in ns",
                "    result = ns['example']()",
                "    assert isinstance(result, str)",
                "    assert result != \"\"",
                "",
            ]
        ),
        encoding="utf-8",
    )

    notebook = _make_notebook(args.title)
    nb_path.write_text(json.dumps(notebook, indent=2), encoding="utf-8")

    print(f"Created exercise: {exercise_key}")
    print(f"- {ex_dir.relative_to(ROOT)}")
    print(f"- {nb_path.relative_to(ROOT)}")
    print(f"- {test_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
