from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Pasajero(Base):
    __tablename__ = "pasajeros"

    id_pasajero = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, index=True)
    sexo = Column(String)
    fecha_nacimiento = Column(Date)
    email = Column(String, unique=True)
    telefono = Column(String)
