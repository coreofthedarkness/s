from django import forms
from .models import Szafka

class SzafkaSzukaj(forms.Form):
    id_wyszukiwania = forms.IntegerField()
    
    class meta:
        model = Szafka
        

class SzafkaForm(forms.Form):

    nazwa       = forms.CharField (max_length=300)
    szerokosc   = forms.IntegerField()
    wysokosc    = forms.IntegerField()
    glebokosc   = forms.IntegerField()
    plyta       = forms.IntegerField()
    ilosc_drzwi = forms.IntegerField()
    narozna     = forms.BooleanField(required=False)
    glebokosc_wneki = forms.IntegerField(help_text="n/a wpisz 0")
    ilosc_polek = forms.IntegerField()
    wzor_frontu = forms.CharField(max_length=300)
    wzor_sciany = forms.CharField(max_length=300)


    class meta:
        model = Szafka
        
