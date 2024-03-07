from django.contrib import admin

from .models import TradingAccount

@admin.register(TradingAccount)
class TradingAccountAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'type', 'initial_balance', 'active', 'created_at']
    list_filter = ['active', 'type']
    search_fields = ['title', 'description']
