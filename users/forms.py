from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    account_no = forms.IntegerField(required=False, help_text='Optional.')
    username = forms.CharField(required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('account_no', 'username', 'password1', 'password2', )
