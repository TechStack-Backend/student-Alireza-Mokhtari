from django.http import HttpResponse
def hello_world(request):
    return HttpResponse("Hello World!\nMy name is Alireza Mokhtari")

# Create your views here.
