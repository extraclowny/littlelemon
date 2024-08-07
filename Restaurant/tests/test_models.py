from django.test import TestCase
from Restaurant.models import Menu

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80)
        self.assertEqual(str(item), "IceCream : 80")