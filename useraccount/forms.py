from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    grade = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            },
            choices=[
             ('MBB', 'MBB'),
        ('Professor', 'Professor'),
        ('doctor', 'doctor'),
        ('MBA', 'MBA'),
       
    ]
        )
    )
   
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_teacher', 'is_student','is_headdep','grade' )
       
       
