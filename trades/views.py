from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import TradingAccount, Trade


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    

class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class HomePageView(TemplateView):
    template_name = 'home.html'


class TradingAccountsCreateView(LoginRequiredMixin, CreateView):
    model = TradingAccount
    fields = ['identifier', 'title', 'description', 'type', 'initial_balance', 'active']
    success_url = reverse_lazy('accounts_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(TradingAccountsCreateView, self).form_valid(form)


class TradingAccountsListView(LoginRequiredMixin, OwnerMixin, ListView):
    model = TradingAccount
    context_object_name = 'accounts'
    template_name = 'accounts_list.html'


class TradingAccountUpdateView(LoginRequiredMixin, OwnerEditMixin, UpdateView):
    model = TradingAccount
    fields = ['identifier', 'title', 'description', 'type', 'initial_balance', 'active']
    success_url = reverse_lazy('accounts_list')
    template_name_suffix = '_update_form'


class TradingHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'trading_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = TradingAccount.objects.filter(owner=self.request.user)
        context['trades'] = Trade.objects.filter(owner=self.request.user)
        return context


class TradingAccountDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = TradingAccount
    success_url = reverse_lazy('accounts_list')
    template_name = 'trades/tradingaccount_confirm_delete.html'
