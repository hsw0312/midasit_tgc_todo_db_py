from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from app import crud, database, models, schema
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    database.create_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todos/")
async def get_todos(db: Session = Depends(get_db)):
    todos = crud.get_todos(db)
    return todos

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo

@app.post("/todos/")
async def create_todo(todo: schema.TodoCreate, db: Session = Depends(get_db)):
    crud.create_todo(db, todo)

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, updated_todo: schema.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    crud.update_todo(db, db_todo, updated_todo)

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    crud.delete_todo(db, db_todo)
    return {"message": "todo deleted successfully"}