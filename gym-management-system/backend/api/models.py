from django.db import models
from django.contrib.auth.models import User

# Model representing additional information about the user.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links this profile to a User object. Deletes profile if user is deleted.
    is_admin = models.BooleanField(default=False)  # Boolean flag indicating if the user has admin privileges.
# Model to track user body measurements over time.
class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the measurement to a User.
    date = models.DateField()  # Date when the measurement was taken.
    weight = models.FloatField()  # User's weight.
    body_fat = models.FloatField()  # Body fat percentage.
    arm_size = models.FloatField()  # Size of the user's arm (inches or cm).
    chest_size = models.FloatField()  # Chest size measurement.
    waist_size = models.FloatField()  # Waist size measurement.
    hip_size = models.FloatField()  # Hip size measurement.
    thigh_size = models.FloatField()  # Thigh size measurement.
    calf_size = models.FloatField()  # Calf size measurement.
# Model to track individual workout sessions.
class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the workout session to a User.
    date = models.DateField()  # Date of the workout session.
    duration = models.DurationField()  # Duration of the workout (hours/minutes).
# Model to track personal records (PR) in different exercises.
class PersonalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the record to a User.
    exercise = models.CharField(max_length=100)  # The name of the exercise (e.g., squat, bench press).
    weight = models.FloatField()  # The personal record weight lifted by the user.
    date = models.DateField()  # Date when the record was achieved.
# Model to store user workout routines.
class WorkoutRoutine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the routine to a User.
    name = models.CharField(max_length=100)  # Name of the workout routine (e.g., "Leg Day Routine").
    description = models.TextField()  # Detailed description of the workout routine (exercises, sets, etc.).
# Model to track appointments for users.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the appointment to a User.
    date = models.DateTimeField()  # Date and time of the appointment.
    purpose = models.CharField(max_length=100)  # Purpose or reason for the appointment (e.g., "body measurement").
