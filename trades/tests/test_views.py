from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from ..models import TradingAccount

from .. import views


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Home')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'I should not be on the page')

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            views.HomePageView.as_view().__name__
        )


class TradingAccountCreateViewTest(TestCase):

    fixtures = ['user']

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('accounts_create')
        cls.user = get_user_model().objects.get(pk=2)

    def test_ta_create_status_code(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_ta_create_template(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertTemplateUsed(
            response,
            'trading_accounts/tradingaccount_create.html'
        )

    def test_ta_create_contains_correct_html(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        self.assertContains(response, 'type')

    def test_ta_create_doesnot_contain_incorrect_html(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertNotContains(response, 'I should not be here!')
    
    def test_ta_create_url_resolves_ta_create_view(self):
        view = resolve('/accounts_create/')
        self.assertEqual(
            view.func.__name__,
            views.TradingAccountsCreateView.as_view().__name__
        )

    def test_ta_create_anonymous_cannot_see_page(self):
        response = self.client.get(self.url)
        self.assertRedirects(
            response,
            '/accounts/login/?next=/accounts_create/'
        )

    def test_ta_create_authenticated_user_can_see_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_ta_creation(self):
        data = {
            'title': 'new title',
            'identifier': 'newidentifier',
            'description': 'new description',
            'type': 'REAL',
            'initial_balance': 10000,
            'active': True
        }
        self.client.force_login(self.user)
        response = self.client.post(self.url, data=data)
        self.assertEqual(TradingAccount.objects.count(), 1)
        self.assertRedirects(response, reverse('accounts_list'))
