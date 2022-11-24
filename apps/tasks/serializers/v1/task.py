from rest_framework import serializers

from apps.tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault())
    )

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'created_at', 'user')


class UpdateStatusTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('status',)
        extra_kwargs = {
            'status': {'required': True, 'allow_blank': False},
        }
