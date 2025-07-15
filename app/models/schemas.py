# app/models/schemas

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SensorData(BaseModel):
    sensor_id: str = Field(..., description="Unique Sensor ID")
    type: str = Field(..., description="Sensor Type (temperatur, humidity, etc.)")
    value: float = Field(..., description="Measured Value")
    timestamp: datetime = Field(..., description="Timestamp")

class SensorDataResponse(SensorData):
    id: int