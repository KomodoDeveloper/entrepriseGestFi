from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=40, verbose_name="nom", unique=True)
    address = models.CharField(max_length=180, verbose_name="adresse")
    country = models.CharField(max_length=80, verbose_name="pays", default="Suisse")
    contact = models.CharField(max_length=100, verbose_name="personne de contact")

    class Meta:
        verbose_name = "Company"
        ordering = ['name']

    def __str__(self):
        return self.name

class FormuCompta(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE )
    month = models.ForeignKey('Month', on_delete=models.CASCADE)
    year = models.ForeignKey('Year', on_delete=models.CASCADE)
    ca = models.FloatField(default=0.0, verbose_name="CA")
    frais_achat = models.FloatField(default=0.0, verbose_name="Frais d'achat")
    charges_sociales = models.FloatField(default=0.0, verbose_name="Charges sociales")
    fg = models.FloatField(default=0.0, verbose_name="Frais généraux")
    autres_frais = models.FloatField(default=0.0, verbose_name="Autres frais")
    ebitda = models.FloatField(default=0.0, verbose_name="EBITDA")
    credits_ct = models.FloatField(default=0.0, verbose_name="Crédits courts termes")
    credits_lt = models.FloatField(default=0.0, verbose_name="Crédits long termes")
    cashflow = models.FloatField(default=0.0, verbose_name="Cashflow")
    investissements = models.FloatField(default=0.0, verbose_name="Investissements")

    class Meta:
        verbose_name = "FormuCompta"
        ordering = ['-year', '-month']

    def __str__(self):
        return self.month.month + str(self.year)

class Month(models.Model):
    number = models.IntegerField(verbose_name="num", unique=True)
    month = models.CharField(max_length=20, verbose_name="mois", unique=True)

    class Meta:
        verbose_name = "Month"

    def __str__(self):
        return self.month

class Year(models.Model):
    year = models.IntegerField(verbose_name="année", unique=True)

    class Meta:
        verbose_name = "Year"

    def __str__(self):
        return str(self.year)
