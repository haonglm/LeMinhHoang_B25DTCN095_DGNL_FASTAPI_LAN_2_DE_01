from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import BookCreate
import services

router = APIRouter(
    prefix= "/books",
    tags= ["books"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_new_book(book_in: BookCreate, db: Session = Depends(get_db)):
    new_book = services.create_new_book(book_in,db)

    if new_book == "NOT_EXISTED":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="book_category_id không tồn tại"
        )

    if new_book == "IS_DUPLICATED":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="book_code bị trùng"
        )

    return {
        "statusCode": status.HTTP_201_CREATED,
        "error": None,
        "message": "tạo sách mới thành công",
        "data": new_book
    }

@router.get("/", status_code=status.HTTP_200_OK)
def get_all_book(db: Session = Depends(get_db)):
    return {
        "statusCode": status.HTTP_200_OK,
        "error": None,
        "message": "lấy danh sách thành công",
        "data": services.get_all_book(db)
    }