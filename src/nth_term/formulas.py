from .differences import calculate_differences
from .models import (
    ArithmeticFormula,
    CubicFormula,
    GeometricFormula,
    QuadraticFormula,
    SequenceData,
    SequenceType,
)

GENERAL_FORMULAS: dict[SequenceType, str] = {
    SequenceType.ARITHMETIC: r"U_n = an + b",
    SequenceType.QUADRATIC: r"U_n = an^2 + bn + c",
    SequenceType.CUBIC: r"U_n = an^3 + bn^2 + cn + d",
    SequenceType.GEOMETRIC: r"U_n = ar^{n-1}",
}

COEFFICIENT_NAMES: dict[SequenceType, tuple[str, ...]] = {
    SequenceType.ARITHMETIC: ("a", "b"),
    SequenceType.QUADRATIC: ("a", "b", "c"),
    SequenceType.CUBIC: ("a", "b", "c", "d"),
    SequenceType.GEOMETRIC: ("a", "r"),
}


def calculate_arithmetic_formula(
    sequence: SequenceData,
) -> ArithmeticFormula:
    """Calculate the nth-term formula for a arithmetic sequence.

    Args:
        sequence (SequenceData): A sequence with constant first differences.

    Returns:
        ArithmeticFormula: The coefficients of the arithmetic nth-term formula.
    """

    differences = calculate_differences(sequence)
    common_difference = differences[0]

    first_term = sequence[0]
    b = first_term - common_difference

    return ArithmeticFormula(
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


def calculate_geometric_formula(
    sequence: SequenceData,
) -> GeometricFormula:
    """Calculate the nth-term formula for an geometric sequence.

    Args:
        sequence (SequenceData): A sequence with constant common ratio.

    Returns:
        GeometricFormula: The coefficients of the geometric nth-term formula.
    """

    first_term = sequence[0]
    common_ratio = sequence[1] / sequence[0]

    return GeometricFormula(
        a=first_term,
        r=common_ratio,
    )
