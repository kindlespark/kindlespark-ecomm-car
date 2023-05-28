from pydantic import BaseModel


class Car(BaseModel):
    id: int
    brand: str
    capacity: str
    price: str
