# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from accounts import models
from accounts.forms import SignUpForm
from accounts.models import User, Transaction, Profile
from . import forms


def sign_up(request2):
    # form_class = UserCreationForm
    # success_url = reverse_lazy('login')
    # template_name = 'signup.html'
    # form = SignUpForm()
    # return render(request, 'SignUp.html', {form:'form'})

    if request2.method == 'POST':
        form = SignUpForm(request2.POST)
        if form.is_valid():
            username_temp = request.POST.get('username')
            password_temp = request.POST.get('password1')
            balance_temp = request.POST.get('balance')

            user, created = User.objects.get_or_create(username=username_temp, email='NA')
            if created:
                user.set_password(password_temp)
            profile = Profile.objects.filter(user = user)
            profile.balance = balance_temp
            profile.username = username_temp
            user.save()
            return render(request, 'Home.html')
        else:
            return render(request, 'SignUp.html', {form: 'form'})


def login_customer(request):
    username_temp = request.POST.get('username', '')
    password_temp = request.POST.get('password', '')
    user = authenticate(request, username = username_temp, password = password_temp)
    if user is not None:
        login(request, user)
    return render(request, 'home.html')


def transaction_set(request):
    if request.method == 'POST':
     form = forms.TransactionForm(request.POST)
     user = User.objects.get(username=request.user)
     if form.is_valid():
        amount = form.cleaned_data['amount']
        formset = form.save()
        # sender.lower_balance(sender,amount)
        # receiver.increase_balance(sender,amount)
        sender = User.objects.get(username=user)
        reciever = User.objects.get(username=formset.reciever)
        sender.balance = sender.balance - amount
        reciever.balance = reciever.balance + amount
        return redirect(request, 'home.html')

    else:
        form = forms.TransactionForm()
        return render(request, 'transaction_form.html', {'form': form})


def user_login(request2):
    username_temp = request2.POST.get('username')
    password_temp = request2.POST.get('password')
    user = authenticate(request2, username = username_temp, password = password_temp)
    if user is not None:
        login(request2, user)
        return render(request2, 'home.html')

    else:
        return render(request, status=404)


def user_logout(request2):
    logout(request2)
    return render(request2, 'home.html')


def withdraw(request):
    user = request.user
    print(user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('home.html')
    withdraw_amount = int(request.POST.get('amount', ''))
    #print(request.POST)
    cur_balance = user.profile.balance
    user.profile.balance = user.profile.balance - withdraw_amount
    user.save()


def deposit(request):
    if not request.user.is_authenticated:
        return redirect('home.html')
    user = request.user
    deposit_amount = int(request.POST.get('amount', ''))
    user.profile.balance = user.profile.balance + deposit_amount
    user.save()
