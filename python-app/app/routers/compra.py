from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/compras/", response_model=list[schemas.Compra])
def read_compras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_compras(db, skip=skip, limit=limit)

@router.post("/compras/", response_model=schemas.Compra)
def create_compra(compra: schemas.CompraCreate, db: Session = Depends(get_db)):
    return crud.create_compra(db=db, compra=compra)
