from django.urls import path
from .views import LoginView, CreateUserView, ItemListView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api-token'),
    path('api/create_user/', CreateUserView.as_view(), name='create-user'),
    path('api/items/', ItemListView.as_view(), name='item-list'),


    # Add more URL patterns as needed
]