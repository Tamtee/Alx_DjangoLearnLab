from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # link the accounts app
    path('', include('blog.urls')),  # your blog app
]
