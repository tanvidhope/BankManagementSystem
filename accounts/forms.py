from django import forms
from . import models


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ['sender', 'receiver', 'amount']
