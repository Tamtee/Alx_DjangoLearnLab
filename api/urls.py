# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, index

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', index, name='api-index'),
    path('', include(router.urls)),
]
