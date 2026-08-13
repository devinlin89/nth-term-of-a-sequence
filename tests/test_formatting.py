from fractions import Fraction

import pytest

from nth_term.formatting import (
    format_fraction,
    format_signed_constant,
    format_signed_term,
    format_term,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (Fraction(0), "0"),
        (Fraction(1), "1"),
        (Fraction(-1), "-1"),
        (Fraction(2), "2"),
        (Fraction(-2), "-2"),
        (Fraction(1, 2), r"\frac{1}{2}"),
        (Fraction(-1, 2), r"-\frac{1}{2}"),
        (Fraction(3, 4), r"\frac{3}{4}"),
        (Fraction(-5, 3), r"-\frac{5}{3}"),
    ],
)
def test_format_fraction(
    value: Fraction,
    expected: str,
):
    assert format_fraction(value) == expected


@pytest.mark.parametrize(
    ("coefficient", "variable", "expected"),
    [
        (Fraction(0), "n", ""),
        (Fraction(1), "n", "n"),
        (Fraction(-1), "n", "-n"),
        (Fraction(2), "n", "2n"),
        (Fraction(-2), "n", "-2n"),
        (Fraction(1, 2), "n", r"\frac{1}{2}n"),
        (Fraction(-3, 4), "n", r"-\frac{3}{4}n"),
        (Fraction(2), "n^2", "2n^2"),
        (Fraction(-1), "n^3", "-n^3"),
    ],
)
def test_format_term(
    coefficient: Fraction,
    variable: str,
    expected: str,
):
    assert format_term(coefficient, variable) == expected


@pytest.mark.parametrize(
    ("coefficient", "variable", "expected"),
    [
        (Fraction(0), "n", ""),
        (Fraction(1), "n", "+ n"),
        (Fraction(-1), "n", "- n"),
        (Fraction(2), "n", "+ 2n"),
        (Fraction(-2), "n", "- 2n"),
        (Fraction(1, 2), "n", r"+ \frac{1}{2}n"),
        (Fraction(-3, 4), "n", r"- \frac{3}{4}n"),
        (Fraction(1), "n^2", "+ n^2"),
        (Fraction(-1), "n^3", "- n^3"),
    ],
)
def test_format_signed_term(
    coefficient: Fraction,
    variable: str,
    expected: str,
):
    assert format_signed_term(coefficient, variable) == expected


@pytest.mark.parametrize(
    ("coefficient", "expected"),
    [
        (Fraction(0), ""),
        (Fraction(1), "+ 1"),
        (Fraction(-1), "- 1"),
        (Fraction(2), "+ 2"),
        (Fraction(-2), "- 2"),
        (Fraction(1, 2), r"+ \frac{1}{2}"),
        (Fraction(-3, 4), r"- \frac{3}{4}"),
    ],
)
def test_format_signed_constant(
    coefficient: Fraction,
    expected: str,
):
    assert format_signed_constant(coefficient) == expected