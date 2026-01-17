from fastapi import FastAPI, Depends
app = FastAPI()
from sqlalchemy.orm import session
from src.database import get_db, engine, Base
from src.routes.book_routes import router as book_routes

#create all tables 
Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "welcome to bookstore curd"

app.include_router(book_routes)