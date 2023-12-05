from typing import Optional
from datetime import date

from pydantic import BaseModel

class ChildBaseSchema(BaseModel):
    unique_child_id_code: str
    first_name: str
    last_name: str
    dob: date
    allergies: Optional[str]
    pediatrician_name: Optional[str]
    pediatrician_number: Optional[str]

class ChildCreateSchema(ChildBaseSchema):
    first_name: str
    last_name: str
    dob: date

class ChildUpdateSchema(ChildBaseSchema):
    first_name: str
    last_name: str
    dob: date
    allergies: str
    pediatrician_name: str
    pediatrician_number: str

class ChildInDBBaseSchema(ChildBaseSchema):
    id: Optional[int]

    class Config:
        from_attributes = True

class ChildSchema(ChildInDBBaseSchema):
    pass