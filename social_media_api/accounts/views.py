from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from .models import User




class FollowUserView(APIView):
permission_classes = [IsAuthenticated]


def post(self, request, user_id):
user_to_follow = get_object_or_404(User, id=user_id)


if user_to_follow == request.user:
return Response({'error': 'You cannot follow yourself'}, status=400)


request.user.following.add(user_to_follow)
return Response({'message': f'You are now following {user_to_follow.username}'})




class UnfollowUserView(APIView):
permission_classes = [IsAuthenticated]


def post(self, request, user_id):
user_to_unfollow = get_object_or_404(User, id=user_id)


request.user.following.remove(user_to_unfollow)
return Response({'message': f'You unfollowed {user_to_unfollow.username}'})
