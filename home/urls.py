from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('contact', views.contact, name='about'),  
    path('about', views.about, name='about'),  
]
