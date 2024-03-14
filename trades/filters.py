from django_filters.filterset import FilterSet

from .models import TradingAccount, Trade


class TradingAccountFilter(FilterSet):
    class Meta:
        model = TradingAccount
        fields = ['type', 'active']


class TradeFilter(FilterSet):
    class Meta:
        model = Trade
        fields = ['trading_account', 'symbol', 'side', 'reason']
