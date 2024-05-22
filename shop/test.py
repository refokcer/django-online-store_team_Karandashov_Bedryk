from django.test import TestCase

from accounts.models import User
from django.urls import reverse


from shop.models import Product, Category


class ShopTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', full_name="test", password='12345')
        self.category = Category.objects.create(title='test', slug='test')
        self.product = Product.objects.create(category=self.category, image='test.jpg', price=10,
                                              title="test", description="test", slug="test")

    def test_user_shop_view_favorites(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('shop:favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites.html')

    def test_user_shop_view_home_page(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('shop:home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_user_shop_view_product_detail(self):
        self.client.login(email='testuser@gmail.com', password='12345')
        response = self.client.get(reverse('shop:product_detail', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')





