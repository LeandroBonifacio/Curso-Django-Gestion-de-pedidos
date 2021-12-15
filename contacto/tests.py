from django.test import TestCase

# Create your tests here.

def contacto(request):
    return render(request, "ProjectoWebApp/contacto.html")
