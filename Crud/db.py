from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# MySQL connection URL from environment variable or hardcoded
DATABASE_URL = os.getenv("DATABASE_URL", "mysql://avnadmin:your_password@mysql-ef3c4eb-bhudkea-8b2f.aivencloud.com:25440/defaultdb")

# Correct SSL arguments for MySQLdb
ssl_args = {
    "ssl": {
        "ca": "C:\\Users\\bhudk\\Downloads\\ca-cert.pem",  # Path to your CA certificate
        "cert": "C:\\Users\\bhudk\\Downloads\\client-cert.pem",  # Path to your client certificate
        "key": "C:\\Users\\bhudk\\Downloads\\client-key.pem",  # Path to your client key
    }
}

# Create the database engine with proper SSL configuration
engine = create_engine(DATABASE_URL, connect_args=ssl_args)

# Session for interacting with the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative model
Base = declarative_base()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
