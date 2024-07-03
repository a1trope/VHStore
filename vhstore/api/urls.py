from django.urls import path, include
from . import views

urlpatterns = [
    path('cassettes', views.get_cassettes, name="get_cassettes"),
]
