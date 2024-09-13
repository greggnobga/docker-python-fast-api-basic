
from sqlmodel import SQLModel, Field # type: ignore

class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

    class Config:
        json_schema_extra = {
            "example": {
                "size": "m",
                "doors": 5,
                "fuel": "hybrid",
                "transmission": "manual"
            }
        }

class Car(CarInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
