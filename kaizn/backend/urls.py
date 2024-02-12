from django.urls import path
# from .views import LoginView, CreateUserView, ItemListView
from .views.loginView import LoginView, CreateUserView
from .views.item_views import ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView






urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api-token'),
    path('api/create_user/', CreateUserView.as_view(), name='create-user'),
  path('api/items/', ItemListCreateAPIView.as_view(), name='item-list'),
    path('api/items/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail'),

    # Add more URL patterns as needed
]