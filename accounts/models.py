from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class User(models.Model):
    account_number = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    # address = models.CharField(max_length=100)
    # phone_number = models.CharField(max_length=12)
    balance = models.IntegerField(default=0)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # date_of_birth = models.DateField(null=True)
    # Acc_balance = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    def lower_balance(self, amount):
        self.balance -= amount
        self.save()

    def increase_balance(self, amount):
        self.balance += amount
        self.save()


class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_money', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_money', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
