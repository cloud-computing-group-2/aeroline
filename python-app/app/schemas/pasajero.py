from pydantic import BaseModel
from datetime import date

class PasajeroBase(BaseModel):
    nombre_completo: str
    sexo: str
    fecha_nacimiento: date
    email: str
    telefono: str

class PasajeroCreate(PasajeroBase):
    pass

class Pasajero(PasajeroBase):
    id_pasajero: int

    class Config:
        orm_mode = True
