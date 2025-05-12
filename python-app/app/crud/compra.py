from sqlalchemy.orm import Session
from app.models.compra import Compra as CompraModel  # Importa el modelo SQLAlchemy
from app.schemas.compra import CompraCreate  # Importa el esquema Pydantic

def get_compras(db: Session, skip: int = 0, limit: int = 100):

    return db.query(CompraModel).offset(skip).limit(limit).all()

def create_compra(db: Session, compra: CompraCreate):

    compra_db = CompraModel(**compra.dict())  # Convierte el esquema Pydantic a un objeto del modelo SQLAlchemy
    db.add(compra_db)
    db.commit()
    db.refresh(compra_db)
    return compra_db
