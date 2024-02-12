from rest_framework import generics
from ..models import StockItem
from ..serializers import StockItemSerializer

class StockItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
