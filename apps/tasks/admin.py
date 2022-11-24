from django.contrib import admin

from apps.tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Task Admin Class"""
    list_display = ('name', 'user', 'status', 'created_at',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name', 'description', 'user__username', 'user__email',)
    fields = ('name', 'description', 'status', 'user', 'created_at', 'updated_at',)
    ordering = ('-created_at',)
