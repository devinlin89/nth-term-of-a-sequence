from fractions import Fraction

import pytest

from nth_term.formatting import format_formula
from nth_term.models import (
    ArithmeticFormula,
    CubicFormula,
    GeometricFormula,
    QuadraticFormula,
)


@pytest.mark.parametrize(
    ("formula", "expected"),
    [
        (
            ArithmeticFormula(Fraction(3), Fraction(-1)),
            r"3n - 1",
        ),
        (
            ArithmeticFormula(Fraction(-2), Fraction(5)),
            r"-2n + 5",
        ),
        (
            QuadraticFormula(
                Fraction(2),
                Fraction(3),
                Fraction(1),
            ),
            r"2n^2 + 3n + 1",
        ),
        (
            CubicFormula(
                Fraction(2),
                Fraction(-1),
                Fraction(3),
                Fraction(-2),
            ),
            r"2n^3 - n^2 + 3n - 2",
        ),
        (
            GeometricFormula(
                Fraction(3),
                Fraction(2),
            ),
            r"3\left(2\right)^{n-1}",
        ),
    ],
)
def test_format_formula(formula, expected: str):
    assert format_formula(formula) == expected
