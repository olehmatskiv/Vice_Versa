from django.http import HttpResponse

def about(request):
    return HttpResponse('This is main page')

def home(request):
    return HttpResponse('HOME PAGE')