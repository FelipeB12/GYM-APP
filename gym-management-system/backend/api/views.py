from rest_framework import viewsets  # Import Django REST Framework's viewsets, which provide CRUD operations.
from rest_framework.permissions import IsAuthenticated  # Import the permission class that restricts access to authenticated users only.
from .models import UserProfile, Measurement, WorkoutSession, PersonalRecord, WorkoutRoutine, Appointment  # Import models from the current app (api).
from .serializers import (  # Import serializers, which handle the conversion of model instances to JSON and vice versa.
    UserProfileSerializer, MeasurementSerializer, WorkoutSessionSerializer, 
    PersonalRecordSerializer, WorkoutRoutineSerializer, AppointmentSerializer
)
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()  # Queryset retrieves all UserProfile instances from the database.
    serializer_class = UserProfileSerializer  # Specifies the serializer to be used for this viewset.
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users only.
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()  # Queryset retrieves all Measurement instances.
    serializer_class = MeasurementSerializer  # Uses the MeasurementSerializer for data serialization and validation.
    permission_classes = [IsAuthenticated]  # Access restricted to authenticated users.
class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()  # Fetches all WorkoutSession records.
    serializer_class = WorkoutSessionSerializer  # Uses the WorkoutSessionSerializer for serialization.
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users.
class PersonalRecordViewSet(viewsets.ModelViewSet):
    queryset = PersonalRecord.objects.all()  # Retrieves all PersonalRecord entries.
    serializer_class = PersonalRecordSerializer  # Uses the PersonalRecordSerializer for data handling.
    permission_classes = [IsAuthenticated]  # Access limited to authenticated users.
class WorkoutRoutineViewSet(viewsets.ModelViewSet):
    queryset = WorkoutRoutine.objects.all()  # Fetches all WorkoutRoutine records.
    serializer_class = WorkoutRoutineSerializer  # Uses the WorkoutRoutineSerializer for serialization.
    permission_classes = [IsAuthenticated]  # Access restricted to logged-in users.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()  # Retrieves all Appointment entries.
    serializer_class = AppointmentSerializer  # Uses the AppointmentSerializer for handling data serialization.
    permission_classes = [IsAuthenticated]  # Limits access to authenticated users.
