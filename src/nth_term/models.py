from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction

type SequenceData = Sequence[Fraction]


class SequenceType(Enum):
    ARITHMETIC = "arithmetic"
    QUADRATIC = "quadratic"
    CUBIC = "cubic"
    GEOMETRIC = "geometric"
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


@dataclass(frozen=True)
class ArithmeticFormula:
    a: Fraction
    b: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.b)


@dataclass(frozen=True)
class QuadraticFormula:
    a: Fraction
    b: Fraction
    c: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.b, self.c)


@dataclass(frozen=True)
class CubicFormula:
    a: Fraction
    b: Fraction
    c: Fraction
    d: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.b, self.c, self.d)


@dataclass(frozen=True)
class GeometricFormula:
    a: Fraction
    r: Fraction

    @property
    def coefficients(self) -> tuple[Fraction, ...]:
        return (self.a, self.r)


type Formula = ArithmeticFormula | QuadraticFormula | CubicFormula | GeometricFormula
