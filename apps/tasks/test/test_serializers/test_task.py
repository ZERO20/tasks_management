# tests/test_serializers.py
from django.test import TestCase, RequestFactory

from apps.tasks.models import Task
from apps.tasks.serializers.v1.task import TaskSerializer
from apps.users.tests.factories.user import UserFactory


class TaskSerializerTest(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.factory_request = RequestFactory()
        self.data_to_create = {
            'name': 'Task 1',
            'description': 'Task #1',
        }

    def setup_request(self):
        request = self.factory_request.get('/')
        request.user = self.user
        return request

    def test_is_valid(self):
        """Test for is_valid method"""
        request = self.setup_request()
        serializer = TaskSerializer(data=self.data_to_create, context={'request': request})
        self.assertEqual(serializer.is_valid(), True)

    def test_save(self):
        """Test for save method
        """
        request = self.setup_request()
        serializer = TaskSerializer(data=self.data_to_create, context={'request': request})
        self.assertEqual(serializer.is_valid(), True)
        serializer.save()
        self.assertEqual(Task.objects.all().count(), 1)
