from django.urls import path
from . import views

# definition of the application's urls
urlpatterns = [
    path('home', views.home, name='home'),
    path('listCompany',views.listCompany, name='listCompany'),
    path('addCompany', views.addCompany, name='addCompany'),
    path('editCompany/<int:id>', views.editCompany, name='editCompany'),
    path('deleteCompany/<int:id>', views.deleteCompany, name='deleteCompany'),
    path('summaryCompany/<int:id>', views.summaryCompany, name='summaryCompany'),
    path('addFormuCompta/<int:id>', views.addFormuCompta, name='addFormuCompta'),
    path('deleteFormuCompta/<int:id>/<int:id2>', views.deleteFormuCompta, name='deleteFormuCompta'),
    path('editFormuCompta/<int:id>/<int:id2>', views.editFormuCompta, name='editFormuCompta'),
    path('showGraph/<int:id>', views.showGraph, name='showGraph'),
    path('', views.homeRedirection, name='homeRedirection'),
]
