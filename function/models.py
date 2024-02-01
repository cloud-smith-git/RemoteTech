from django.db import models


# Create your models here.
class Part(models.Model):
    text = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.text

class Vehicle(models.Model):
    miles = models.IntegerField()

class Fuel(models.Model):
    miles = models.IntegerField()
    amount = models.FloatField()

class Test(models.Model):
    pass

