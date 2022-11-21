from django.test import TestCase

from products.models import *
from django.contrib.auth.models import AnonymousUser


class ProductTestCase(TestCase):
    def setUp(self):
        self.consumer = Category.objects.create(name="Consumer")
        self.annon_user = User.objects.create_user(username='testuser', password='12345')  # AnonymousUser()
        self.test_asset = Item.objects.create(
            seller=self.annon_user, category=self.consumer, title='Test asset', price=1234, status='PENDING')

    def test_category(self):
        consumer = Category.objects.get(name="Consumer")
        self.assertEqual(str(consumer), 'Consumer')

    def test_user(self):
        self.assertEqual(self.annon_user.username, 'testuser')

    def test_asset(self):
        print(self.test_asset)
        self.assertEqual(int(self.test_asset.price), 1234)
