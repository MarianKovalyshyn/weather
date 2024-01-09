from django.urls import path
from . import views

urlpatterns = [
    path("city/", views.City.as_view()),
    path("temperature/", views.Temperature.as_view()),
    path("condition/", views.Condition.as_view()),
]