from django.db import models

class Resources(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=200)


    def __str__(self):
        return self.title
