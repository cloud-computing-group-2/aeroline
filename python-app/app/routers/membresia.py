from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
router = APIRouter()

@router.get("/membresias/", response_model=list[schemas.Membresia])
def read_membresias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_membresias(db, skip=skip, limit=limit)

@router.post("/membresias/", response_model=schemas.Membresia)
def create_membresia(membresia: schemas.MembresiaCreate, db: Session = Depends(get_db)):
    return crud.create_membresia(db=db, membresia=membresia)
