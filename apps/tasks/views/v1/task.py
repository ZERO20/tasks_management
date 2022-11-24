from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.tasks.models import Task
from apps.tasks.serializers.v1.task import TaskSerializer, UpdateStatusTaskSerializer
from apps.tasks.pagination import TaskPagination


class TaskViewSet(ModelViewSet):
    """Task CRUD ModelViewSet"""
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = TaskPagination

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        name = self.request.query_params.get('name')
        description = self.request.query_params.get('description')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)
        return queryset

    @extend_schema(
        parameters=[OpenApiParameter(
            name='name',
            type={'type': 'string'},
            location=OpenApiParameter.QUERY,
            required=False,
            style='form',
            explode=False,
        ),
        OpenApiParameter(
            name='description',
            type={'type': 'string'},
            location=OpenApiParameter.QUERY,
            required=False,
            style='form',
            explode=False,
        )],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['put'], url_path='update/status', url_name='update-status')
    def update_status(self, request, pk=None):
        """Update the status of a task to complete/imcomplete"""
        task = self.get_object()
        serializer = UpdateStatusTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task.status = serializer.validated_data.get('status')
        task.save()
        return Response(serializer.data)
