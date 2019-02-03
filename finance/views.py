from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import CompanyForm, FormuComptaForm
from .models import Company, FormuCompta
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
    formuComptaForCompany = FormuCompta.objects.filter(company__id=company.id)
    return render(request, 'finance/summaryCompany.html', locals())

def addFormuCompta(request,id):
    company = get_object_or_404(Company, id=id)
    form = FormuComptaForm(request.POST or None)
    if form.is_valid():
        formTemp = form.save(commit=False)
        formucompta = FormuCompta(company = Company.objects.get(id=company.id), month = formTemp.month, year = formTemp.year, ca = formTemp.ca, frais_achat = formTemp.frais_achat, charges_sociales = formTemp.charges_sociales, fg = formTemp.fg, autres_frais = formTemp.autres_frais, ebitda = formTemp.ebitda, credits_ct = formTemp.credits_ct, credits_lt = formTemp.credits_lt, cashflow = formTemp.cashflow, investissements = formTemp.investissements)
        formucompta.save()
        return redirect('summaryCompany', id=company.id)
    return render(request, 'finance/addFormuCompta.html', locals())

def deleteFormuCompta(request,id,id2):
    formucompta = get_object_or_404(FormuCompta, id=id)
    company = get_object_or_404(Company, id=id2)
    formucompta.delete()
    return redirect('summaryCompany', id=company.id)

def editFormuCompta(request,id, id2):
    formucompta = get_object_or_404(FormuCompta, id=id)
    company = get_object_or_404(Company, id=id2)
    form = FormuComptaForm(request.POST or None, instance=formucompta)
    if form.is_valid():
        form.save()
        return redirect('summaryCompany', id=company.id)
    return render(request, 'finance/editFormuCompta.html', {'form':form})

def showGraph(request,id):
    company = get_object_or_404(Company, id=id)
    formuComptaForCompany = FormuCompta.objects.filter(company__id=company.id)
    return render(request, 'finance/showGraph.html', locals())
