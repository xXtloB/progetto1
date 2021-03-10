from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto

# Create your views here.

def contatti(request):

    if request.method =="POST":
        form=FormContatto(request.POST)

        if form.is_valid():
            print("Il form è valido")
            print("Nome: ", form.cleaned_data["nome"])
            print("Cognome: ",form.cleaned_data["cognome"])
            print("Email: ",form.cleaned_data["email"])
            print("Contenuto: ",form.cleaned_data["contenuto"])

            return HttpResponse("<h1>Grazie per averci contattato</h1>")
        else:
            return HttpResponse("<h1>Contenuto form non valido</h1>")

    else:
        form=FormContatto()
        context={"form": form}
        return render(request,"home_form.html",context)
