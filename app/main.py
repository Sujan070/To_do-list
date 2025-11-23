from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from fastapi.middleware.cors import CORSMiddleware
api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api.get('/todos/{todo_id}', response_model=schemas.Todo)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

@api.get('/todos', response_model=List[schemas.Todo])
def get_todos(first_n: int = None, db: Session = Depends(get_db)):
    query = db.query(models.Todo)
    if first_n:
        return query.limit(first_n).all()
    return query.all()

@api.post('/todos', response_model=schemas.Todo, status_code=201)
def create_todo(todo: schemas.Todocreate, db: Session = Depends(get_db)):
    
    new_todo = models.Todo(
        name=todo.name,
        description=todo.description,
        priority=todo.priority,
        date_cre=todo.date_cre,
        status = todo.status
      
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@api.put('/todos/{todo_id}', response_model=schemas.Todo)
def update_todo(todo_id: int, updated_todo: schemas.Todoupdate, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    if updated_todo.name is not None:
        todo.name = updated_todo.name
    if updated_todo.description is not None:
        todo.description = updated_todo.description
    if updated_todo.priority is not None:
        todo.priority = updated_todo.priority
    if updated_todo.date_cre is not None:
        todo.date_cre = updated_todo.date_cre
    if updated_todo.status is not None:
        todo.status = updated_todo.status
    db.commit()
    db.refresh(todo)
    return todo

@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully", "id": todo_id}


