from datetime import datetime
from pydantic import BaseModel

class Complaint(BaseModel):
    complaint_id: int   
    text: str
    timestamp: datetime
    latitude: float
    longitude: float