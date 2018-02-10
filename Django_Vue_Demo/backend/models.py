from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64)
    page = models.IntegerField()

    def __str__(self):
        return '%s' % self.name