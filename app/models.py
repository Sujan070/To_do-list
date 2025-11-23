from sqlalchemy import create_engine, Integer, String, Column, Date, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from enum import IntEnum as PyIntEnum

class Priority(PyIntEnum):
   low = 3
   medium = 2
   high = 1
class Status(PyIntEnum):
   pending = 1
   completed = 2
   discarded = 3

engine = create_engine('postgresql://postgres:Sujan%401@localhost:5432/todo_db')
Base = declarative_base()



class Todo(Base):
   __tablename__ = 'todos' 
   id = Column(Integer, primary_key=True)
   name = Column(String, nullable=False)
   description = Column(String)
   priority = Column(Enum(Priority), nullable=False, default=Priority.low) 
   status = Column(Enum(Status), nullable=False, default=Status.pending)
   date_cre = Column(Date, nullable=False)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


    

