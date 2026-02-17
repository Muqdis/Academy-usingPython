# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     USER_TYPE = (
#         ('student', 'Student'),
#         ('teacher', 'Teacher'),
#     )

#     SERVICE_TYPE = (
#         ('tuition', 'Tuition'),
#         ('technical', 'Technical'),
#         ('professional', 'Professional'),
#     )

#     TIME_PREF = (
#         ('morning', 'Morning'),
#         ('evening', 'Evening'),
#         ('night', 'Night'),
#     )

#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     user_type = models.CharField(max_length=10, choices=USER_TYPE)

#     # Teacher fields
#     service_type = models.CharField(max_length=20, choices=SERVICE_TYPE, blank=True)
#     charge_fee = models.BooleanField(default=False)
#     preferred_time = models.CharField(max_length=10, choices=TIME_PREF)

#     # Student fields
#     education_level = models.CharField(max_length=50, blank=True)
#     subjects = models.CharField(max_length=200, blank=True)

#     def __str__(self):
#         return self.user.username
# from django.db import models
# from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     USER_TYPE_CHOICES = (
#         ('student', 'Student'),
#         ('teacher', 'Teacher'),
#     )

#     SERVICE_CHOICES = (
#         ('tuition', 'Tuition'),
#         ('technical', 'Technical'),
#         ('professional', 'Professional'),
#     )

#     user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
#     service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, blank=True)
#     charge = models.BooleanField(default=False)
#     preferred_time = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    SERVICE_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    service_type = models.CharField(
        max_length=10, choices=SERVICE_CHOICES, blank=True, null=True
    )

    subjects = models.TextField(blank=True)
    preferred_timings = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username