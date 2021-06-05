from sqlalchemy import (
    Column,
    Integer
)
from base import Base


class User(Base):
    __tablename__ = 'userdata'
    user_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    sex = Column(Integer)
    city = Column(Integer)
    relation = Column(Integer)


class Matches(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    match_id = Column(Integer)
    seen = Column(Integer)