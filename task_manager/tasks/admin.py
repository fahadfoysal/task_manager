from typing import Any
from django.contrib import admin
from .models import Task, TaskImage

class TaskImageAdmin(admin.ModelAdmin):
    list_display = ['task', 'image']

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['priority', 'is_completed']
    list_display = ['title', 'priority', 'is_completed', 'due_date']

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('priority')

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskImage, TaskImageAdmin)
