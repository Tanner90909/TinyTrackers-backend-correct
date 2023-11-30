from typing import Optional
from sqlalchemy import DateTime, Time

from pydantic import BaseModel

class EventSchema(BaseModel):
    when: DateTime

class MedicineEventSchema(BaseModel):
    dose: int
    medicine_type: str
    time_to_next_dose: Time
    description: str

class SymptomEventSchema(BaseModel):
    symptom_type: str
    severity: int
    description: str

class OtherEventSchema(BaseModel):
    description: str

class EventTypeSchema(BaseModel):
    name: str