"""All views of home app"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from .models import ClicksUser


# Create your views here.


def home(request):
    """Display the home page"""
    user = request.user
    clicks_objects = ClicksUser.objects   #pylint: disable=no-member
    user_clicks = clicks_objects.values('clicker', 'clicks')
    # Variable information of logged in user
    username = user.username
    while True:
        try:
            # Attempt to get user click data
            user_clicks = clicks_objects.filter(clicker=user.id) #pylint: disable=no-member
            user_clicks = user_clicks.values('clicks')[0]['clicks']
            break
        # Raised if no record for user exists
        except IndexError:
            try:
                # Attempt to create record for user
                new_clicker = ClicksUser(clicker=user)
                new_clicker.save()
            # Raised if no user is logged in
            except ValueError:
                user_clicks = 0
                break
    
    # Variable containing summary information
    clicks_objects = clicks_objects.all()
    total_clicks = sum(x.clicks for x in clicks_objects)
    last_clicker = max(clicks_objects, key=lambda x: x.last_click).clicker
    average_clicks = round(sum(x.clicks for x in clicks_objects)/len(clicks_objects),1)
    most_clicker = max(clicks_objects, key=lambda x: x.clicks).clicker
    return render(request, 'home/home.html',
                  {'username': username,
                   'user_clicks': user_clicks,
                   'total_clicks': total_clicks,
                   'average_clicks': average_clicks,
                   'last_clicker': last_clicker,
                   'most_clicker': most_clicker})


def clicked(request):
    """PLACEHOLDER"""
    user = request.user
    print(user)
    clicks_objects = ClicksUser.objects.filter(clicker=user.id)   #pylint: disable=no-member
    clicks_objects.update(clicks=F('clicks') + 1)
    clicks_objects.update(last_click=datetime.now())
    return HttpResponseRedirect(reverse('home:home'))
