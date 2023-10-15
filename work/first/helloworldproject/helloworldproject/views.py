from django.views.generic import TemplateView
from django.http import HttpResponse

def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>HttpResponse Test</h1>')
    return returnedobject

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'
