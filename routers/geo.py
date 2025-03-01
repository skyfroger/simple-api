from typing import Union, List
from pydantic import BaseModel

from fastapi import APIRouter

router = APIRouter(tags=["Сябры"])


# модель точки на холсте
class GeoMarker(BaseModel):
    lat: float
    lng: float
    id: str


class MapContent(BaseModel):
    map: List[GeoMarker]


map_content = []  # массив с маркерами


@router.post("/geo", response_model=GeoMarker)
async def add_marker_to_map(user: GeoMarker):
    if len(map_content) < 128:
        existing_user = [u for u in map_content if user.id == u.id]
        if len(existing_user) > 0:
            existing_user[0].lat = user.lat
            existing_user[0].lng = user.lng
        else:
            map_content.append(user)
    return user


@router.get("/geo", response_model=MapContent)
async def get_map_content():
    return {"map": map_content}


@router.delete("/geo", response_model=MapContent)
async def clear_map():
    map_content.clear()
    return {"map": map_content}
