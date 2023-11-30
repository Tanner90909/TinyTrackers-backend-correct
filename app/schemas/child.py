from typing import Optional
from sqlalchemy import Date

from pydantic import BaseModel, EmailStr

class ChildBaseSchema(BaseModel):
    first_name: str
    last_name: str
    dob: Date
    allergies: str
    pediatrician_name: str
    pediatrician_number: str