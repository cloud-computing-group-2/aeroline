from fastapi import FastAPI
from users import create_user, get_user
from baggage import create_equipment, get_equipment
from entities import EquipmentCreate
from flights import create_flight, get_flight_by_id, get_all_flights, update_flight, delete_flight
import os

app = FastAPI()

# Usuarios
@app.post("/user")
async def create_user_endpoint(user: dict):
    return create_user(user)

@app.get("/user/{id}")
async def get_user_endpoint(id: str):
    return get_user(id)

# Equipaje
@app.post("/equipment", )
async def create_equipment_endpoint(equipment: EquipmentCreate):
    return create_equipment(equipment)

@app.get("/equipment/{id}")
async def get_equipment_endpoint(id: int):
    return get_equipment(id)

# Vuelos
@app.post("/flight")
async def create_flight_endpoint(flight: dict):
    return create_flight(flight)


@app.get("/flight/all")
async def get_all_flights_endpoint():
    return get_all_flights()

@app.get("/flight/{id_flight}")
async def get_flight_by_id_endpoint(id_flight: int):
    return get_flight_by_id(id_flight)

@app.put("/flight/{id_flight}")
async def update_flight_endpoint(id_flight: int, flight: dict):
    return update_flight(id_flight, flight)

@app.delete("/flight/{id_flight}")
async def delete_flight_endpoint(id_flight: int):
    return delete_flight(id_flight)
