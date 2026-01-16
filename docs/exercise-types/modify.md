### Modification Exercise Formats

Normally, modification type exercises come after the debugging exercises when students have familiarised themselves with the basics of that particular construct. They provide students with working code which they then need to modify to meet the expected output. As with the debugging exercises, they should start simple, requiring a single, straightforward modification and then gradually increase in difficulty.

Each exercise should follow the notebook JSON format below (so the grader can extract the tagged cell):

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown" },
      "source": [
        "# Exercise 1 — Modify the function",
        "The cell below shows working code. Modify the tagged student cell so it meets the task described."
      ]
    },
    {
      "cell_type": "code",
      "metadata": { "language": "python" },
      "source": [
        "# Working Code",
        "def greet(name):",
        "    return 'Hello ' + name",
        "",
        "# Example (when unmodified):",
        "# greet('Ana')  -> 'Hello Ana'"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": { "language": "markdown" },
      "source": [
        "### Task",
        "Modify `greet()` so it returns the greeting in the form: \"Hello, NAME!\" where `NAME` is the uppercase version of the input.",
        "",
        "### Expected Output",
        "When correct:",
        "```\n        greet('Ana')  -> 'Hello, ANA!'\n        ```"
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
        "def greet(name):",
        "    \"\"\"Return a greeting for `name`.",
        "",
        "    Example:",
        "      greet('Ana') -> 'Hello, ANA!'",
        "    \"\"\"",
        "    # Start from the working implementation below and modify it.",
        "    return 'Hello ' + name"
      ]
    }
  ]
}
```