from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path("index/", views.index),
    path("", views.home, name="websiteApp-home"),
    path("info/", views.info, name="websiteApp-info"),
    path("courts/", views.courts, name="websiteApp-courts"),
    path("store/", views.store, name="websiteApp-store"),
    path("store_result/", views.store_result, name="websiteApp-store_result"),
    path("store/sproduct1/", views.sproduct1, name="websiteApp-sproduct1"),
    path("store/sproduct2/", views.sproduct2, name="websiteApp-sproduct2"),
    path("store/sproduct3/", views.sproduct3, name="websiteApp-sproduct3"),
    path("store/sproduct4/", views.sproduct4, name="websiteApp-sproduct4"),
    path("store/sproduct5/", views.sproduct5, name="websiteApp-sproduct5"),
]
