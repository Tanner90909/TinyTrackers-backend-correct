from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.schemas import UserInDB
from datetime import date
from typing import List

from app.db.base_class import Base

class Child(Base):
    __tablename__ = "children"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    unique_child_code: Mapped[str] = Column(String, nullable=False)
    first_name: Mapped[str] = Column(String, nullable=False)
    last_name: Mapped[str] = Column(String, nullable=False)
    dob: Mapped[str] = Column(String, nullable=False)
    allergies: Mapped[str] = Column(String)
    pediatrician_name: Mapped[str] = Column(String)
    pediatrician_number: Mapped[str] = Column(String)

    events: Mapped[List["Event"]] = relationship(back_populates="child", cascade="all, delete-orphan")
    child_users: Mapped[List["UserChildren"]] = relationship("UserChildren", back_populates="child")