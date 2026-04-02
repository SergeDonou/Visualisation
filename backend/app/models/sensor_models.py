from pydantic import BaseModel
from datetime import datetime

class SensorData(BaseModel):
    id: int
    sensor_name: str
    value: float
    timestamp: datetime
