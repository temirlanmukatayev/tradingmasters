from django_tables2 import Table, TemplateColumn

from .models import Trade, TradingAccount


class TradingAccountTable(Table):
    actions = TemplateColumn(
        template_code="<a href='{% url 'trades_list' %}?trading_account={{record.pk}}'><i class='bi bi-card-checklist'></i></a>"
            " <a class='p-3' href='{% url 'accounts_update' record.pk %}'><i class='bi bi-pencil-square'></i></a>",
        orderable=False
    )

    class Meta:
        model = TradingAccount
        fields = [
            'identifier', 'title', 'type', 'initial_balance',
            'active', 'created_at', 'actions'
        ]
        orderable = True


class TradeTable(Table):
    actions = TemplateColumn(
        template_code="<a class='p-3' href='{% url 'trades_detail' record.pk %}'><i class='bi bi-envelope-open'></i></a>"
            " <a href='{% url 'trades_delete' record.pk %}'><i class='bi bi-trash'></i></a>",
        orderable=False
    )

    class Meta:
        model = Trade
        fields = [
            'identifier', 'trading_account', 'symbol', 'side',
            'opened_at', 'open_price', 'volume', 'stop_loss',
            'take_profit', 'close_price', 'reason', 'actions'
        ]
        orderable = True
