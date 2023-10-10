from django.db import models

# Create your models here.
class items(models.Model):
    Item_id=models.CharField(max_length=30)
    Item_name=models.CharField(max_length=100)
    Quantity=models.CharField(max_length=100)
    Price=models.CharField(max_length=100)
