from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import (
    CreateView, DeleteView, FormView, UpdateView)
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from .filters import TradeFilter, TradingAccountFilter
from .forms import TradeForm, TradeImportForm, TradingAccountForm
from .mixins import OwnerEditMixin, OwnerMixin
from .models import Trade, TradingAccount
from .tables import TradeTable, TradingAccountTable


class HomePageView(TemplateView):
    template_name = 'home.html'


class TradingAccountsCreateView(LoginRequiredMixin, CreateView):
    model = TradingAccount
    form_class = TradingAccountForm
    success_url = reverse_lazy('accounts_list')
    template_name = 'trading_accounts/tradingaccount_create.html'

    def form_valid(self, form):
        """Set the current user as TradingAccount owner."""
        form.instance.owner = self.request.user
        return super(TradingAccountsCreateView, self).form_valid(form)
    
    def get_form_kwargs(self):
        """Pass the request object to the form class."""
        kwargs = super(TradingAccountsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class TradingAccountListView(
    LoginRequiredMixin, OwnerMixin,FilterView, SingleTableView):
    model = TradingAccount
    table_class = TradingAccountTable
    filterset_class = TradingAccountFilter
    paginate_by = 10
    template_name = 'trading_accounts/tradingaccounts_list.html'
    ordering = ['-created_at']


class TradingAccountUpdateView(LoginRequiredMixin, OwnerEditMixin, UpdateView):
    model = TradingAccount
    fields = [
        'identifier', 'title', 'description',
        'type','initial_balance', 'active'
    ]
    success_url = reverse_lazy('accounts_list')
    template_name = 'trading_accounts/tradingaccount_update.html'


class TradingAccountDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = TradingAccount
    success_url = reverse_lazy('accounts_list')
    template_name = 'trading_accounts/tradingaccount_confirm_delete.html'


class TradeListView(LoginRequiredMixin, OwnerMixin, FilterView, SingleTableView):
    model = Trade
    table_class = TradeTable
    filterset_class = TradeFilter
    paginate_by = 10
    template_name = 'trades/trades_list.html'
    ordering = ['-opened_at']


class TradeDetailView(LoginRequiredMixin, OwnerMixin, DetailView):
    model = Trade
    template_name = 'trades/trades_detail.html'
    context_object_name = 'trade'


class TradeCreateView(LoginRequiredMixin, CreateView):
    model = Trade
    form_class = TradeForm
    success_url = reverse_lazy('trades_list')
    template_name = 'trades/trades_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        result = super(TradeCreateView, self).form_valid(form)
        return(result)
    
    def get_form_kwargs(self):
        """Pass the request object to the form class."""
        kwargs = super(TradeCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class TradeUpdateView(LoginRequiredMixin, OwnerEditMixin, UpdateView):
    model = Trade
    form_class = TradeForm
    success_url = reverse_lazy('trades_list')
    template_name = 'trades/trade_update.html'

    def get_form_kwargs(self):
        """Pass the request object to the form class. Necessary to display
        only TradingAccounts that belong to the current user."""
        kwargs = super(TradeUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class TradeDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Trade
    success_url = reverse_lazy('trades_list')
    template_name = 'trades/trade_confirm_delete.html'


class TradeImportView(LoginRequiredMixin, OwnerMixin, FormView):
    template_name = 'trades/trades_import.html'
    form_class = TradeImportForm
    success_url = reverse_lazy('trades_list')

    def form_valid(self, form):
        """Call form's method trade_import."""
        total = form.trade_import()
        messages.success(self.request, f'{total} trades imported')
        return(super().form_valid(form))
    
    def get_form_kwargs(self):
        """Pass the request object to the form class. Necessary to display
        only TradingAccounts that belong to the current user."""
        kwargs = super(TradeImportView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
