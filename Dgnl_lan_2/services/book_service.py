from sqlalchemy.orm import Session, joinedload
from models import bookModel, bookCategoryModel
from schemas import BookCreate

def create_new_book(book_in: BookCreate, db: Session):
    book_category_id = db.query(bookCategoryModel).filter(bookCategoryModel.id == book_in.book_category_id).first()

    if not book_category_id:
        return "NOT_EXISTED"

    book = db.query(bookModel).filter(bookModel.book_code == book_in.book_code).first()

    if book:
        return "IS_DUPLICATED"

    new_book = bookModel(**book_in.model_dump())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book 

def get_all_book(db: Session):
    return db.query(bookModel).options(joinedload(bookModel.book_category)).all()