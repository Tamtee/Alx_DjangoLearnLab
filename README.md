# Advanced API Project - Book Views Documentation

## View Endpoints

### 1. List Books
- URL: /api/books/
- Method: GET
- Permission: AllowAny (public access)
- Description: Retrieves a list of all books.
- Features:
  1. **Filtering:** Filter by `title`, `author`, and `publication_year`.  
     Example: `/api/books/?title=Django&author=Vincent`
  2. **Searching:** Search for partial matches in `title` and `author`.  
     Example: `/api/books/?search=Django`
  3. **Ordering:** Order results by any field (`title`, `publication_year`).  
     Example: `/api/books/?ordering=title` or `/api/books/?ordering=-publication_year`

### 2. Book Detail
- URL: /api/books/<id>/
- Method: GET
- Permission: AllowAny
- Description: Retrieves details of a single book by ID.

### 3. Create Book
- URL: /api/books/create/
- Method: POST
- Permission: Admin users
- Description: Create a new book with title, author, and publication year.
- Notes: Uses `perform_create` hook for validation and saving


### 4. Update Book
- URL: /api/books/<id>/update/
- Method: PUT
- Permission: Admin users
- Description: Update an existing book by ID.

### 5. Delete Book
- URL: /api/books/<id>/delete/
- Method: DELETE
- Permission: Admin users
- Description: Delete a book by ID.

## Custom Settings / Hooks
- `perform_create` and `perform_update` methods are included for potential custom logic during create or update operations.
- Permissions are enforced using DRF’s `AllowAny` and `IsAdminUser` classes to protect endpoints.
- Filtering, searching, and ordering are enabled via DRF backends:
  - `DjangoFilterBackend` for filtering
  - `SearchFilter` for search
  - `OrderingFilter` for ordering
