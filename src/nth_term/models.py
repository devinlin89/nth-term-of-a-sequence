from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction

type SequenceData = Sequence[Fraction]


class SequenceType(Enum):
    LINEAR = "linear"
    QUADRATIC = "quadratic"
    CUBIC = "cubic"
    EXPONENTIAL = "exponential"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class NthTermResult:
    """Result of determining a sequence's nth-term formula.

    Attributes:
        sequence_type (SequenceType): The type of sequence that was detected.
        formula (str | None): The nth-term formula in LaTeX, or None if the
            sequence type is unknown.
        coefficients (tuple[Fraction, ...]): The formula coefficients in order,
            or an empty tuple if the sequence type is unknown.
    """

    sequence_type: SequenceType
    formula: str | None
    coefficients: tuple[Fraction, ...]