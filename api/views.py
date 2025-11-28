from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# ----------------------------
# List all books
# Public endpoint: anyone can view
# Supports filtering by title and author
# ----------------------------
# List all books (public access)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']  # exact match filters

# Retrieve a single book (public access)
# Public endpoint: anyone can view
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book (authenticated users only)
# Restricted to authenticated users
# perform_create ensures data validation and saving
# ----------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
# ----------------------------
# Update an existing book
# Restricted to authenticated users
# perform_update ensures data validation and saving
# ----------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
