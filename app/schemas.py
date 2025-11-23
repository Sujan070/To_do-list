from typing import  Optional
from enum import IntEnum
from pydantic import BaseModel, Field 
from datetime import date
from models import Priority, Status


class Todobase(BaseModel):
   name: str = Field(..., min_length=3, max_length=512, description='name of todo')
   description: str = Field(..., description= 'Description of todo')
   date_cre: date = Field(..., description='date of todo')
   status: Status = Field(default=Status.pending, description='status of todo')
   priority: Priority = Field(default=Priority.low, description='priority of todo')


class Todocreate(Todobase):
   pass

class Todo(Todobase):
   id: int = Field(..., description='unique identifier of the todo')

   class Config:
       orm_mode = True
      

class Todoupdate(BaseModel):
   name: Optional[str] = Field(None, min_length=3, max_length=512, description='name of todo')
   description: Optional[str] = Field(None, description='Description of todo')
   priority: Optional[Priority] = Field(default=None, description='priority of todo')
   status: Optional[Status] = Field(default=None)
   date_cre: Optional[date] = None

