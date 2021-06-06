import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from settings import DSN
from factories import UserFactory, MatchesFactory
from database.models import User, Matches
from database.queries import Queries
from database.inserts import Inserts

engine = create_engine(DSN)
Session = sessionmaker()


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope='function')
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)

    UserFactory._meta.sqlalchemy_session = session
    MatchesFactory._meta.sqlalchemy_session = session

    yield session
    session.close()
    transaction.rollback()


def my_func_to_delete_user(session, user_id):
    session.query(User).filter(User.user_id == user_id).delete()


def test_case(session):
    user = UserFactory.create()
    assert session.query(User).one()
    my_func_to_delete_user(session, user.user_id)
    result = session.query(User).one_or_none()
    assert result is None


def test_get_user_db(session):
    count = 6
    users = UserFactory.create_batch(count)
    chosen_one = users.pop()
    result = Queries(session).get_user_db(chosen_one.user_id)
    assert result


def test_check_user_exists(session):
    count = 6
    users = UserFactory.create_batch(count)
    chosen_one = users.pop()
    result = Inserts(session).check_user_exists(chosen_one.user_id)
    assert result


def test_check_match_exists(session):
    count = 6
    matches = MatchesFactory.create_batch(count)
    chosen_one = matches.pop()
    result = Inserts(session).check_match_exists(chosen_one.match_id, chosen_one.user_id)
    assert result


def test_insert_matches(session):
    data = {
        "response": {
            "items": [{
                "id": 1,
                "is_closed": False
                }]
            }
        }
    Inserts(session).insert_matches(data, 0)
    Inserts(session).insert_matches(data, 0)
    result = session.query(Matches).one_or_none()
    assert result


def test_insert_data(session):
    data = {'user_id': 1,
            'age': 1,
            'sex': 1,
            'city': 1,
            'relation': 1}
    Inserts(session).insert_data(data)
    query = Queries(session).get_user_db(1)

    assert query == data


def test_get_matches(session):
    data = {
        "response": {
            "items": [{
                "id": 1,
                "is_closed": False
                }]
            }
        }
    Inserts(session).insert_matches(data, 0)
    match = Queries(session).get_matches(0)
    assert match[0] == 1

