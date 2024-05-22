from django.test import TestCase

from accounts.models import User
from django.urls import reverse


class OrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', full_name="test", password='12345')

    def test_user_cart_view_add_to_card(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('cart:add_to_cart', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{reverse("shop:product_detail", args=[1])}')

    def test_user_cart_view_remove_from_cart(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('cart:remove_from_cart', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{reverse("cart:show_cart")}')

    def test_user_cart_view_show_cart(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('cart:show_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
