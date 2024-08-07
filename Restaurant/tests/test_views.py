from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('menu-list')  # Replace 'menu-list' with the actual name of your URL pattern
        # Creating test instances of the Menu model
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(title="Cake", price=120, inventory=50)

    def test_getall(self):
        # Making GET request to retrieve all Menu objects
        response = self.client.get(self.url)
        # Serializing the data
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data
        # Checking if the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Checking if the serialized data matches the response data
        self.assertEqual(response.data, expected_data)