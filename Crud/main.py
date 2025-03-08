from db import Base, engine, get_db
from models import Item
from sqlalchemy.orm import Session

# Test database connection
try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print("Connection successful, result:", result.scalar())
except Exception as e:
    print("Error connecting to the database:", e)

# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)

# Example function to add an item (CRUD operation)
def create_item(name: str, description: str, db: Session):
    new_item = Item(name=name, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Example function to test item creation
if __name__ == "__main__":
    init_db()
    db = next(get_db())
    item = create_item(name="Sample Item", description="This is a test item", db=db)
    print(f"Created item: {item.name} with ID {item.id}")
