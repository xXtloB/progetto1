from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html") 

def menu(request):
    return HttpResponse("<ol><li>Prima opzione</li><li>Seconda opzione</li><li>Terza opzione</li></ol>")

def chi_siamo(request):
    return render(request, "chi_siamo.html")
    
def variabili(request):
    context= { 'var1': '10','var2': 'ciao', 'var3' : '123 hello world'}
    return render(request, "variabili.html",context)

def index(request):
    return render(request, "index.html")
    