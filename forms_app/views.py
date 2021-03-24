from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import FormContatto,FormRegistrazione
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

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

def registrazioneView(request):
    if request.method=="POST":
        form=FormRegistrazione(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password1"]
            User.objects.create_user(username=username,password=password,email=email)
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect("/")
    else:
        form=FormRegistrazione()
    
    context={"form":form}
    return render(request,'registration/registrazione.html',context)

