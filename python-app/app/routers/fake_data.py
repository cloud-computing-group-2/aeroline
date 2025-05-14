from fastapi import APIRouter

from app import schemas
from app.scripts import faking_db, faking_db_2

router = APIRouter()

@router.post("/fake-data/passenger")
def create_fake_data(count: int = 10):
    """
    Create fake data for testing purposes.
    """
    faking_db(count)
    return {"message": f"Fake data created successfully with count: {count}"}


@router.post("/fake-data/reservation")
def create_fake_data(count: int = 10):
    """
    Create fake data for testing purposes.
    """
    faking_db_2(count)
    return {"message": f"Fake data created successfully with count: {count}"}
