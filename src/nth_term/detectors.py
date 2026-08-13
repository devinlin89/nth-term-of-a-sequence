from itertools import pairwise

from .differences import calculate_differences
from .models import (
    SequenceData,
    SequenceType,
)


def _is_arithmetic(sequence: SequenceData) -> bool:
    """Return whether the sequence has a constant common difference."""

    # At least three terms are needed to establish a arithmetic pattern
    if len(sequence) < 3:
        return False

    first_differences = calculate_differences(sequence)

    common_difference = first_differences[0]

    return all(difference == common_difference for difference in first_differences)


def _is_quadratic(sequence: SequenceData) -> bool:
    """Return whether the sequence has constant second differences."""

    # Four terms are needed to obtain two second differences
    if len(sequence) < 4:
        return False

    first_differences = calculate_differences(sequence)
    second_differences = calculate_differences(first_differences)

    common_difference = second_differences[0]

    return all(difference == common_difference for difference in second_differences)


def _is_cubic(sequence: SequenceData) -> bool:
    """Return whether the sequence has constant third differences."""

    # Five terms are needed to obtain two third differences
    if len(sequence) < 5:
        return False

    first_differences = calculate_differences(sequence)
    second_differences = calculate_differences(first_differences)
    third_differences = calculate_differences(second_differences)

    common_difference = third_differences[0]

    return all(difference == common_difference for difference in third_differences)


def _is_geometric(sequence: SequenceData) -> bool:
    """Return whether the sequence has a constant common ratio."""

    # At least three terms are needed to establish a common ratio
    if len(sequence) < 3:
        return False

    # A common ratio cannot be calculated when a term is zero
    if 0 in sequence:
        return False

    ratios = tuple(current / previous for previous, current in pairwise(sequence))

    common_ratio = ratios[0]

    return all(ratio == common_ratio for ratio in ratios)


def detect_sequence_type(sequence: SequenceData) -> SequenceType:
    """Determine the type of a sequence.

    Args:
        sequence (SequenceData): A sequence of numeric values to analyze

    Returns:
        SequenceType: The detected type of the sequence
            (ARITHMETIC, QUADRATIC, CUBIC, GEOMETRIC, or UNKNOWN)
    """

    if _is_arithmetic(sequence):
        return SequenceType.ARITHMETIC

    if _is_quadratic(sequence):
        return SequenceType.QUADRATIC

    if _is_cubic(sequence):
        return SequenceType.CUBIC

    if _is_geometric(sequence):
        return SequenceType.GEOMETRIC

    return SequenceType.UNKNOWN
