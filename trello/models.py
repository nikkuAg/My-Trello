from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser, User
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField

# imports for Token Authentications
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class AppUser(AbstractUser):
    username = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.username)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    wiki = RichTextField()
    date_started = models.DateField(auto_now_add=True)
    team_members = models.ManyToManyField(
        AppUser, related_name='team_member')
    creator = models.ManyToManyField(AppUser, related_name='maintainer')

    def __str__(self) -> str:
        return self.name


class List(models.Model):
    name = models.CharField(max_length=255, unique=True)
    project = models.ForeignKey(to=Project, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = RichTextField()
    complete = models.BooleanField(default=False)
    assignee = models.ManyToManyField(AppUser, related_name='Assignees')
    list = models.ForeignKey(to=List, on_delete=CASCADE)
    due_date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(to=AppUser, on_delete=CASCADE)
    message = models.CharField(max_length=255)
    card = models.ForeignKey(to=Card, on_delete=CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
