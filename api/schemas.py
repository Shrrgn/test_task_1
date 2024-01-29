from pydantic import BaseModel

from api.enums import OperatorTypes, ColorTypes


class OperatorsResponse(BaseModel):
    operators:  list[str]


class CalculateRequest(BaseModel):
    operand1: int
    operand2: int
    operator: OperatorTypes


class CalculateResponse(BaseModel):
    result: int | float
    color: str
