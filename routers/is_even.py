from pydantic import BaseModel

from fastapi import APIRouter
router = APIRouter(tags=["Число чётное?"])

# модель ответа о чётности числа
class EvenNumberAnser(BaseModel):
    number: int
    isEven: bool

@router.get("/is-even/{number}", response_model=EvenNumberAnser)
async def is_number_even(number: int):
    return {"number": number, "isEven": number % 2 == 0}
