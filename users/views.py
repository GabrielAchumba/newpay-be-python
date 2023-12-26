from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
 
from users.models import User
from users.serializers import UserSerializer
from users.user_service import UserService
from rest_framework.decorators import api_view


@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False)

@api_view(['POST'])
def RegisterUser(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def LoginUser(request):
    user_data = JSONParser().parse(request)
    token, _ = Token.objects.get_or_create(user=user_data)
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        # return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"token": token.key}) 
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_users(request):
    userService = UserService()
    return userService.delete_users()

@api_view(['GET'])
def GetUser(request, pk):
    try: 
        user = User.objects.get(pk=pk) 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data)
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 

@api_view(['PUT'])
def update_user(request, pk):
    try: 
        user = User.objects.get(pk=pk) 
        user_data = JSONParser().parse(request) 
        user_serializer = UserSerializer(user, data=user_data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 


@api_view(['DELETE'])
def delete_user(request, pk):
    try: 
        user = User.objects.get(pk=pk) 
        user.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
