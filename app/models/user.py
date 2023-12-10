from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.schemas import UserInDB
from typing import List

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = Column(String, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = Column(String, nullable=False)
    is_active: Mapped[bool] = Column(Boolean(), default=True)
    is_superuser: Mapped[bool] = Column(Boolean(), default=False)
    
    events: Mapped[List["Event"]] = relationship(back_populates="author", cascade="all, delete-orphan")
    user_children: Mapped[List["UserChildren"]] = relationship("UserChildren", back_populates="user")

class UserChildren(Base):
    __tablename__ = "userchildren"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    child_id: Mapped[int] = mapped_column(ForeignKey("children.id"))

    user: Mapped["User"] = relationship("User", back_populates="user_children")
    child: Mapped["Child"] = relationship("Child", back_populates="child_users")
     

    def to_schema(self):
        return UserInDB(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            is_superuser=self.is_superuser
        )