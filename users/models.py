from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    ADMINISTRATOR = 'administrator'
    COURIER = 'courier'
    OFFICE_WORKER = 'office_worker'
    ROLE_CHOICES = [
        (ADMINISTRATOR, 'administrator'),
        (COURIER, 'courier'),
        (OFFICE_WORKER, 'office_worker')
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=OFFICE_WORKER)


class Report(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creatied_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)