import asyncio
from users.models import User
from users.serializers import UserSerializer
from django.http.response import JsonResponse
from rest_framework import status

class UserService:
    def users_list():
        print("users_list 1")
        users = User.objects.all()
        print("users_list 2")
        users_serializer = UserSerializer(users, many=True)
        print("users_list 3")
        return JsonResponse(users_serializer.data, safe=False)
    
    def create_user(user_data):
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete_users(request):
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)