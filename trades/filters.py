from django_filters.filterset import FilterSet

from .models import TradingAccount


class TradingAccountFilter(FilterSet):
    class Meta:
        model = TradingAccount
        fields = ['type', 'active']
