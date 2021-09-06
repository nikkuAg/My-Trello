from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

"""
    Client Id : jB4kkv0oEjEUbNTCQK4gHtZ3lykaAMlkACtM5yXr
    Client secret: 5vig9qLMpr7C3G9kDNJGqARg3nHwtAyE3JnYUDtDNphfFx1mtPU0Qes1AOaoWSC4wgEDL4DlGFZTlriZ1LDytrs4yjvr033wBRAVyX9kxjUOc2jLOreUyPy9OODvWZwT

"""


class AppUser(AbstractUser):
    username = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.username)


class Project(models.Model):
    name = models.CharField(max_length=255)
    wiki = RichTextField()
    date_started = models.DateField(auto_now_add=True)
    team_members = models.ManyToManyField(AppUser, related_name='team_member')
    maintainer = models.ManyToManyField(AppUser, related_name='maintainer')

    def __str__(self) -> str:
        return self.name


class List(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(to=Project, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)
    assignee = models.ManyToManyField(AppUser, related_name='Assignees')
    list = models.ForeignKey(to=List, on_delete=CASCADE)
    due_date = models.DateField()

    def __str__(self) -> str:
        return self.title