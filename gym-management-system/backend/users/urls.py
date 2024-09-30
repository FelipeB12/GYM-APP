# Import the path function from Django's url module
from django.urls import path

# Import the register_user view function from the views module
from .views import register_user

# Define a list of URL patterns
urlpatterns = [
    # Define a URL pattern for the 'register' endpoint
    # The URL pattern is '/register/'
    # The view function to be called is 'register_user'
    # The name of the URL pattern is 'register'
    path('register/', register_user, name='register'),
]