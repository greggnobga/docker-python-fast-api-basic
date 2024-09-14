from fastapi import FastAPI, Request # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi.responses import FileResponse # type: ignore
from sqlmodel import SQLModel # type: ignore

from  starlette.responses import JSONResponse # type: ignore
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY # type: ignore

from src.db import engine
from src.routers import web, cars, auth
from src.routers.cars import BadTripException

app = FastAPI(title="Car Sharing")

favicon_path = '/app/src/favicon.ico'

app.include_router(web.router)
app.include_router(cars.router)
app.include_router(auth.router)

origins = [
    "http://python.hermes.pod"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.exception_handler(BadTripException)
async def unicorn_exceptio_handler(request: Request, exc: BadTripException):
    return JSONResponse (
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad Trip."}
    )

@app.middleware("http")
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cars_cookie", value="_random_cookie_value")
    return response

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
