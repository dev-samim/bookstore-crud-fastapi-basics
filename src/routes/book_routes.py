from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import session
from src.database import get_db
from src.models.book_model import Book
from src.services import book_service
from src.schemas.book_schema import bookBase, bookUpdate, bookResponse

router = APIRouter(prefix="/api/book", tags=['books'])


@router.get("/", response_model=list[bookResponse])
def get_all_books(db : session = Depends(get_db)):
    books = book_service.get_all_bookes(db,Book)
    return books

@router.post("/", response_model=bookResponse, status_code=201)
def insert_book(book : bookBase, db : session = Depends(get_db)):
    new_book = book_service.add_book(database=db, book=book, BookModel=Book)
    return new_book

@router.get("/{book_id}", response_model=bookResponse)
def find_book_by_id(book_id : str,db : session = Depends(get_db)):
    book = book_service.find_book_id(database=db, BookModel=Book, book_id=book_id)
    if not book:
        raise HTTPException(404, "book not found")
    return book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id : str,db : session = Depends(get_db)):
    result = book_service.delete_book_by_id(database=db, BookModel=Book, book_id=book_id)
    if result == 0:
        raise HTTPException(404, "book not found")
    return

@router.put("/{book_id}", response_model=bookResponse)
def update_book(book_data : bookUpdate,book_id : str,db : session = Depends(get_db)):
    book =  book_service.update_book_by_id(db,book_data,book_id,Book)
    if not book:
        raise HTTPException(404, "book not found")
    return book