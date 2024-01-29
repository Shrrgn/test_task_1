from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from api.enums import OperatorTypes, ColorTypes
from api.schemas import OperatorsResponse, CalculateRequest, CalculateResponse
from api.calculator import Calculator
from api.parity import ParityChecker

router = APIRouter()
calculator = Calculator()
parity_checker = ParityChecker()


@router.get("/operators", response_model=OperatorsResponse)
async def get_operators():
    operators = OperatorTypes.options()
    return OperatorsResponse(operators=operators)


@router.post("/calculate", response_model=CalculateResponse, status_code=HTTP_200_OK)
async def calculate(payload: CalculateRequest):
    try:
        result = calculator.calculate(payload.operand1, payload.operand2, payload.operator)
        color: ColorTypes = parity_checker.check_parity(result)
        return CalculateResponse(result=result, color=color)

    except ValueError as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
