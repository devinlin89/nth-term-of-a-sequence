from fractions import Fraction

import pytest

from nth_term.detectors import detect_sequence_type
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
            SequenceType.ARITHMETIC,
        ),
        (
            (
                Fraction(10),
                Fraction(7),
                Fraction(4),
                Fraction(1),
                Fraction(-2),
            ),
            SequenceType.ARITHMETIC,
        ),
        (
            (
                Fraction(-5),
                Fraction(-2),
                Fraction(1),
                Fraction(4),
                Fraction(7),
            ),
            SequenceType.ARITHMETIC,
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
                Fraction(6),
                Fraction(15),
                Fraction(28),
                Fraction(45),
                Fraction(66),
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
                Fraction(2),
                Fraction(16),
                Fraction(54),
                Fraction(128),
                Fraction(250),
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
            SequenceType.GEOMETRIC,
        ),
        (
            (
                Fraction(32),
                Fraction(16),
                Fraction(8),
                Fraction(4),
                Fraction(2),
            ),
            SequenceType.GEOMETRIC,
        ),
    ],
)
def test_detect_sequence_type(
    sequence: tuple[Fraction, ...],
    expected_type: SequenceType,
):
    assert detect_sequence_type(sequence) == expected_type


@pytest.mark.parametrize(
    "sequence",
    [
        (Fraction(1), Fraction(-100), Fraction(4), Fraction(6700), Fraction(11)),
        (Fraction(1), Fraction(2), Fraction(6), Fraction(24), Fraction(120)),
    ],
)
def test_detect_unknown_sequence(sequence: tuple[Fraction, ...]):
    assert detect_sequence_type(sequence) == SequenceType.UNKNOWN


@pytest.mark.parametrize(
    "sequence",
    [
        (),
        (Fraction(1),),
        (Fraction(1), Fraction(2)),
    ],
)
def test_short_sequences(sequence: tuple[Fraction, ...]):
    assert detect_sequence_type(sequence) == SequenceType.UNKNOWN


def test_constant_sequence():
    sequence = (
        Fraction(5),
        Fraction(5),
        Fraction(5),
        Fraction(5),
    )

    assert detect_sequence_type(sequence) == SequenceType.ARITHMETIC


def test_arithmetic_sequence_with_zero_difference():
    sequence = (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )

    assert detect_sequence_type(sequence) == SequenceType.ARITHMETIC


def test_geometric_sequence_with_fractional_ratio():
    sequence = (
        Fraction(16),
        Fraction(8),
        Fraction(4),
        Fraction(2),
    )

    assert detect_sequence_type(sequence) == SequenceType.GEOMETRIC


def test_geometric_sequence_with_negative_ratio():
    sequence = (
        Fraction(2),
        Fraction(-4),
        Fraction(8),
        Fraction(-16),
    )

    assert detect_sequence_type(sequence) == SequenceType.GEOMETRIC
