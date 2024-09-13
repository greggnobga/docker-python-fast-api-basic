from fastapi import FastAPI, HTTPException # type: ignore
from sqlmodel import create_engine, SQLModel, Session, select # type: ignore

from src.schemas import Car, CarInput

app = FastAPI(title="Car Sharing")

DATABASE_URL = "sqlite:///./app/carsharing.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def welcome(name: str):
    if(name):
        return {"message": f"Welcome, {name}!"}
    else:
        return {"message": "Welcome, guest!"}

@app.get("/api/cars")
def get_cars(size: str = None, doors: int = None) -> list:
    with Session(engine) as session:
        query = select(Car)
        if size:
            query = query.where(Car.size == size)
        if doors:
            query = query.where(Car.doors >= doors)
    return session.exec(query).all()

@app.get("/api/cars/{id}")
def car_by_id(id: int):
    result =  True
    if result:
        return  True
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")

@app.post("/api/cars", response_model=Car)
def add_car(car_input: CarInput):
    with Session(engine) as session:
        new_car = Car.from_orm(car_input)
        session.add(new_car)
        session.commit()
        session.refresh(new_car)
        return new_car
