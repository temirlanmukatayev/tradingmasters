from urllib.parse import urlparse

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class TradingAccount(models.Model):

    class AccountType(models.TextChoices):
        REAL = 'REAL', 'Real'
        CHALLENGE = 'CHAL', 'Challenge'
        FUNDED = 'FUND', 'Funded'

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    identifier = models.CharField(blank=True, null=True, max_length=25)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=4,
        choices=AccountType.choices,
        default=AccountType.REAL,
    )
    initial_balance = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['identifier', 'owner'],
                name='unique_tradingaccount_and_owner'
            )                                                  
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('accounts_detail', kwargs={'pk': self.pk})


class Trade(models.Model):

    class TradingSide(models.TextChoices):
        BUY = 'BUY', 'Buy'
        SELL = 'SEL', 'Sell'

    class TradingMarket(models.TextChoices):
        FOREX = 'FX', 'Forex'
        FUTURES = 'FT', 'Futures'
        INDICES = 'IN', 'Indices'
        CRYPTO = 'CR', 'Crypto'

    class Reason(models.TextChoices):
        TP = 'TP', 'TP'
        SL = 'SL', 'SL'

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    trading_account = models.ForeignKey(
        TradingAccount, on_delete=models.CASCADE
    )
    opened_at = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(blank=True, null=True, max_length=25)
    symbol = models.CharField(max_length=16)
    side = models.CharField(
        max_length=3,
        choices=TradingSide.choices,
        default=TradingSide.SELL,
    )
    volume = models.FloatField(blank=True, null=True)
    open_price = models.FloatField(blank=True, null=True)
    take_profit = models.FloatField(blank=True, null=True)
    stop_loss = models.FloatField(blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    swap = models.FloatField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    reason = models.CharField(
        max_length=2,
        choices=Reason.choices,
    )
    market = models.CharField(
        max_length=2,
        choices=TradingMarket.choices,
        default=TradingMarket.FOREX,
    )
    rr = models.IntegerField(blank=True, null=True)
    risk = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    links = models.TextField(max_length=1024, blank=True,
                             help_text=
                             'Each link from new line in the format: '
                             'http://tradingview.com/')
    image = models.ImageField(upload_to='trades/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['trading_account', 'identifier', 'owner'],
                name='unique_tradingaccount_and_owner_and_identifier'
            )                                                  
        ]

    def __str__(self):
        return self.identifier
    
    def get_absolute_url(self):
        return reverse("trades_detail", kwargs={"pk": self.pk})


# class Setup(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     trade = models.ForeignKey(Trade, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['title']
#         # indexes = [
#         #     models.Index(fields=['-title']),
#         # ]


# class Argument(models.Model):
#     title = models.CharField(max_length=100)
#     short_name = models.CharField(max_length=10)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     trade = models.ForeignKey(Trade, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['title']
#         # indexes = [
#         #     models.Index(fields=['title']),
#         # ]
