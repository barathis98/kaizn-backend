from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from ..models import StockItem, Item, Category, Tag, User  # Adjust imports based on your app structure

class DashboardAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user and token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Setup test data
        category = Category.objects.create(name='Test Category')
        tag = Tag.objects.create(name='Test Tag')
        self.item_data = {
            'SKU': 'SKU123',
            'name': 'Test Item',
            'category_name': category,  # Adjusted to use name directly, ensure this aligns with your model structure
            'cost': 10.99,
            'is_assembly': False,
            'is_component': False,
            'is_purchaseable': True,
            'is_salable': True,
            'is_bundle': False
        }
        item = Item.objects.create(self.item_data)
        item.tags.add(tag)
        StockItem.objects.create(item=item, quantity=10)

    def test_dashboard_access_unauthenticated(self):
        # Clear authentication credentials
        self.client.credentials()

        url = reverse('dashboard-api')  # Use the actual path name for your DashboardAPIView
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_dashboard_list_retrieve(self):
        url = reverse('dashboard-api')  # Use the actual path name for your DashboardAPIView
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one stock item exists

    def test_dashboard_filter_by_sku(self):
        url = f"{reverse('dashboard-api')}?SKU=SKU123"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['item']['SKU'], 'SKU123')

    def test_dashboard_filter_by_name(self):
        url = f"{reverse('dashboard-api')}?name=Test Item"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['item']['name'], 'Test Item')


