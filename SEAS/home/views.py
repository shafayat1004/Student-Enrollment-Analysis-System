from django.shortcuts import render

def index(request):
    context = {

    }
    render(request, 'home/home.html')