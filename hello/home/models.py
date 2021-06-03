from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=22)
    email = models.CharField(max_length=22)
    phone = models.CharField(max_length=22)
    desc = models.TextField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name