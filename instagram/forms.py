# myapp/forms.py
from django import forms
from .models import LoginAttempt

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginAttempt
        fields = ['username_or_email', 'password']
        widgets = {
            'username_or_email': forms.TextInput(attrs={'placeholder': 'Phone number, username, or email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
