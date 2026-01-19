from fastapi import FastAPI, Depends, Request
app = FastAPI()
from fastapi.responses import JSONResponse
from sqlalchemy.orm import session
from src.database import get_db, engine, Base
from src.routes.book_routes import router as book_routes
from src.routes.user_routes import router as user_routes

#create all tables 
Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "welcome to bookstore curd"

app.include_router(book_routes)
app.include_router(user_routes)

@app.exception_handler(Exception)
def not_found_handler(request: Request, exc : Exception):
    return JSONResponse(status_code=500, content={"message": "exception occurred", "details": str(exc)})