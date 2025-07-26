from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrSuperUser(BasePermission):
    """
    Custom permission to only allow owners of an object or superuser to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS — allow all users to read
        if request.method in SAFE_METHODS:
            return True

        # Only the creator or a superuser can update/delete
        return obj.created_by == request.user or request.user.is_superuser
