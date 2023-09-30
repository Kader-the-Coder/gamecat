"""URL configuration for registration app"""

from django.urls import path
from . import views

app_name = 'home'   # pylint: disable=invalid-name
urlpatterns = [
    path('', views.home, name='home'),
    path('clicked', views.clicked, name='clicked'),
]