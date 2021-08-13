from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='marketplace-home'),
    path('about/', views.about, name='marketplace-about'),
]
