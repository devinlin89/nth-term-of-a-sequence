from fractions import Fraction


def format_fraction(value: Fraction) -> str:
    """Format a fraction as a LaTeX number."""

    if value.denominator == 1:
        return str(value.numerator)

    sign = "-" if value < 0 else ""
    numerator = abs(value.numerator)

    return f"{sign}\\frac{{{numerator}}}{{{value.denominator}}}"


def format_term(coefficient: Fraction, variable: str) -> str:
    """Format a coefficient-variable term as LaTeX."""

    if coefficient == 0:
        return ""

    if coefficient == 1:
        return variable

    if coefficient == -1:
        return f"-{variable}"

    return f"{format_fraction(coefficient)}{variable}"


def format_signed_term(
    coefficient: Fraction,
    variable: str,
) -> str:
    """Format a non-leading coefficient-variable term as LaTeX."""

    if coefficient == 0:
        return ""

    sign = "+" if coefficient > 0 else "-"
    term = format_term(abs(coefficient), variable)

    return f"{sign} {term}"


def format_signed_constant(coefficient: Fraction) -> str:
    """Format a non-leading constant as LaTeX."""

    if coefficient == 0:
        return ""

    sign = "+" if coefficient > 0 else "-"
    magnitude = format_fraction(abs(coefficient))

    return f"{sign} {magnitude}"