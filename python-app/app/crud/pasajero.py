from sqlalchemy.orm import Session
from app.models.pasajero import Pasajero as PasajeroModel  # importa modelo SQLAlchemy
from app.schemas.pasajero import PasajeroCreate  # importa esquema Pydantic

def get_pasajeros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PasajeroModel).offset(skip).limit(limit).all()

def create_pasajero(db: Session, pasajero: PasajeroCreate):
    pasajero_db = PasajeroModel(**pasajero.dict())  # convierte de Pydantic a ORM
    db.add(pasajero_db)
    db.commit()
    db.refresh(pasajero_db)
    return pasajero_db
