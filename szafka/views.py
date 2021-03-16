from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .formularze import SzafkaForm
from .models import Szafka

class boki:
    y=0
    z=0
    okleina="Okleina"
class dol:
    x=0
    z=0
    okleina="Okleina"
class gora:
    x=0
    z=0
    okleina="Okleina"
class front:
    ilosc_drzwi=0
    x=0
    y=0
    okleina="Okleina"
class polki:
    x=0
    z=0
    okleina="Okleina"


def szafka_rozpisana_view(request,id):

    obj = Szafka.objects.get(id = id)
    boki_s = boki()
    boki_s.y = obj.wysokosc - obj.plyta
    boki_s.z = obj.glebokosc

    dol_s = dol()
    dol_s.x =obj.szerokosc
    dol_s.z =obj.glebokosc

    gora_s = gora()
    gora_s.x =obj.szerokosc - 2*obj.plyta
    gora_s.z =obj.glebokosc

    front_s = front()
    front_s.ilosc_drzwi = obj.ilosc_drzwi
    if (obj.narozna == False):
        if ( front_s.ilosc_drzwi == 2 ):
            front_s.x = obj.szerokosc / 2  - 4
            front_s.y = obj.wysokosc - 9
        elif ( front_s.ilosc_drzwi == 1 ):
            front_s.x = obj.szerokosc - 4
            front_s.y = obj.wysokosc - 9
        else :
            front_s.x = obj.szerokosc - 4
            front_s.y = obj.wysokosc - 9
    else :
        if ( front_s.ilosc_drzwi == 2 ):
            front_s.x = obj.szerokosc / 2  - 4 - obj.glebokosc_wneki
            front_s.y = obj.wysokosc - 9
        elif ( front_s.ilosc_drzwi == 1 ):
            front_s.x = obj.szerokosc - 4 - obj.glebokosc_wneki
            front_s.y = obj.wysokosc - 9
        else :
            front_s.x = obj.szerokosc - 4 - obj.glebokosc_wneki
            front_s.y = obj.wysokosc - 9
            
    polki_s = polki()
    polki_s.x =obj.szerokosc - 2*obj.plyta -1
    polki_s.z =obj.glebokosc - 10



    context = {
        'szafka':obj,
        'boki':boki_s,
        'dol':dol_s,
        'gora':gora_s,
        'front':front_s,
        'polki':polki_s,
    }
    return render (request, "rozpisana.html", context)


def szafka_create_view(request,*args,**kwargs):

    d_nowa = SzafkaForm()
    if request.method == 'POST':
        d_nowa = SzafkaForm(request.POST)
        if d_nowa.is_valid():
             new = Szafka.objects.create(**d_nowa.cleaned_data)
             path= "../szafka/"+str(new.id)
             return redirect(path)
        else:
             print(d_nowa.errors)


    context = {
       'form': d_nowa
    }

    return render (request, "create_view.html", context)
# Create your views here.
