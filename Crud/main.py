from fastapi import FastAPI
from db import engine, get_db
from models import Item
from sqlalchemy.orm import Session

# Initialize FastAPI app
app = FastAPI()

# Simple route for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}

# Route to test database connection
@app.get("/test-db")
async def test_db():
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            return {"status": "Connection successful", "result": result.scalar()}
    except Exception as e:
        return {"status": "Error connecting to the database", "error": str(e)}
