from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from backend.models import Item, User

class ItemListViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create test data for the items


        # Create a test client
        self.client = APIClient()

    def test_get_items_authenticated(self):
        self.client.force_authenticate(user=self.user)
        self.item1 = Item.objects.create(name='Item 1', category='Electronics', stock_quantity=10)
        self.item2 = Item.objects.create(name='Item 2', category='Clothing', stock_quantity=5)


        url = reverse('item-list')  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    def test_filter_items_by_name_authenticated(self):
        self.client.force_authenticate(user=self.user)
        self.item1 = Item.objects.create(name='Item 1', category='Electronics', stock_quantity=10)
        self.item2 = Item.objects.create(name='Item 2', category='Clothing', stock_quantity=5)

        url = reverse('item-list')
        response = self.client.get(url, {'name': 'Item 1'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Item 1')

    def test_create_item_authenticated(self):
        # Authenticate the client
        self.client.force_authenticate(user=self.user)

        # Test POST request to create a new item
        url = reverse('item-list')  # Assuming you have a name for your URL pattern
        data = {
            "sku": "ABC123",
            "name": "Test Item",
            "category": "Electronics",
            "tags": "testing",
            "stock_quantity": 50
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the item was created in the database
        self.assertEqual(Item.objects.count(), 1)
        created_item = Item.objects.get()
        self.assertEqual(created_item.name, 'Test Item')
