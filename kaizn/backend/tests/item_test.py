from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Item, Category, User  # Adjust import paths as necessary

class ItemViewsTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Instead of manually obtaining a token and setting it in the request header,
        # use DRF's `force_authenticate` to simulate an authenticated request.
        self.client.force_authenticate(user=self.user)

        # Setup test data as before
        category_name = "Test Category"
        category = Category.objects.create(name=category_name)
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
        self.item = Item.objects.create(**self.item_data)

    def tearDown(self):
        # Reset authentication for the client after tests have run
        self.client.force_authenticate(user=None)

    def test_item_list_create_api_view(self):
        url = reverse('item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)  # Assuming only one item exists


