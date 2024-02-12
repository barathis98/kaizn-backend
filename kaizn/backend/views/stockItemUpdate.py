from ..models import StockItem
from ..serializers import StockItemSerializer
from rest_framework import generics

class StockItemRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer

    def get_object(self):
        sku = self.kwargs.get('sku')
        return StockItem.objects.get(item__SKU=sku)
