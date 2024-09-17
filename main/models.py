from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = models.URLField()
    brands = models.CharField(max_length=255)
    price = models.IntegerField()
    categories = models.CharField(max_length=255)
    description = models.TextField()
    
    

    
