from django.urls import path, include
from . import views

urlpatterns = [
    path('cassettes', views.cassettes_list),
    path('cassettes/<int:id>', views.cassettes_detail),
]
