from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:22121944@localhost:3306/library_db"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

base = declarative_base()

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()