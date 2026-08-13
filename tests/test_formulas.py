from fractions import Fraction

import pytest

from nth_term.formulas import (
    ArithmeticFormula,
    CubicFormula,
    GeometricFormula,
    QuadraticFormula,
    calculate_arithmetic_formula,
    calculate_cubic_formula,
    calculate_geometric_formula,
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
def test_calculate_arithmetic_formula(
    sequence: tuple[Fraction, ...],
    a: Fraction,
    b: Fraction,
):
    formula = calculate_arithmetic_formula(sequence)

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
def test_calculate_geometric_formula(
    sequence: tuple[Fraction, ...],
    a: Fraction,
    r: Fraction,
):
    formula = calculate_geometric_formula(sequence)

    assert formula.a == a
    assert formula.r == r


def test_arithmetic_formula_coefficients():
    formula = ArithmeticFormula(
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


def test_geometric_formula_coefficients():
    formula = GeometricFormula(
        a=Fraction(3),
        r=Fraction(2),
    )

    assert formula.coefficients == (
        Fraction(3),
        Fraction(2),
    )
