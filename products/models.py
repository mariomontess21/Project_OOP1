from django.db import models

class Products(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
    brand = models.CharField(max_length=50)
    tag = models.IntegerField()
    
