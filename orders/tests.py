from django.test import TestCase

from accounts.models import User
from django.urls import reverse

class OrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', full_name="test", password='12345')

    def test_user_orders_view_not_auth(self):
        response = self.client.get(reverse('orders:user_orders'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{reverse("accounts:user_login")}?next={reverse("orders:user_orders")}')

    def test_user_orders_view_with_auth(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('orders:user_orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_orders.html')

