from django.test import TestCase

from accounts.models import User
from django.urls import reverse

from orders.models import OrderItem, Order
from shop.models import Product, Category


class OrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', full_name="test", password='12345')
        self.order = Order.objects.create(user=self.user)
        self.category = Category.objects.create(title='test', slug='test')
        self.product = Product.objects.create(category=self.category, image='test.jpg', price=10,
                                              title="test", description="test", slug="test")
        self.orderItem = OrderItem.objects.create(order=self.order, product=self.product, quantity=3, price=10)
        self.orderItem2 = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price=121)

    def test_user_accounts_view_edit_profile(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('accounts:edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')

    def test_user_accounts_view_login(self):
        response = self.client.get(reverse('accounts:user_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_accounts_view_register(self):
        response = self.client.get(reverse('accounts:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_user_accounts_view_user_profile(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('accounts:user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

