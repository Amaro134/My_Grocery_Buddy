from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Include lucky.urls at root path (handles login, signup, etc)
    path('', include('lucky.urls')),
]