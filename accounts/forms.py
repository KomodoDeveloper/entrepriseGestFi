from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# declaration of the form attached to the User model from contrib.auth
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Entrer une adresse email valide.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
