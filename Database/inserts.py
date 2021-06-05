from sqlalchemy import exists
from Database.base import DBSession
from models import User, Matches


def store_matches(data, user_id):
    for match in data['response']['items']:
        if match['is_closed'] is False:
            get_or_create(DBSession, Matches, user_id=user_id, match_id=match['id'], seen=0)


def insert_data(userinfo):
    if not check_user_exists(userinfo['user_id']):
        user = User(**userinfo)
        DBSession.add(user)
        DBSession.commit()


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def check_user_exists(session: DBSession, user_id: int) -> bool:
    is_exists = session.query(exists().where(User.user_id == user_id)).scalar()
    return is_exists
