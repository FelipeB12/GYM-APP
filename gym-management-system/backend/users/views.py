# Import necessary modules from Django and Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from api.models import UserProfile

# Define a view function to handle user registration
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to register
def register_user(request):
    # Get the data sent in the POST request
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    is_admin = request.data.get('is_admin', False)  # Default to False if not provided

    # Check if the required fields are present
    if not username or not email or not password:
        # Return a 400 Bad Request response with an error message
        return Response({'error': 'Please provide username, email, and password'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        # Return a 400 Bad Request response with an error message
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new user with the provided data
    user = User.objects.create_user(username=username, email=email, password=password)

    # Create a new UserProfile instance for the user
    UserProfile.objects.create(user=user, is_admin=is_admin)

    # Return a 201 Created response with a success message
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)