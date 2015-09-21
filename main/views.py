from django.shortcuts import render
from django.http import HttpResponse
# import RPi.GPIO as GPIO
import wiringpi

def home(request):
    context = {}
    # context['version'] = GPIO.VERSION
    return render(request, 'home.html', context)

def light_on(request):
    context = {}
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(7, GPIO.OUT)
    # GPIO.output(7, True)

    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
    io.pinMode(18,io.OUTPUT)
    io.digitalWrite(18,io.HIGH)

    return HttpResponse(status=200)

def light_off(request):
    context = {}
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(7, GPIO.OUT)
    # GPIO.output(7, False)

    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
    io.pinMode(18,io.OUTPUT)
    io.digitalWrite(18,io.LOW)
    
    return HttpResponse(status=200)
