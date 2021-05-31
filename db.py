import sqlalchemy as sq
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import exists
from settings import DSN

engine = create_engine(DSN)
Base = declarative_base()


class User(Base):
    __tablename__ = 'userdata'
    user_id = sq.Column(sq.Integer, primary_key=True)
    age = sq.Column(sq.Integer)
    sex = sq.Column(sq.Integer)
    city = sq.Column(sq.Integer)
    relation = sq.Column(sq.Integer)


class Matches(Base):
    __tablename__ = 'matches'
    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer)
    match_id = sq.Column(sq.Integer)
    seen = sq.Column(sq.Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def get_matches(user_id):
    matches = session.query(Matches.match_id).filter(Matches.user_id == user_id).limit(1).all()
    i = 0
    for v in matches:
        matches[i] = v[0]
        i += 1
    for m_id in matches:
        session.query(Matches).filter(Matches.match_id == m_id).update({'seen': Matches.seen + 1})
        session.commit()
    return matches


def store_matches(data, user_id):
    for match in data['response']['items']:
        if match['is_closed'] is False:
            get_or_create(session, Matches, user_id=user_id, match_id =match['id'], seen=0)


def row_to_dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


def get_user_db(user_id):
    data = session.query(User).filter(User.user_id == user_id).one_or_none()
    data = row_to_dict(data)
    return data


def check_user_exists(user_id):
    return bool(session.query(exists().where(User.user_id == user_id)).scalar())


def insert_data(userinfo):
    if not check_user_exists(userinfo['user_id']):
        user = User(**userinfo)
        session.add(user)
        session.commit()

