from django.test import TestCase

from apps.tasks.models import Task
from apps.tasks.test.factories.task import TaskFactory

class TaskModelsTestCase(TestCase):

    def setUp(self):
        self.task_1 = TaskFactory(name='Task 1')

    def test_get_task(self):
        # read
        task = Task.objects.get(name="Task 1")
        self.assertEqual(task.id, self.task_1.id)


    def test_update_task(self):
        # update
        self.task_1.name = 'Task 1 - test'
        self.task_1.save()
        self.assertEqual(self.task_1.name, 'Task 1 - test')
