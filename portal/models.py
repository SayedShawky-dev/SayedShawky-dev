from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    
