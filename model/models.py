from django.db import models

# Create your models here.

class Community(models.Model):
    full_name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    contact = models.CharField(max_length=300)

def __str__(self):
    return self.title