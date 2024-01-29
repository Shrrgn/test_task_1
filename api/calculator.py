from typing import Final
from abc import ABC, abstractmethod

from api.enums import OperatorTypes


class BaseOperation(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> float:
        pass


class AddOperation(BaseOperation):
    def execute(self, a: int, b: int) -> float:
        return a + b


class SubtractOperation(BaseOperation):
    def execute(self, a: int, b: int) -> float:
        return a - b


class MultiplyOperation(BaseOperation):
    def execute(self, a: int, b: int) -> float:
        return a * b


class DivideOperation(BaseOperation):
    def execute(self, a: int, b: int) -> float:
        if b == 0:
            return 0

        return a / b


class Calculator:
    _round_digits: Final[int] = 3
    _operations: dict[OperatorTypes, BaseOperation] = {
        OperatorTypes.ADD: AddOperation(),
        OperatorTypes.SUBTRACT: SubtractOperation(),
        OperatorTypes.MULTIPLY: MultiplyOperation(),
        OperatorTypes.DIVIDE: DivideOperation(),
    }

    def calculate(self, a: int, b: int, operator: OperatorTypes) -> int | float:
        if operator in self._operations:
            result = self._operations[operator].execute(a, b)
            return round(result, self._round_digits)
        else:
            raise ValueError(f"Invalid operator: {operator}")
