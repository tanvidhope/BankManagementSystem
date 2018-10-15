from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User
from . import models


class TransactionForm(forms.ModelForm):

    # sender = models
    class Meta:
        model = models.Transaction
        fields = ('sender', 'receiver', 'amount')


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=False, help_text='Optional.')
    balance = forms.IntegerField(required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'balance', 'password1', 'password2')
