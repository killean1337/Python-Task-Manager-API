# Python — Task Manager API

```md id="py_readme"
# Task Manager API (FastAPI)

A REST API built with FastAPI for managing tasks.  
This project demonstrates backend development fundamentals such as CRUD operations and database integration.

---

## Features

- Create tasks
- Read tasks
- Delete tasks
- SQLite database integration
- Automatic API documentation (Swagger UI)

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## Project Structure

app/
├── main.py
├── models.py
├── database.py
├── schemas.py

---

## How to run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
