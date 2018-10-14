# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.http import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from accounts import models
from accounts.forms import SignUpForm
from accounts.models import User, Transaction
from . import forms


def sign_up():
    # form_class = UserCreationForm
    # success_url = reverse_lazy('login')
    # template_name = 'signup.html'
    # --------------------jays-------------
    # username_temp = request.POST.get('username', '')
    # password_temp = request.POST.get('password', '')
    # balance = request.POST.get('balance', '')
    # user = User.objects.get_or_create(username=username_temp, email='NA')
    # user.set_password(password_temp)
    # profile = User.objects.filter(user=user)
    # user.profile.balance(balance)
    # user.save()
    form = SignUpForm()
    return render(request, 'SignUp.html', {form:'form'})


def transaction_set(request2):
    if request2.method == 'POST':
     form = forms.TransactionForm(request2.POST)
     user = User.objects.get(username=request2.user)
     if form.is_valid():
        amount = form.cleaned_data['amount']
        formset = form.save()
        # sender.lower_balance(sender,amount)
        # receiver.increase_balance(sender,amount)
        sender = User.objects.get(username=user)
        reciever = User.objects.get(username=formset.reciever)
        sender.balance = sender.balance - amount
        reciever.balance = reciever.balance + amount
        # sender.User.lower_balance(formset.amount)
        # reciever.User.increase_balance(formset.amount)
        # TODO: save transaction to db

    else:
        form = forms.TransactionForm()
        return render(request2, 'accounts/templates/transaction_form.html', {'form': form})


def lower_balance(self, amount):
    self.balance -= amount
    self.save()


def increase_balance(self, amount):
    self.balance += amount
    self.save()


def user_login(request2):
    username_temp = request2.POST.get('username', '')
    password_temp = request2.POST.get('password', '')
    user = authenticate(request2, username = username_temp, password = password_temp)
    if user is not None:
        login(request2, user)
        return render(request2, 'home.html')

    else:
        return render(request, status=404)


def user_logout(request2):
    logout(request2)
    return render(request2, 'home.html')
