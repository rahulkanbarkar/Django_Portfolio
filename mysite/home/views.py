from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello world")

def paths(request):
    return HttpResponse("path is hear u find")