from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import DSN

Base = declarative_base()
engine = create_engine(DSN)
Session = sessionmaker(bind=engine)
DBSession = Session()


class Database:
    def __init__(self, session: DBSession):
        self.session = session




