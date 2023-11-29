from sqlalchemy import Boolean, DateTime, Time, Column, Integer, String
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    when = Column(DateTime, nullable=False)

class EventType(Base):
    __tablename__ = "eventtypes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class MedicineEvent(Base):
    __tablename__ = "medicine"

    id = Column(Integer, primary_key=True, index=True)
    dose = Column(Integer, nullable=False)
    when = Column(DateTime, nullable=False)
    medicine_type = Column(String, nullable=False)
    time_to_next_dose = Column(Time, nullable=False)
    description = Column(String)

class SymptomEvent(Base):
    __tablename__ = "symptom"

    id = Column(Integer, primary_key=True, index=True)
    symptom_type = Column(String, nullable=False)
    severity = Column(Integer, nullable=False)
    when = Column(DateTime, nullable=False)
    description = Column(String)

class OtherEvent(Base):
    __tablename__ = "other"

    id = Column(Integer, primary_key=True, index=True)
    when = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)