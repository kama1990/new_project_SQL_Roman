from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:Kamila123@localhost:3306/DVDstore"
)

Session = sessionmaker(bind=engine)
session = Session()
