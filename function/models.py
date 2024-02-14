from django.db import models

WINDSHIELD_CHOICES = [
    ('Good', 'Good'),
    ('Cracked', 'Cracked'),
    ('Chipped', 'Chipped'),
    ]
WIPER_CHOICES = [
        ('Good', 'Good'),
        ('Worn', 'Worn'),
    ]
OIL_CHOICES = [
        ('Good', 'Good'),
        ('Low', 'Low'),
    ] 
TIRE_CHOICES = [
        ('Good', 'Good'),
        ('Leaking', 'Leaking'),
        ('Worn', 'Worn'),
    ] 
HEADLIGHT_CHOICES = [
        ('Good', 'Good'),
        ('Need Replaced', 'Need Replaced'),
    ]  
TAILLIGHT_CHOICES = [
        ('Good', 'Good'),
        ('Need Replaced', 'Need Replaced'),
    ]
class VehicleCheck(models.Model):

    name = models.CharField(max_length=50, default='None')
    vehicle = models.IntegerField(default=0)   
    miles = models.IntegerField(default=0)
    oil_change = models.IntegerField(default=0)
    windshield = models.CharField(
        choices=WINDSHIELD_CHOICES,
        default='Good',
        max_length=50
    )
    wipers = models.CharField(
        choices=WIPER_CHOICES,
        default='Good',
        max_length=50
    )
    oil = models.CharField(
        choices=OIL_CHOICES,
        default='Good',
        max_length=50
    )
    tires = models.CharField(
        choices=TIRE_CHOICES,
        default='Good',
        max_length=50
    )
    headlights = models.CharField(
        choices=HEADLIGHT_CHOICES,
        default='Good',
        max_length=50
    )
    tail_lights = models.CharField(
        choices=TAILLIGHT_CHOICES,
        default='Good',
        max_length=50
    )
    additional = models.CharField(
        max_length=255,
        default='None')

class PartRequest(models.Model):
    name = models.CharField(max_length=50)
    parts = models.CharField(max_length=255)

class FuelPurchase(models.Model):
    vehicle = models.IntegerField()
    miles = models.IntegerField()
    amount = models.FloatField()
    image = models.ImageField(upload_to='djangouploads/files/receipts', blank=True, default='None')
    
class Test(models.Model):
    pass

