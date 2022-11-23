import factory
import factory.fuzzy

from apps.tasks.models import Task
from apps.tasks.test.factories.user import UserFactory


class TaskFactory(factory.django.DjangoModelFactory):
    """Task Factory"""
    name = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')
    status = factory.fuzzy.FuzzyChoice(Task.STATUS_CHOICES, getter=lambda c: c[0])
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Task
