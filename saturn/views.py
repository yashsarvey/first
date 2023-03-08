from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Titan(request):
    return HttpResponse('<h2> Titan is the 1st moon of the saturn <h2>')