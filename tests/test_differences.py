from fractions import Fraction

import pytest

from nth_term.differences import calculate_differences


@pytest.mark.parametrize(
    ("sequence", "expected"),
    [
        (
            (Fraction(1), Fraction(4), Fraction(9), Fraction(16)),
            (Fraction(3), Fraction(5), Fraction(7)),
        ),
        (
            (Fraction(2), Fraction(5), Fraction(8), Fraction(11)),
            (Fraction(3), Fraction(3), Fraction(3)),
        ),
        (
            (Fraction(10), Fraction(7), Fraction(4), Fraction(1)),
            (Fraction(-3), Fraction(-3), Fraction(-3)),
        ),
        (
            (Fraction(-5), Fraction(-2), Fraction(1), Fraction(4)),
            (Fraction(3), Fraction(3), Fraction(3)),
        ),
        (
            (Fraction(1, 2), Fraction(1), Fraction(3, 2)),
            (Fraction(1, 2), Fraction(1, 2)),
        ),
    ],
)
def test_calculate_differences(
    sequence: tuple[Fraction, ...],
    expected: tuple[Fraction, ...],
):
    assert calculate_differences(sequence) == expected


def test_calculate_differences_with_two_terms():
    sequence = (Fraction(3), Fraction(8))

    assert calculate_differences(sequence) == (Fraction(5),)


def test_calculate_differences_with_single_term():
    assert calculate_differences((Fraction(5),)) == ()


def test_calculate_differences_with_empty_sequence():
    assert calculate_differences(()) == ()


def test_calculate_differences_does_not_modify_sequence():
    sequence = (Fraction(1), Fraction(4), Fraction(9))

    calculate_differences(sequence)

    assert sequence == (
        Fraction(1),
        Fraction(4),
        Fraction(9),
    )