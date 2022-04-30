from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class createAccount(UserCreationForm):
    first_name =  forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'First Name'}) , max_length=200)
    last_name = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'username', 'email', 'address', 'city', 'country', 'password1', 'password2']