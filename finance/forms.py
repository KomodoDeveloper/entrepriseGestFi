from django import forms
from django.db import models
from .models import Company, FormuCompta

# creation of the forms. most of them are derived from the models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class FormuComptaForm(forms.ModelForm):
    class Meta:
        model = FormuCompta
        fields = ('month', 'year', 'ca', 'frais_achat', 'charges_sociales', 'fg', 'autres_frais', 'ebitda', 'credits_ct', 'credits_lt', 'cashflow', 'investissements')
