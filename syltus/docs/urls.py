from django.urls import path
from . import views

app_name = "docs"

urlpatterns = [
    path("", views.index, name="index"),
    path("show/<int:id>/", views.show, name="show"),
    path("list/", views.queue, name="list"),
    path("list/page-<int:page>/", views.queue, name="list-arg")
]