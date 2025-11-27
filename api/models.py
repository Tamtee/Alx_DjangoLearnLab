from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
from api.models import Book

# Including the published date
Book.objects.create(
    title="Django for Beginners",
    author="William S. Vincent",
    published="2025-11-19"
)

# Or without published date (since it's optional)
Book.objects.create(
    title="Another Book",
    author="Some Author"
)
