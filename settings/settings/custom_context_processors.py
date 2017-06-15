from local_apps.frontend.models import Site

def menu(request):
    """
    # Menu preprocessor 
    """
    context = {}
    site = Site.objects.all()
    if site:
        context['site'] = site[0]
    return context


def sessions(request):
    """# Cookies prepeocessor """
    context = {}
    site_description = 'Asesalud Laboral 2727 C.A'
    context['site_description'] = site_description
    return context
