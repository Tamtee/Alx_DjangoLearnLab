import os
import sys
import django

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        print(f"Books by {author_name}:")
        for book in author.books.all():
            print("-", book.title)
    except Author.DoesNotExist:
        print(f"No author named '{author_name}'")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in library '{library_name}':")
        for book in library.books.all():
            print("-", book.title)
    except Library.DoesNotExist:
        print(f"No library named '{library_name}'")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Librarian for {library_name}: {library.librarian.name}")
    except Library.DoesNotExist:
        print(f"No library named '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"Library '{library_name}' has no librarian assigned")

if __name__ == "__main__":
    books_by_author("Jane Doe")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
