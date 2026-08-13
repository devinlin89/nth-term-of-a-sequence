from dataclasses import dataclass
from fractions import Fraction
from itertools import pairwise

from .differences import calculate_differences
from .models import SequenceData


def _format_fraction(value: Fraction) -> str:
    """Format a fraction as a LaTeX number."""

    if value.denominator == 1:
        return str(value.numerator)

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


@dataclass(frozen=True)
class LinearFormula:
    a: Fraction
    b: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.b)

    def __str__(self) -> str:
        terms = [
            _format_term(self.a, "n"),
            _format_signed_constant(self.b),
        ]

        return " ".join(term for term in terms if term)


@dataclass(frozen=True)
class QuadraticFormula:
    a: Fraction
    b: Fraction
    c: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.b, self.c)

    def __str__(self) -> str:
        terms = [
            _format_term(self.a, "n^2"),
            _format_signed_term(self.b, "n"),
            _format_signed_constant(self.c),
        ]

        return " ".join(term for term in terms if term)


@dataclass(frozen=True)
class CubicFormula:
    a: Fraction
    b: Fraction
    c: Fraction
    d: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.b, self.c, self.d)

    def __str__(self) -> str:
        terms = [
            _format_term(self.a, "n^3"),
            _format_signed_term(self.b, "n^2"),
            _format_signed_term(self.c, "n"),
            _format_signed_constant(self.d),
        ]

        return " ".join(term for term in terms if term)


@dataclass(frozen=True)
class ExponentialFormula:
    a: Fraction
    r: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.r)

    def __str__(self) -> str:
        return (
            f"{_format_fraction(self.a)}"
            f"({_format_fraction(self.r)})^{{n-1}}"
        )


type Formula = (
    LinearFormula
    | QuadraticFormula
    | CubicFormula
    | ExponentialFormula
)


def calculate_linear_formula(
    sequence: SequenceData,
) -> LinearFormula:
    """Calculate the nth-term formula for a linear sequence."""

    differences = calculate_differences(sequence)
    common_difference = differences[0]

    first_term = sequence[0]
    b = first_term - common_difference

    return LinearFormula(
        a=common_difference,
        b=b,
    )


def calculate_quadratic_formula(
    sequence: SequenceData,
) -> QuadraticFormula:
    """Calculate the nth-term formula for a quadratic sequence."""

    first_differences = calculate_differences(sequence)
    second_differences = calculate_differences(first_differences)

    a = second_differences[0] / 2
    b = first_differences[0] - 3 * a
    c = sequence[0] - a - b

    return QuadraticFormula(
        a=a,
        b=b,
        c=c,
    )


def calculate_cubic_formula(
    sequence: SequenceData,
) -> CubicFormula:
    """Calculate the nth-term formula for a cubic sequence."""

    first_differences = calculate_differences(sequence)
    second_differences = calculate_differences(first_differences)
    third_differences = calculate_differences(second_differences)

    a = third_differences[0] / 6
    b = (second_differences[0] - 12 * a) / 2
    c = first_differences[0] - 7 * a - 3 * b
    d = sequence[0] - a - b - c

    return CubicFormula(
        a=a,
        b=b,
        c=c,
        d=d,
    )


def calculate_exponential_formula(
    sequence: SequenceData,
) -> ExponentialFormula:
    """Calculate the nth-term formula for an exponential sequence."""

    first_term = sequence[0]

    ratios = tuple(
        current / previous
        for previous, current in pairwise(sequence)
    )
    common_ratio = ratios[0]

    return ExponentialFormula(
        a=first_term,
        r=common_ratio,
    )