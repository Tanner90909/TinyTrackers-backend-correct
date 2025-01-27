from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.controllers.BaseController import BaseController
from app.models.user import User, UserChildren
from app.schemas.user import UserCreate, UserUpdate, UserChildrenCreateSchema, UserChildrenUpdateSchema
from app.models.child import Child


class UserController(BaseController[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            username=obj_in.username,
            is_superuser=obj_in.is_superuser,
            
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = UserController(User)

class UserChildrenController(BaseController[UserChildren, UserChildrenCreateSchema, UserChildrenUpdateSchema]):
    def create_user_child_relationship(self, db: Session, user_child_data: dict):
        db_user_child = UserChildren(**user_child_data)
        db.add(db_user_child)
        db.commit()
        db.refresh(db_user_child)
        return db_user_child
    
    def get_children_from_pivot(self, db: Session, current_user_id: int):
        return db.query(UserChildren).filter(UserChildren.user_id == current_user_id).all()
    
    def get_children_data(self, db: Session, current_user_id: int):
        return (db.query(Child)
                .join(Child.child_users)
                .filter(UserChildren.user_id == current_user_id)
                .all())
    
user_children = UserChildrenController(UserChildren)