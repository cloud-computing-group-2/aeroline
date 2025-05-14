from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.database import Base

class Pasajero(Base):
    __tablename__ = "pasajeros"

    id_pasajero = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    nombre_completo = Column(String(256), index=True)
    sexo = Column(String(16))
    fecha_nacimiento = Column(Date)
    email = Column(String(48), unique=True)
    telefono = Column(String(32), unique=True)
    membresias = relationship("Membresia", back_populates="pasajero", cascade="all, delete")
    compras = relationship("Compra", back_populates="pasajero", cascade="all, delete")
