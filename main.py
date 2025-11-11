from fastapi import FastAPI , HTTPException
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field 

api = FastAPI()
class Priority(IntEnum):
   low = 3
   medium = 2
   high = 1

class Todobase(BaseModel):
   todo_name: str = Field(..., min_length=3, max_length=512, description='name of todo')
   todo_desc: str = Field(..., description= 'Description of todo')
   priority: Priority = Field(default=Priority.low, description='priority of todo')

class Todocreate(Todobase):
   pass

class Todo(Todobase):
   todo_id: int = Field(...,description='unique identifier of the todo')

class Todoupdate(BaseModel):
   todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='name of todo')
   todo_desc: Optional[str] = Field(None, description='Description of todo')
   priority: Optional[Priority] = Field(default=None, description='priority of todo')


all_todos = [
 Todo(todo_id=1, todo_name="read", todo_desc="reading the book", priority= Priority.medium),
 Todo(todo_id=2, todo_name="play", todo_desc="play the guitar",  priority= Priority.low),
 Todo(todo_id=3, todo_name="project", todo_desc="finish the college project", priority= Priority.high),
 Todo(todo_id=5, todo_name="documentation", todo_desc="documentation of upcoming project", priority= Priority.medium),
 Todo(todo_id=6, todo_name="journal", todo_desc="keep the journal of day", priority= Priority.medium)
]



@api.get('/todos/{todo_id}', response_model= Todo)
def get_todo(todo_id:int):
    for todo in all_todos:
        if todo.todo_id== todo_id:
            return todo
        
    raise HTTPException(status_code=404, detail='todo not found')
    
@api.get('/todos', response_model= List[Todo])
def get_todos(first_n: int = None):
    if first_n:
     return all_todos[:first_n]
    else :
     return all_todos
    
@api.post('/todos', response_model= Todo)
def cerate_todo(todo: Todocreate):
   new_todo_id = max(todo.todo_id for todo in all_todos)+ 1

   new_todo = Todo(todo_id = new_todo_id,
                   todo_name= todo.todo_name,
                   todo_desc= todo.todo_desc,
                   priority= todo.priority
                   )
   all_todos.append(new_todo)

   return new_todo

@api.put('/todos/{todo_id}', response_model= Todo)
def update_todo(todo_id: int, updated_todo: Todoupdate):
   for todo in all_todos:
      if todo.todo_id == todo_id:
         if updated_todo.todo_name is not None:
          todo.todo_name = updated_todo.todo_name
         if updated_todo.todo_desc is not None:
          todo.todo_desc = updated_todo.todo_desc
         if updated_todo.priority is not None:
          todo.priority = updated_todo.priority
         return todo
      
   raise HTTPException(status_code=404, detail='todo not found')

@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    
    raise HTTPException(status_code=404, detail='Todo not found')

       
      
   
 

