from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto

# Create your views here.

def contatti(request):

    if request.method =="POST":
        form=FormContatto(request.POST)

        if form.is_valid():
            print("Salvo il contatto nel database")
            nuovo_contatto=form.save()
            print("new post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            return HttpResponse("<h1>Grazie per averci contattato</h1>")
        else:
            return HttpResponse("<h1>Contenuto form non valido</h1>")

    else:
        form=FormContatto()
        context={"form": form}
        return render(request,"home_form.html",context)
