from sqlalchemy import exists, and_
from database.base import DBSession
from database.models import User, Matches


def insert_matches(session: DBSession, data, user_id: int):
    for match in data['response']['items']:
        if match['is_closed'] is False:
            if not check_match_exists(session, match['id'], user_id):
                session.add(Matches(user_id=user_id, match_id=match['id'], seen=0))
                session.commit()


def insert_data(userinfo: dict):
    if not check_user_exists(userinfo['user_id']):
        user = User(**userinfo)
        DBSession.add(user)
        DBSession.commit()


def check_user_exists(session: DBSession, user_id: int) -> bool:
    is_exists = session.query(exists().where(User.user_id == user_id)).scalar()
    return is_exists


def check_match_exists(session: DBSession, match_id: int, user_id: int) -> bool:
    is_exists = session.query(exists().where(and_(Matches.match_id == match_id, Matches.user_id == user_id))).scalar()
    return is_exists
