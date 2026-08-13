from .differences import calculate_differences
from .models import (
    CubicFormula,
    ExponentialFormula,
    LinearFormula,
    QuadraticFormula,
    SequenceData,
    SequenceType,
)

GENERAL_FORMULAS: dict[SequenceType, str] = {
    SequenceType.LINEAR: r"U_n = an + b",
    SequenceType.QUADRATIC: r"U_n = an^2 + bn + c",
    SequenceType.CUBIC: r"U_n = an^3 + bn^2 + cn + d",
    SequenceType.EXPONENTIAL: r"U_n = ar^{n-1}",
}

COEFFICIENT_NAMES: dict[SequenceType, tuple[str, ...]] = {
    SequenceType.LINEAR: ("a", "b"),
    SequenceType.QUADRATIC: ("a", "b", "c"),
    SequenceType.CUBIC: ("a", "b", "c", "d"),
    SequenceType.EXPONENTIAL: ("a", "r"),
}


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