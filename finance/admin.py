from django.contrib import admin
from .models import Company, Year, Month, FormuCompta

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display   = ('name', 'address', 'country', 'contact')
    list_filter    = ('name','contact', 'country')
    ordering       = ('name', )
    search_fields  = ('name', 'address', 'country' ,'contact')

class FormuComptaAdmin(admin.ModelAdmin):
    list_display   = ('company', 'month', 'year', 'ca', 'frais_achat', 'charges_sociales', 'fg', 'autres_frais', 'ebitda', 'credits_ct', 'credits_lt', 'cashflow', 'investissements')
    list_filter    = ('company','month', 'year')
    ordering       = ('-year', '-month')
    search_fields  = ('company', 'month', 'year' ,'ca','frais_achat','charges_sociales','fg','autres_frais','ebitda','credits_ct','credits_lt','cashflow','investissements')

class YearAdmin(admin.ModelAdmin):
    list_display   = ('year', )
    list_filter    = ('year', )
    ordering       = ('year', )
    search_fields  = ('year', )

class MonthAdmin(admin.ModelAdmin):
    list_display   = ('number', 'month')
    list_filter    = ('number', 'month')
    ordering       = ('number', )
    search_fields  = ('number', 'month')

admin.site.register(Company, CompanyAdmin)
admin.site.register(FormuCompta, FormuComptaAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Month, MonthAdmin)
