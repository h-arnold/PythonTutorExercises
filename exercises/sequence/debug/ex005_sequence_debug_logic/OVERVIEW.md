# Teaching notes: Sequence Debug Logic

## Prerequisites
- Students should be comfortable with:
  - Using `print()` or returning strings from a simple `solve()` function
  - Assigning string values to variables
  - Concatenating strings with `+`

## Purpose
These debug tasks focus on common *logical* mistakes learners make when working with short strings and variables (wrong values, wrong order, missing punctuation, wrong prompt text). They practise reading expected output carefully and making targeted changes.

## Common misconceptions
- Students change code but not the exact wording (missing punctuation or different casing).
- Using incorrect variable values rather than adjusting the right variable.
- Overlooking small differences in the prompt or message wording.

## Teaching approach
1. Demonstrate one example (pick exercise 1 or 3). Show how to compare actual vs expected output and find the mismatch.
2. Ask students to fix exercises 1–5 (single error each) in-class, then check with `pytest`.
3. Have students attempt 6–10 (multiple small errors across the code) to build confidence troubleshooting multiple issues.

## Worked example (for teacher)
- Bug: `greeting = "Hello from Python!"` expected `"Hi there!"`.
- Fix: change the string value assigned to `greeting`.
- Teaching tip: emphasise exact matching of the expected output (spaces, punctuation).

## Expected duration
- 15–25 minutes in class, depending on student experience.

## Tests
- Tests verify both the corrected behaviour and that the student wrote a brief explanation for each fix (explanation > 10 characters).

