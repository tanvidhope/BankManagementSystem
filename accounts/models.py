from django.db import models

# Create your models here.
from django.db.models import CASCADE


class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    balance = models.IntegerField()

    def lower_balance(self, amount):
        self.balance -= amount
        self.save

    def increase_balance(self, amount):
        self.balance += amount
        self.save


class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_money', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_money', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
