from pydantic import BaseModel
from datetime import date

class CompraBase(BaseModel):
    fecha: date
    asiento: str
    id_pasajero: int
    id_vuelo: int

class CompraCreate(CompraBase):
    pass

class Compra(CompraBase):
    id_historial: int

    class Config:
        orm_mode = True
