

from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from ..models import StockItem
from ..serializers import StockItemDashboardSerializer
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema



class DashboardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class DashboardAPIView(generics.ListAPIView):
    queryset = StockItem.objects.select_related('item__category_name').prefetch_related('item__tags')
    serializer_class = StockItemDashboardSerializer
    pagination_class = DashboardPagination
    # @method_decorator(cache_page(60*30))
    permission_classes = [IsAuthenticated]

   
    @swagger_auto_schema(security=[{'Token': []}])
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

# from rest_framework import generics
# from rest_framework.response import Response
# from django.db.models import Q
# from ..models import StockItem
# from ..serializers import StockItemDashboardSerializer
# from rest_framework.pagination import PageNumberPagination
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema

# class DashboardPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# class DashboardAPIView(generics.ListAPIView):
#     queryset = StockItem.objects.select_related('item__category_name').prefetch_related('item__tags')
#     serializer_class = StockItemDashboardSerializer
#     pagination_class = DashboardPagination
#     permission_classes = [IsAuthenticated]

#     @swagger_auto_schema(security=[{'Token': []}])
#     @method_decorator(cache_page(60*30))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    
#     def get_queryset(self):
#         sku = self.request.query_params.get('SKU')
#         name = self.request.query_params.get('name')
#         category = self.request.query_params.get('category')
#         tags = self.request.query_params.getlist('tags')

#         queryset = self.queryset

#         if sku:
#             queryset = queryset.filter(item__SKU__icontains=sku)

#         if name:
#             queryset = queryset.filter(item__name__icontains=name)

#         if category:
#             queryset = queryset.filter(Q(item__category_name__name__icontains=category))

#         if tags:
#             queryset = queryset.filter(item__tags__name__in=tags)

#         return queryset

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         # Custom logic to create your response
#         custom_data = {
#             'message': 'Custom response from DashboardAPIView',
#             'count': queryset.count(),
#             'data': self.serializer_class(queryset, many=True).data
#         }

#         response = Response(custom_data)
#         # Set CORS headers
#         response["Access-Control-Allow-Origin"] = "*"  # Allow requests from any origin
#         response["Access-Control-Allow-Methods"] = "GET, OPTIONS"  # Allowed HTTP methods
#         response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"  # Allowed headers
#         return Response(custom_data)

