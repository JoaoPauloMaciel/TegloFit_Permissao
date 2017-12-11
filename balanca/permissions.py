from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissão personalizada para permitir apenas aos proprietários de um objeto para editá-lo.
    """
    def has_object_permission(self, request, view, obj):
        # As permissões de leitura são permitidas para qualquer solicitação,
        # então vamos sempre permitir pedidos GET, HEAD ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True
        #As permissões de gravação só são permitidas ao proprietário do trecho
        return obj.owner == request.user