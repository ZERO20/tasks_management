from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from apps.users.tests.factories.user import UserFactory


faker = Faker()

class TaskViewSetTest(APITestCase):
    """Task APITestCase"""

    def test_create(self):
        """Test for POST"""
        data_to_create = {
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'email': faker.email(),
            'username': faker.user_name(),
            'password': faker.password()
        }
        create_url = reverse('api_v1:users_api_v1:users-list')
        response = self.client.post(create_url, data=data_to_create)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_get_token(self):
        """Gets a token for an user"""
        password = faker.password()
        user = UserFactory(password=password)
        data = {
            'username': user.username,
            'password': password
        }
        token_url = reverse('api_v1:users_api_v1:token_obtain_pair')
        response = self.client.post(token_url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('access', response.data.keys())
        self.assertIn('refresh', response.data.keys())
