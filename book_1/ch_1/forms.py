from django import forms
from .models import Student , gamer

class UserForm1(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','city']


class UserForm2(forms.ModelForm):
    class Meta:
        model = gamer
        fields = ['username','password', 'email','character','game','picture','type','dateandtime',]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'character': forms.TextInput(attrs={'class': 'form-control'}),
            'game': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'dateandtime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'name': 'Full Name',
            'password' : 'password',
            'email' : 'email address',
            'character': 'Main Character',
            'game': 'Game Title',
            'picture': 'Upload Picture',
            'type': 'Game Type',
            'dateandtime': 'Date & Time',
        }