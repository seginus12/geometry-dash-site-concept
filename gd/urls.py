from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="mainpage"),
    path("profile", views.profile, name="profile"),
    path("top_hardest", views.top_hardest, name="top_hardest"),
    path("rankings", views.rankings, name="rankings")
]