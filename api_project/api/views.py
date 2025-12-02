from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Simple list view (existing)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()       # Get all Book objects
    serializer_class = BookSerializer   # Use the serializer we created

# Full CRUD viewset
class BookViewSet(viewsets.ModelViewSet):
    """
    Handles all CRUD operations for Book.
    """
    queryset = Book.objects.all()       # Get all Book objects
    serializer_class = BookSerializer   # Use the serializer we created
