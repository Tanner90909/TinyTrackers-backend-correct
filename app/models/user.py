from sqlalchemy import Boolean, Column, Integer, String, EmailString, Mapped, List, ForeignKey
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    
    events: Mapped[List["Event"]] = relationship(back_populates="author", cascade="all, delete-orphan")

class UserChildren(Base):
    __tablename__ = "userchildren"

    id = Column(Integer, primary_key=True, index=True)
    user_id: Column(Integer, ForeignKey("users.id"))
    child_id: Column(Integer, ForeignKey("children.id"))
     

    def to_schema(self):
        return UserInDB(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            is_superuser=self.is_superuser
        )