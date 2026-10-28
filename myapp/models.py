from django.db import models

# Create your models here.
class Emp(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    salry = models.IntegerField()
    age = models.IntegerField()