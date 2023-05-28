from fastapi import FastAPI
from car import Car 

app = FastAPI()
car_list = [

    {
        "id": 1,
        "brand": "Hyundai",
        "capacity": "1.2",
        "price": "10000"
    }
]



@app.get("/")
def car_shop():
    print(f"inside car_shop")
    return{"message": "Welcome to the Car shop"}


@app.post("/new_car")
def add_new_car(Car:Car):
    car_list.append(Car.dict())
    return car_list

@app.get("/cars")
def get_all_cars():
    return car_list

