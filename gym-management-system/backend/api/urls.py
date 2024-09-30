from django.urls import path, include  # Import Django functions to define URL routes and include other URL configurations.
from rest_framework.routers import DefaultRouter  # Import Django REST Framework's DefaultRouter, which automatically generates URL routes for viewsets.
from .views import (  # Import all the viewsets from the views.py file.
    UserProfileViewSet, MeasurementViewSet, WorkoutSessionViewSet, 
    PersonalRecordViewSet, WorkoutRoutineViewSet, AppointmentViewSet
)

router = DefaultRouter()  # Create an instance of the DefaultRouter, which automatically generates RESTful URL patterns.

router.register(r'userprofiles', UserProfileViewSet)  # Registers the UserProfileViewSet at the /userprofiles/ endpoint.
router.register(r'measurements', MeasurementViewSet)  # Registers the MeasurementViewSet at the /measurements/ endpoint.
router.register(r'workoutsessions', WorkoutSessionViewSet)  # Registers the WorkoutSessionViewSet at the /workoutsessions/ endpoint.
router.register(r'personalrecords', PersonalRecordViewSet)  # Registers the PersonalRecordViewSet at the /personalrecords/ endpoint.
router.register(r'workoutroutines', WorkoutRoutineViewSet)  # Registers the WorkoutRoutineViewSet at the /workoutroutines/ endpoint.
router.register(r'appointments', AppointmentViewSet)  # Registers the AppointmentViewSet at the /appointments/ endpoint.

urlpatterns = [
    path('', include(router.urls)),  # Include all the URLs that the router has automatically generated into the base URL pattern.
]
