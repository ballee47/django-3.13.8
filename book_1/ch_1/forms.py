from django import forms
from .models import web_user



class UserForm2(forms.ModelForm):
    class Meta:
        model = web_user
        fields = ['username','password', 'email','picture','type','dateandtime',]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'dateandtime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'name': 'Full Name',
            'password' : 'password',
            'email' : 'email address',
            'picture': 'Upload Picture',
            'type': 'role',
            'dateandtime': 'Date & Time',
        }