from django.db import models
from django.db.models.fields import CharField

type_access_choices = (
    ('life access' , 'life access'),
    ('One year', 'One year'),
)

class Course(models.Model):
    name = models.CharField(max_length=50)
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    content = models.TextField(max_length=2000)
    duration = models.IntegerField(default=0)
    type_access = models.CharField(max_length=20,choices=type_access_choices)
    articles = models.ForeignKey('Article', on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.name
        

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
        

    
