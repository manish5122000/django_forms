from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import AccountDetails


class myform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    lastname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))
   

    class Meta:
        model = User
        fields = ['firstname','lastname','username', 'email','password1','password2']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}

class AccountForm(forms.ModelForm):
    locality = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    zipcode = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    state = forms.Select(attrs={'class':"form-control"})
    account_number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    IFSC_Code = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))

    class Meta:
        model = AccountDetails
        fields = ['locality', 'city', 'zipcode', 'state', 'Account_Number', 'IFSC_Code']