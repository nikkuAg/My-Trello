from django.http.response import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import AppUser, Project, List, Card
from .serializers import UserSerializer, ProjectSerializer, ListSerializer, CardSerializer
import requests
from .data import urls, keys
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


def oAuth(request):
    """
        Redirects to Channeli OAuth Authorization page
    """

    return redirect(urls['authorization_url'])


def loginOauth(request):
    """
        Login/SignUp using Channeli OAuth
    """

    code = request.GET.get('code')
    url = urls['auth']
    param = {
        'client_id': keys['client_id'],
        'client_secret': keys['client_secret'],
        'grant_type': 'authorization_code',
        'redirect_uri': urls['redirect1'],
        'code': code,
    }
    req = requests.post(url, data=param)
    data = req.json()
    token = data['access_token']
    type = data['token_type']
    url = urls['get_data']
    req = requests.get(url, headers={"Authorization": f"{type} {token}"})
    data = req.json()
    username = data["username"]
    name = data["person"]["fullName"]
    role = False
    try:
        AppUser.objects.get(username=username)
    except AppUser.DoesNotExist:
        for x in data["person"]["roles"]:
            roleIterateor = x
            if roleIterateor["role"] == "Maintainer":
                role = True
                AppUser.objects.create(
                    password=token, username=username, name=name, admin=role)
        if role == "":
            return HttpResponse("You are not eligible for this app")
    AppUser.objects.filter(username=username).update(password=token)
    user = AppUser.objects.get(username=username)
    if user is not None:
        login(request, user)
        return redirect("http://localhost:8000/trello/")
    else:
        user.delete()
        return HttpResponse("Failed Login")
