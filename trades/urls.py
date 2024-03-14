from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('accounts_create/', views.TradingAccountsCreateView.as_view(), name='accounts_create'),
    path('accounts_list/', views.TradingAccountListView.as_view(), name='accounts_list'),
    path('accounts/<pk>/update/', views.TradingAccountUpdateView.as_view(), name='accounts_update'),
    path('accounts/<pk>/delete/', views.TradingAccountDeleteView.as_view(), name='accounts_delete'),
]