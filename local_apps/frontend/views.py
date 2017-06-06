import datetime
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    """ Home view """
    template = 'frontend/index.html'
    pg_title = 'Inicio'
    context = {
        'pg_title':pg_title,
    }

    return render(request, template, context)


def contact_thanks(request):
    """ Home view """
    template = 'frontend/contact_thanks.html'
    pg_title = 'Contacto'
    context = {
        'pg_title':pg_title,
    }

    return render(request, template, context)


def contact(request):
    """ Home view """
    template = 'frontend/index.html'
    pg_title = 'Contacto'
    context = {
        'pg_title':pg_title,
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
        message_user = 'Gracias %s, su mensaje ha sido enviado correctamente. '
        message_main = """%s ha querido comunicarse y dejó el siguiente mensaje 
            \n %s \nLe interesa %s 
            \n Su correo es %s
            \n Su número de telefono es %s""" % (form_name, form_message, form_select, form_email, form_phone_number)

        try:
            # Send to user
            send_mail(subject_user, message_user, from_email_user, [form_email])
            # Send to us
            send_mail(subject_main, message_main, from_email_main, ['jhernandez.18p@dev2tech.xyz'])
            # send_mail(subject_main, message_main, from_email_main, ['asesaludlaboral2727ca@gmail.com'])

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('gracias/')

    else:
        print('No post')
    print(form_name,form_email,form_phone_number,form_select,form_message)
    
    return render(request, template, context)
