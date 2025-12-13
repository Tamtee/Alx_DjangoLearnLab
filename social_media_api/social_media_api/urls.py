from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
    
    path('api/', include('posts.urls')),  # Include the posts rou
]

