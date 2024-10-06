from rest_framework import permissions
from .models import CustomUser


class IsAdministrator(permissions.BasePermissions):
    def has_permissions(self, request, view):
        return request.user.is_authenticated and request.user.role == CustomUser.ADMINISTRATOR
    
class CanDeleteReport(permissions.BasePermissions):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.COURIER