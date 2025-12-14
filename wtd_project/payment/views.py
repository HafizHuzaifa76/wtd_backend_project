from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def payment():
    return HttpResponse('hey there, its payment!')