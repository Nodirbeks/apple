from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title',
            'content',
            'photo',
            'category'
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название статьи"
            }),
            'content': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Содержание статьи"
            }),
            'photo': forms.FileInput(attrs={
                'class': "form-control",
            }),
            'category': forms.Select(attrs={
                'class': "form-control",
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, help_text='Максимум 16 символов',
                               widget=forms.TextInput(attrs={
                                   'class': "form-control",
                                   'placeholder': 'Имя пользователья'
                               }))

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': "form-control",
                                   'placeholder': 'Пароль'
                               }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': 'Пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': 'Подтвердите пароль'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Имя пользователья'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Фамилия'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Почта'
    }))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')
