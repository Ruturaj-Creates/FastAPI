from fastapi import FastAPI,HTTPException,Depends
from database import get_db,engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
import model

app=FastAPI()

class bookstore(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str

@app.post("/book")
def new_book(book_detail:bookstore,db:Session=Depends(get_db)):
    new_book=model.Book(id=book_detail.id,title=book_detail.title,author=book_detail.author,publish_date=book_detail.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/book")
def all_books(db:Session=Depends(get_db)):
    all_books= db.query(model.Book).all()
    return all_books
