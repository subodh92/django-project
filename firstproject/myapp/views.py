from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    return HttpResponse("<h1> hello world</h1>")

def morning_view(request):
    return HttpResponse("<h1> good morning</h1>")
