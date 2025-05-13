from fastapi import FastAPI
from app.routers import pasajero, membresia, compra, fake_data
from app.database import init_db

app = FastAPI()

app.include_router(pasajero.router)
app.include_router(membresia.router)
app.include_router(compra.router)
app.include_router(fake_data.router)

init_db()


