from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import DSN

Base = declarative_base()
engine = create_engine(DSN)
Session = sessionmaker(bind=engine)
DBSession = Session()
Base.metadata.create_all(engine)


