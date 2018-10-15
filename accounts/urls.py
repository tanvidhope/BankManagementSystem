# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('transaction/', views.transaction_set, name='transaction'),
    path('login/', views.login_customer, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
]