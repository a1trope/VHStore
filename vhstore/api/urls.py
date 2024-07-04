from django.urls import path, include
from . import views, auth_views

urlpatterns = [
    path('auth/login', auth_views.login),
    path('auth/logout', auth_views.logout),
    path('auth/signup', auth_views.signup),

    path('cassettes/', views.cassettes_list),
    path('cassettes/<int:id>', views.cassettes_detail),
]
