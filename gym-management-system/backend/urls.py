from django.contrib import admin
from django.urls import path, include

# URL routing configuration for the Django project.
# This maps URLs to specific apps and views within the project.
urlpatterns = [
    # Route for the Django admin interface. Accessed via '/admin/'.
    path('admin/', admin.site.urls),
    
    # Route for the API app. Includes URLs from the 'api.urls' file.
    path('api/', include('api.urls')),
    
    # Route for the 'users' app. Includes URLs from the 'users.urls' file.
    path('users/', include('users.urls')),
]
