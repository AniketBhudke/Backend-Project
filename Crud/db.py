from sqlalchemy import create_engine
import os

# MySQL connection URL from environment variable or hardcoded
# SSL arguments for PyMySQL (or other MySQL drivers)
ssl_args = {
    "ssl": {
        "ca": "C:\\Users\\bhudk\\Downloads\\ca-cert.pem",
        "cert": "C:\\Users\\bhudk\\Downloads\\client-cert.pem",
        "key": "C:\\Users\\bhudk\\Downloads\\client-key.pem",
    }
}

# Correct database URL (for PyMySQL driver)
DATABASE_URL = "mysql+pymysql://avnadmin:your_password@mysql-ef3c4eb-bhudkea-8b2f.aivencloud.com:25440/defaultdb"

# Create the database engine with proper SSL configuration
engine = create_engine(DATABASE_URL, connect_args=ssl_args)

# Test database connection
try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print("Connection successful, result:", result.scalar())
except Exception as e:
    print("Error connecting to the database:", e)
