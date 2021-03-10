from django.shortcuts import render
from .forms import FormContatto

# Create your views here.

def contatti(request):
    form=FormContatto()
    context={"form": form}
    return render(request,"home_form.html",context)