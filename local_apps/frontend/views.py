from django.shortcuts import render

# Create your views here.
def home(request):
    """ Home view """
    template = 'frontend/index.html'
    pg_title = 'inicio'
    context = {
        'pg_title':pg_title,
    }
    print('Hello world')
    return render(request, template, context)
