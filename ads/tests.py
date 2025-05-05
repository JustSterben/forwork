from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ad

class AdModelTest(TestCase):
    def test_create_ad(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        ad = Ad.objects.create(
            user=user,
            title='Тестовый товар',
            description='Описание',
            category='техника',
            condition='new'
        )
        self.assertEqual(ad.title, 'Тестовый товар')
