# -*- coding: utf-8 -*-

from django.urls import path, include
import apps.tasks.urls.urls_v1 as tasks_api_v1
import apps.users.urls.urls_v1 as users_api_v1


urlpatterns = [
    path('tasks/api/v1/',
        include((tasks_api_v1, 'apps.tasks'), namespace='tasks_api_v1'), name='tasks_v1'),
    path('users/api/v1/',
        include((users_api_v1, 'apps.users'), namespace='users_api_v1'), name='users_v1'),
]
