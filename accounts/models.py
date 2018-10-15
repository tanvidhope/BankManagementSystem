from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class User(models.Model):
    username = models.CharField(max_length=100, default=0)
    balance = models.IntegerField(default=500)


class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_money', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_money', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


