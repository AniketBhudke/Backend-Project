from sqlalchemy import Column, Integer, String
from db import Base

# Item model (equivalent to the items table)
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255))
