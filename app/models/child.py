from sqlalchemy import Boolean, Date, Column, Integer, String, Mapped, List
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class Child(Base):
    __tablename__ = "children"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    allergies = Column(String)
    pediatrician_name = Column(String)
    pediatrician_number = Column(String)

    events: Mapped[List["Event"]] = relationship(back_populates="child", cascade="all, delete-orphan")