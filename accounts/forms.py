from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User
from . import models


class TransactionForm(forms.ModelForm):

    sender = forms.ModelChoiceField(queryset=User.objects.all())
    receiver = forms.ModelChoiceField(queryset=User.objects.all())
    amount = forms.IntegerField(required=True)

    class Meta:
        model = models.Transaction
        fields = ('sender', 'receiver', 'amount')


class SignUpForm(forms.ModelForm):
    username = forms.CharField(required=False, help_text='Optional.')
    balance = forms.IntegerField(required=True, help_text='Required.')
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'balance', 'password1', 'password2')
