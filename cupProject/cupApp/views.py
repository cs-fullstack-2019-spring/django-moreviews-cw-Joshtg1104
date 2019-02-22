from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup


# Create your views here.
def index(request):
    return HttpResponse("Test URL")


def hello(request, name):
    return HttpResponse("Hello " + str(name))


def times2(request, number):
    return HttpResponse("The Product times 2 is: " + str(number * 2))


def total(request, number):
    num = ""
    for num in range(0, number):
        num = sum(range(0, number))
    return HttpResponse("The sum of all numbers from 0 to the integer is: " + str(num))


def addCup(request):
    newCup = Cup(name="Toddler Sippy Cup", material="Plastic", manufacturerDate="2018-09-12")
    newCup.save()
    return HttpResponse()


def createCup(request):
    newCup = Cup.objects.create(name="Party Cup", material="Styrofoam", manufacturerDate="2019-01-21")
    return HttpResponse()
