from django import forms

from .models import Trade


class TradeForm(forms.ModelForm):
    url_title = forms.CharField(required=False, max_length=64)
    url = forms.URLField(required=False)
    
    class Meta:
        model = Trade
        fields = ['trading_account', 'identifier', 'symbol',
                  'side', 'opened_at', 'open_price', 'volume',
                  'stop_loss', 'take_profit', 'close_price',
                  'reason', 'closed_at', 'market']
        widgets = {
            'opened_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'closed_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }