from django.db import models
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os


class User(AbstractUser):
    """
    Primary User Authentication Model
    """
    USER_TYPE = (
        ('Student', 'Student'),
        ('Faculty', 'Faculty')
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(('Phone Number'),
                                    validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    department = models.CharField(max_length=255)
    type = models.CharField(
        ('Type'), choices=USER_TYPE, max_length=18, default=USER_TYPE[0][0])
    is_volunteer = models.BooleanField(default=False)
    is_complainant = models.BooleanField(default=False)
    is_panelist = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.first_name + self.last_name + str(self.id)


class Complaint(models.Model):

    ACTION = (
        ('Problem Dismissed', 'Problem Dismissed'),
        ('Action Taken', 'Action Taken'),
        ('Problem Settled', 'Problem Settled')
    )

    complainant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='complaint')
    subject = models.CharField(max_length=255)
    date = models.DateField(null=False)
    description = models.TextField(max_length=500)
    proof = models.FileField(upload_to='uploaded_files/')
    action = models.CharField(
        ('Status'), choices=ACTION, max_length=18)
    action_description = models.TextField(max_length=500)
    action_report = models.FileField(upload_to='uploaded_files/')

    @staticmethod
    def extension(self):
        name, extension = os.path.splitext(self.proof.name)
        return extension

    @property
    def filename(value):
        return os.path.basename(value.proof.name)

    def __str__(self) -> str:
        return str(self.pk)


class VolunteerAction(models.Model):

    ACTION = (
        ('Seminar', 'Seminar'),
        ('Workshop', 'Workshop'),
        ('Campaign', 'Campaign')
    )

    volunteer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='action')
    name = models.CharField('Event Name', max_length=255)
    date = models.DateField(null=False)
    report = models.FileField(upload_to='uploaded_files/')
    action = models.CharField(
        ('Action Type'), choices=ACTION, max_length=18)
