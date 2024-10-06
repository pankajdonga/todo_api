from django.contrib import admin
from django.urls import path,include
from apioverview import views

urlpatterns = [
    path('apioverview/',views.apioverview),
]