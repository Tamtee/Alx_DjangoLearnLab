# Admin Setup

1. Registered the Book model in `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
