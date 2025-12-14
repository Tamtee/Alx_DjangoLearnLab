from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts endpoints
    path('api/accounts/', include('accounts.urls')),

    # Posts endpoints (feed, posts, etc.)
    path('api/posts/', include('posts.urls')),
]
