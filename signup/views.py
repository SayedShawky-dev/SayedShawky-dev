from django.shortcuts import render
from .models import signup

def signPage(request):
    
    return(request,'signup\signup.html')