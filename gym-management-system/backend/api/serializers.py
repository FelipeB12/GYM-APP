from rest_framework import serializers
from .models import UserProfile, Measurement, WorkoutSession, PersonalRecord, WorkoutRoutine, Appointment

# Serializer for the UserProfile model.
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'is_admin']  # Specifies which fields to include in the serialized output.
# Serializer for the Measurement model.
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'  # Serializes all fields in the Measurement model.
# Serializer for the WorkoutSession model.
class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = '__all__'  # Serializes all fields in the WorkoutSession model.
# Serializer for the PersonalRecord model.
class PersonalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalRecord
        fields = '__all__'  # Serializes all fields in the PersonalRecord model.
# Serializer for the WorkoutRoutine model.
class WorkoutRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutRoutine
        fields = '__all__'  # Serializes all fields in the WorkoutRoutine model.
# Serializer for the Appointment model.
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'  # Serializes all fields in the Appointment model.
