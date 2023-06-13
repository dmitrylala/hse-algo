from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("a", "b", "c", "timestamp")
    search_fields = ["a", "b", "c"]


admin.site.register(Task, TaskAdmin)
