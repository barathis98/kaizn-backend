from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Item, Category, User
from ..serializers import ItemSerializer

class ItemViewsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Log the user in by obtaining a token
        response = self.client.post(reverse('api-token'), {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data.get('token')

        category_name = "Test Category"
        category = Category.objects.create(name=category_name)
        self.item_data = {
            'SKU': 'SKU123',
            'name': 'Test Item',
            'category_name': category.pk,  # Assign category primary key
            'cost': 10.99,
            'is_assembly': False,
            'is_component': False,
            'is_purchaseable': True,
            'is_salable': True,
            'is_bundle': False
        }
        self.item = Item.objects.create(**self.item_data)

    def test_item_list_create_api_view(self):
        url = reverse('item-list')
        # Include token in the headers
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Token {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one item exists

    def test_item_retrieve_update_destroy_api_view(self):
        url = reverse('item-detail', kwargs={'pk': self.item.pk})
        # Include token in the headers
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Token {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item_data['name'])

        updated_data = {
            'name': 'Updated Item Name'
        }
        response = self.client.put(url, updated_data, HTTP_AUTHORIZATION=f'Token {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])

        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
