from rest_framework.permissions import SAFE_METHODS, BasePermission


class isSuperUserOrOwner(BasePermission):
    def has_object_permission(self, request, _, obj):
        if obj.user == request.user or request.user.is_superuser == True:
            return True
        return False
