from django.test import TestCase

from accounts.models import User
from django.urls import reverse, resolve

from shop.models import Product, Category


class OrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', full_name="test", password='12345')

    def test_user_cart_view_show_cart(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('cart:show_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
