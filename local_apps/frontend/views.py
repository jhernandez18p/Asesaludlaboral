from django.core.mail import send_mail
from django.shortcuts import render
from decouple import config

# Create your views here.
def home(request):
    context = {
        'title':'Home',
    }
    return render(request, 'frontend/index.html' ,context )

def contact(request):

    if request.method == 'GET':

        return render(request, 'frontend/index.html',{'title':'Home','error':[{'title':'Mensaje vacío.','content':'Ud. debe ingresar contenido en el formulario.'}]})

    elif request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']

        if name == '':

            return render(request, 'frontend/index.html',{'title':'Home'})

        elif email == '':

            return render(request, 'frontend/index.html',{'title':'Home'})

        elif comments == '':

            return render(request, 'frontend/index.html',{'title':'Home'})

        send_mail(
		            'Email de contacto, página web',
		            '%s, ha estado visitando la página web. Su email es: %s, nos ha dejado el siguiente mensaje. \n %s' % (name,email,comments) ,
		            config("ASESALUD_EMAIL_HOST_USER",),
		            [config("ASESALUD_EMAIL_HOST_USER",),'jhernandez.18p@gmil.com'],
		            fail_silently=False,
		        )

        context = {
            'title': 'Mensaje enviado'
        }
        return render(request, 'frontend/index.html', context)
