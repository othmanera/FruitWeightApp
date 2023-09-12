from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def detection(request):
    return render(request, "detection.html")