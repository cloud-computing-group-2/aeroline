from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Description(BaseModel):
    type: str
    details: str

class EquipmentCreate(BaseModel):
    passenger_id: str
    flight_id: str
    weight: str
    description: Description
    registered_date: Optional[datetime] = None
