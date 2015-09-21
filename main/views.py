from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO

def home(request):
    context = {}
    context['version'] = GPIO.VERSION
    return render(request, 'home.html', context)

def light_on(request):
    context = {}


    return HttpResponse(status=200)

def light_off(request):
    context = {}

    
    return HttpResponse(status=200)
