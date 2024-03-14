from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from .filters import TradingAccountFilter
from .models import TradingAccount, Trade
from .tables import TradingAccountTable
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
