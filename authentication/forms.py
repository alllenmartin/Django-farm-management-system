from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    other_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'eg. Allen'}))
    email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'eg. example@gmail.com'}))


    class Meta:
        model = User
        fields = ('username', 'other_name', 'email', 'password1', 'password2', )