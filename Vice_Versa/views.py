from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is main page')

def home(request):
    return render(request, 'index.html' )