from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import TradingAccount


class TradingAccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            username='test',
            email='test@mail.com',
            password='testpass123'
        )
        cls.trading_account = TradingAccount.objects.create(
            owner=cls.user,
            identifier='testidentifier1',
            title='Test Trading Account',
            description='Test Trading Account Description',
            type='REAL',
            initial_balance=10000,
            active=True,
            created_at='2024, 3, 27, 17, 49, 49, 461243',
            updated_at='2024, 3, 27, 17, 50, 13, 995630'
        )
    
    def test_identifier_field(self):
        identifier = self.trading_account._meta.get_field('identifier')
        self.assertEqual(identifier.verbose_name, 'identifier')
        self.assertEqual(identifier.max_length, 25)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.trading_account.get_absolute_url(),
            reverse('trades_detail', self.trading_account.pk)
        )
