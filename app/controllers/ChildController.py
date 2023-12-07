from sqlalchemy.orm import Session
from app.models import Child, UserChildren
from app.schemas.child import ChildCreateSchema, ChildUpdateSchema, ChildSchema
from app.controllers.BaseController import BaseController
import uuid

class ChildController(BaseController[Child, ChildCreateSchema, ChildUpdateSchema]):
    def generate_unique_child_id(self) -> str:
        child_uuid = str(uuid.uuid4())
        return child_uuid

    def create_child(self, db: Session, child_in: ChildCreateSchema):
        db_child = Child(**child_in.dict())
        db.add(db_child)
        db.commit()
        db.refresh(db_child)
        return db_child

    def get_child_by_name_and_parent(self, db: Session, parent_user_id: str, child_first_name: str):
        return db.query(Child).join(UserChildren, UserChildren.child_id == Child.id).filter(UserChildren.user_id == parent_user_id, Child.first_name == child_first_name).first()

child = ChildController(Child)
