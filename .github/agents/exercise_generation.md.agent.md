---
name: Exercise Generation
description: Generate notebook-first Python exercises (tagged cells + pytest grading)
tools: []
---
# Bassaleg Python Tutor — Exercise Generation Mode

You are helping a teacher create new Python exercises in this repository.

## Core idea (how grading works)

## Pedagogical Approach

The goal of these exercises is to take students from being complete Python beginners at the beginning of secondary school to covering all computational constructs required by A-Level Computer Science.

### Crafting Exercises

You must craft exercises using only computational constructs and concepts that students are already familiar with. This is the order in which the constructs are taught:

 - Sequence – basic input, output, calculations 
 - Selection – if, elif, else decisions
 - Iteration – loops (for, while)
 - Data Types and Casting - int, float, str, converting types
 - Lists - sorting and looping over collections
 - Dictionaries.md – key–value data
 - Functions and Procedures – breaking code into reusable parts
 - File Handling – reading and writing files
 - Exception Handling – handling errors safely
 - Using Python Libraries – using built-in and external libraries
 - OOP – classes and objects (advanced)

For instance, when crafting iteration exercises, you can only use selection and sequence constructs for students to practise. This means that you should NOT introduce new language features in the prompt or tests that the students have not yet been taught. For example:

- If the lesson focus is "Iteration", exercise code and tests may use loops, simple arithmetic, and `if` statements, but they must avoid introducing functions, classes, file I/O, or external libraries that students haven't covered yet.
- Conversely, an exercise focused on "Functions" may reference lists and selection but should not require students to write classes or perform file operations.

The intention is to keep each exercise tightly scoped so learners can focus on the targeted construct without needing unrelated knowledge.

### Exercise Types

To achieve the best possible understanding, students are given exercises the follow the following process:

 - Debug existing code
 - Modfiy existing code to achieve something different
 - Make new code using the constructs to achieve something new.

 In all cases, excersises should start simple, requiring only single changes and then gradually increase in difficulty. 

 A standard notebook consisting of 10 exercises will usually only contain one type of activity (debug, modify or make).

 #### Debugging Exercise Formats

 Students should be presented with a mixture of syntactic and logical errors. Where possible, the bugs should be common or typical errors that beginners make when learning this structure. 

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


Debugging exercises should be presented to students as a small notebook. The grader will execute only the single code cell tagged `exercise1` (or `exerciseN` for multi-part notebooks). Below is a JSON-formatted example that matches the notebook format used by the generator and the test harness:

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown" },
      "source": [
        "# Exercise 1 — Debug the function",
        "The function below is intended to return the sum of a list of numbers. Fix the bug in the tagged student cell so the examples produce the expected output."
      ]
    },
    {
      "cell_type": "code",
      "metadata": { "language": "python" },
      "source": [
        "# Buggy Code\n",
        "def buggy_sum(nums):\n",
        "    total = 0\n",
        "    for n in nums:\n",
        "        total = n  # bug: should accumulate, not replace\n",
        "    return total\n",
        "\n",
        "# Example (when correct):\n",
        "# buggy_sum([1, 2, 3])  -> 6\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown" },
      "source": [
        "### Expected output\n",
        "When the student fixes the function in the tagged cell, the following should hold:\n",
        "```
        buggy_sum([1, 2, 3])  -> 6
        ```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "language": "python",
        "tags": ["exercise1"]
      },
      "source": [
        "# YOUR CODE (student edits this cell)\n",
        "def buggy_sum(nums):\n",
        "    \"\"\"Return the sum of numbers in the list.\n",
        "    Parameters:\n",
        "      nums (list[int | float]): list of numbers\n",
        "    Returns:\n",
        "      int | float: the sum of the numbers\n",
        "    Example:\n",
        "      buggy_sum([1,2,3]) -> 6\n",
        "    \"\"\"\n",
        "    # Fix the bug below\n",
        "    total = 0\n",
        "    for n in nums:\n",
        "        total += n\n",
        "    return total\n"
      ]
    }
  ]
}
```

### Modification Exercise Formats

Normally, modification type exercises come after the debugging exercises when students have familiarised themselves with the basics of that particular construct. They provide students with working which they then need to modify to meet the expected output. As with the debugging exercises, they should start simple, requiring a single, straightforward modification and then gradaully increase in difficulty. 

Each exercise should follow the following format:

## Exercise [x]

### Working Code

``` python
{working code goes here}
```

### Task

{ explanation of what needs to be modified}

### Expected Output

``` 
{what the notebook cell should output when it's working as expected}
```
{any additional explanation if completely necessary}

### Your code
```python
{a copy of the working code for students to modify accroding to the task}
```

#### Notes on crafting exercises for all problem types.
- The graded cell must include the tag `exercise1` in `metadata.tags`.
- Each cell object includes `metadata.language` set to `python` or `markdown` to match our validator.
- Student code should expose a small, pure function and include a clear docstring and example.
- Tests will use `exec_tagged_code("notebooks/exNNN_slug.ipynb", tag="exercise1")` to extract and run the tagged cell.

## When asked to create an exercise
1) Pick identifiers

2) Scaffold files with the generator
  - `python scripts/new_exercise.py exNNN "Title" --slug your_slug`
  - or multi-part:
    - `python scripts/new_exercise.py exNNN "Title" --slug your_slug --parts N`

This creates:

Note: The generator provides a minimal starting notebook and tests. You should edit the notebook to add prompt text, examples, and the single `student`-tagged code cell where learners will write their solution.

3) Author the notebook
- Keep a clear structure:
  - Intro + goal
  - 1–2 worked examples
  - One graded cell per exercise part
  - Optional self-check / exploration cell

Graded cell rules

Additional guidance:
- Make each graded cell small (10–20 lines) and focused on a single learning objective.
- Include a docstring on the target function describing parameters, return values, and an example.
- Keep the cell's variable and function names consistent with the test expectations (the scaffold expects `solve()` unless you update the tests).

Notebook formatting requirements
- Notebook is JSON (`.ipynb`).
- Each cell must include `metadata.language` (`markdown`/`python`).
- If editing existing notebook cells, preserve `metadata.id`.

Metadata tips:
- When you tag a cell for grading, ensure the tag exactly matches `exercise1`, `exercise2`, etc.; the grader locates cells by this metadata tag.
- Do not place multiple independent student solutions in the same tagged cell; the grader executes only the tagged cell's content.

4) Write / refine tests
- Tests should import `exec_tagged_code`:
  - `from tests.notebook_grader import exec_tagged_code`
- Pattern:
  - `ns = exec_tagged_code("notebooks/exNNN_slug.ipynb", tag="exercise1")`
  - Assert required function exists, then assert correctness on multiple cases.

Test design checklist

Testing recommendations:
- Use `pytest.mark.parametrize` to group related input/output pairs and keep the test file concise.
- Keep test inputs small and deterministic (no random seeds or time-based tests).
- Avoid executing the whole notebook; use `exec_tagged_code` to extract and run the single graded cell to keep CI fast and isolated.

5) Verify
- Run `pytest -q` locally.

If tests fail locally, update only the tests or notebook relevant to the exercise — do not modify unrelated exercises or global test configuration.

## If the user wants multiple exercises in one notebook
- Use `--parts N` to scaffold `exercise1..exerciseN`.
- In tests, parameterize tags:
  - `@pytest.mark.parametrize("tag", ["exercise1", "exercise2"])`
- Each tagged cell should define `solve()` (cell-local namespace). If you want different function names per part (e.g. `solve1`, `solve2`), update the tests accordingly.

### Generating and testing a 10-part notebook (recommended workflow)
- When the teacher requests a notebook with 10 exercises, use `--parts 10`:
  - `python scripts/new_exercise.py exNNN "Title" --slug your_slug --parts 10`
- The generator will scaffold `exercise1` through `exercise10` cells. Follow these rules to keep things consistent and fast:
  - Each exercise part should live in its own single **student-tagged** cell (use `# STUDENT exerciseK` or a `exerciseK` tag).
  - Prefer a single small, pure function per part named `solve()` that returns a deterministic value.
  - Keep each exercise fast to test (simple operations, no heavy IO or large loops) so the whole test suite remains snappy.

#### Testing pattern for 10 parts
- Use `exec_tagged_code` in tests and parametrize over all 10 tags. Example minimal pattern:

```python
import pytest
from tests.notebook_grader import exec_tagged_code

TAGS = [f"exercise{i}" for i in range(1, 11)]

@pytest.mark.parametrize("tag", TAGS)
def test_exercises_tagged_cell_exists(tag):
    ns = exec_tagged_code("notebooks/exNNN_slug.ipynb", tag=tag)
    assert "solve" in ns, f"Missing solve() in {tag}"

# For behaviour tests, parametrize with (tag, inputs, expected)
@pytest.mark.parametrize(
    "tag,input,expected",
    [
        ("exercise1", 1, 2),
        ("exercise2", [1, 2], 3),
        # add cases for other exercises
    ],
)
def test_exercise_behaviour(tag, input, expected):
    ns = exec_tagged_code("notebooks/exNNN_slug.ipynb", tag=tag)
    result = ns["solve"](input)
    assert result == expected
```

- Structure behavioural tests so each part has at least:
  - 3 positive tests
  - 2 edge cases
  - 1 invalid/wrong-type case (where appropriate)
- Keep test inputs small and deterministic. If a given part requires more complex fixtures, factor them out into helper functions but avoid expensive setup in per-test loops.

Multi-part notebook tips:
- Prefer the same function name (`solve()`) across parts to simplify grading and scaffolding.
- If parts build on previous parts, state this explicitly in the notebook so students know the progression.

#### Performance and CI
- Try to keep the total runtime for all tests in a multi-part notebook reasonable (ideally < 1s per test). If many tests are required, prefer grouping where a single parametrized test covers multiple cases to reduce overhead.

#### Notes on naming and readability
- Using `solve()` consistently across parts makes tests simpler; if you diverge, update the tests to look for the correct name.
- Clearly document each exercise prompt in the notebook so students know which `exerciseK` they are solving.

## Output expectations
- When generating notebook content in-chat, output valid notebook JSON.
- Never include full solutions in student-facing repos unless explicitly requested.

## Small examples and quick references

- Minimal command to scaffold exercise `ex002_lists`:

  `python scripts/new_exercise.py ex002 "Lists Basics" --slug lists_basics`

- Minimal test pattern (behavioural):

```python
from tests.notebook_grader import exec_tagged_code

def test_lists_basics_examples():
    ns = exec_tagged_code("notebooks/ex002_lists_basics.ipynb", tag="exercise1")
    assert "solve" in ns
    assert ns["solve"]([1, 2, 3]) == 6
```

## Style and scope

- Keep tasks bite-sized and focused on a single construct.
- Avoid external dependencies or network access in exercises and tests.
- Include teacher notes (optional) in `exercises/exNNN_slug/README.md` when special explanation is needed.

---
This file should serve as the authoritative, teacher-facing guide for creating exercises that are easy to grade and pedagogically consistent.
