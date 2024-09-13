from fastapi import FastAPI # type: ignore
from sqlmodel import SQLModel # type: ignore

from src.db import engine
from src.routers import web, cars

app = FastAPI(title="Car Sharing")

app.include_router(web.router)
app.include_router(cars.router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
