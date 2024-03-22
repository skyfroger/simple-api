from typing import Union, List
from pydantic import BaseModel

from fastapi import APIRouter
router = APIRouter(tags=["Холст"])

# модель точки на холсте
class CanvasPoint(BaseModel):
    x: Union[int|float]
    y: Union[int|float]
    color: Union[int, str]

class CanvasContent(BaseModel):
    canvas: List[CanvasPoint]


pixels_field = []  # массив с координатами и цветами пикселей

@router.post("/api/canvas", response_model=CanvasPoint)
async def add_point_to_canvas(point: CanvasPoint):
    if len(pixels_field) < 256:
        pixels_field.append(point)
    return point

@router.get("/api/canvas", response_model=CanvasContent)
async def get_canvas_content():
    return {"canvas": pixels_field}

@router.delete("/api/canvas", response_model=CanvasContent)
async def clear_canvas():
    pixels_field.clear()
    return {"canvas": pixels_field}
