from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User
from . import models


class TransactionForm(forms.ModelForm):

    # sender = models

    class Meta:
        model = models.Transaction
        fields = ['sender', 'receiver', 'amount']


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('account_number', 'username', 'balance', 'password1', 'password2')
