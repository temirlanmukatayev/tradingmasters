from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from .filters import TradingAccountFilter, TradeFilter
from .forms import TradeForm
from .models import TradingAccount, Trade
from .tables import TradingAccountTable, TradeTable
from .mixins import OwnerMixin, OwnerEditMixin
    

class HomePageView(TemplateView):
    template_name = 'home.html'


class TradingAccountsCreateView(LoginRequiredMixin, CreateView):
    model = TradingAccount
    fields = ['identifier', 'title', 'description', 'type', 'initial_balance', 'active']
    success_url = reverse_lazy('accounts_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(TradingAccountsCreateView, self).form_valid(form)


class TradingAccountListView(LoginRequiredMixin, OwnerMixin, FilterView, SingleTableView):
    model = TradingAccount
    table_class = TradingAccountTable
    filterset_class = TradingAccountFilter
    paginate_by = 10
    template_name = 'accounts_list.html'


class TradingAccountUpdateView(LoginRequiredMixin, OwnerEditMixin, UpdateView):
    model = TradingAccount
    fields = ['identifier', 'title', 'description', 'type', 'initial_balance', 'active']
    success_url = reverse_lazy('accounts_list')
    template_name_suffix = '_update_form'


class TradingAccountDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = TradingAccount
    success_url = reverse_lazy('accounts_list')
    template_name = 'trades/tradingaccount_confirm_delete.html'


class TradeListView(LoginRequiredMixin, OwnerMixin, FilterView, SingleTableView):
    model = Trade
    table_class = TradeTable
    filterset_class = TradeFilter
    paginate_by = 10
    template_name = 'trades_list.html'


class TradeCreateView(LoginRequiredMixin, CreateView):
    model = Trade
    form_class = TradeForm
    success_url = reverse_lazy('trades_list')
    template_name = 'trades/trades_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(TradeCreateView, self).form_valid(form)


class TradeUpdateView(LoginRequiredMixin, OwnerEditMixin, UpdateView):
    model = Trade
    form_class = TradeForm
    success_url = reverse_lazy('trades_list')
    template_name = 'trade_update.html'


class TradeDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Trade
    success_url = reverse_lazy('trades_list')
    template_name = 'trade_confirm_delete.html'
