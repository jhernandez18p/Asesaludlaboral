def menu(request):
    """
    # Menu preprocessor 
    """
    context = {}
    site_name = 'Asesalud Laboral 2727 C.A'
    context['site_name'] = site_name
    return context


def sessions(request):
    """# Cookies prepeocessor """
    context = {}
    site_description = 'Asesalud Laboral 2727 C.A'
    context['site_description'] = site_description
    return context
