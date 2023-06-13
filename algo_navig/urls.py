from django.urls import path

from . import views

app_name = "algo_navig"
urlpatterns = [
    path("", views.first_page),
    path("page/<int:pk>", views.page, name="page"),
]
