from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class HistoricalUser(Base):

    __tablename__ = "historical_users"

    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True)
    role = Column(String(50))

class HistoricalEvent(Base):

    __tablename__ = "historical_events"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    event_year = Column(Integer)
    created_by = Column(Integer, ForeignKey("historical_users.id"))

class EventDependency(Base):

    __tablename__ = "event_dependencies"

    id = Column(Integer, primary_key=True)
    source_event_id = Column(Integer)
    dependent_event_id = Column(Integer)

class HistoricalVersion(Base):

    __tablename__ = "historical_versions"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    version_number = Column(Integer)
    change_summary = Column(Text)
