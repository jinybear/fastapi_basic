'''
data, api model layer 이다.
database connector 들을 생성 및 관리하는 역할도 담당.
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from config import oper_settings

DATABASE_URL = oper_settings.setting['database']['SQL_URL']

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class NoSQL_engine:
    def get_db(self):
        DATABASE_URL = oper_settings.setting['database']['MONGO_URL']
        self.engine = MongoClient(DATABASE_URL)

