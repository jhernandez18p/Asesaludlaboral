from django.shortcuts import render

# Create your views here.
def blog(request):

    context = {
                'title':'blog',
            }

    return render(request, 'frontend/blog.html')
