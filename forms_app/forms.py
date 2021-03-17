from django import forms
from django.core.exceptions import ValidationError
from .models import Contatto
class FormContatto(forms.ModelForm):
    class Meta:
        model=Contatto
        fields="__all__"
        widgets={
            'nome':forms.TextInput(attrs={'placeholder':'compila questo campo','class':'form-control'}),
            'cognome':forms.TextInput(attrs={'placeholder':'compila questo campo','class':'form-control'}),
            'email':forms.TextInput(attrs={'placeholder':'compila questo campo','class':'form-control'}),
            'Contenuto':forms.Textarea(attrs={'placeholder':'area testuale scrivi pure','class':'form-control'})
        }


    def clean_contenuto(self):
        dati=self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viola le norme del sito!")
        
        if len(dati)<20:
            raise ValidationError("Il contenuto inserito è troppo breve")
        return dati
    

    