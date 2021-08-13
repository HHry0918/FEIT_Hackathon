from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, time, timedelta

today = datetime.now()
_x_days_ago = today + timedelta(days=-30)
today_str = today.strftime("%H:%M %m/%d/%Y")
_x_days_ago_str = _x_days_ago.strftime("%H:%M %m/%d/%Y")

items_list = [
    {
        'item_name' : 'Nintendo Switch',
        'seller' : 'Harry',
        'student_id' : '13002884',
        'description' : 'Unused - Damage cover',
        'date' : today_str,
        'status' : 'Verified',
        'price' : '150$'
    }, 
    {
        'item_name' : 'PS5',
        'seller' : 'Tu',
        'student_id' : '13002885',
        'description' : 'Brand New',
        'date' : _x_days_ago_str,
        'status' : 'Verified',
        'price' : '300$'
    }
]

def home(request):
    context = {
        'items':items_list
    }
    return render(request, 'marketplace/home.html', context)

def about(request):
    context = {
        'title':'About'
    }

    return render(request, 'marketplace/about.html', context)