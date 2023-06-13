from django.urls import path

from . import views

app_name = "algo_navig"
urlpatterns = [
    path("", views.index),
    path("page/<int:pk>", views.page, name="page"),
]
