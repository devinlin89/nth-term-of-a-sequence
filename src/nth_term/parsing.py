from fractions import Fraction


def parse_sequence(value: str) -> tuple[Fraction, ...]:
    """Parse a comma-separated sequence into exact rational numbers."""

    if not value.strip():
        raise ValueError("The sequence cannot be empty.")

    terms = value.split(",")

    try:
        sequence = tuple(
            Fraction(term.strip())
            for term in terms
        )
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError("The sequence contains an invalid number.") from error

    return sequence