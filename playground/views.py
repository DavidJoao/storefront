from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Is considered a request handler, gets requests and returns responses

def say_hello(request):
    return HttpResponse('Hello World')
    