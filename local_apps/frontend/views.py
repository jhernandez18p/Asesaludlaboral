import datetime
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from local_apps.widgets.models import (Carousel)

# Create your views here.

def home(request):
    """ Home view """
    template = 'frontend/index.html'
    pg_title = 'Home'
    title = 'Inicio'
    context = {
        'pg_title':pg_title,
        'title':title,
    }

    carousel = Carousel.objects.all().filter(template=1)
    if carousel:
        if str(carousel[0].position) == 'HEADER':
            context['header_carousel'] = carousel[0]


    return render(request, template, context)

def assessment(request):
    """ assessment view """
    template = 'frontend/assessment.html'
    pg_title = 'Assessment'
    title = 'Evaluaciones'
    context = {
        'pg_title':pg_title,
        'title':title,
    }

    return render(request, template, context)

def training(request):
    """ training view """
    template = 'frontend/training.html'
    pg_title = 'Training'
    title = 'Capacitaciones'
    context = {
        'pg_title':pg_title,
        'title':title,
    }

    return render(request, template, context)

def counseling(request):
    """ counseling view """
    template = 'frontend/counseling.html'
    pg_title = 'Counseling'
    title = 'Asesorias'
    context = {
        'pg_title':pg_title,
        'title':title,
    }

    return render(request, template, context)

def contact_thanks(request):
    """ Home view """
    template = 'frontend/contact_thanks.html'
    pg_title = 'Contact'
    title = 'Contacto'
    context = {
        'pg_title':pg_title,
        'title':title,
    }

    return render(request, template, context)


def contact(request):
    """ Home view """
    template = 'frontend/index.html'
    pg_title = 'Contact'
    title = 'Contacto'
    context = {
        'pg_title':pg_title,
        'title':title,
    }
    form_name = ''
    form_email = ''
    form_phone_number = ''
    form_select = ''
    form_message = ''
    if request.method == 'POST':
        form_name = request.POST.get('form_name','')
        form_email = request.POST.get('form_email','')
        form_phone_number = request.POST.get('form_phone_number','')
        form_select = request.POST.get('form_select','')
        form_message = request.POST.get('form_message','')
        subject_user = 'Su mensaje ha sido enviado.'
        subject_main = 'Asesaludlaboral.com.ve | nuevo mensaje de %s' % form_name
        from_email_user = 'noreply@asesaludlaboral.com.ve'
        from_email_main = form_email
        message_user = 'Gracias %s, su mensaje ha sido enviado correctamente.' % (form_name)
        message_main = """ %s ha querido comunicarse y dejó el siguiente mensaje 
            \n %s \nLe interesa %s 
            \n Su correo es %s
            \n Su número de telefono es %s
            \n --- Este mensaje se ha enviado desde la página web https://www.asesaludlaboral.com.ve/---""" % (form_name, form_message, form_select, form_email, form_phone_number)

        try:
            # Send to user
            send_mail(subject_user, message_user, from_email_user, [form_email])
            # Send to us
            # send_mail(subject_main, message_main, from_email_main, ['jhernandez.18p@dev2tech.xyz'])
            send_mail(subject_main, message_main, from_email_main, ['asesaludlaboral2727ca@gmail.com'])

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('gracias/')

    else:
        print('No post')
    print(form_name,form_email,form_phone_number,form_select,form_message)
    
    return render(request, template, context)
