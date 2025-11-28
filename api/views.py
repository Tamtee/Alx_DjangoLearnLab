# api/views.py

from rest_framework import generics, permissions, serializers, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
import datetime

# -----------------------------
# List all books
# -----------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can see the list
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Allow filtering by title, author, or publication year
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Enable search by title or author name
    search_fields = ['title', 'author__name']
    
    # Enable ordering by title or publication_year
    ordering_fields = ['title', 'publication_year']
    
    # Optional: filter dynamically by query params
    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author__name__icontains=author)
        return queryset

# -----------------------------
# Retrieve a single book
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

# -----------------------------
# Create a new book
# -----------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

    # Step 3 customization: prevent future publication year
    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

# -----------------------------
# Update an existing book
# -----------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

    def perform_update(self, serializer):
        if serializer.validated_data.get('publication_year', None):
            if serializer.validated_data['publication_year'] > datetime.datetime.now().year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

# -----------------------------
# Delete a book
# -----------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users