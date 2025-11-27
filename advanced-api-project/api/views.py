from rest_framework import generics, filters
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# List all books with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__id', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# Create a book (Admin only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        """
        Custom behavior during creation:
        - Enforces that only admin can create
        - Can add additional logic here (e.g., logging, notifications)
        """
        # Example: custom validation or preprocessing
        if serializer.validated_data['publication_year'] < 1900:
            raise serializers.ValidationError("Publication year cannot be before 1900")
        
        serializer.save()


# Update a book (Admin only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        """
        Custom behavior during update:
        - Validates data
        - Can modify certain fields automatically before saving
        """
        # Example: automatically capitalize the book title
        title = serializer.validated_data.get('title', None)
        if title:
            serializer.validated_data['title'] = title.title()
        serializer.save()


# Delete a book (Admin only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
