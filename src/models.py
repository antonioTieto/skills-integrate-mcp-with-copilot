"""
SQLAlchemy ORM models for the Activities API.
Defines the data structure for activities and participants.
"""

from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# Association table for the many-to-many relationship between activities and participants
activity_participants = Table(
    'activity_participants',
    Base.metadata,
    Column('activity_id', Integer, ForeignKey('activity.id', ondelete='CASCADE'), primary_key=True),
    Column('participant_email', String, primary_key=True)
)


class Activity(Base):
    """
    Represents an extracurricular activity or club.
    """
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    max_participants = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to participants
    participants = relationship(
        "Participant",
        secondary=activity_participants,
        back_populates="activities",
        cascade="all, delete"
    )

    def to_dict(self):
        """Convert activity to dictionary format."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "schedule": self.schedule,
            "max_participants": self.max_participants,
            "participants": [p.email for p in self.participants],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class Participant(Base):
    """
    Represents a student participant in activities.
    """
    __tablename__ = "participant"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to activities
    activities = relationship(
        "Activity",
        secondary=activity_participants,
        back_populates="participants"
    )

    def to_dict(self):
        """Convert participant to dictionary format."""
        return {
            "id": self.id,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }
