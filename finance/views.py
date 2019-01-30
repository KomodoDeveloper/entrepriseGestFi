from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import CompanyForm
from .models import Company
import os, time, datetime

# Create your views here.
def home(request):
    return render(request, 'finance/home.html', locals())

def homeRedirection(request):
    return redirect('home')

def listCompany(request):
    companies = Company.objects.all()
    return render(request, 'finance/listCompany.html', {'companies':companies})

def addCompany(request):
    # Build the form, either with the data posted,
    # or empty if the user accesses for the first time the page.
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        validEntry = True

    # Whatever happens, we display the page of the form.
    return render(request, 'finance/addCompany.html', locals())

def editCompany(request,id):
    company = get_object_or_404(Company, id=id)
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        form.save()
        return redirect('listCompany')
    return render(request, 'finance/editCompany.html', {'form':form})

def deleteCompany(request,id):
    company = get_object_or_404(Company, id=id)
    company.delete()
    return redirect('listCompany')

def summaryCompany(request,id):
    company = get_object_or_404(Company, id=id)
    return render(request, 'finance/summaryCompany.html', locals())
