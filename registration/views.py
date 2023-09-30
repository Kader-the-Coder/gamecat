"""All views of authentication app"""

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm     #pylint: disable=import-error


# Create your views here.


def register(request):
    """Register a new user"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('registration:authenticated')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def authentication(request):
    """Checks if user exists in database"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('home:home')
            )

    login(request,user)
    return HttpResponseRedirect(reverse('registration:authenticated'))


def authenticated(request):     # pylint: disable=unused-argument
    """Go to home page if authenticated"""
    return HttpResponseRedirect(reverse('home:home'))


def logout_user(request):
    """Log user out"""
    logout(request)
    return render(request, 'registration/logout.html')