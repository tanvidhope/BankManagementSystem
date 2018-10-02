# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class TransactionSet:
    template_name = 'transaction_form.html'


class TransactionViewSet:
    template_name = 'transaction_info.html'
