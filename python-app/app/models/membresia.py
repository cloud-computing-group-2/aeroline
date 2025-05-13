from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Membresia(Base):
    __tablename__ = "membresias"

    id_membresia = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(12))  # Puede ser 'clasica' o 'premium'
    fecha_exploracion = Column(Date)
    id_pasajero = Column(Integer, ForeignKey("pasajeros.id_pasajero"))

    pasajero = relationship("Pasajero", back_populates="membresias")
