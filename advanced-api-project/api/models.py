from django.db import models

# Author model:
# This model represents a book author.
# Each author has only a name, but can be linked to many Book entries.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model:
# This model represents a book written by an author.
# - title: name of the book
# - publication_year: year the book was published
# - author: a ForeignKey creates a one-to-many relationship with Author
#   Meaning: one author can have many books
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

