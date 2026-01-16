from __future__ import annotations

import pytest

from tests.notebook_grader import exec_tagged_code


def _run(tag: str):
    ns = exec_tagged_code('notebooks/ex005_sequence_debug_logic.ipynb', tag=tag)
    assert 'solve' in ns, 'Student cell must define solve()'
    result = ns['solve']()
    # Placeholder guard: student must change the scaffold
    assert result != 'TODO'
    return result


@pytest.mark.parametrize('tag', ['exercise1', 'exercise2', 'exercise3', 'exercise4', 'exercise5', 'exercise6', 'exercise7', 'exercise8', 'exercise9', 'exercise10'])
def test_exercise_cells_run(tag: str) -> None:
    _run(tag)

# Explanation cell checks for debug exercises
import json

def _get_explanation(notebook_path: str, tag: str = 'explanation1') -> str:
    nb = json.load(open(notebook_path, 'r', encoding='utf-8'))
    for cell in nb.get('cells', []):
        tags = cell.get('metadata', {}).get('tags', [])
        if tag in tags:
            return ''.join(cell.get('source', []))
    raise AssertionError(f'No explanation cell with tag {tag}')

import pytest
TAGS = [f'explanation{i}' for i in range(1, 10 + 1)]
@pytest.mark.parametrize('tag', TAGS)
def test_explanations_have_content(tag: str) -> None:
    explanation = _get_explanation('notebooks/ex005_sequence_debug_logic.ipynb', tag=tag)
    assert len(explanation.strip()) > 10, 'Explanation must be more than 10 characters'
