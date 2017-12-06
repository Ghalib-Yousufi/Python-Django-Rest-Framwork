from rest_framework import permissions

class AdminsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return False
        elif view.action == 'create':
            return request.user.is_authenticated() and request.user.is_superuser
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() and request.user.is_superuser
        elif view.action in ['retrieve']:
            return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.is_authenticated() and request.user.is_superuser
        elif view.action == 'destroy':
            return request.user.is_authenticated() and request.user.is_superuser
        else:
            return False