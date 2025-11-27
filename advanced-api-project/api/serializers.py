from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer:
# Serializes all fields of the Book model.
# Includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation:
    # Makes sure the year is not greater than the current year.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer:
# Serializes the author’s name PLUS a list of their books.
# The books field uses a nested BookSerializer.
# 'many=True' because an author can have multiple books.
# 'read_only=True' so books are only shown, not created here.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
