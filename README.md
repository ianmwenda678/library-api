# 📚 Library API

A simple library management API built with FastAPI, SQLModel, and PostgreSQL.

**Student Name:** [Your Name]  
**Admission Number:** C027-01-0902/2024  
**Course:** CIT 3107 - Back-End Development  
**Lab:** Lab 4 - PostgreSQL & SQLModel

---

## 🚀 Features

- ✅ Create and manage books
- ✅ Categorize books (Fiction, Non-Fiction, Science, History, etc.)
- ✅ Search books by author or title
- ✅ Update book details
- ✅ Filter books by availability
- ✅ Interactive API documentation (Swagger UI)

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Web framework for building APIs |
| **SQLModel** | ORM + Pydantic combined for database operations |
| **PostgreSQL** | Relational database |
| **Uvicorn** | ASGI server for running FastAPI |
| **Docker** | Containerization for PostgreSQL |
| **Python 3.12+** | Programming language |

---

## 📋 API Endpoints

### Root
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |

### Categories (Exercise 1)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/categories` | Create a new category |
| GET | `/categories` | List all categories |

### Books
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/books` | Create a new book |
| GET | `/books` | List all books (with optional filters) |
| GET | `/books/{book_id}` | Get a specific book by ID |
| GET | `/books/search` | Search books by author or title (Exercise 2) |
| PATCH | `/books/{book_id}` | Update a book (Exercise 3) |

---

## 🏗️ Project Structure
