from django.contrib import admin

from .models import (
    Page,
    Result,
    Task,
)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.get_fields()]
    search_fields = ["a", "b", "c"]
    list_filter = ["timestamp"]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Result._meta.get_fields()]
    search_fields = ["is_increasing", "is_decreasing"]
    list_filter = ["is_increasing", "is_decreasing", "timestamp"]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Page._meta.get_fields()]
    list_display_links = ["title"]
    list_editable = ["navig", "navig_position", "context_type", "content"]
    search_fields = ["content"]
    list_filter = ["title", "navig", "context_type"]
