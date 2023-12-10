from sqlalchemy import Boolean, DateTime, Time, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.schemas import UserInDB
from typing import List

from app.db.base_class import Base

class EventType(Base):
    __tablename__ = "eventtypes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    
    event: Mapped["Event"] = relationship(back_populates="event_type")

class MedicineEvent(Base):
    __tablename__ = "medicines"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    dose: Mapped[int] = Column(Integer, nullable=False)
    medicine_type: Mapped[str] = Column(String, nullable=False)
    time_to_next_dose: Mapped[Time] = Column(Time, nullable=False)
    description: Mapped[str] = Column(String)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))

    event: Mapped["Event"] = relationship(back_populates="medicine")



class SymptomEvent(Base):
    __tablename__ = "symptoms"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    symptom_type: Mapped[str] = Column(String, nullable=False)
    severity: Mapped[int] = Column(Integer, nullable=False)
    description: Mapped[str] = Column(String)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))

    event: Mapped["Event"] = relationship(back_populates="symptom")

class OtherEvent(Base):
    __tablename__ = "others"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str] = Column(String, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))

    event: Mapped["Event"] = relationship(back_populates="other")

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    when: Mapped[DateTime] = Column(DateTime, nullable=False)
    child_id: Mapped[int] = mapped_column(ForeignKey("children.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_type_id: Mapped[int] = mapped_column(ForeignKey("eventtypes.id"))

    author: Mapped["User"] = relationship(back_populates="events")
    child: Mapped["Child"] = relationship(back_populates="events")
    event_type: Mapped["EventType"] = relationship(back_populates="event")
    medicine: Mapped["MedicineEvent"] = relationship(back_populates="event")
    symptom: Mapped["SymptomEvent"] = relationship(back_populates="event")
    other: Mapped["OtherEvent"] = relationship(back_populates="event")