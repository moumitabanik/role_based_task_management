from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    """
    Custom permission to only allow admins and managers to create tasks and projects.
    """
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.role_id == 2)
    
class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admins.
    """
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff)