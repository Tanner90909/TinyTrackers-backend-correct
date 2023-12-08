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

@router.post("/registerchild", response_model=schemas.ChildSchema)
def register_child(*,
            db: Session = Depends(deps.get_db),
            child_first_name: Annotated[str, Form()],
            child_last_name: Annotated[str, Form()], 
            child_dob: Annotated[str, Form()], 
            child_allergies: Annotated[str, Form()],
            child_pediatrician_name: Annotated[str, Form()], 
            child_pediatrician_phone_number: Annotated[str, Form()],
            current_user: models.User = Depends(deps.get_current_active_user),
            ) -> Any:
    """
    Create new child profile
    """

    # generating unique_child_code
    child_unique_code_to_register = controllers.child.generate_unique_child_id()
    # creating object to call the create function on
    child_to_register = schemas.ChildCreateSchema(
        unique_child_code=child_unique_code_to_register, 
        first_name=child_first_name, 
        last_name=child_last_name, 
        dob=child_dob, 
        allergies=child_allergies, 
        pediatrician_name=child_pediatrician_name, 
        pediatrician_number=child_pediatrician_phone_number)
    # call the create function
    new_child = controllers.child.create(db, obj_in = child_to_register)

    # map the parent child relationship
    user_child_data = {"user_id": current_user.id, "child_id": new_child.id}
    controllers.user_children.create_user_child_relationship(db, user_child_data)
    return {
        "id": str(new_child.id),
        "unique_child_code": new_child.unique_child_code,
        "first_name": new_child.first_name,
        "last_name": new_child.last_name,
        "dob": new_child.dob,
        "allergies": new_child.allergies,
        "pediatrician_name": new_child.pediatrician_name,
        "pediatrician_number": new_child.pediatrician_number,
    }

@router.post("/registerchildwithcode", response_model=schemas.ChildSchema)
def register_child_with_code(*,
    db: Session = Depends(deps.get_db),
    unique_child_code: Annotated[str, Form()],
    current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Register already existing child to new parent profile
    """

    # call function to find the child with that unique_child_code
    child_to_register = controllers.child.get_child_by_unique_code(db, unique_child_code)
    # if incorrect code entered or code not found in db throw error
    if not child_to_register:
        raise HTTPException(status_code=404, detail="Child not found")
    # map the parent child relationship
    user_child_data = {"user_id": current_user.id, "child_id": child_to_register.id}
    controllers.user_children.create_user_child_relationship(db, user_child_data)
    return {
        "id": str(child_to_register.id),
        "unique_child_code": child_to_register.unique_child_code,
        "first_name": child_to_register.first_name,
        "last_name": child_to_register.last_name,
        "dob": child_to_register.dob,
        "allergies": child_to_register.allergies,
        "pediatrician_name": child_to_register.pediatrician_name,
        "pediatrician_number": child_to_register.pediatrician_number,
    }


@router.get("/getchildren", response_model=List[schemas.ChildSchema])
def get_children_for_user(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Get all children for an authenticated user
    """

    # get the ids of the children we want to get
    current_user_id = current_user.id
    # children_to_get_ids = controllers.user_children.get_children_from_pivot(db, current_user_id)
    children_data = controllers.user_children.get_children_data(db, current_user_id=current_user_id)
    print(children_data)
    
    return children_data




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

