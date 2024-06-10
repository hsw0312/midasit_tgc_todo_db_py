from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy

DATABASE_URL = sqlalchemy.engine.URL.create(
	drivername="mysql+pymysql",
    username="midas",
    password="mid@sit",
    host="127.0.0.1",
    port="5306",
    database="todo",
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")