from __future__ import annotations

import builtins
import io
import sys

from tests.notebook_grader import exec_tagged_code


def _run_and_capture(tag: str, *, inputs: list[str] | None = None) -> str:
    """Execute the tagged cell while capturing stdout and optional inputs."""
    old_stdout = sys.stdout
    buffer = io.StringIO()
    sys.stdout = buffer

    original_input = builtins.input
    if inputs is not None:
        iterator = iter(inputs)

        def fake_input(prompt: str | None = "") -> str:
            try:
                return next(iterator)
            except StopIteration as exc:
                raise RuntimeError("Test expected more input values") from exc

        builtins.input = fake_input

    try:
        exec_tagged_code('notebooks/ex003_sequence_modify_variables.ipynb', tag=tag)
    finally:
        sys.stdout = old_stdout
        builtins.input = original_input

    return buffer.getvalue()


def test_exercise1_prints_hi_there() -> None:
    output = _run_and_capture('exercise1')
    assert output.strip() == "Hi there!", f"Unexpected output: {output!r}"


def test_exercise2_prints_coding_message() -> None:
    output = _run_and_capture('exercise2')
    assert output.strip() == "I enjoy coding lessons.", f"Unexpected output: {output!r}"


def test_exercise3_prints_favourite_food() -> None:
    output = _run_and_capture('exercise3')
    assert output.strip() == "My favourite food is sushi", f"Unexpected output: {output!r}"


def test_exercise4_prompt_and_fruit_message() -> None:
    output = _run_and_capture('exercise4', inputs=["mango"])
    lines = output.strip().splitlines()
    assert lines == [
        "Type the name of your favourite fruit:",
        "I like mango",
    ], f"Unexpected lines: {lines!r}"


def test_exercise5_prompt_and_town_message() -> None:
    output = _run_and_capture('exercise5', inputs=["Cardiff"])
    lines = output.strip().splitlines()
    assert lines == [
        "Which town do you like the most?",
        "I would visit Cardiff",
    ], f"Unexpected lines: {lines!r}"


def test_exercise6_prompt_and_name_message() -> None:
    output = _run_and_capture('exercise6', inputs=["Alex"])
    lines = output.strip().splitlines()
    assert lines == [
        "Please enter your name:",
        "Welcome, Alex!",
    ], f"Unexpected lines: {lines!r}"


def test_exercise7_prints_variables_matter() -> None:
    output = _run_and_capture('exercise7')
    assert output.strip() == "Variables matter", f"Unexpected output: {output!r}"


def test_exercise8_prints_keep_experimenting() -> None:
    output = _run_and_capture('exercise8')
    assert output.strip() == "Keep experimenting", f"Unexpected output: {output!r}"


def test_exercise9_prints_good_evening_message() -> None:
    output = _run_and_capture('exercise9')
    assert output.strip() == "Good evening everyone!", f"Unexpected output: {output!r}"


def test_exercise10_prints_combined_message() -> None:
    output = _run_and_capture('exercise10')
    assert output.strip() == "Variables and strings make a message!", f"Unexpected output: {output!r}"
