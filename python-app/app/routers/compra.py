from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.crud.compra import create_compra, vuelo_existe  # Importas la validación y CRUD

router = APIRouter()

@router.get("/compras/", response_model=list[schemas.Compra])
def read_compras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_compras(db, skip=skip, limit=limit)

@router.post("/compras/", response_model=schemas.Compra)
async def crear_compra_endpoint(compra: schemas.CompraCreate, db: Session = Depends(get_db)):
    # Validamos que el vuelo existe
    if not await vuelo_existe(compra.id_vuelo):
        raise HTTPException(status_code=400, detail="El vuelo no existe en el microservicio de viajes")
    
    # Creamos la compra
    compra_db = create_compra(db=db, compra=compra)
    return compra_db
