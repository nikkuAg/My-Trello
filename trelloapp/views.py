from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import AppUser, Project, List, Card, Maintainer
from .serializers import AppUserSerializer, ProjectSerializer, ListSerializer, CardSerializer, MaintainerSerializer
import requests
import json
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class MaintainerViewSet(viewsets.ModelViewSet):
    queryset = Maintainer.objects.all()
    serializer_class = MaintainerSerializer


def login(request):
    """
        authorization url: https://channeli.in/oauth/authorise?client_id=jB4kkv0oEjEUbNTCQK4gHtZ3lykaAMlkACtM5yXr&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Ftrello%2Fafter%5Flogin%2F&state=Login%7Fsuccess%7Fusing%7Foauth

    """
    code = request.GET.get('code')
    url = 'https://channeli.in/open_auth/token/'
    param = {
        'client_id': 'jB4kkv0oEjEUbNTCQK4gHtZ3lykaAMlkACtM5yXr',
        'client_secret': '5vig9qLMpr7C3G9kDNJGqARg3nHwtAyE3JnYUDtDNphfFx1mtPU0Qes1AOaoWSC4wgEDL4DlGFZTlriZ1LDytrs4yjvr033wBRAVyX9kxjUOc2jLOreUyPy9OODvWZwT',
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://localhost:8000/trello/after_login/',
        'code': code,
    }
    req = requests.post(url, data=param)
    data = req.json()
    token = data['access_token']
    type = data['token_type']
    url = 'https://channeli.in/open_auth/get_user_data/'
    req = requests.get(url, headers={"Authorization": f"{type} {token}"})
    data = req.json()
    return HttpResponse(data["username"] + " " + data['person']["fullName"])


"""
    {"userId":13296,"username":"20312012","person":{"fullName":"Divyansh Agarwal","roles":[{"role":"Student","activeStatus":"ActiveStatus.IS_ACTIVE"},{"role":"Maintainer","activeStatus":"ActiveStatus.IS_ACTIVE"}]},"student":{"enrolmentNumber":"20312012"}}
"""
