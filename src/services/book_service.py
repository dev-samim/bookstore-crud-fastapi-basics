def get_all_bookes(database, Book):
        return database.query(Book).all() 

def add_book(database,book,BookModel):
        new_book = BookModel(name=book.name, author=book.author, price=book.price, in_stock=book.in_stock)
        database.add(new_book)
        database.commit()
        database.refresh(new_book)
        return new_book

def find_book_id(database, book_id , BookModel):
        book = database.query(BookModel).filter(BookModel.id==book_id).first()
        return book

def delete_book_by_id(database, book_id , BookModel):
        book = database.query(BookModel).filter(BookModel.id==book_id).first()
        if not book:
            return 0
        database.delete(book)
        database.commit()
        return 1

def update_book_by_id(database,book_data,book_id,BookModel):
        print(book_id)
        book = database.query(BookModel).filter(BookModel.id==book_id).first()
        if not book:
                return
        data = book_data.dict(exclude_unset=True)
        
        for key,value in data.items():
                setattr(book,key,value)
        
        database.commit()
        database.refresh(book)
        return book
       