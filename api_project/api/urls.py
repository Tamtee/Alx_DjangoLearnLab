from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# Combine both the router URLs and the original list view
urlpatterns = [
    path('', include(router.urls)),           # Full CRUD API via ViewSet
    path('books-list/', BookList.as_view(), name='book-list'),  # Original ListAPIView
]
