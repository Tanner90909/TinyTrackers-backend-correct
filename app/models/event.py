from sqlalchemy import Boolean, DateTime, Time, Column, Integer, String, ForeignKey, Mapped, List
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    when = Column(DateTime, nullable=False)
    child_id = Column(Integer, ForeignKey("children.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    event_type_id = Column(Integer, ForeignKey("eventtypes.id"))

    author: Mapped["User"] = relationship(back_populates="events")
    child: Mapped["Child"] = relationship(back_populates="events")

class EventType(Base):
    __tablename__ = "eventtypes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class MedicineEvent(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    dose = Column(Integer, nullable=False)
    when = Column(DateTime, nullable=False)
    medicine_type = Column(String, nullable=False)
    time_to_next_dose = Column(Time, nullable=False)
    description = Column(String)



class SymptomEvent(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    symptom_type = Column(String, nullable=False)
    severity = Column(Integer, nullable=False)
    when = Column(DateTime, nullable=False)
    description = Column(String)

class OtherEvent(Base):
    __tablename__ = "others"

    id = Column(Integer, primary_key=True, index=True)
    when = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)