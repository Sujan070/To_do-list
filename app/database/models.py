from sqlalchemy import Column, Integer, String, Enum, DateTime, Date, ForeignKey, Index, func
from sqlalchemy.orm import relationship
from app.database.connection import Base
from enum import IntEnum, Enum as PyEnum

class Priority(IntEnum):
    low = 3
    medium = 2
    high = 1

class TodoDB(Base):
    __tablename__ = "todos"

    todo_id = Column(Integer, primary_key=True, index=True)
    todo_name = Column(String, nullable=False)
    todo_description = Column(String)
    priority = Column(Enum(Priority), default=Priority.low)


