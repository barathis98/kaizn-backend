from django.db import models

class Item(models.Model):
    SKU = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_assembly = models.BooleanField(default=False)
    is_component = models.BooleanField(default=False)
    is_purchaseable = models.BooleanField(default=True)
    is_salable = models.BooleanField(default=True)
    is_bundle = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
