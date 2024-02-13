from django.urls import path
# from .views import LoginView, CreateUserView, ItemListView
from .views.loginView import LoginView, CreateUserView
from .views.item_views import ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView
from .views.categoryView import CategoryListCreateAPIView
from .views.stockItemCreate import StockItemListCreateAPIView
from .views.stockItemUpdate import StockItemRetrieveUpdateAPIView
from .views.dashboardView import DashboardAPIView
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication



schema_view = get_schema_view(
   openapi.Info(
      title="Kaizn Backend API",
      default_version='v1',
      description="API description",
      terms_of_service="https://barathisridhar.me",
      contact=openapi.Contact(email="barathis1998@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
      authentication_classes=(TokenAuthentication,),
)


urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api-token'),
    path('api/create_user/', CreateUserView.as_view(), name='create-user'),
    path('api/items/', ItemListCreateAPIView.as_view(), name='item-list'),
    path('api/items/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('stockitems/', StockItemListCreateAPIView.as_view(), name='stockitem-list-create'),
    path('stockitems/<str:sku>/', StockItemRetrieveUpdateAPIView.as_view(), name='stockitem-retrieve-update'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]