from sqlalchemy import Column, Integer, String, DateTime, JSON, create_engine, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

class Base(DeclarativeBase):
    pass

class LogEntry(Base):
    __tablename__ = 'log_entry'

    id: Mapped[int] = mapped_column(primary_key=True)
    endpoint: Mapped[str] = mapped_column(String())
    timestamp: Mapped[str] = mapped_column(DateTime(), default=datetime.datetime.utcnow())
    payload: Mapped[dict] = mapped_column(JSON())

class NamedEntityMapping(Base):
    __tablename__ = 'named_entity_mapping'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chatbot_id: Mapped[str] = mapped_column(String())
    name: Mapped[str] = mapped_column(String())
    pseudonym: Mapped[str] = mapped_column(String())

    __table_args__ = (UniqueConstraint('chatbot_id', 'name', name='uq_person_mapping'),)

def db_init(engine):
    Base.metadata.create_all(engine)