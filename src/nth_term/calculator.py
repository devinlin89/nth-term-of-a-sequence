from .detectors import detect_sequence_type
from .formatting import format_formula
from .formulas import (
    calculate_cubic_formula,
    calculate_exponential_formula,
    calculate_linear_formula,
    calculate_quadratic_formula,
)
from .models import (
    Formula,
    NthTermResult,
    SequenceData,
    SequenceType,
)


def find_nth_term(sequence: SequenceData) -> NthTermResult:
    """Determine the sequence type and calculate its nth-term formula.

    Args:
        sequence (SequenceData): The sequence of terms to analyze.

    Returns:
        NthTermResult: The detected sequence type, nth-term formula in LaTeX,
        and formula coefficients. If the sequence type is unknown, the
        formula is None and the coefficients are empty.
    """

    sequence_type = detect_sequence_type(sequence)

    formula: Formula

    match sequence_type:
        case SequenceType.LINEAR:
            formula = calculate_linear_formula(sequence)

        case SequenceType.QUADRATIC:
            formula = calculate_quadratic_formula(sequence)

        case SequenceType.CUBIC:
            formula = calculate_cubic_formula(sequence)

        case SequenceType.EXPONENTIAL:
            formula = calculate_exponential_formula(sequence)

        case SequenceType.UNKNOWN:
            return NthTermResult(
                sequence_type=sequence_type,
                formula=None,
                coefficients=(),
            )

    return NthTermResult(
        sequence_type=sequence_type,
        formula=format_formula(formula),
        coefficients=formula.coefficients,
    )