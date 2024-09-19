from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import pymysql
import os

load_dotenv()
db_user = os.getenv('MARIADB_ID')
db_password = os.getenv('MARIADB_PASSWORD')
db_name = os.getenv('DB_NAME')
DB_URL=f'mysql+pymysql://' + db_user + ":" + db_password + "@db:3306/" + db_name

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()