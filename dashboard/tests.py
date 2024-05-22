from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class DashboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', full_name="test", password='12345')
        self.admin = User.objects.create_superuser(email='testadmin@gmail.com', full_name="test", password='12345')

    def test_products_view_not_admin(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('dashboard:products'))
        self.assertEqual(response.status_code, 404)

    def test_products_view_admin(self):
        self.client.login(email='testadmin@gmail.com', password='12345')
        response = self.client.get(reverse('dashboard:products'))
        self.assertEqual(response.status_code, 200)

    def test_orders_view_not_admin(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('dashboard:orders'))
        self.assertEqual(response.status_code, 404)

    def test_orders_view_admin(self):
        self.client.login(email='testadmin@gmail.com', password='12345')
        response = self.client.get(reverse('dashboard:orders'))
        self.assertEqual(response.status_code, 200)