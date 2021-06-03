import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from settings import DSN
from factories import UserFactory
from db import User


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