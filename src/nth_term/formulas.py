from dataclasses import dataclass
from fractions import Fraction

from .differences import calculate_differences
from .formatting import (
    format_fraction,
    format_signed_constant,
    format_signed_term,
    format_term,
)
from .models import SequenceData


@dataclass(frozen=True)
class LinearFormula:
    a: Fraction
    b: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.b)

    def __str__(self) -> str:
        terms = (
            format_term(self.a, "n"),
            format_signed_constant(self.b),
        )

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
        terms = (
            format_term(self.a, "n^2"),
            format_signed_term(self.b, "n"),
            format_signed_constant(self.c),
        )

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
        terms = (
            format_term(self.a, "n^3"),
            format_signed_term(self.b, "n^2"),
            format_signed_term(self.c, "n"),
            format_signed_constant(self.d),
        )

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
            f"{format_fraction(self.a)}\\left({format_fraction(self.r)}\\right)^{{n-1}}"
        )


type Formula = LinearFormula | QuadraticFormula | CubicFormula | ExponentialFormula


def calculate_linear_formula(
    sequence: SequenceData,
) -> LinearFormula:
    """Calculate the nth-term formula for a linear sequence.

    Args:
        sequence (SequenceData): A sequence with constant first differences.

    Returns:
        LinearFormula: The coefficients of the linear nth-term formula.
    """

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
    """Calculate the nth-term formula for a quadratic sequence.

    Args:
        sequence (SequenceData): A sequence with constant second differences.

    Returns:
        QuadraticFormula: The coefficients of the quadratic nth-term formula.
    """

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
    """Calculate the nth-term formula for a cubic sequence.

    Args:
        sequence (SequenceData): A sequence with constant third differences.

    Returns:
        CubicFormula: The coefficients of the cubic nth-term formula.
    """

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
    """Calculate the nth-term formula for an exponential sequence.

    Args:
        sequence (SequenceData): A sequence with constant common ratio.

    Returns:
        ExponentialFormula: The coefficients of the exponential nth-term formula.
    """

    first_term = sequence[0]
    common_ratio = sequence[1] / sequence[0]

    return ExponentialFormula(
        a=first_term,
        r=common_ratio,
    )