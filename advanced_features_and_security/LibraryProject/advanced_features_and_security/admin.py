from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Article


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        "username",
        "email",
        "date_of_birth",
        "is_staff",
        "is_active",
    )

    # Add custom fields to the existing UserAdmin fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Add custom fields to the add_fieldsets for admin user creation
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)
