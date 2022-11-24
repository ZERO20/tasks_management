# tests/test_serializers.py
from faker import Faker

from django.test import TestCase

from apps.tasks.models import User
from apps.users.serializers.v1.user import UserSerializer

faker = Faker()


class UserSerializerTest(TestCase):

    def setUp(self):
        self.data_to_create = {
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'email': faker.email(),
            'username': faker.user_name(),
            'password': faker.password()
        }

    def test_is_valid(self):
        """Test for is_valid method"""
        serializer = UserSerializer(data=self.data_to_create)
        self.assertEqual(serializer.is_valid(), True)

    def test_save(self):
        """Test for save method
        """
        serializer = UserSerializer(data=self.data_to_create)
        self.assertEqual(serializer.is_valid(), True)
        serializer.save()
        self.assertEqual(User.objects.all().count(), 1)
