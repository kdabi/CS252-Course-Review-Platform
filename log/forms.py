from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.forms import ModelForm, Textarea
from log.models import Review

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment', 'summary']#['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 50, 'rows': 10})
        }
