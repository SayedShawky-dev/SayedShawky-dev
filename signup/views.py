from django.shortcuts import render


def signPage(request):
    return render(request,'signup/signup.html')