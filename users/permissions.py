from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

class isSuperUser(permissions.IsAdminUser):
    def has_permission(self, request, _):
        if request.user.is_superuser:
            return True

        return False


class isSuperUserOrOwner(BasePermission):
    def has_object_permission(self, request, _, obj):
        if bool(request.user and request.user.is_superuser):
            return True
        return request.user == obj