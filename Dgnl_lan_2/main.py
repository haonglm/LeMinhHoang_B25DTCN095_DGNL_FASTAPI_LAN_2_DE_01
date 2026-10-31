from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from database import base, engine
import models

from routers.book_router import router as book_router

base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(HTTPException)
def http_exception_handler(req: Request, exp: HTTPException):
    return JSONResponse(
        status_code=exp.status_code,
        content= {
            "statusCode": exp.status_code,
            "error": exp.detail,
            "message": exp.detail,
            "data": None
        }
    )

@app.get("/")
def test_connect():
    return{
        "msg": "ok"
    }

app.include_router(book_router)