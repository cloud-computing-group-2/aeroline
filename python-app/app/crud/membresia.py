from sqlalchemy.orm import Session
from app.models.membresia import Membresia as MembresiaModel  # Importa el modelo SQLAlchemy
from app.schemas.membresia import MembresiaCreate  # Importa el esquema Pydantic

def get_membresias(db: Session, skip: int = 0, limit: int = 100):

    return db.query(MembresiaModel).offset(skip).limit(limit).all()

def create_membresia(db: Session, membresia: MembresiaCreate):

    membresia_db = MembresiaModel(**membresia.dict())  # Convierte el esquema Pydantic a un objeto del modelo SQLAlchemy
    db.add(membresia_db)
    db.commit()
    db.refresh(membresia_db)
    return membresia_db
