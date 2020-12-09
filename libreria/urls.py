from django.urls import path
from .views import LibroListView,AutoreDetailViewCB,AutoreListView
app_name='libreria'

urlpatterns = [
    path('lista_libri', LibroListView.as_view(), name="lista_articoli"),
     path('autore/<int:pk>', AutoreDetailViewCB.as_view(), name="autore_detail"),
    path('lista_autori', AutoreListView.as_view(), name="lista_autori"),

]