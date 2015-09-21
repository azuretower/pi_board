from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def home(request):
    context = {}
    context['version'] = GPIO.VERSION
    return render(request, 'home.html', context)

def light_on(request):
    context = {}
    GPIO.output(7, True)

    return HttpResponse(status=200)

def light_off(request):
    context = {}
    GPIO.output(7, False)
    
    return HttpResponse(status=200)
