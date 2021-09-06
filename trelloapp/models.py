from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

"""
    Client Id : jB4kkv0oEjEUbNTCQK4gHtZ3lykaAMlkACtM5yXr
    Client secret: 5vig9qLMpr7C3G9kDNJGqARg3nHwtAyE3JnYUDtDNphfFx1mtPU0Qes1AOaoWSC4wgEDL4DlGFZTlriZ1LDytrs4yjvr033wBRAVyX9kxjUOc2jLOreUyPy9OODvWZwT

"""


class AppUser(models.Model):
    username = models.IntegerField()
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)


class Project(models.Model):
    name = models.CharField(max_length=255)
    wiki = models.CharField(max_length=500)
    team_members = models.ForeignKey(to=AppUser, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name


class Maintainer(models.Model):
    user = models.ForeignKey(to=AppUser, on_delete=CASCADE)
    project = models.ForeignKey(to=Project, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.project.name


class List(models.Model):
    name = models.CharField(max_length=255)

    project = models.ForeignKey(to=Project, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)
    assignee = models.ForeignKey(to=AppUser, on_delete=CASCADE)
    list = models.ForeignKey(to=List, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title
