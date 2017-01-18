from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    context = {}
    return render(request, 'mysite/index.html', context)


def signup(request):
    try:
        username = request.POST["username"]
        email = request.POST["email"]
        pwd = request.POST["psw"]
        pwd2 = request.POST["psw2"]
    except KeyError:
        return render(request, 'mysite/index.html', {'error_message': "You didn't do all the fields"})
    else:
        if pwd != pwd2:
            return render(request, 'mysite/index.html', {'error_message': 'Passwords are not the same'})
        user = User.objects.create_user(username=username, email=email, password=pwd)
        login(request, user)
        return HttpResponseRedirect("/")

