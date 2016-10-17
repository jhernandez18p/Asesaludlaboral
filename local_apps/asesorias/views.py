from django.views.generic.detail import DetailView
from django.shortcuts import render

# Create your views here.
from .models import *

def asesorias(request):

    asesorias = Asesorias.objects.all()

    context = {
        'title':'Asesoría',
        'asesorias':asesorias,
    }


    return render(request, 'frontend/asesorias.html',context)


def detalle(request,id):

    asesoria = Asesorias.objects.all().filter(pk='1')

    context = {
        'title':'Asesoría',
        'asesorias':asesoria,
    }
    return render(request, 'asesorias/asesoria.html',context)
