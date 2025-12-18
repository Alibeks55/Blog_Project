from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied, NotAuthenticated


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or request.user.is_anonymous:
            raise NotAuthenticated(detail='Not authenticated')
        if obj.author != request.user:
            raise PermissionDenied(detail='Not the author')
        return True