import os
from fastapi import FastAPI
from app.routers import pasajero, membresia, compra
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

app = FastAPI()

app.include_router(pasajero.router)
app.include_router(membresia.router)
app.include_router(compra.router)

if __name__ == "__main__":
    import uvicorn
    PORT = int(os.getenv("PORT", 8082))
    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)
