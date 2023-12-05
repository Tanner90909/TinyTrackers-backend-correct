from typing import Any, List, Annotated
import json

from fastapi import APIRouter, Body, Depends, HTTPException, Form
from fastapi.encoders import jsonable_encoder
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
                   child_to_reg: schemas.ChildSchema,
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
    
    # existing_child = controllers.child.get_child_by_name_and_parent(db, parent_user_id=parent_user_id, child_first_name=child_first_name)
    # if existing_child:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="A child with this name already exists for the parent",
    #     )
    
    # child_in = schemas.ChildCreateSchema(first_name=child_first_name, parent_id= parent_user_id)
    new_child = controllers.ChildController.child.create_child(db, child_in=child_to_reg)
    # new_child = controllers.child.create(db, obj_in = child_in)

    # return {"child_id": str(new_child.id), "message": "Child registered successfully"}
    return new_child