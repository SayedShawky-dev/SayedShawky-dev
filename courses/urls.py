
from courses.models import Course
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('',views.course_list),
    path('<int:id>',views.course_detail),
]
