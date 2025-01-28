from rest_framework.permissions import BasePermission

# admin bolgan foydalanuvchiga ruxsat beradi
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
    

    
