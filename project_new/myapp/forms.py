from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .models import contact,booking


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-primary', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-primary', 'placeholder': 'Repeat Password'}))
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control text-primary','placeholder': 'Enter Firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control text-primary','placeholder': 'Enter Lastname'}),
            'username': forms.TextInput(attrs={'class': 'form-control text-primary','placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control text-primary','placeholder': 'Enter Email'}),
            #'password1':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),

        }


class contactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','phone','message']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter name"}),
            'email':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter email"}),
            'phone':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter phone"}),
            'message':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter message"}),
        }

class bookingForm(forms.ModelForm):
    class Meta:
        model=booking
        fields=['name','email','phone','city','country']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter name"}),
            'email':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter email"}),
            'phone':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter phone"}),
            'city':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter city"}),
            'country':forms.TextInput(attrs={'class':'form-control text-primary','placeholder':"Enter country"}),
        }
