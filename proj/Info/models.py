from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    rpassword = models.CharField(max_length=50)
