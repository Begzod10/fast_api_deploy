from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
    },
    {
        "id": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
    },
    {
        "id": 4,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
    },
    {
        "id": 5,
        "title": "1984",
        "author": "George Orwell",
    },
    {
        "id": 6,
        "title": "The Hobbit",
    }
]


class BookSchema(BaseModel):
    title: str
    author: str


@app.get("/books", tags=["books"])
def get_books():
    return books


@app.post("/books", tags=["books"])
def add_books(book: BookSchema):
    books.append({
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    })
    return {"message": "Book added successfully"}
