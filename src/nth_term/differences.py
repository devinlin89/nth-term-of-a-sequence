from fractions import Fraction
from itertools import pairwise

from .models import SequenceData


def calculate_differences(
    sequence: SequenceData,
) -> tuple[Fraction, ...]:
    """Calculate the differences between consecutive terms."""

    return tuple(
        current - previous
        for previous, current in pairwise(sequence)
    )