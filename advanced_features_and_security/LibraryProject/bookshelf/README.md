# Permissions & Groups Setup

This project uses custom permissions for the Book model:

- can_view
- can_create
- can_edit
- can_delete

Groups:
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions

Views use @permission_required to enforce access control.
