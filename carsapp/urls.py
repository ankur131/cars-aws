from django.contrib import admin
from django.urls import path
from carsapp import views

urlpatterns = [
    path("", views.index, name='carsapp'),
    path("about", views.about, name='about'),
]