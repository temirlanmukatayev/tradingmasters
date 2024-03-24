from django_filters import ModelChoiceFilter
from django_filters.filterset import FilterSet

from .models import Trade, TradingAccount


def trading_accounts(request):
    """Return TradingAccount list of the current user."""
    return TradingAccount.objects.filter(owner=request.user.id)


class TradingAccountFilter(FilterSet):
    
    class Meta:
        model = TradingAccount
        fields = ['type', 'active']


class TradeFilter(FilterSet):

    trading_account = ModelChoiceFilter(queryset=trading_accounts)

    class Meta:
        model = Trade
        fields = ['trading_account', 'symbol', 'side', 'reason']
