from pydantic import BaseModel, Field
from typing import Literal
from uuid import uuid4
from datetime import datetime


class Description(BaseModel):
    type: str = Field(..., description="Type of equipment", example="backpack")
    colour: str = Field(..., description="Colour of the equipment", example="blue")


class EquipmentCreate(BaseModel):
    passenger_id: str = Field(..., description="Passenger's ID", example="12345")
    flight_id: str = Field(..., description="Flight ID", example="67890")
    weight: str = Field(..., description="Weight of the equipment", example="15kg")
    description: Description
    registered_date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "passenger_id": "12345",
                "flight_id": "67890",
                "weight": "15kg",
                "description": {
                    "type": "backpack",
                    "colour": "blue"
                }
            }
        }
