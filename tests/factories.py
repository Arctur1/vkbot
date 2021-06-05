import factory
from Database.models import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    user_id = factory.Sequence(lambda n: '%s' % n)
    age = factory.Sequence(lambda n: '%s' % n)
    sex = factory.Sequence(lambda n: '%s' % n)
    city = factory.Sequence(lambda n: '%s' % n)
    relation = factory.Sequence(lambda n: '%s' % n)

    class Meta:
        model = User
