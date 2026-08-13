from fractions import Fraction

import pytest

from nth_term.formulas import (
    CubicFormula,
    ExponentialFormula,
    LinearFormula,
    QuadraticFormula,
    calculate_cubic_formula,
    calculate_exponential_formula,
    calculate_linear_formula,
    calculate_quadratic_formula,
)


@pytest.mark.parametrize(
    ("sequence", "a", "b"),
    [
        (
            (Fraction(2), Fraction(5), Fraction(8), Fraction(11)),
            Fraction(3),
            Fraction(-1),
        ),
        (
            (Fraction(10), Fraction(7), Fraction(4), Fraction(1)),
            Fraction(-3),
            Fraction(13),
        ),
        (
            (Fraction(-5), Fraction(-2), Fraction(1), Fraction(4)),
            Fraction(3),
            Fraction(-8),
        ),
        (
            (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)),
            Fraction(1, 2),
            Fraction(0),
        ),
    ],
)
def test_calculate_linear_formula(
    sequence: tuple[Fraction, ...],
    a: Fraction,
    b: Fraction,
):
    formula = calculate_linear_formula(sequence)

    assert formula.a == a
    assert formula.b == b


@pytest.mark.parametrize(
    ("sequence", "a", "b", "c"),
    [
        (
            (Fraction(1), Fraction(4), Fraction(9), Fraction(16)),
            Fraction(1),
            Fraction(0),
            Fraction(0),
        ),
        (
            (Fraction(6), Fraction(15), Fraction(28), Fraction(45)),
            Fraction(2),
            Fraction(3),
            Fraction(1),
        ),
        (
            (Fraction(-2), Fraction(-7), Fraction(-16), Fraction(-29)),
            Fraction(-2),
            Fraction(1),
            Fraction(-1),
        ),
        (
            (Fraction(3), Fraction(7), Fraction(13), Fraction(21)),
            Fraction(1),
            Fraction(1),
            Fraction(1),
        ),
    ],
)
def test_calculate_quadratic_formula(
    sequence: tuple[Fraction, ...],
    a: Fraction,
    b: Fraction,
    c: Fraction,
):
    formula = calculate_quadratic_formula(sequence)

    assert formula.a == a
    assert formula.b == b
    assert formula.c == c


@pytest.mark.parametrize(
    ("sequence", "a", "b", "c", "d"),
    [
        (
            (
                Fraction(1),
                Fraction(8),
                Fraction(27),
                Fraction(64),
                Fraction(125),
                Fraction(216),
            ),
            Fraction(1),
            Fraction(0),
            Fraction(0),
            Fraction(0),
        ),
        (
            (
                Fraction(5),
                Fraction(26),
                Fraction(83),
                Fraction(194),
                Fraction(377),
                Fraction(650),
            ),
            Fraction(3),
            Fraction(0),
            Fraction(0),
            Fraction(2),
        ),
        (
            (
                Fraction(2),
                Fraction(16),
                Fraction(52),
                Fraction(122),
                Fraction(238),
                Fraction(412),
            ),
            Fraction(2),
            Fraction(-1),
            Fraction(3),
            Fraction(-2),
        ),
    ],
)
def test_calculate_cubic_formula(
    sequence: tuple[Fraction, ...],
    a: Fraction,
    b: Fraction,
    c: Fraction,
    d: Fraction,
):
    formula = calculate_cubic_formula(sequence)

    assert formula.a == a
    assert formula.b == b
    assert formula.c == c
    assert formula.d == d


@pytest.mark.parametrize(
    ("sequence", "a", "r"),
    [
        (
            (Fraction(3), Fraction(6), Fraction(12), Fraction(24)),
            Fraction(3),
            Fraction(2),
        ),
        (
            (Fraction(32), Fraction(16), Fraction(8), Fraction(4)),
            Fraction(32),
            Fraction(1, 2),
        ),
        (
            (Fraction(2), Fraction(-4), Fraction(8), Fraction(-16)),
            Fraction(2),
            Fraction(-2),
        ),
        (
            (Fraction(1, 2), Fraction(3, 2), Fraction(9, 2), Fraction(27, 2)),
            Fraction(1, 2),
            Fraction(3),
        ),
    ],
)
def test_calculate_exponential_formula(
    sequence: tuple[Fraction, ...],
    a: Fraction,
    r: Fraction,
):
    formula = calculate_exponential_formula(sequence)

    assert formula.a == a
    assert formula.r == r


def test_linear_formula_coefficients():
    formula = LinearFormula(
        a=Fraction(3),
        b=Fraction(-1),
    )

    assert formula.coefficients == (
        Fraction(3),
        Fraction(-1),
    )


def test_quadratic_formula_coefficients():
    formula = QuadraticFormula(
        a=Fraction(2),
        b=Fraction(3),
        c=Fraction(1),
    )

    assert formula.coefficients == (
        Fraction(2),
        Fraction(3),
        Fraction(1),
    )


def test_cubic_formula_coefficients():
    formula = CubicFormula(
        a=Fraction(2),
        b=Fraction(-1),
        c=Fraction(3),
        d=Fraction(-2),
    )

    assert formula.coefficients == (
        Fraction(2),
        Fraction(-1),
        Fraction(3),
        Fraction(-2),
    )


def test_exponential_formula_coefficients():
    formula = ExponentialFormula(
        a=Fraction(3),
        r=Fraction(2),
    )

    assert formula.coefficients == (
        Fraction(3),
        Fraction(2),
    )


@pytest.mark.parametrize(
    ("formula", "expected"),
    [
        (
            LinearFormula(Fraction(3), Fraction(-1)),
            r"3n - 1",
        ),
        (
            LinearFormula(Fraction(-2), Fraction(5)),
            r"-2n + 5",
        ),
        (
            LinearFormula(Fraction(1, 2), Fraction(-3, 4)),
            r"\frac{1}{2}n - \frac{3}{4}",
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
            QuadraticFormula(
                Fraction(-1),
                Fraction(0),
                Fraction(4),
            ),
            r"-n^2 + 4",
        ),
        (
            QuadraticFormula(
                Fraction(1, 2),
                Fraction(-3, 4),
                Fraction(0),
            ),
            r"\frac{1}{2}n^2 - \frac{3}{4}n",
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
            CubicFormula(
                Fraction(1),
                Fraction(0),
                Fraction(0),
                Fraction(0),
            ),
            r"n^3",
        ),
        (
            ExponentialFormula(
                Fraction(3),
                Fraction(2),
            ),
            r"3\left(2\right)^{n-1}",
        ),
        (
            ExponentialFormula(
                Fraction(1, 2),
                Fraction(1, 3),
            ),
            r"\frac{1}{2}\left(\frac{1}{3}\right)^{n-1}",
        ),
    ],
)
def test_formula_str(formula, expected: str):
    assert str(formula) == expected