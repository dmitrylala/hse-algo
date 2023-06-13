from django.urls import path

from . import views

app_name = "algo"
urlpatterns = [
    # ex: /algo/
    path("", views.index, name="index"),
    # ex: /algo/task/
    path("task/", views.task, name="task"),
    # ex: /algo/task_result/5/
    path("task_result/<int:pk>/", views.ResultView.as_view(), name="task_result"),
    # ex: /algo/empty_history/
    path("empty_history/", views.empty_history, name="empty_history"),
    # ex: /algo/history/, /algo/history/task__a
    path("history/", views.ResultListView.as_view(), name="history"),
]
