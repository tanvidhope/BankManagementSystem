# from django.db import models

# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    account_no = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=15,blank=True)
    balance = models.IntegerField(blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
