from django.shortcuts import render
from .models import Item

def home(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'marketplace/home.html', context)

def about(request):
    context = {
        'title':'About'
    }

    return render(request, 'marketplace/about.html', context)