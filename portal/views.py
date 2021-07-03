from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request,'index.html')

def contact(request):
    pass    
