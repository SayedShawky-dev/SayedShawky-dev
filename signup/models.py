from django.db import models
from django.db.models.fields import EmailField

class Signup(models.Model):
    username = models.CharField(max_length=30)
    email= models.EmailField(null=False,blank=False)
    password =models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
