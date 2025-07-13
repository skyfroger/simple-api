from pydantic import BaseModel
from enum import Enum
from typing import Dict, List

from random import choice

from fastapi import APIRouter

router = APIRouter(tags=["Цитаты"])


# модель ответа о чётности числа
class QuoteData(BaseModel):
    text: str
    author: str


class QuoteTheme(str, Enum):
    didact = "didact"
    inf = "inf"


quotes_data: Dict[QuoteTheme, List[QuoteData]] = {
    "inf": [
        {
            "text": "Программисты — это люди, которые решают проблемы, которые не существовали до их появления.",
            "author": "Билл Гейтс",
        },
        {
            "text": "Программы должны писаться для людей, которые будут их читать.",
            "author": "Харольд Абельсон",
        },
        {
            "text": "Программирование — это не просто работа, это стиль жизни.",
            "author": "Мартин Фаулер",
        },
    ],
    "didact": [
        {"text": "Обучая учусь.", "author": "Сенека Старший"},
        {
            "text": "Плохой учитель преподносит истину, хороший учит ее находить.",
            "author": "Адольф Дистервег",
        },
        {
            "text": "Мы лишаем детей будущего, если продолжаем учить сегодня так, как учили этому вчера.",
            "author": "Джон Дьюи",
        },
        {
            "text": "Ни один наставник не должен забывать, что его главнейшая обязанность состоит в приучении воспитанников к умственному труду и что эта обязанность более важна, нежели передача самого предмета.",
            "author": "Константин Ушинский",
        },
    ],
}


@router.get(
    "/quote/{theme}",
    response_model=QuoteData,
    summary="Получить случайную цитату",
    description="Возвращает цитату по одной из тем: физика, математика или информатика",
)
async def get_quote(theme: QuoteTheme):
    return choice(quotes_data.get(theme, []))
