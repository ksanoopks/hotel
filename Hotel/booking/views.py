from django.shortcuts import render
from .models import Hotel

# Create your views here.

def home(request):
    hotel= Hotel.objects.all()
    print(hotel)
    return render(request,"home.html",{"Hotels":hotel})
