from django_tables2 import Table, Column, TemplateColumn

from .models import TradingAccount, Trade

class TradingAccountTable(Table):
    # title = Column(linkify=True)
    links = TemplateColumn(template_code=
                             "<a href='{% url 'accounts_update' record.pk %}'><i class='bi bi-card-checklist'></i> \
                             <a class='p-3' href='{% url 'accounts_update' record.pk %}'><i class='bi bi-pencil-square'></i></a>",
                             orderable=False)

    class Meta:
        # attrs = {"class": "table table-hover"}
        # 'thead': {
        # 'class': 'table-light',
        # },
        attrs = {
            "th" : {
                "_ordering": {
                    "orderable": "sortable", # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`
                }
            }
        }
        model = TradingAccount
        fields = ['identifier', 'title', 'type',
                  'initial_balance', 'active', 'created_at', 'links']
        orderable = True


class TradeTable(Table):
    # title = Column(linkify=True)
    links = TemplateColumn(template_code=
                             "<a class='p-3' href='{% url 'trades_update' record.pk %}'><i class='bi bi-pencil-square'></i></a> \
                             <a href='{% url 'trades_delete' record.pk %}'><i class='bi bi-trash'></i>",
                             orderable=False)

    class Meta:
        attrs = {
            "th" : {
                "_ordering": {
                    "orderable": "sortable", # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`
                }
            }
        }
        model = Trade
        fields = ['identifier', 'trading_account', 'symbol',
                  'side', 'opened_at', 'open_price', 'volume',
                  'stop_loss', 'take_profit', 'close_price',
                  'closed_at', 'reason']
        orderable = True