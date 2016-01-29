from django.db import models
#from django.template.defaultfilters import default

# Create your models here.

class Beam(models.Model):
    beam_name = models.CharField(max_length = 30)
    satellite_name = models.CharField(max_length = 30, default = "None")
    def __str__(self):
        return self.beam_name
    
class Point(models.Model):
    beam = models.ForeignKey(Beam)
    latitude = models.DecimalField(max_digits=17, decimal_places=14)
    longitude = models.DecimalField(max_digits=17, decimal_places=14)