from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("a", "b", "c", "timestamp")
    search_fields = ["a", "b", "c"]
