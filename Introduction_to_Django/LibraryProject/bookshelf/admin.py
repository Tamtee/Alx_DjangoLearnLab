from django.contrib import admin
from .models import Book

# Define a basic custom admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show columns in admin
    list_filter = ('author', 'publication_year')           # add simple filters
    search_fields = ('title', 'author')                    # enable search

# Register Book with the custom admin class
admin.site.register(Book, BookAdmin)
