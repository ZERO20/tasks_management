from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from django.urls import reverse

from apps.tasks.models import Task
from apps.tasks.test.factories.task import TaskFactory
from apps.users.tests.factories.user import UserFactory


class TaskViewSetTest(APITestCase):
    """Task APITestCase"""
    def setUp(self) -> None:
        self.user_password = 'TaskDemo$'
        self.user = UserFactory()
        self.token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def get_token(self):
        """Gets a token for an user"""
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def get_detail_url(self, task_id):
        """Get the detail url"""
        return reverse('api_v1:tasks_api_v1:tasks-detail', kwargs={'pk': task_id})

    def test_create(self):
        """Test for POST"""
        data = {
            'name': 'Task 1',
            'description': 'This is the task #1'
        }
        create_url = reverse('api_v1:tasks_api_v1:tasks-list')
        response = self.client.post(create_url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_list(self):
        """Test for list GET"""
        tasks = TaskFactory.create_batch(5, user=self.user)
        list_url = reverse('api_v1:tasks_api_v1:tasks-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['results'], [])
        self.assertEqual(
            set(task['id'] for task in response.data['results']),
            set(task.id for task in tasks)
        )

    def test_search_list(self):
        """Test for search by name and description in list GET"""
        description = 'Task testing'
        TaskFactory.create_batch(5, user=self.user)
        TaskFactory(user=self.user, description=description)
        list_url = reverse('api_v1:tasks_api_v1:tasks-list')
        response = self.client.get(list_url, {'description': 'testing'})
        response_results = response.data['results']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response_results, [])
        self.assertNotEqual(set(task for task in response_results if description.lower() in task['name']), [])

    def test_retrieve(self):
        """Test for detail GET"""
        task = TaskFactory(user=self.user)
        response = self.client.get(self.get_detail_url(task_id=task.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], task.name)

    def test_update(self):
        """Test for PUT"""
        task = TaskFactory(user=self.user)
        data = {
            'name': 'Task Demo',
            'description': 'Task Demo',
            'status': 'incomplete',
        }
        response = self.client.put(self.get_detail_url(task_id=task.id), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # The object has really been updated
        task.refresh_from_db()
        for field_name in data.keys():
            self.assertEqual(getattr(task, field_name), data[field_name])

    def test_patch(self):
        """Test for PATCH"""
        task = TaskFactory(user=self.user)
        data = {
            'name': 'Task Demo'
        }
        response = self.client.patch(self.get_detail_url(task_id=task.id), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # The object has really been updated
        task.refresh_from_db()
        self.assertEqual(task.name, data['name'])

    def test_destroy(self):
        """Test for DELETE"""
        task = TaskFactory(user=self.user)
        task_id = task.pk
        response = self.client.delete(self.get_detail_url(task_id=task_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.filter(pk=task_id).exists(), False)


    def test_update_status(self):
        """Test for status update PUT"""
        task = TaskFactory(user=self.user, status='incomplete')
        self.assertEquals(task.status, 'incomplete')
        data = {
            'status': 'complete'
        }
        update_status_url = reverse('api_v1:tasks_api_v1:tasks-update-status', kwargs={'pk': task.id})
        response = self.client.put(update_status_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # The object has really been updated
        task.refresh_from_db()
        self.assertEqual(task.status, data['status'])

    def test_only_operations_task_owner(self):
        """Test for only owner operations"""
        user_2 = UserFactory()
        task = TaskFactory(user=user_2)
        # retrieve
        retrieve_response = self.client.get(self.get_detail_url(task_id=task.id))
        self.assertEqual(retrieve_response.status_code, status.HTTP_404_NOT_FOUND)
        # list
        list_url = reverse('api_v1:tasks_api_v1:tasks-list')
        list_response = self.client.get(list_url)
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(list_response.data['results'], [])
        # update
        data = {
            'name': 'Task Demo update',
            'description': 'Task Demo update',
            'status': 'complete',
        }
        update_response = self.client.put(self.get_detail_url(task_id=task.id), data=data)
        self.assertEqual(update_response.status_code, status.HTTP_404_NOT_FOUND)
        # patch
        data = {
            'name': 'Task Demo'
        }
        patch_response = self.client.patch(self.get_detail_url(task_id=task.id), data=data)
        self.assertEqual(patch_response.status_code, status.HTTP_404_NOT_FOUND)
        # update status
        data = {
            'status': 'complete'
        }
        update_status_url = reverse('api_v1:tasks_api_v1:tasks-update-status', kwargs={'pk': task.id})
        update_status_response = self.client.put(update_status_url, data=data)
        self.assertEqual(update_status_response.status_code, status.HTTP_404_NOT_FOUND)
        # destroy
        destroy_response = self.client.delete(self.get_detail_url(task_id=task.id))
        self.assertEqual(destroy_response.status_code, status.HTTP_404_NOT_FOUND)
