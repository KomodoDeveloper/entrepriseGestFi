from django.contrib import admin
from .models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display   = ('name', 'address', 'country', 'contact')
    list_filter    = ('name','contact', 'country')
    ordering       = ('name', )
    search_fields  = ('name', 'address', 'country' ,'contact')


admin.site.register(Company, CompanyAdmin)
