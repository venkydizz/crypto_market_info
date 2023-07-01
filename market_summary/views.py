from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ping(request):
    # Service health check
    return HttpResponse('pong')

