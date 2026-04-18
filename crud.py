from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books_data = [
    [
        {"id": 1, "title": "1984", "author": "George Orwell", "publish_date": "1949-06-08"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publish_date": "1960-07-11"},
        {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publish_date": "1925-04-10"},
        {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "publish_date": "1813-01-28"},
        {"id": 5, "title": "The Hobbit", "author": "J.R.R. Tolkien", "publish_date": "1937-09-21"}
    ]
]

app= FastAPI()

@app.get("/books")
def get_book_data():
    return books_data

@app.get("/books/{id}")
def get_book_id(id:int):
    for book_list in books_data:          # outer list
        for book in book_list:            # inner list
            if book["id"] == id:          # correct comparison
                return book     
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")

class Book(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str

@app.post("/books")
def create_book(book:Book):
    new_book= book.model_dump()
    books_data.append(new_book)
    return new_book

class Book_update(BaseModel):
    title:str
    author:str
    publish_date:str

@app.put("/books/{id}")
def update_book(id:int,book_detail:Book_update):
    for book_list in books_data:
        for book in book_list:
            if book["id"]==id:
                book["title"]=book_detail.title
                book["author"]=book_detail.author
                book["publish_date"]=book_detail.publish_date
                return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")
        
@app.delete("/book/{book_id}")
def del_book(book_id:int):
    for books in books_data:
        for book in books:
             if (book["id"])==book_id:
                  books.remove(book)
                  return 'book deleted'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")