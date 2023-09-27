from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeBase
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# PostgreSQL database configuration
DATABASE_URL = "postgresql://test:test@db/test"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = DeclarativeBase()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
