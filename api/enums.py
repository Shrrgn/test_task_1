from enum import Enum


class OperatorTypes(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

    @classmethod
    def options(cls):
        return [op.value for op in cls]


class ColorTypes:
    RED = "red"
    GREEN = "green"
