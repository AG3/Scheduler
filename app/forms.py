from django import forms
from django.contrib.auth.models import User
from .models import Professor


class UserForm(forms.ModelForm):
    # username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

'''
class LoginForm(forms.ModelForm):
'''


class SearchForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('email',)
