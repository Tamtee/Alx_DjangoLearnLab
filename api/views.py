# api/views.py

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# API ViewSet for Book Model (Requires Authentication)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
"""
    A simple ViewSet for viewing and editing books.
    
    Permissions:
    - IsAuthenticated: only users with a valid token can access.
    - You can replace/add other permissions like IsAdminUser for admin-only actions.
    """
# Simple public endpoint to test API
def index(request):
    return JsonResponse({"message": "API is working successfully!"})
