from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, "index.html")

def ticketform (request):
    return render(request, "ticketform.html")

def ticketstatus (request):
    return render(request, "ticketstatus.html")

def dashboard (request):
    return render(request, "dashboard.html")