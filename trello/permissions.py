from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import List, Project


class AdminPermission(BasePermission):
    """
        Admin can create user, update or delete user.
        User not having admin rights can only view all users.
    """

    message = "You do not have admin rights"

    def has_permission(self, request, view):
        admin_methods = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE']
        if request.user.is_authenticated:
            if request.user.admin == True and (request.method in admin_methods):
                return True
            elif request.user.admin == False and (request.method in SAFE_METHODS):
                return True

    def has_object_permission(self, request, view, obj):
        if request.user.admin == True:
            return True


class ProjectPermission(BasePermission):
    """
        Anyone can create project
        Team member, creator, admin can update, delete project
    """

    team_methods = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE']

    message = "You are not a part of this project"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated:
            team_ids = []
            creator_ids = []
            for x in obj.team_members.all():
                team_ids.append(x.id)
            for x in obj.creator.all():
                creator_ids.append(x.id)
            if (user.id in team_ids) or (user.id in creator_ids) or (user.admin == True):
                return True


class ProjectCreatorPermission(BasePermission):
    """
        Special Permission of Creator
        Only creator can add new team members
    """

    message = "Only Creator can add team_members"

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            creator_ids = []
            for x in obj.creator.all():
                creator_ids.append(x.id)
            if request.user.id in creator_ids:
                return True


class ListCardPermission(BasePermission):

    message = "You are not a part of this project"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated:
            list = obj.list
            project = List.objects.get(name=list).project
            data = Project.objects.get(name=project)
            team_id = []
            creator_id = []
            for x in data.team_members.all():
                team_id.append(x.id)
            for x in data.creator.all():
                creator_id.append(x.id)
            if (user.id in team_id) or (user.id in creator_id) or (user.admin == True):
                return True
