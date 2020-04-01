from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or view.kwargs['user_id'] == request.user.pk
