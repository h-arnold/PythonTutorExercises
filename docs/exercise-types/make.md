### Make Exercise Formats

This is the final exercise type that builds on the skills developed in the previous debugging and modification exercises. If not specified, scan the repo for the preceding exercises to give yourself a feel for the scope of make problems you can create.

As make problems are typically more difficult, you would normally generate 3–5 of these. Students are required to code a solution from scratch with only a brief description and expected output; the graded cell should provide a clear function skeleton for them to fill in.

Below is a JSON-formatted example that matches the notebook format used by the generator and the test harness. The student is asked to implement `solve()` from scratch (a common pattern for make problems and the default expected by the tests).

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown" },
      "source": [
        "# Exercise 1 — Create a function",
        "Write a function that computes the sum of squares of a list of integers."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown" },
      "source": [
        "### Task",
        "Implement `solve(nums)` which takes a list of integers and returns the sum of their squares.",
        "",
        "### Expected Output",
        "When correct:",
        "```\n        solve([1, 2, 3])  -> 14\n        ```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "language": "python",
        "tags": ["exercise1"]
      },
      "source": [
        "# YOUR CODE (student edits this cell)",
        "def solve(nums):",
        "    \"\"\"Return the sum of squares of the integers in `nums`.",
        "",
        "    Parameters:\n      nums (list[int]): list of integers\n",
        "    Returns:\n      int: sum of squares\n",
        "    Example:\n      solve([1,2,3]) -> 14\n    \"\"\"",
        "    # Implement the function below",
        "    raise NotImplementedError()"
      ]
    }
  ]
}
```