import factory
import factory.fuzzy
from faker import Faker

from django.contrib.auth import get_user_model

from apps.tasks.models import Task


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """User Factory"""
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', Faker().password())

    class Meta:
        model = User


class TaskFactory(factory.django.DjangoModelFactory):
    """Task Factory"""
    name = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')
    status = factory.fuzzy.FuzzyChoice(Task.STATUS_CHOICES, getter=lambda c: c[0])
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Task
