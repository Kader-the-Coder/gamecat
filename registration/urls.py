"""URL configuration for registration app"""

from django.urls import path
from django.contrib.auth import login
from . import views

app_name = 'registration'   # pylint: disable=invalid-name
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', login, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('authentication/', views.authentication, name='authentication'),
    path('authenticated/', views.authenticated, name='authenticated')
]
