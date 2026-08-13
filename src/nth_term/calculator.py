from .detectors import detect_sequence_type
from .formulas import (
    Formula,
    calculate_cubic_formula,
    calculate_exponential_formula,
    calculate_linear_formula,
    calculate_quadratic_formula,
)
from .models import (
    NthTermResult,
    SequenceData,
    SequenceType,
)


def find_nth_term(sequence: SequenceData) -> NthTermResult:
    """Determine the sequence type and calculate its nth-term formula."""

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
        formula=str(formula),
        coefficients=formula.coefficients,
    )