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
