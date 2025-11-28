import django
import os

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # 1. Query all books by a specific author
    author_name = "John Doe"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")


    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")


    # 3. Retrieve the librarian for a library
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")


if __name__ == "__main__":
    run_queries()
