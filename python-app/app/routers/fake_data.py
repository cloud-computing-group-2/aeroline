from fastapi import APIRouter

from app import schemas
from app.database import faking_db

router = APIRouter()

@router.post("/fake-data")
def create_fake_data(count: int = 10):
    """
    Create fake data for testing purposes.
    """
    faking_db(count)
    return {"message": f"Fake data created successfully with count: {count}"}
