from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = ['id', 'title', 'publication_year', 'author']
>>>>>>> ae49109d48f364862425e57e89e2410d32902227
