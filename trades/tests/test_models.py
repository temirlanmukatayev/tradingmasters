from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import TradingAccount, Trade


class TradingAccountModelTest(TestCase):

    fixtures = ['user', 'tradingaccount']

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.get(pk=2)
        cls.ta = TradingAccount.objects.get(pk=1)

    def test_owner(self):
        field = self.ta._meta.get_field('owner')
        self.assertEqual(field.verbose_name, 'owner')
        self.assertEqual(self.ta.owner, self.user)
    
    def test_identifier(self):
        field = self.ta._meta.get_field('identifier')
        self.assertEqual(field.verbose_name, 'identifier')
        self.assertEqual(field.max_length, 25)
        self.assertEqual(self.ta.identifier, 'accountidentifier')

    def test_title(self):
        field = self.ta._meta.get_field('title')
        self.assertEqual(field.verbose_name, 'title')
        self.assertEqual(self.ta.title, 'Test Account')
        self.assertEqual(field.max_length, 100)

    def test_description(self):
        field = self.ta._meta.get_field('description')
        self.assertEqual(field.verbose_name, 'description')
        self.assertEqual(self.ta.description, 'Test Account Description')
    
    def test_type(self):
        field = self.ta._meta.get_field('type')
        self.assertEqual(field.verbose_name, 'type')
        self.assertEqual(field.max_length, 4)
        self.assertEqual(self.ta.type, 'REAL')

    def test_initial_balance(self):
        field = self.ta._meta.get_field('initial_balance')
        self.assertEqual(field.verbose_name, 'initial balance')
        self.assertEqual(self.ta.initial_balance, 10000)

    def test_active(self):
        field = self.ta._meta.get_field('active')
        self.assertEqual(field.verbose_name, 'active')
        self.assertTrue(self.ta.active)
    
    def test_createdat(self):
        created = self.ta._meta.get_field('created_at')
        self.assertEqual(created.verbose_name, 'created at')

    def test_updatedat(self):
        updated = self.ta._meta.get_field('updated_at')
        self.assertEqual(updated.verbose_name, 'updated at')

    def test_str(self):
        self.assertEqual(self.ta.__str__(), self.ta.title)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.ta.get_absolute_url(),
            reverse('accounts_detail', kwargs={'pk': self.ta.pk})
        )


class TradeModelTest(TestCase):

    fixtures = ['tradingaccount', 'trade', 'user']

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.get(pk=2)
        cls.ta = TradingAccount.objects.get(pk=1)
        cls.trade = Trade.objects.get(pk=1)

    def test_owner(self):
        field = self.trade._meta.get_field('owner')
        self.assertEqual(field.verbose_name, 'owner')
        self.assertEqual(self.trade.owner, self.user)

    def test_tradingaccount(self):
        field = self.trade._meta.get_field('trading_account')
        self.assertEqual(field.verbose_name, 'trading account')
        self.assertEqual(self.trade.trading_account.title, 'Test Account')
    
    def test_openedat(self):
        field = self.trade._meta.get_field('opened_at')
        self.assertEqual(field.verbose_name, 'opened at')

    def test_identifier(self):
        field = self.trade._meta.get_field('identifier')
        self.assertEqual(field.verbose_name, 'identifier')
        self.assertEqual(self.trade.identifier, 'tradeidentifier')

    def test_symbol(self):
        field = self.trade._meta.get_field('symbol')
        self.assertEqual(field.verbose_name, 'symbol')
        self.assertEqual(self.trade.symbol, 'EURUSD')

    def test_side(self):
        field = self.trade._meta.get_field('side')
        self.assertEqual(field.verbose_name, 'side')
        self.assertEqual(self.trade.side, 'SEL')

    def test_volume(self):
        field = self.trade._meta.get_field('volume')
        self.assertEqual(field.verbose_name, 'volume')
        self.assertEqual(self.trade.volume, 4)

    def test_openprice(self):
        field = self.trade._meta.get_field('open_price')
        self.assertEqual(field.verbose_name, 'open price')
        self.assertEqual(self.trade.open_price, 1.08455)

    def test_takeprofit(self):
        field = self.trade._meta.get_field('take_profit')
        self.assertEqual(field.verbose_name, 'take profit')
        self.assertEqual(self.trade.take_profit, 1.08353)

    def test_stoploss(self):
        field = self.trade._meta.get_field('stop_loss')
        self.assertEqual(field.verbose_name, 'stop loss')
        self.assertEqual(self.trade.stop_loss, 1.08505)

    def test_closedat(self):
        field = self.trade._meta.get_field('closed_at')
        self.assertEqual(field.verbose_name, 'closed at')

    def test_closeprice(self):
        field = self.trade._meta.get_field('close_price')
        self.assertEqual(field.verbose_name, 'close price')
        self.assertEqual(self.trade.close_price, 1.08352)

    def test_comission(self):
        field = self.trade._meta.get_field('commission')
        self.assertEqual(field.verbose_name, 'commission')
        self.assertEqual(self.trade.commission, 20)

    def test_swap(self):
        field = self.trade._meta.get_field('swap')
        self.assertEqual(field.verbose_name, 'swap')
        self.assertEqual(self.trade.swap, 0)

    def test_profit(self):
        field = self.trade._meta.get_field('profit')
        self.assertEqual(field.verbose_name, 'profit')
        self.assertEqual(self.trade.profit, 400)

    def test_reason(self):
        field = self.trade._meta.get_field('reason')
        self.assertEqual(field.verbose_name, 'reason')
        self.assertEqual(self.trade.reason, 'TP')

    def test_market(self):
        field = self.trade._meta.get_field('market')
        self.assertEqual(field.verbose_name, 'market')
        self.assertEqual(self.trade.market, 'FX')

    def test_rr(self):
        field = self.trade._meta.get_field('rr')
        self.assertEqual(field.verbose_name, 'rr')
        self.assertEqual(self.trade.rr, 2)

    def test_risk(self):
        field = self.trade._meta.get_field('risk')
        self.assertEqual(field.verbose_name, 'risk')
        self.assertEqual(self.trade.risk, 2)

    def test_notes(self):
        field = self.trade._meta.get_field('notes')
        self.assertEqual(field.verbose_name, 'notes')
        self.assertEqual(self.trade.notes, 'Test Note')

    def test_links(self):
        field = self.trade._meta.get_field('links')
        self.assertEqual(field.verbose_name, 'links')
        self.assertTrue(self.trade.links, 'https://test.com')

    def test_image(self):
        field = self.trade._meta.get_field('image')
        self.assertEqual(field.verbose_name, 'image')

    def test_createdat(self):
        field = self.trade._meta.get_field('created_at')
        self.assertEqual(field.verbose_name, 'created at')

    def test_updatedat(self):
        field = self.trade._meta.get_field('updated_at')
        self.assertEqual(field.verbose_name, 'updated at')

    def test_str(self):
        self.assertEqual(self.trade.__str__(), 'tradeidentifier')
    
    def test_get_absolute_url(self):
        self.assertEqual(
            self.trade.get_absolute_url(),
            reverse('trades_detail', kwargs={'pk': self.trade.pk})
        )
