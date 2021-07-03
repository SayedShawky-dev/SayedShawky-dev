from django.shortcuts import render
from .models import Course,Article,Exercise

def course_list(request):
    courses_list_context = Course.objects.all()
    context= {'courses': courses_list_context}
    return render(request, 'courses/courses_list.html', context)


def course_detail(request, id):
    course_information = Course.objects.get(id=id)
    context = {'course' : course_information}
    return render(request, 'courses/course_detail.html', context)
    
    
