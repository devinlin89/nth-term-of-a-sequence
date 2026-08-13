from fractions import Fraction

import pytest

from nth_term.parsing import parse_sequence


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (
            "1, 2, 3, 4",
            (Fraction(1), Fraction(2), Fraction(3), Fraction(4)),
        ),
        (
            "1,2,3,4",
            (Fraction(1), Fraction(2), Fraction(3), Fraction(4)),
        ),
        (
            " 1 , 2 , 3 , 4 ",
            (Fraction(1), Fraction(2), Fraction(3), Fraction(4)),
        ),
        (
            "-1, -2, -3",
            (Fraction(-1), Fraction(-2), Fraction(-3)),
        ),
        (
            "1/2, 1, 3/2",
            (Fraction(1, 2), Fraction(1), Fraction(3, 2)),
        ),
        (
            "0.5, 1, 1.5",
            (Fraction(1, 2), Fraction(1), Fraction(3, 2)),
        ),
        (
            "1.25, 2.5, 3.75",
            (Fraction(5, 4), Fraction(5, 2), Fraction(15, 4)),
        ),
        (
            "0, 0, 0",
            (Fraction(0), Fraction(0), Fraction(0)),
        ),
    ],
)
def test_parse_sequence(
    value: str,
    expected: tuple[Fraction, ...],
):
    assert parse_sequence(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "",
        "   ",
        "abc",
        "1, abc, 3",
        "1,,3",
        ",1,2",
        "1,2,",
        "1, ,3",
        "1/0, 2",
    ],
)
def test_parse_invalid_sequence(value: str):
    with pytest.raises(ValueError):
        parse_sequence(value)


def test_parse_sequence_returns_tuple():
    result = parse_sequence("1, 2, 3")

    assert isinstance(result, tuple)


def test_parse_sequence_returns_fractions():
    result = parse_sequence("1, 2, 3")

    assert all(isinstance(term, Fraction) for term in result)