# from rest_framework import generics
# from rest_framework.response import Response
# from django.db.models import Q  # Import Q objects for OR conditions
# from ..models import StockItem
# from ..serializers import StockItemDashboardSerializer
# from rest_framework.pagination import PageNumberPagination

# class DashboardPagination(PageNumberPagination):
#     page_size = 10  # Set the number of items per page
#     page_size_query_param = 'page_size'  # Custom query parameter to override page size
#     max_page_size = 100  # Set the maximum page size

# class DashboardAPIView(generics.ListAPIView):
#     pagination_class = DashboardPagination  # Set the pagination class

#     def get(self, request):
#         # Retrieve query parameters
#         sku = request.query_params.get('SKU')
#         name = request.query_params.get('name')
#         category = request.query_params.get('category')
#         tags = request.query_params.getlist('tags')

#         print(f"SKU: {sku}, Name: {name}, Category: {category}, Tags: {tags}")

#         # Filter stock items based on query parameters
#         stock_items = StockItem.objects.select_related('item__category_name').prefetch_related('item__tags')

#         if sku:
#             # Perform partial matching for SKU
#             stock_items = stock_items.filter(item__SKU__icontains=sku)

#         if name:
#             stock_items = stock_items.filter(item__name__icontains=name)
#         if category:
#             # Perform partial matching for category name
#             stock_items = stock_items.filter(Q(item__category_name__name__icontains=category))

#         if tags:
#             stock_items = stock_items.filter(item__tags__name__in=tags)

#         # Serialize data
#         serializer = StockItemDashboardSerializer(stock_items, many=True)

#         # Construct response data
#         data = {
#             'stock_items': serializer.data,
#             # Add more data as needed
#         }

#         return Response(data)

from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from ..models import StockItem
from ..serializers import StockItemDashboardSerializer
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator



class DashboardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class DashboardAPIView(generics.ListAPIView):
    queryset = StockItem.objects.select_related('item__category_name').prefetch_related('item__tags')
    serializer_class = StockItemDashboardSerializer
    pagination_class = DashboardPagination
    # @method_decorator(cache_page(60*30))

    @method_decorator(cache_page(60*30))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        # Retrieve query parameters
        sku = self.request.query_params.get('SKU')
        name = self.request.query_params.get('name')
        category = self.request.query_params.get('category')
        tags = self.request.query_params.getlist('tags')

        # Filter stock items based on query parameters
        queryset = self.queryset

        if sku:
            queryset = queryset.filter(item__SKU__icontains=sku)

        if name:
            queryset = queryset.filter(item__name__icontains=name)

        if category:
            queryset = queryset.filter(Q(item__category_name__name__icontains=category))

        if tags:
            queryset = queryset.filter(item__tags__name__in=tags)

        return queryset

