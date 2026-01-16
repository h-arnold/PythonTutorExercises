# Teaching Notes: Sequence Debug Syntax (ex004)

## Prerequisites
- Students should know: basic `print()` usage, string literals, simple arithmetic, and how to read error messages.
- Prior exercises: `ex002_sequence_modify_basics`, `ex003_sequence_modify_variables`.

## Common Misconceptions
- Missing parentheses or quotes cause syntax errors; students may not spot the missing character.
- `input()` returns a string; adding numbers requires converting to `int()` (this is noted below).

## Teaching Approach
1. Demonstrate reading a Python SyntaxError and locating the line with the problem.
2. For each buggy example, ask students to explain the error first (short written explanation), then fix and run it.
3. For Exercise 7 (apples), we avoid casting in the solution to keep the exercise within Sequence: the solution uses a numeric literal so students can focus on reading and fixing syntax without introducing `int()` casting.

## Hints
- Encourage students to run one cell at a time and read the error trace.
- If casting (`int()`) is unfamiliar to your group, replace that solution with an approach that avoids numeric conversion.
