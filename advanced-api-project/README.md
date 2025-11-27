# Advanced API Project - Book Views Documentation

## View Endpoints

### 1. List Books
- URL: /books/
- Method: GET
- Permission: Authenticated users
- Description: Retrieves a list of all books.

### 2. Book Detail
- URL: /books/<id>/
- Method: GET
- Permission: Authenticated users
- Description: Retrieves details of a single book by ID.

### 3. Create Book
- URL: /books/
- Method: POST
- Permission: Admin users
- Description: Create a new book with title, publication year, and author.

### 4. Update Book
- URL: /books/<id>/
- Method: PUT
- Permission: Admin users
- Description: Update an existing book by ID.

### 5. Delete Book
- URL: /books/<id>/
- Method: DELETE
- Permission: Admin users
- Description: Delete a book by ID.

## Custom Settings / Hooks
- `perform_create` and `perform_update` methods are included for future custom behavior during create or update operations.
- Permissions are enforced using DRF’s `IsAuthenticated` and `IsAdminUser` classes to protect endpoints.
