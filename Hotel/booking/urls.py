from django import views
from django.urls import path
from booking import views

urlpatterns =[
    path("",views.home)
]