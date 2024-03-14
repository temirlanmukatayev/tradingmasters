from django.contrib import admin

from .models import TradingAccount, Trade, TradeLink

@admin.register(TradingAccount)
class TradingAccountAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'type', 'initial_balance', 'active', 'created_at']
    list_filter = ['active', 'type']
    search_fields = ['title', 'description']


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'trading_account', 'symbol', 'opened_at', 'volume', 'side', 'profit', 'reason']
    list_filter = ['reason', 'side', 'market']
    search_fields = ['notes']

@admin.register(TradeLink)
class TradeLinkAdmin(admin.ModelAdmin):
    list_display = ['trade', 'url']