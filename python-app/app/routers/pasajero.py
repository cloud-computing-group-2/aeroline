# app/routers/pasajero.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/pasajeros/", response_model=list[schemas.Pasajero])
def read_pasajeros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_pasajeros(db, skip=skip, limit=limit)

@router.post("/pasajeros/", response_model=schemas.Pasajero)
def create_pasajero(pasajero: schemas.PasajeroCreate, db: Session = Depends(get_db)):
    return crud.create_pasajero(db=db, pasajero=pasajero)

@router.delete("/delete_all")
def delete_all(db: Session = Depends(get_db)):
    return crud.delete_all(db=db)