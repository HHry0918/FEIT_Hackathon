from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item

class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

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