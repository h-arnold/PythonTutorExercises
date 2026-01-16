#### Debugging Exercise Formats

Students should be presented with a mixture of syntactic and logical errors. Where possible, the bugs should be common or typical errors that beginners make when learning this structure.

**Error count progression**: 
- Exercises 1-5: Each should contain exactly **one error** to help students build confidence and focus on a single issue at a time.
- Exercises 6-10: Gradually increase the number of errors where possible and appropriate to the task (e.g., exercise 6 might have 1-2 errors, exercise 10 might have 2-3).
- Errors should be **realistic** (what students would actually write) whenever possible. If realistic errors aren't appropriate for the learning objective, then use contrived errors that serve the pedagogical goal. 

**Common syntactic and logical errors (examples)**

- **Selection (if/elif/else):**
  - Syntax: forgetting the colon, e.g. `if x > 0` -> SyntaxError; correct: `if x > 0:`
  - Logical: wrong branch order, e.g. `if x > 0: ... elif x > 10: ...` — the `elif` never runs for `x > 10` because the first condition already matches.

- **Iteration (for/while):**
  - Syntax: missing indentation after the loop header causes IndentationError.
  - Logical: off-by-one or infinite loops, e.g. `while i >= 0:` without decrementing `i` causes an infinite loop.
  - Logical: mutating a list while iterating, e.g. `for x in items: items.remove(x)`, which skips elements.

- **Data types & casting:**
  - Logical/runtime: `input()` returns a string — `n = input(); total = n + 5` leads to concatenation or TypeError; cast with `int()`/`float()` as appropriate.
  - Runtime: passing `'3.5'` to `int()` raises ValueError — choose the right converter.

- **Lists:**
  - Logical: index errors (`mylist[3]` when length is 3 -> IndexError).
  - Semantic: using parentheses `()` instead of brackets `[]` creates a tuple rather than a list.
  - Logical: aliasing vs copying, e.g. `b = a` shares the same list; use `a.copy()` when you need a separate copy.

- **Dictionaries:**
  - Logical: `d['key']` on a missing key raises KeyError; prefer `d.get('key')` or `if 'key' in d:`.
  - TypeError: using an unhashable key (like a list) fails — keys must be immutable/hashable.

- **Functions & return values:**
  - Logical: forgetting `return` (function implicitly returns `None`).
  - Semantic: referencing the function object instead of calling it (`f` vs `f()`).
  - Logical: mutable default arguments, e.g. `def f(x, lst=[])` reuses the same list across calls.

- **File handling:**
  - Logical: opening a file with `'w'` unintentionally truncates it; use `'a'` to append when appropriate.
  - Resource bug: not using `with open(...) as f:` can leave files open when exceptions occur.

- **Exception handling:**
  - Logical: overly broad `except:` hides unrelated bugs — prefer explicit exceptions like `except ValueError:`.
  - Logical: catching and ignoring exceptions (`except: pass`) masks failures that tests should detect.


Debugging exercises should be presented to students as a small notebook with a clear, student-facing structure. The grader will execute only the single code cell tagged `exercise1` (or `exerciseN` for multi-part notebooks). The recommended layout for a single-part debug exercise is:

1. A *markdown* cell that describes what the program should do and **shows the expected output** (do not tell the student how to fix the code; only display the correct output that should appear when the corrected code is run).
2. A *code* cell containing the buggy implementation. This *code* cell should be tagged with `exercise1` so students edit it directly to fix the behaviour.
3. A *markdown* cell titled **"What actually happened"** that prompts the student to describe what occurred when they ran (or attempted to run) the code. This markdown cell must include the metadata tag `explanation1` (or `explanationN` for multi-part notebooks).

Below is a JSON-formatted example that matches the notebook format used by the generator and the test harness. Notice the order: expected-output markdown, the buggy `exercise1` code cell, then the `explanation1` markdown cell:

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown" },
      "source": [
        "# Exercise 1 — Expected behaviour",
        "The function below should return the sum of a list of numbers.\n",
        "### Expected output\n",
        "``\n",
        "buggy_sum([1, 2, 3])  -> 6\n",
        "``"
      ]
    },
    {
      "cell_type": "code",
      "metadata": { "language": "python", "tags": ["exercise1"] },
      "source": [
        "# BUGGY IMPLEMENTATION (students edit this tagged cell)\n",
        "def buggy_sum(nums):\n",
        "    total = 0\n",
        "    for n in nums:\n",
        "        total = n  # bug: should accumulate, not replace\n",
        "    return total\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown", "tags": ["explanation1"] },
      "source": [
        "### What actually happened\n",
        "Describe briefly what happened when you ran the code (include any error messages or incorrect output).",
        "\n",
        "Example: `I got 3 instead of 6 because the loop replaces rather than accumulates.`"
      ]
    }
  ]
}
```

Testing guidance (required):

- Tests for debug exercises should still verify the corrected behaviour by executing the tagged `exercise1` cell and checking function outputs.
- Additionally, tests must assert that the student's explanation in the `explanationN` markdown cell is meaningfully filled in. For now, tests should check that the explanation is more than 10 characters (non-whitespace).

Example test helper to read an explanation cell from a notebook using the standard library:

```python
import json

def _get_explanation(notebook_path: str, tag: str = "explanation1") -> str:
    nb = json.load(open(notebook_path, "r", encoding="utf-8"))
    for cell in nb.get("cells", []):
        tags = cell.get("metadata", {}).get("tags", [])
        if tag in tags:
            return "".join(cell.get("source", []))
    raise AssertionError(f"No explanation cell with tag {tag}")

# Example test
def test_explanation_has_content():
    explanation = _get_explanation("notebooks/ex004_sequence_debug_syntax.ipynb", tag="explanation1")
    assert len(explanation.strip()) > 10, "Explanation must be more than 10 characters"
```

##### Important: Debugging Exercise Cell Comments

**Do NOT** include explanatory comments in the student `exercise` cells that reveal what the bug is. For example:

❌ **Bad** (reveals the bug):

``` python
    # Bug: apostrophe inside single quotes
    phrase = 'It's nice'
    return phrase
```
