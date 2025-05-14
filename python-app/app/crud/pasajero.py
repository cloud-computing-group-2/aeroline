from sqlalchemy.orm import Session
from app.models.pasajero import Pasajero as PasajeroModel  # importa modelo SQLAlchemy
from app.schemas.pasajero import PasajeroCreate  # importa esquema Pydantic
from app.models.compra import Compra  # importa modelo SQLAlchemy para Compras
from app.models.membresia import Membresia  # importa modelo SQLAlchemy para Membresías

def get_pasajeros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PasajeroModel).offset(skip).limit(limit).all()

def create_pasajero(db: Session, pasajero: PasajeroCreate):
    pasajero_db = PasajeroModel(**pasajero.dict())  # convierte de Pydantic a ORM
    db.add(pasajero_db)
    db.commit()
    db.refresh(pasajero_db)
    return pasajero_db

def delete_all(db: Session):
    try:

         # Eliminar todos los registros de Compras (si es necesario, aunque las relaciones ya están manejadas)
        db.query(Compra).delete()  # Eliminar todas las compras asociadas a los pasajeros
        db.commit()

        # Eliminar todos los Pasajeros (y sus Membresías y Compras asociadas, gracias a la cascada)
        db.query(PasajeroModel).delete()  # Elimina todos los Pasajeros y sus objetos relacionados
        db.commit()
        
        return {"message": "All pasajeros, membresias, and compras deleted successfully."}
    except Exception as e:
        db.rollback()  # Realizar rollback en caso de error
        return {"error": f"Error deleting records: {str(e)}"}