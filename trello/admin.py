from django.contrib import admin
from .models import AppUser, Project, List, Card
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Project)
admin.site.register(List)
admin.site.register(Card)
