from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship
from database import base

class bookCategoryModel(base):
    __tablename__ = "bookCategories"

    id = Column(Integer, primary_key=True)

    name = Column(String(50), unique=True, nullable=False)

    books = relationship("bookModel", back_populates="book_category")