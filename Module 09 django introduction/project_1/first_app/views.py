from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is first app home")
def contact(request):
    return HttpResponse("This is first app contact")
def courses(request):
    return HttpResponse("This is first app courses page")