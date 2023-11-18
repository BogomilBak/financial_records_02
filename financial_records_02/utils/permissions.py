from rest_framework import permissions


class IsOwnerOfAnItemOrObject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
