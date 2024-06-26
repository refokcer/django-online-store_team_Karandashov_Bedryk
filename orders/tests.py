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

    def test_user_orders_view_not_auth(self):
        response = self.client.get(reverse('orders:user_orders'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{reverse("accounts:user_login")}?next={reverse("orders:user_orders")}')

    def test_create_order_view_with_auth(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('orders:checkout', kwargs={'order_id': self.order.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_user_orders_view_with_auth(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('orders:user_orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_orders.html')

    def test_get_price(self):
        self.assertEqual(self.orderItem.get_cost(), 30)

    def test_get_full_price(self):
        self.assertEqual(self.order.get_total_price, 272)