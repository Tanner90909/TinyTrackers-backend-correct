from typing import Optional

from pydantic import BaseModel

class ChildBaseSchema(BaseModel):
    unique_child_code: str
    first_name: str
    last_name: str
    dob: str
    allergies: Optional[str]
    pediatrician_name: Optional[str]
    pediatrician_number: Optional[str]

class ChildCreateSchema(ChildBaseSchema):
    unique_child_code: str

class ChildUpdateSchema(ChildBaseSchema):
    unique_child_code: str
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