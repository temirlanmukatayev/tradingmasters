from django.db import models
from django.contrib.auth import get_user_model


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
    description = models.TextField(blank=True)
    type = models.CharField(max_length=4,
        choices=AccountType.choices,
        default=AccountType.REAL,
    )
    initial_balance = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True)
    login = models.CharField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-title']),
        ]

    def __str__(self):
        return self.title


# class Trade(models.Model):

#     class TradingSide(models.TextChoices):
#         BUY = 'BUY', 'Buy'
#         SELL = 'SEL', 'Sell'

#     class TradingMarket(models.TextChoices):
#         FOREX = 'FX', 'Forex'
#         INDICES = 'IN', 'Indices'
#         CRYPTO = 'CR', 'Crypto'

#     symbol = models.CharField(max_length=10)
#     opened_at = models.DateTimeField(blank=True, null=True)
#     closed_at = models.DateTimeField(blank=True, null=True)
#     side = models.CharField(
#         max_length=3,
#         choices=TradingSide,
#         default=TradingSide.SELL,
#     )
#     market = models.CharField(
#         max_length=2,
#         choices=TradingMarket,
#         default=TradingMarket.FOREX,
#     )
#     rr = models.IntegerField(blank=True, null=True)
#     risk = models.IntegerField(blank=True, null=True)
#     notes = models.CharField(max_length=200, blank=True)
#     link = models.URLField(blank=True)
#     image = models.ImageField(upload_to='trades/images/%Y/%m/%d/', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-opened_at']
#         # indexes = [
#         #     models.Index(fields=['-publish']),
#         # ]

#     def __str__(self):
#         return self.pk


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
