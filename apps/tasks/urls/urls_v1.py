from rest_framework import routers

from apps.tasks.views.v1.task import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="tasks")

urlpatterns = [
] + router.urls
