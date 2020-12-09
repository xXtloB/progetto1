from django.db import models


class Autore(models.Model):
    nome = models.CharField(max_length=20)
    nazione = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

class Genere(models.Model):
    genere = models.CharField(max_length=100)
    
    def __str__(self):
        return self.genere

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Libro(models.Model):
    titolo = models.CharField(max_length=100)
    autore = models.ForeignKey(
        Autore, on_delete=models.CASCADE, related_name="libri")
    genere = models.ForeignKey(
        Genere, on_delete=models.CASCADE, related_name="libri")
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"



# Create your models here.
