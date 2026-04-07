# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a REST API for managing a collection of books using the FastAPI framework. You'll learn how to set up a FastAPI application, define data models, and implement CRUD (Create, Read, Update, Delete) operations.

## 📝 Tasks

### 🛠️	Set up FastAPI Application

#### Description
Install FastAPI and Uvicorn, then create a basic FastAPI application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Have FastAPI and Uvicorn installed
- Create a FastAPI app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Be able to run the server with `uvicorn main:app --reload`


### 🛠️	Create Book Data Model

#### Description
Define a Pydantic model for a Book with fields: id (integer), title (string), author (string), and year (integer).

#### Requirements
Completed program should:

- Import BaseModel from Pydantic
- Define a Book class inheriting from BaseModel
- Include all required fields with appropriate types


### 🛠️	Implement CRUD Endpoints

#### Description
Implement REST API endpoints for managing books: GET all books, GET single book by ID, POST to create a new book, PUT to update a book, DELETE to remove a book.

#### Requirements
Completed program should:

- Have a list or dictionary to store books in memory
- GET /books: Return all books as JSON
- GET /books/{book_id}: Return a single book by ID, return 404 if not found
- POST /books: Accept JSON data to create a new book, assign an ID, return the created book
- PUT /books/{book_id}: Update an existing book, return 404 if not found
- DELETE /books/{book_id}: Delete a book, return 404 if not found