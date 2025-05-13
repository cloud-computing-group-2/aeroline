from fastapi import FastAPI
from app.routers import pasajero, membresia, compra
from app.database import init_db

app = FastAPI()

app.include_router(pasajero.router)
app.include_router(membresia.router)
app.include_router(compra.router)

init_db()


