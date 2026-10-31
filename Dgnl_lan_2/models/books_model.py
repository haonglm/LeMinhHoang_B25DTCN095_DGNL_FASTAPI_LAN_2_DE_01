from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import base

class bookModel(base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)

    book_code = Column(String(10), unique=True, nullable=False)

    price = Column(Float, nullable=False)

    book_category_id = Column(Integer, ForeignKey("bookCategories.id"))

    book_category = relationship("bookCategoryModel", back_populates="books")