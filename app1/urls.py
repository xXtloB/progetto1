from django.urls import path
from .views import homepage, menu, chi_siamo, variabili, index

urlpatterns = [
    path('welcome/', homepage, name='home'),
    path('menu/', menu, name='menu'),
    path('chi_siamo/', chi_siamo, name='chi_siamo'),
    path('variabili/', variabili, name='variabili'),
    path('index/', index, name='index'),

]