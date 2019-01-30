from django import forms
from django.db import models
from .models import Company

# creation of the forms. most of them are derived from the models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
