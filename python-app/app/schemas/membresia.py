from pydantic import BaseModel
from datetime import date

class MembresiaBase(BaseModel):
    tipo: str
    fecha_exploracion: date
    id_pasajero: int

class MembresiaCreate(MembresiaBase):
    pass

class Membresia(MembresiaBase):
    id_membresia: int

    class Config:
        orm_mode = True
