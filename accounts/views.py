# accounts/views.py
from django.http import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from accounts import models
from accounts.models import User, Transaction
from . import forms


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def transactionset(request2):
    if request2.method == 'POST':
     form = forms.TransactionForm(request2.POST)
     user = User.objects.get(username=request.user)
     if form.is_valid():
        amount = form.cleaned_data['amount']
        formset = form.save()
        # sender.lower_balance(sender,amount)
        # receiver.increase_balance(sender,amount)
        sender = User.objects.get(username=request.user)
        reciever = User.objects.get(username=formset.reciever)
        sender.User.lower_balance(formset.amount)
        reciever.User.increase_balance(formset.amount)
        # TODO: save transaction to db

    else:
        form = forms.TransactionForm()
        return render(request2, 'templates/transaction_form.html', {'form': form})


class TransactionViewSet:
    template_name = 'transaction_info.html'
