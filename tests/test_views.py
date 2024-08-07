from rest_framework.test import APITestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer

class MenuItemViewTest(APITestCase):
    def setUp(self):
        # Create test data
        Menu.objects.create(title="IceCream", price=80)
        Menu.objects.create(title="Cake", price=150)
    
    def test_getall(self):
        response = self.client.get('/api/menuview')
        expected_data = {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': 2,
                    'title': 'IceCream',
                    'price': '80.00',
                },
                {
                    'id': 3,
                    'title': 'Cake',
                    'price': '150.00',
                }
            ]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
