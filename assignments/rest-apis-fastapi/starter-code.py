from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Task 2: Define Book model here
class Book(BaseModel):
    pass  # Replace with actual fields

# In-memory storage for books
books = []

# Task 1: Root endpoint
@app.get("/")
def read_root():
    pass  # Return welcome message

# Task 3: CRUD endpoints
@app.get("/books")
def get_books():
    pass  # Return all books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass  # Return single book or 404

@app.post("/books")
def create_book(book: Book):
    pass  # Create new book and return it

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    pass  # Update book or 404

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    pass  # Delete book or 404