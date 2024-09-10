from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, name="name")
    image = models.ImageField()
    brands = models.CharField(max_length=255, name="brands")
    price = models.IntegerField(name="price")
    categories = models.TextField(name="categories")
    description = models.TextField(name="description")
    
    

    def __str__(self):
        return f"Name: {self.name} {self.brands} {self.price} {self.categories} {self.description} {self.image}"
