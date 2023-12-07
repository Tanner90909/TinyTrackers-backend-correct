from typing import Any, List, Annotated
import json

from fastapi import APIRouter, Body, Depends, HTTPException, Form
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Date
from sqlalchemy.orm import Session

from app import controllers, models, schemas
from app.api import deps
from app.core.config import settings

from datetime import timedelta
from app.core import security

router = APIRouter()

# @router.post("/registerchild", response_model=schemas.ChildSchema)
# def register_child(*, 
#                    db: Session = Depends(deps.get_db), 
#                    parent_token: str = Form(), 
#                    child_first_name: str = Form(),
#                    child_last_name: str = Form(), 
#                    child_dob: str = Form(), 
#                    child_allergies: str = Form(),
#                    child_pediatrician_name: str = Form(), 
#                    child_pediatrician_phone_number: str = Form(),
#                    ) -> Any:
#     """
#     Create new child profile
#     """

#     parent_user_id = security.verify_token(parent_token)
#     if not parent_user_id:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid or expired parent authentication token",
#         )

# # instead of checking against parent_user_id and child_first_name, check against the token given to the child when created
#     existing_child = controllers.child.get_child_by_name_and_parent(db, parent_user_id=parent_user_id, child_first_name=child_first_name)
#     if existing_child:
#         raise HTTPException(
#             status_code=400,
#             detail="A child with this name already exists for the parent",
#         )

#     child_in = schemas.ChildCreateSchema(first_name=child_first_name, last_name=child_last_name, dob=child_dob, allergies=child_allergies, pediatrician_name=child_pediatrician_name, pediatrician_number=child_pediatrician_phone_number)
#     new_child = controllers.child.create(db, obj_in = child_in)

#     user_child_data = {"user_id": parent_user_id, "child_id": new_child.id}
#     controllers.user_children.create_user_child_relationship(db, user_child_data)

#     return {"child_id": str(new_child.id), "message": "Child registered successfully"}

# @router.post("/registernewchild", response_model=schemas.ChildSchema)
# def register_child_2(
#     *, 
#     db: Session = Depends(deps.get_db),
#     parent_token: str = Form(), 
#     child_in: schemas.ChildBaseSchema,
#     ) -> Any:
#     """
#     Create new child profile
#     """

#     parent_user_id = security.verify_token(parent_token)
#     if not parent_user_id:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid or expired parent authentication token",
#         )

#     existing_child = controllers.child.get_child_by_name_and_parent(db, parent_user_id=parent_user_id, child_first_name=child_first_name)
#     if existing_child:
#         raise HTTPException(
#             status_code=400,
#             detail="A child with this name already exists for the parent",
#         )

#     new_child = controllers.child.create(db, obj_in = child_in)

#     user_child_data = {"child_id": new_child.id}
#     controllers.user_children.create_user_child_relationship(db, user_child_data)

#     return {"child_id": str(new_child.id), "message": "Child registered successfully"}

@router.post("/registerchild", response_model=schemas.ChildSchema)
def register_child(*,
                   db: Session = Depends(deps.get_db),
                #    parent_token: Annotated[str, Form()],
                   child_first_name: Annotated[str, Form()],
                   child_last_name: Annotated[str, Form()], 
                   child_dob: Annotated[str, Form()], 
                   child_allergies: Annotated[str, Form()],
                   child_pediatrician_name: Annotated[str, Form()], 
                   child_pediatrician_phone_number: Annotated[str, Form()],
                   ) -> Any:
    """
    Create new child profile
    """

    # parent_user_id = security.verify_token(parent_token)
    # if not parent_user_id:
    #     raise HTTPException(
    #         status_code=401,
    #         detail="Invalid or expired parent authentication token",
    #     )

    child_to_register = schemas.ChildCreateSchema(first_name=child_first_name, last_name=child_last_name, dob=child_dob, allergies=child_allergies, pediatrician_name=child_pediatrician_name, pediatrician_number=child_pediatrician_phone_number)
    new_child = controllers.child.create(db, obj_in = child_to_register)
    # user_child_data = {"user_id": parent_user_id, "child_id": new_child.id}
    # controllers.user_children.create_user_child_relationship(db, user_child_data)
    return {
        "id": str(new_child.id),
        "first_name": new_child.first_name,
        "last_name": new_child.last_name,
        "dob": new_child.dob,
        "allergies": new_child.allergies,
        "pediatrician_name": new_child.pediatrician_name,
        "pediatrician_number": new_child.pediatrician_number,
    }