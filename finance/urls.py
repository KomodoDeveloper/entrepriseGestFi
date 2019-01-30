from django.urls import path
from . import views

# definition of the application's urls
urlpatterns = [
    path('home', views.home, name='home'),
    path('listCompany',views.listCompany, name='listCompany'),
    path('addCompany', views.addCompany, name='addCompany'),
    path('editCompany/<int:id>', views.editCompany, name='editCompany'),
    path('deleteCompany/<int:id>', views.deleteCompany, name='deleteCompany'),
    path('', views.homeRedirection, name='homeRedirection'),
]
