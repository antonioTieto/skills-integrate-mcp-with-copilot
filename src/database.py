"""
Database configuration and session management for the Activities API.
Uses SQLAlchemy ORM with SQLite for persistent data storage.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path

# Database file location
DB_FILE = os.path.join(Path(__file__).parent, "activities.db")
DATABASE_URL = f"sqlite:///{DB_FILE}"

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Required for SQLite
    echo=False  # Set to True for SQL logging during development
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()


def get_db():
    """Dependency for FastAPI to inject database sessions into routes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(bind=engine)


def get_session():
    """Get a new database session."""
    return SessionLocal()
