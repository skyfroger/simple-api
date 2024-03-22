from typing import Union, List
from random import choice

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# модель ответа для Магического шара
class Ball8Answer(BaseModel):
    answer: str

# модель ответа о чётности числа
class EvenNumberAnser(BaseModel):
    number: int
    isEven: bool

# модель точки на холсте
class CanvasPoint(BaseModel):
    x: int
    y: int
    color: Union[int, str]

class CanvasContent(BaseModel):
    canvas: List[CanvasPoint]

@app.get("/api/8ball", response_model=Ball8Answer)
async def get_8ball_message():
    messages = [
        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Определённо да",
        "Можешь быть уверен в этом",
        "Мне кажется — «да»",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят — «да»",
        "Да",
        "Пока не ясно, попробуй снова",
        "Спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять",
        "Даже не думай",
        "Мой ответ — «нет»",
        "По моим данным — «нет»",
        "Перспективы не очень хорошие",
        "Весьма сомнительно",
    ]
    return {"answer": choice(messages)}

@app.get("/api/is-even/{number}", response_model=EvenNumberAnser)
async def is_number_even(number: int):
    return {"number": number, "isEven": number % 2 == 0}

pixels_field = []  # массив с координатами и цветами пикселей

@app.post("/api/canvas", response_model=CanvasPoint)
async def add_point_to_canvas(point: CanvasPoint):
    if len(pixels_field) < 256:
        pixels_field.append(point)
    return point

@app.get("/api/canvas", response_model=CanvasContent)
async def get_canvas_content():
    return {"canvas": pixels_field}

@app.delete("/api/canvas", response_model=CanvasContent)
async def clear_canvas():
    pixels_field.clear()
    return {"canvas": pixels_field}