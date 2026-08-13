from fractions import Fraction

import pytest

from nth_term.calculator import find_nth_term
from nth_term.models import SequenceType


@pytest.mark.parametrize(
    ("sequence", "expected_type"),
    [
        (
            (
                Fraction(2),
                Fraction(5),
                Fraction(8),
                Fraction(11),
                Fraction(14),
            ),
            SequenceType.LINEAR,
        ),
        (
            (
                Fraction(1),
                Fraction(4),
                Fraction(9),
                Fraction(16),
                Fraction(25),
            ),
            SequenceType.QUADRATIC,
        ),
        (
            (
                Fraction(1),
                Fraction(8),
                Fraction(27),
                Fraction(64),
                Fraction(125),
            ),
            SequenceType.CUBIC,
        ),
        (
            (
                Fraction(3),
                Fraction(6),
                Fraction(12),
                Fraction(24),
                Fraction(48),
            ),
            SequenceType.EXPONENTIAL,
        ),
    ],
)
def test_find_nth_term(
    sequence: tuple[Fraction, ...],
    expected_type: SequenceType,
):
    result = find_nth_term(sequence)

    assert result.sequence_type == expected_type


def test_find_linear_formula():
    sequence = (
        Fraction(2),
        Fraction(5),
        Fraction(8),
        Fraction(11),
        Fraction(14),
    )

    result = find_nth_term(sequence)

    assert result.formula == r"3n - 1"
    assert result.coefficients == (
        Fraction(3),
        Fraction(-1),
    )


def test_find_quadratic_formula():
    sequence = (
        Fraction(6),
        Fraction(15),
        Fraction(28),
        Fraction(45),
        Fraction(66),
    )

    result = find_nth_term(sequence)

    assert result.formula == r"2n^2 + 3n + 1"
    assert result.coefficients == (
        Fraction(2),
        Fraction(3),
        Fraction(1),
    )


def test_find_cubic_formula():
    sequence = (
        Fraction(4),
        Fraction(14),
        Fraction(40),
        Fraction(88),
        Fraction(164),
    )

    result = find_nth_term(sequence)

    assert result.formula == r"n^3 + 2n^2 - 3n + 4"
    assert result.coefficients == (
        Fraction(1),
        Fraction(2),
        Fraction(-3),
        Fraction(4),
    )


def test_find_exponential_formula():
    sequence = (
        Fraction(3),
        Fraction(6),
        Fraction(12),
        Fraction(24),
        Fraction(48),
    )

    result = find_nth_term(sequence)

    assert result.formula == r"3\left(2\right)^{n-1}"
    assert result.coefficients == (
        Fraction(3),
        Fraction(2),
    )


def test_find_unknown_sequence():
    sequence = (
        Fraction(1),
        Fraction(2),
        Fraction(6),
        Fraction(24),
        Fraction(120),
    )

    result = find_nth_term(sequence)

    assert result.sequence_type == SequenceType.UNKNOWN
    assert result.formula is None
    assert result.coefficients == ()