from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    book_code: str = Field(..., min_length=4, max_length=10)

    price: float = Field(..., gt=0)

    book_category_id: int = Field(...)

class BookResponse(BaseModel):
    book_code: str = Field(..., min_length=4, max_length=10)

    category: str 

    price: float = Field(..., gt=0)

    status: str