from django.shortcuts import render
from django.http import HttpResponse

def europa(request):
    return HttpResponse('<h1>Europa is the first moon of jupiter</h1>')
