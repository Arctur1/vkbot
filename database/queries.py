from database.base import DBSession as session
from database.models import User, Matches


def get_user_db(user_id, db):
    data = db.query(User).filter(User.user_id == user_id).one_or_none()
    data = row_to_dict(data)
    return data


def row_to_dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


def get_matches(user_id):
    matches = session.query(Matches.match_id).filter(Matches.user_id == user_id).limit(1).all()
    i = 0
    for match_tuple in matches:
        matches[i] = match_tuple[0]
        i += 1
    for m_id in matches:
        session.query(Matches).filter(Matches.match_id == m_id).update({'seen': Matches.seen + 1})
        session.commit()
    return matches