from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # trading accounts
    path('accounts_create/', views.TradingAccountsCreateView.as_view(), name='accounts_create'),
    path('accounts_list/', views.TradingAccountListView.as_view(), name='accounts_list'),
    path('accounts/<pk>/update/', views.TradingAccountUpdateView.as_view(), name='accounts_update'),
    path('accounts/<pk>/delete/', views.TradingAccountDeleteView.as_view(), name='accounts_delete'),
    # trades
    path('trades_list/', views.TradeListView.as_view(), name='trades_list'),
    path('trades/<pk>/detail/', views.TradeDetailView.as_view(), name='trades_detail'),
    path('trades_create/', views.TradeCreateView.as_view(), name='trades_create'),
    path('trades/<pk>/update/', views.TradeUpdateView.as_view(), name='trades_update'),
    path('trades/<pk>/delete/', views.TradeDeleteView.as_view(), name='trades_delete'),
]