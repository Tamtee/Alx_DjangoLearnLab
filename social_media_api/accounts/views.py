from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()


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
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class FollowUserView(APIView):

    def post(self, request, user_id):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        user_to_follow = get_object_or_404(User, id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        if request.user.following.filter(id=user_id).exists():
            return Response({"message": "You already follow this user"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_201_CREATED)


class UnfollowUserView(APIView):

    def post(self, request, user_id):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        user_to_unfollow = get_object_or_404(User, id=user_id)
        if not request.user.following.filter(id=user_id).exists():
            return Response({"error": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
