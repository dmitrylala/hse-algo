from django.contrib import admin

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "navig", "navig_position", "content", "timestamp"]
    list_display_links = ["title"]
    list_editable = ["navig", "navig_position", "content"]
    search_fields = ["content"]
    list_filter = ["title", "navig"]
    list_per_page = 15
