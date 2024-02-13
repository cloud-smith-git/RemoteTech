from django.db import models

class VehicleCheck(models.Model):
    miles = models.IntegerField()

class PartRequest(models.Model):
    name = models.CharField(max_length=50)
    parts = models.CharField(max_length=255)


class FuelPurchase(models.Model):
    vehicle = models.IntegerField()
    miles = models.IntegerField()
    amount = models.FloatField()
    # image = models.ImageField(upload_to='fuel_images', blank=True, default='fuel_images/default.jpg')
    

class Test(models.Model):
    pass

