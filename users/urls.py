# accounts/urls.py
from django.urls import path

from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views as core_views



urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    # path('transaction/', views.TransactionSet, name='transaction'),
]