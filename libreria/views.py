from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from .models import Genere, Libro, Autore
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

#Libri

class LibroListView(ListView):
    model=Libro
    template_name="lista_libri.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["libri"]=Libro.objects.all()
        return context

#Giornalisti
def autoreDetailView(request, pk):
    autore=get_object_or_404(Autore, pk=pk)
    context={"autore":autore}
    return render(request, "autore_detail.html", context)

class AutoreDetailViewCB(DetailView):
    model=Autore
    template_name="autore_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libri'] = context['autore'].libri.all()
        return context

class AutoreListView(ListView):
    model=Autore
    template_name="lista_autori.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["autori"]=Autore.objects.all()
        return context