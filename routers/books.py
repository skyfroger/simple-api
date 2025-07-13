from pydantic import BaseModel
from typing import List, Annotated

from fastapi import APIRouter, Query

router = APIRouter(tags=["Библиотека"])


# модель ответа о чётности числа
class BookData(BaseModel):
    title: str
    author: str
    year: int


books: List[BookData] = [
    {"title": "Новая земля", "author": "Якуб Колас", "year": 1935},
    {"title": "Каласы пад сярпом тваім", "author": "Владимир Короткевич", "year": 1965},
    {"title": "Альпийская баллада", "author": "Василий Быков", "year": 1970},
    {"title": "Людзі на балоце", "author": "Иван Мележ", "year": 1957},
    {
        "title": "Христос приземлился в Гродно",
        "author": "Уладзімір Караткевіч",
        "year": 1966,
    },
    {"title": "На росстанях", "author": "Якуб Колас", "year": 1948},
    {
        "title": "Дикая охота короля Стаха",
        "author": "Владимир Короткевич",
        "year": 1957,
    },
    {"title": "Знак беды", "author": "Василий Быков", "year": 1970},
    {"title": "Тревожное счастье", "author": "Иван Шамякин", "year": 1970},
    {"title": "Круглянский мост", "author": "Василий Быков", "year": 1968},
    {"title": "Журавлиный крик", "author": "Василий Быков", "year": 1959},
    {"title": "Курган", "author": "Якуб Колас", "year": 1947},
    {"title": "Могила льва", "author": "Якуб Колас", "year": 1959},
    {"title": "Она и я", "author": "Янка Купала", "year": 1937},
    {"title": "Серебро жизни", "author": "К. Черный", "year": 1935},
    {"title": "По дороге", "author": "К. Черный", "year": 1938},
]


@router.get(
    "/books/",
    response_model=List[BookData],
    summary="Получить список книг",
)
async def get_books(author: Annotated[str, Query(title="Автор", max_length=128)]):
    def match_author(book: BookData) -> bool:
        return author.upper() in book["author"].upper()

    return list(filter(match_author, books))
