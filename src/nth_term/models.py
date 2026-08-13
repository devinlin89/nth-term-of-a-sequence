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
    sequence_type: SequenceType
    formula: str | None
    coefficients: tuple[Fraction, ...]