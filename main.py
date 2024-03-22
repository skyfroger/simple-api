from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import ball8, is_even, canvas

app = FastAPI(title="Simple API", description="Набор тестовых API", root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ball8.router)
app.include_router(is_even.router)
app.include_router(canvas.router)
