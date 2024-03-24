import csv
from io import TextIOWrapper

from django import forms
from django.core.validators import FileExtensionValidator

from .models import Trade, TradingAccount


class TradingAccountForm(forms.ModelForm):
    '''Form for TradingAccount creation'''
    
    class Meta:
        model = TradingAccount
        fields = [
            'identifier', 'title', 'description',
            'type', 'initial_balance', 'active'
        ]
    
    def __init__(self, *args, **kwargs):
        '''Grants access to the request object.'''
        self.request = kwargs.pop('request')
        super(TradingAccountForm, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        identifier = self.cleaned_data['identifier']
        duplicates = TradingAccount.objects.filter(
            identifier=identifier,
            owner=self.request.user
        )
        if self.instance.pk:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise forms.ValidationError(
                'Trading Account with such Identifier already exists.'
                'Please set another Identifier'
            )


class TradeForm(forms.ModelForm):
    links = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}),
        help_text='Each url from a new line'
    )
    
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


class TradeImportForm(forms.Form):

    def __init__(self, *args, **kwargs):
        '''
        Grants access to the request object so that only members of the
        current user are given as options.
        '''
        self.request = kwargs.pop('request')
        super(TradeImportForm, self).__init__(*args, **kwargs)
        self.fields['accounts'].queryset = TradingAccount.objects.filter(
            owner=self.request.user)
        self.user = self.request.user

    accounts = forms.ModelChoiceField(queryset=TradingAccount.objects.all())
    file = forms.FileField(validators=[FileExtensionValidator(['csv'])])

    def trade_import(self):
        '''Imports trades from file'''
        new_trade = {}
        total = 0
        account = self.cleaned_data['accounts']
        try:
            f = TextIOWrapper(self.cleaned_data['file'])
            trades = list(csv.DictReader(f))
            for trade in trades:
                for key, value in trade.items():
                    if account:
                        new_trade['trading_account'] = account
                    if self.user:
                        new_trade['owner'] = self.user
                    if key.lower() == 'id':
                        new_trade['identifier'] = value
                    if key.lower() == 'deal':
                        new_trade['identifier'] = value
                    if key.lower() == 'symbol':
                        if value.endswith('x'):
                            value = value.rstrip('x')
                        new_trade['symbol'] = value
                    if key.lower() == 'open time':
                        new_trade['opened_at'] = value
                    if key.lower() == 'volume':
                        new_trade['volume'] = value
                    if key.lower() == 'side':
                        if value.lower() == 'buy':
                            new_trade['side'] = 'BUY'
                        if value.lower() == 'sell':
                            new_trade['side'] = 'SEL'
                    if key.lower() == 'close time':
                        new_trade['closed_at'] = value
                    if key.lower() == 'open price':
                        new_trade['open_price'] = value
                    if key.lower() == 'close price':
                        new_trade['close_price'] = value
                    if key.lower() == 'stop loss':
                        new_trade['stop_loss'] = value
                    if key.lower() == 'take profit':
                        new_trade['take_profit'] = value
                    if key.lower() == 'swap':
                        new_trade['swap'] = value
                    if key.lower() == 'comission':
                        new_trade['comission'] = value
                    if key.lower() == 'profit':
                        new_trade['profit'] = value
                    if key.lower() == 'reason':
                        if value == 'Stop Loss' or 'Stop Out':
                            value = 'SL'
                        if value == 'Take Profit':
                            value = 'TP'
                        new_trade['reason'] = value
                try:
                    if Trade.objects.create(**new_trade):
                        total += 1
                except:
                    print(f"Trade {new_trade['identifier']} already exists")
                    continue
            return total

        except csv.Error:
            status = 'CSV file error'
