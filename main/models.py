from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    brands = models.CharField(max_length=255)
    price = models.IntegerField()
    categories = models.TextField()
    description = models.TextField()
    
    

    
