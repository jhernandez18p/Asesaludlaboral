from django.shortcuts import render

# Create your views here.
def capacitaciones(request):

    context = {
                'title':'capacitaciones',
            }

    return render(request, 'frontend/capacitaciones.html', context)
