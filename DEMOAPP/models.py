from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class SubmitTask(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    address = models.CharField(max_length=230)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name


