from django.urls import path
from . import views

# definition of the application's urls
urlpatterns = [
    path('signup', views.signup, name='signup'),
]
