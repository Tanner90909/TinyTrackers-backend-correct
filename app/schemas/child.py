from typing import Optional

from pydantic import BaseModel

class ChildBaseSchema(BaseModel):
    first_name: str
    last_name: str
    dob: str
    allergies: Optional[str]
    pediatrician_name: Optional[str]
    pediatrician_number: Optional[str]

class ChildCreateSchema(ChildBaseSchema):
    first_name: str
    last_name: str
    dob: str

class ChildUpdateSchema(ChildBaseSchema):
    first_name: str
    last_name: str
    dob: str
    allergies: str
    pediatrician_name: str
    pediatrician_number: str

class ChildInDBBaseSchema(ChildBaseSchema):
    id: Optional[int]

    class Config:
        from_attributes = True

class ChildSchema(ChildInDBBaseSchema):
    pass