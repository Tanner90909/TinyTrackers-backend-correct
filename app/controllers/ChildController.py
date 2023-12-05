from sqlalchemy.orm import Session
from app.models import Child, UserChildren
from app.schemas.child import ChildCreateSchema, ChildUpdateSchema, ChildSchema
from app.controllers.BaseController import BaseController

class ChildController(BaseController[Child, ChildCreateSchema, ChildUpdateSchema]):
    def create_child(self, db: Session, child_in: ChildCreateSchema):
        db_child = Child(
            unique_child_id_code=child_in.unique_child_id_code,
            first_name=child_in.first_name,
            last_name=child_in.last_name,
            dob= child_in.dob,
            allergies=child_in.allergies,
            pediatrician_name=child_in.pediatrician_name,
            pediatrician_number=child_in.pediatrician_number
        )
        db.add(db_child)
        db.commit()
        db.refresh(db_child)
        return db_child

    def get_child_by_name_and_parent(self, db: Session, parent_user_id: str, child_first_name: str):
        return db.query(Child).join(UserChildren, UserChildren.child_id == Child.id).filter(UserChildren.user_id == parent_user_id, Child.first_name == child_first_name).first()

child = ChildController(Child)
