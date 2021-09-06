from django.contrib import admin
from .models import AppUser, Project, List, Card, Maintainer
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Project)
admin.site.register(Maintainer)
admin.site.register(List)
admin.site.register(Card)
