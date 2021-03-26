from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Пользовательское разрешение на уровне объекта.
    Проверяет, что действие совершает автор, если не он,
    то разрешены только безопасные запросы.
    '''
    def has_object_permission(self, request, view, obj):
        # Разрешены GET, HEAD, OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Для остальных запросы может делать только автор объекта.
        return obj.author == request.user
