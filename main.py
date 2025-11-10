from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id':1, 'todo_name':"study", 'todo_des':"read a lot."},
    {'todo_id':2, 'todo_name':"play", 'todo_des':"play basketball."},
    {'todo_id':3, 'todo_name':"code", 'todo_des':"finish cooding."},
    {'todo_id':4, 'todo_name':"sing", 'todo_des':"play guitar and sing."},
    {'todo_id':5, 'todo_name':"gym", 'todo_des':"workout biceps."}
]

@api.get('/')
def index():
    return {"messege":"Hello World"}

@api.get('/todos/{todo_id}')
def get_todo(todo_id:int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return{'results': todo}
    
@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
     return all_todos[:first_n]
    else :
     return all_todos
 

