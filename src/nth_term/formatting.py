from fractions import Fraction

from .models import (
    CubicFormula,
    ExponentialFormula,
    Formula,
    LinearFormula,
    QuadraticFormula,
)


def _format_fraction(value: Fraction) -> str:
    """Format a fraction as a LaTeX number."""

    if value.denominator == 1:
        return str(value.numerator)

    if value.numerator < 0:
        return f"-\\frac{{{abs(value.numerator)}}}{{{value.denominator}}}"

    return f"\\frac{{{value.numerator}}}{{{value.denominator}}}"


def _format_term(coefficient: Fraction, variable: str) -> str:
    """Format a coefficient-variable term as LaTeX."""

    if coefficient == 0:
        return ""

    if coefficient == 1:
        return variable

    if coefficient == -1:
        return f"-{variable}"

    return f"{_format_fraction(coefficient)}{variable}"


def _format_signed_term(coefficient: Fraction, variable: str) -> str:
    """Format a non-leading coefficient-variable term as LaTeX."""

    if coefficient == 0:
        return ""

    sign = "+" if coefficient > 0 else "-"
    magnitude = abs(coefficient)

    if magnitude == 1:
        term = variable
    else:
        term = f"{_format_fraction(magnitude)}{variable}"

    return f"{sign} {term}"


def _format_signed_constant(coefficient: Fraction) -> str:
    """Format a non-leading constant as LaTeX."""

    if coefficient == 0:
        return ""

    sign = "+" if coefficient > 0 else "-"
    magnitude = abs(coefficient)

    return f"{sign} {_format_fraction(magnitude)}"


def format_formula(formula: Formula) -> str:
    """Format a sequence formula as a LaTeX expression.

    Args:
        formula: The formula to format.

    Returns:
        A LaTeX representation of the formula.
    """

    if isinstance(formula, LinearFormula):
        terms = [
            _format_term(formula.a, "n"),
            _format_signed_constant(formula.b),
        ]

    elif isinstance(formula, QuadraticFormula):
        terms = [
            _format_term(formula.a, "n^2"),
            _format_signed_term(formula.b, "n"),
            _format_signed_constant(formula.c),
        ]

    elif isinstance(formula, CubicFormula):
        terms = [
            _format_term(formula.a, "n^3"),
            _format_signed_term(formula.b, "n^2"),
            _format_signed_term(formula.c, "n"),
            _format_signed_constant(formula.d),
        ]

    elif isinstance(formula, ExponentialFormula):
        terms = [
            (
                f"{_format_fraction(formula.a)}"
                f"\\left({_format_fraction(formula.r)}\\right)^{{n-1}}"
            )
        ]

    else:
        raise TypeError(
            f"Unsupported formula type: {type(formula).__name__}"
        )

    return " ".join(term for term in terms if term)