from django.urls import path
# from .views import LoginView, CreateUserView, ItemListView
from .views.loginView import LoginView, CreateUserView
from .views.item_views import ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView
from .views.categoryView import CategoryListCreateAPIView
from .views.stockItemCreate import StockItemListCreateAPIView
from .views.stockItemUpdate import StockItemRetrieveUpdateAPIView
from .views.dashboardView import DashboardAPIView


urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api-token'),
    path('api/create_user/', CreateUserView.as_view(), name='create-user'),
    path('api/items/', ItemListCreateAPIView.as_view(), name='item-list'),
    path('api/items/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('stockitems/', StockItemListCreateAPIView.as_view(), name='stockitem-list-create'),
    path('stockitems/<str:sku>/', StockItemRetrieveUpdateAPIView.as_view(), name='stockitem-retrieve-update'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),

]