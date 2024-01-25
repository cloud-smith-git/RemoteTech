from django.db import models

# Create your models here.
class Request(models.Model):
    text = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return self.text