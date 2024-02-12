# myapp/models/stockitem.py
from django.db import models

class StockItem(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    in_stock = models.IntegerField()
    total_allocated = models.IntegerField()
    allocated_to_builds = models.IntegerField()
    allocated_to_sales = models.IntegerField()
    available_stock = models.IntegerField()
    incoming_stock = models.IntegerField()
    net_stock = models.IntegerField()

    def __str__(self):
        return f"{self.item.name} - {self.in_stock} in stock"
