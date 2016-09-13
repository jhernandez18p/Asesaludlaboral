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
