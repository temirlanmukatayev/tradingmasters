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
        cls.tr_account = TradingAccount.objects.create(
            owner=cls.user,
            identifier='testidentifier',
            title='Test Title',
            description='Test Description',
            type='REAL',
            initial_balance=10000,
            active=True,
            created_at='2024, 3, 27, 18, 59, 23, 395340',
            updated_at='2024, 3, 27, 18, 59, 48, 473482'
        )

    def test_owner(self):
        field = self.tr_account._meta.get_field('owner')
        self.assertEqual(field.verbose_name, 'owner')
        self.assertEqual(self.tr_account.owner, self.user)
    
    def test_identifier(self):
        field = self.tr_account._meta.get_field('identifier')
        self.assertEqual(field.verbose_name, 'identifier')
        self.assertEqual(field.max_length, 25)
        self.assertEqual(self.tr_account.identifier, 'testidentifier')

    def test_title(self):
        field = self.tr_account._meta.get_field('title')
        self.assertEqual(field.verbose_name, 'title')
        self.assertEqual(self.tr_account.title, 'Test Title')
        self.assertEqual(field.max_length, 100)

    def test_description(self):
        field = self.tr_account._meta.get_field('description')
        self.assertEqual(field.verbose_name, 'description')
        self.assertEqual(self.tr_account.description, 'Test Description')
    
    def test_type(self):
        field = self.tr_account._meta.get_field('type')
        self.assertEqual(field.verbose_name, 'type')
        self.assertEqual(field.max_length, 4)
        self.assertEqual(self.tr_account.type, 'REAL')

    def test_initial_balance(self):
        field = self.tr_account._meta.get_field('initial_balance')
        self.assertEqual(field.verbose_name, 'initial balance')
        self.assertEqual(self.tr_account.initial_balance, 10000)

    def test_active(self):
        field = self.tr_account._meta.get_field('active')
        self.assertEqual(field.verbose_name, 'active')
        self.assertTrue(self.tr_account.active)
    
    def test_created_and_updated_dates(self):
        created = self.tr_account._meta.get_field('created_at')
        self.assertEqual(created.verbose_name, 'created at')
        updated = self.tr_account._meta.get_field('updated_at')
        self.assertEqual(updated.verbose_name, 'updated at')

    def test_str(self):
        self.assertEqual(self.tr_account.__str__(), self.tr_account.title)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.tr_account.get_absolute_url(),
            reverse('accounts_detail', kwargs={'pk': self.tr_account.pk})
        )
